"""Predicción de ejemplo con los cinco campos de la API."""
import joblib
import pandas as pd
from .common import ROOT

if __name__ == "__main__":
    model = joblib.load(ROOT / "models" / "champion.joblib")
    person = pd.DataFrame([{"tenure": 5, "MonthlyCharges": 85.5, "TotalCharges": 427.5,
                            "Contract": "Month-to-month", "InternetService": "Fiber optic"}])
    print({"prediction": int(model.predict(person)[0]),
           "churn_probability": float(model.predict_proba(person)[0, 1])})
