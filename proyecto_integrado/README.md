# Telco Customer Churn — proyecto integrado MLOps (datos Kaggle aportados)

Este proyecto usa **el CSV real dentro del archivo Dataset.zip que aportó el docente**, copiado sin alteraciones en `data/raw/telco.csv` (SHA256 `88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a`). Fuente indicada: https://www.kaggle.com/datasets/blastchar/telco-customer-churn. Verifica las condiciones de distribución antes de publicar copias del CSV en repositorios públicos.

## Objetivo didáctico

- Comparar Regresión Logística, Random Forest y SVM (RBF).
- 5 variables para que la API HTML sea manejable: `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `InternetService`.
- El CSV original se conserva con 21 columnas; `TotalCharges` trae **11 espacios en blanco** y el pipeline los imputa usando SOLO entrenamiento.
- Partición estratificada fija: 60% entrenamiento / 20% validación / 20% prueba (`random_state=42`).
- Seleccionar Champion por ROC-AUC de validación y evaluar una sola vez en prueba reservada.

## Primer uso en Windows (CMD dentro de Visual Studio Code)

**Opción sencilla:** abre `scripts/01_verificar_en_windows.bat` (instala requisitos y ejecuta pruebas). Después `scripts/02_iniciar_fastapi.bat` inicia la aplicación. Si prefieres comandos, sigue lo siguiente:

```bat
py -3.11 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m src.check_data
.venv\Scripts\python.exe -m src.train_models
.venv\Scripts\python.exe -m src.evaluate
.venv\Scripts\python.exe -m pytest -v
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Si `py -3.11` no existe, utilizar `python -m venv .venv` con Python 3.11 o superior compatible. En el navegador abrir `http://127.0.0.1:8000/`, `/docs` y `/health`.

## Dónde está el dataset

`data/raw/telco.csv` es la copia íntegra de Kaggle que entregaste. No hay que descargarlo otra vez. Las prácticas tienen una copia independiente para evitar que una modificación afecte a otra.

## Prácticas y comandos

En `practicas/` dentro del paquete general hay nueve actividades autónomas. Lee `GUIA_ALUMNO.md` de cada una. También puedes descargar cada ZIP por separado.

## Docker de API

```bat
docker build -t telco-api:v1 .
docker run --rm -p 8000:8000 telco-api:v1
```

## Airflow + MLflow (opcional, Docker Desktop en modo Linux)

```bat
docker compose up -d --build
```

Abrir Airflow en `http://localhost:8080` (consultar el usuario/contraseña de inicio con `docker compose logs airflow`), MLflow en `http://localhost:5000`. Detener con `docker compose down` (sin `-v`, para conservar volúmenes). Es una demostración local, no configuración productiva. **Debe verificarse en tu PC con Docker**, ya que no se ha probado el motor de contenedores aquí.

## MLflow sin Airflow

Instalar `requirements-mlflow.txt`, iniciar servidor MLflow con SQLite en otra consola:

```bat
.venv\Scripts\python.exe -m mlflow server --backend-store-uri sqlite:///mlflow.db --serve-artifacts --artifacts-destination ./mlartifacts --host 127.0.0.1 --port 5000
```

En la primera consola: `.venv\Scripts\python.exe -m src.mlflow_tracking`

## Monitoreo Evidently

Instalar `requirements-monitoring.txt` y ejecutar:

```bat
.venv\Scripts\python.exe -m src.make_monitoring_data
.venv\Scripts\python.exe -m src.monitoring --source simulated
```

Se genera `reports/data_drift_simulated.html`. Los cambios en los datos actuales **son simulados adrede**; no representan eventos observados de la empresa.

## CI/CD

El workflow `.github/workflows/cicd.yml` se ejecuta en GitHub al subir este proyecto a `main`: tests y, si pasan, imagen de GHCR. Es necesario crear tu propio repositorio y autorizar la publicación del paquete.

## Alcance y seguridad

Ejercicio educativo. Ninguna predicción reemplaza criterio humano y la demo carece de autenticación y control de acceso para producción. **Nunca cargues archivos joblib de fuentes desconocidas**. Los logs de inferencia se guardan en `runtime/` sin ID de cliente y no deben usarse con información personal real.
