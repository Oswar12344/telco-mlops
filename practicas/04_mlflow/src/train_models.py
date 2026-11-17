"""Entrenar Logistic, Forest y SVM; Champion por ROC-AUC de validación."""
import argparse
import json
from datetime import datetime, timezone
import joblib
import pandas as pd
from .common import ROOT, get_splits, build_pipeline, metrics


def train_and_select():
    X_train, X_val, X_test, y_train, y_val, y_test = get_splits()
    model_dir = ROOT / "models"
    (model_dir / "candidates").mkdir(parents=True, exist_ok=True)
    (ROOT / "reports").mkdir(parents=True, exist_ok=True)
    table, pipelines = [], {}
    for algo in ("logistic", "forest", "svm"):
        model = build_pipeline(algo)
        model.fit(X_train, y_train)
        score = metrics(model, X_val, y_val)
        table.append({"model": algo, **score})
        pipelines[algo] = model
        joblib.dump(model, model_dir / "candidates" / f"{algo}.joblib")
        print(f"{algo:10s} validación ROC-AUC: {score['roc_auc']:.4f}")
    summary = pd.DataFrame(table).sort_values("roc_auc", ascending=False)
    summary.to_csv(ROOT / "reports" / "comparison.csv", index=False)
    champion = str(summary.iloc[0]["model"])
    joblib.dump(pipelines[champion], model_dir / "champion.joblib")
    test_metrics = metrics(pipelines[champion], X_test, y_test)
    metadata = {
        "champion": champion, "selection_metric": "roc_auc_validation",
        "train_rows": len(X_train), "validation_rows": len(X_val), "test_rows": len(X_test),
        "random_seed": 42, "evaluation_test": test_metrics,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "note": "Dataset de ejemplo didáctico aportado por el docente; no usar para decisiones reales.",
    }
    (model_dir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (ROOT / "reports" / "test_metrics.json").write_text(json.dumps(test_metrics, indent=2), encoding="utf-8")
    print(f"Champion: {champion}; prueba ROC-AUC: {test_metrics['roc_auc']:.4f}")
    return metadata


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    train_and_select()


if __name__ == "__main__":
    main()
