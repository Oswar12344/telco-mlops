# Verificación de entorno y actividades del docente

## Pruebas realizables aquí

- CSV Kaggle original: leído y comparado.
- Entrenamiento de tres modelos: ejecutado.
- Champion seleccionado con validación ROC-AUC.
- Evaluación solo en test: ejecutada.
- Endpoint /predict con Pydantic: tests locales ejecutados.
- Datos de monitoreo simulados: generados.

## Comprobaciones que debe hacer el docente en su equipo

- DVC: instalar y probar un push/pull al remoto local.
- MLflow: instalar, registrar 3 modelos, comprobar alias champion.
- Airflow: ejecutar docker compose, revisar usuarios/credenciales de standalone y DAG.
- Docker: construir imagen, ejecutar API y revisar puerto.
- GitHub: crear un repositorio, revisar Actions y permisos de GHCR.
- Evidently: instalar y generar HTML.

## Precauciones

- El conjunto de prueba no se debe utilizar para seleccionar el Champion.
- `TotalCharges` tiene 11 valores en blanco y se imputa dentro del Pipeline.
- Cinco columnas de entrada por claridad; no todos los 20 predictores.
- El escenario de drift está simulado; no confundas con cambios históricos reales.
- No subir contenido sensible a GitHub ni logs con información personal.
- Revisar licencia/términos de redistribución del CSV de Kaggle antes de crear repositorio público.