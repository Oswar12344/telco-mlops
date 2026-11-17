"""Evaluación final: conjunto de prueba no utilizado para elegir Champion."""
import json
import joblib
from .common import ROOT, get_splits, metrics


def evaluate():
    _, _, X_test, _, _, y_test = get_splits()
    model = joblib.load(ROOT / "models" / "champion.joblib")
    result = metrics(model, X_test, y_test)
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    evaluate()
