# Práctica 4 — MLflow

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar MLflow sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

## Preparación común (CMD o PowerShell en VS Code)

1. Descomprime **este ZIP** y abre la carpeta resultante en VS Code.
2. Abre **Terminal > New Terminal**.
3. Comprueba `python --version` y `git --version` (Git solo donde se use).
4. Crea el entorno e instala dependencias (una sola vez):

```bat
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m src.check_data
```

**Debes ver:** `Dataset válido: 7043 filas; TotalCharges vacíos: 11`. El archivo real de Kaggle ya está en `data/raw/telco.csv`; no necesitas descargarlo otra vez.

**Nota:** si Windows no encuentra `python`, instala Python 3.11 y abre de nuevo la terminal. No uses la carpeta `.venv` de otra práctica.

## Bloque 1 (0–25 min): instalar e iniciar servidor

```bat
.venv\Scripts\python.exe -m pip install -r requirements-mlflow.txt
```

En una **terminal 1**, ejecuta y déjala abierta:

```bat
.venv\Scripts\python.exe -m mlflow server --backend-store-uri sqlite:///mlflow.db --serve-artifacts --artifacts-destination ./mlartifacts --host 127.0.0.1 --port 5000
```

En el navegador abre `http://127.0.0.1:5000`.

## Bloque 2 (25–55 min): registrar tres ejecuciones

En **terminal 2**, desde la carpeta del proyecto:

```bat
.venv\Scripts\python.exe -m src.mlflow_tracking --tracking-uri http://127.0.0.1:5000
```

El script está programado: registra parámetros y métricas de los modelos **reales** previamente entrenados, incluyendo sus artefactos, y crea `Telco_Churn`.

## Bloque 3 (55–85 min): comparar en la UI

Abre el experimento `Telco_Churn` y compara `logistic`, `forest`, `svm`. Busca F1 y ROC-AUC. Completa:

| Modelo | Accuracy | F1 | ROC-AUC |
|---|---|---|---|
| Logistic | | | |
| Forest | | | |
| SVM | | | |

## Bloque 4 (85–110 min): Model Registry

Abre la sección **Models**, busca `TelcoChurnClassifier` y comprueba que existe el alias `champion`. Explica cómo se escogió: ROC-AUC de validación, no del conjunto de prueba.

## Bloque 5 (110–120 min): entrega

Capturas de 3 runs, tabla comparativa, modelo registrado, alias. Si falla la conexión, confirma que la terminal 1 sigue ejecutándose y que el puerto 5000 no esté ocupado.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
