"""Variables, carga de Kaggle, splits reproducibles y construcción de modelos."""
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
FEATURES = ["tenure", "MonthlyCharges", "TotalCharges", "Contract", "InternetService"]
NUMERIC = ["tenure", "MonthlyCharges", "TotalCharges"]
CATEGORICAL = ["Contract", "InternetService"]
RAW_PATH = ROOT / "data" / "raw" / "telco.csv"


def load_raw():
    """Cargar CSV aportado por el docente; mantener todas las filas originales."""
    data = pd.read_csv(RAW_PATH)
    needed = FEATURES + ["Churn"]
    if not set(needed).issubset(data.columns):
        raise ValueError(f"Faltan columnas: {set(needed) - set(data.columns)}")
    data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
    for col in ["tenure", "MonthlyCharges"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    if not set(data["Churn"].dropna().unique()) <= {"Yes", "No"}:
        raise ValueError("Churn solo debe contener Yes o No")
    return data


def get_splits():
    """60% entrenamiento, 20% validación, 20% prueba; siempre semilla 42."""
    data = load_raw()
    X, y = data[FEATURES], data["Churn"].eq("Yes").astype(int)
    X_train, X_rem, y_train, y_rem = train_test_split(
        X, y, test_size=0.40, stratify=y, random_state=42
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_rem, y_rem, test_size=0.50, stratify=y_rem, random_state=42
    )
    return X_train, X_val, X_test, y_train, y_val, y_test


def build_pipeline(algorithm):
    """El preprocesamiento se ajusta dentro de fit, solo con datos de train."""
    prep = ColumnTransformer([
        ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median")),
                               ("scaler", StandardScaler())]), NUMERIC),
        ("categorical", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                                  ("encoder", OneHotEncoder(handle_unknown="ignore"))]), CATEGORICAL),
    ])
    models = {
        "logistic": LogisticRegression(C=1.0, max_iter=1200, random_state=42),
        "forest": RandomForestClassifier(n_estimators=120, max_depth=6, random_state=42, n_jobs=1),
        "svm": SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=42),
    }
    if algorithm not in models:
        raise ValueError(f"Modelo no permitido: {algorithm}")
    return Pipeline([("preprocess", prep), ("classifier", models[algorithm])])


def metrics(model, X, y):
    pred = model.predict(X)
    prob = model.predict_proba(X)[:, 1]
    return {"accuracy": float(accuracy_score(y, pred)),
            "precision": float(precision_score(y, pred, zero_division=0)),
            "recall": float(recall_score(y, pred, zero_division=0)),
            "f1": float(f1_score(y, pred, zero_division=0)),
            "roc_auc": float(roc_auc_score(y, prob))}
