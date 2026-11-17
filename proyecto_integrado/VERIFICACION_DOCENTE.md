# Qué debe comprobar el docente

1. `python -m src.check_data`: 7043 filas y 11 espacios vacíos en TotalCharges.
2. `python -m src.train_models`: 3 modelos, comparación CSV y Champion.
3. `python -m src.evaluate`: ROC-AUC sobre prueba no utilizada para selección.
4. `python -m pytest -v`: tests ejecutados sin error.
5. `/docs` y `/predict`: 200 ante JSON válido, 422 ante tenure -1.
6. Docker: `docker build` y `/health` (requiere Docker Desktop).
7. GitHub Actions: job test verde, job docker publica si se permite GHCR.
8. MLflow: runs y alias champion (requiere instalar mlflow/servidor).
9. Airflow: DAG ejecutado y logging (requiere Docker y más memoria).
10. Evidently: informe HTML con data drift simulado (requiere instalación).

No afirme que Docker, GitHub, DVC, Airflow, MLflow o Evidently fueron probados hasta ejecutarlos en el equipo objetivo.
