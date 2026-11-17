"""Pruebas de API usando el modelo entrenado con Kaggle."""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
SAMPLE = {"tenure": 5, "MonthlyCharges": 85.5, "TotalCharges": 427.5,
          "Contract": "Month-to-month", "InternetService": "Fiber optic"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["model_loaded"] is True

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Predicción de abandono" in response.text

def test_predict(monkeypatch, tmp_path):
    monkeypatch.setenv("PREDICTION_LOG_PATH", str(tmp_path / "requests.jsonl"))
    response = client.post("/predict", json=SAMPLE)
    assert response.status_code == 200
    result = response.json()
    assert result["prediction"] in [0, 1]
    assert 0 <= result["churn_probability"] <= 1
    assert result["risk_level"] in ["Bajo", "Medio", "Alto"]
    assert (tmp_path / "requests.jsonl").exists()

def test_bad_data():
    response = client.post("/predict", json={**SAMPLE, "tenure": -7})
    assert response.status_code == 422
