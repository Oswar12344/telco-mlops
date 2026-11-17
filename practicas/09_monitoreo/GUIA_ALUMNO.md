# Práctica 9 — Monitoreo con Evidently AI

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar Monitoreo con Evidently AI sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

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

## Bloque 1 (0–30 min): preparar Evidently

```bat
.venv\Scripts\python.exe -m pip install -r requirements-monitoring.txt
.venv\Scripts\python.exe -m src.make_monitoring_data
```

Este último script crea `data/monitoring/reference.csv` y `current_shifted.csv` a partir de registros reales de Kaggle, pero **simula adrede cambios** en MonthlyCharges y Contract. No son sucesos históricos de una empresa.

## Bloque 2 (30–55 min): crear reporte HTML

```bat
.venv\Scripts\python.exe -m src.monitoring --source simulated
```

Abre `reports/data_drift_simulated.html` y observa distribuciones antes/después.

## Bloque 3 (55–80 min): interpretar

Responde: ¿qué cambió en `MonthlyCharges` y `Contract`? ¿Cambió la distribución de la probabilidad de abandono? ¿Data drift implica que el modelo está equivocado? (No necesariamente.)

## Bloque 4 (80–105 min): monitorear solicitudes reales de la API

En **terminal 1** inicia:

```bat
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Abre `http://127.0.0.1:8000/`, realiza al menos cinco predicciones cambiando las entradas; el servidor guarda registros en `runtime/predictions.jsonl`. En **terminal 2** ejecuta:

```bat
.venv\Scripts\python.exe -m src.monitoring --source api-logs
```

Abre `reports/data_drift_api-logs.html`. Con solo cinco registros, cualquier prueba de drift es estadísticamente poco confiable; úsala solamente para visualizar el mecanismo de registro.

## Bloque 5 (105–120 min): interpretar y entregar

**Entrega:** dos reportes HTML, valores medios de probabilidades y una explicación de por qué se necesitan etiquetas reales para medir performance/concept drift. Las entradas registradas no contienen ID de cliente, pero NO utilices datos personales reales en esta demo.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
