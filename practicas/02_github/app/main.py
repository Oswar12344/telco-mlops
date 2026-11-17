"""API de predicción: lee el pipeline real entrenado con dataset aportado."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .schemas import CustomerInput

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "champion.joblib"
model = joblib.load(MODEL_PATH)
app = FastAPI(title="Telco Customer Churn — Curso MLOps", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": True}

@app.get("/", response_class=HTMLResponse)
def home():
    return (ROOT / "templates" / "index.html").read_text(encoding="utf-8")

@app.post("/predict")
def predict(customer: CustomerInput):
    payload = customer.model_dump()
    frame = pd.DataFrame([payload])
    label = int(model.predict(frame)[0])
    probability = float(model.predict_proba(frame)[0, 1])
    risk = "Bajo" if probability < 0.30 else "Medio" if probability < 0.70 else "Alto"
    result = {"prediction": label, "churn_probability": round(probability, 6),
              "risk_level": risk, "message": "Se predice abandono" if label == 1 else "Se predice permanencia"}
    # Para la práctica de monitoreo: se registran entradas SIN identificador de cliente.
    log_file = Path(os.getenv("PREDICTION_LOG_PATH", str(ROOT / "runtime" / "predictions.jsonl")))
    log_file.parent.mkdir(parents=True, exist_ok=True)
    record = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), **payload,
              "prediction": label, "prediction_probability": probability}
    with log_file.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return result
