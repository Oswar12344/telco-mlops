"""Registrar modelos ya entrenados y seleccionar Champion en Model Registry."""
import argparse
import joblib
import pandas as pd
from .common import ROOT, get_splits, metrics


def track_models(uri):
    import mlflow
    import mlflow.sklearn
    from mlflow import MlflowClient
    from mlflow.models import infer_signature
    mlflow.set_tracking_uri(uri)
    mlflow.set_experiment("Telco_Churn")
    _, X_val, _, _, y_val, _ = get_splits()
    comparison = pd.read_csv(ROOT / "reports" / "comparison.csv")
    logs = {}
    for algo in ("logistic", "forest", "svm"):
        model = joblib.load(ROOT / "models" / "candidates" / f"{algo}.joblib")
        conf = model.named_steps["classifier"].get_params()
        with mlflow.start_run(run_name=algo):
            mlflow.log_param("algorithm", algo)
            for key in ("C", "kernel", "gamma", "n_estimators", "max_depth", "max_iter"):
                if key in conf: mlflow.log_param(key, conf[key])
            mlflow.log_metrics(metrics(model, X_val, y_val))
            predictions = model.predict(X_val.head(5))
            info = mlflow.sklearn.log_model(
                sk_model=model, name=algo,
                input_example=X_val.head(3),
                signature=infer_signature(X_val.head(5), predictions)
            )
            logs[algo] = info.model_uri
            print(f"Registrado {algo}: {info.model_uri}")
    champion = str(comparison.iloc[0]["model"])
    version = mlflow.register_model(model_uri=logs[champion], name="TelcoChurnClassifier")
    MlflowClient().set_registered_model_alias("TelcoChurnClassifier", "champion", version.version)
    print(f"Champion: {champion} | Registry: TelcoChurnClassifier v{version.version} alias champion")
    return champion

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--tracking-uri", default="http://127.0.0.1:5000")
    args=parser.parse_args()
    track_models(args.tracking_uri)
