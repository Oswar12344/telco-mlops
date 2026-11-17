# Práctica 6 — FastAPI + HTML

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar FastAPI + HTML sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

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

## Bloque 1 (0–30 min): iniciar servidor

```bat
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

La terminal debe mostrar que escucha en `http://127.0.0.1:8000`. Abre `/docs` y `/` en el navegador. `app/main.py` carga automáticamente el Champion REAL creado con el CSV de Kaggle.

## Bloque 2 (30–55 min): enviar JSON desde Swagger

Abre `http://127.0.0.1:8000/docs`, entra a `POST /predict` y selecciona **Try it out**:

```json
{"tenure":5,"MonthlyCharges":85.5,"TotalCharges":427.5,"Contract":"Month-to-month","InternetService":"Fiber optic"}
```

**Comprueba:** devuelve `prediction` (0/1), `churn_probability` (entre 0 y 1), `risk_level` y `message`.

## Bloque 3 (55–80 min): usar HTML

Abre `http://127.0.0.1:8000/`, cambia los campos del formulario, presiona **Calcular predicción** y observa resultado. En `templates/index.html` modifica el encabezado, guarda y recarga.

## Bloque 4 (80–100 min): modificar endpoint

En `app/main.py` cambia el corte de riesgo Alto de `0.70` a `0.60`; guarda (Uvicorn recarga automáticamente) y vuelve a probar. Regresa al valor original al final.

## Bloque 5 (100–120 min): validar entradas

Desde Swagger prueba `tenure=-10` y observa error HTTP 422. Abre `http://127.0.0.1:8000/health`. Finalmente:

```bat
.venv\Scripts\python.exe -m pytest -q
```

**Entrega:** `/docs`, respuesta real JSON, formulario, error 422 y pruebas pasadas.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
