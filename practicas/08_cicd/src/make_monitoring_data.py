"""Preparar dos lotes reales y un cambio sintético claramente señalado."""
import joblib
import pandas as pd
import numpy as np
from .common import ROOT, get_splits


def generate():
    Xt, Xv, Xs, yt, yv, ys = get_splits()
    rng = np.random.default_rng(42)
    reference = Xv.copy().reset_index(drop=True)
    current = Xs.copy().reset_index(drop=True)
    # CAMBIO SIMULADO, NO INFERIR que sucedió de verdad en Telco.
    current["MonthlyCharges"] = (current["MonthlyCharges"] + 25).clip(0, 150)
    mask = rng.random(len(current)) < 0.50
    current.loc[mask, "Contract"] = "Month-to-month"
    model = joblib.load(ROOT / "models" / "champion.joblib")
    for frame in (reference, current):
        frame["prediction_probability"] = model.predict_proba(frame.iloc[:, :5])[:, 1]
    out = ROOT / "data" / "monitoring"
    out.mkdir(parents=True, exist_ok=True)
    reference.to_csv(out / "reference.csv", index=False)
    current.to_csv(out / "current_shifted.csv", index=False)
    # Evaluación real del conjunto test SIN modificar etiquetas ni datos:
    baseline = Xs.reset_index(drop=True).copy()
    baseline["Churn"] = ys.reset_index(drop=True).map({0:"No", 1:"Yes"})
    baseline.to_csv(out / "test_with_labels.csv", index=False)
    print(f"Preparado monitoreo: {len(reference)} referencia, {len(current)} actual con drift simulado")

if __name__ == "__main__":
    generate()
