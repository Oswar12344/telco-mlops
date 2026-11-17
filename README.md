# Telco Customer Churn — Curso MLOps

Repositorio privado de material educativo con dataset Kaggle proporcionado por el docente. El curso abarca Git, GitHub, DVC, MLflow, Airflow, FastAPI, Docker, CI/CD y monitoreo.

> **Estado:** los workflows ya están preparados. Falta subir el archivo `Telco_MLOps_Curso_Completo.zip` para importar el contenido. No se debe afirmar que CI/CD funciona hasta que GitHub Actions finalice correctamente.

## Primer paso (solo una carga de archivo)

1. Descarga el archivo `Telco_MLOps_Curso_Completo.zip` proporcionado en ChatGPT.
2. En este repositorio, selecciona **Add file > Upload files**.
3. Arrastra **el ZIP sin descomprimir**, con el nombre exacto `Telco_MLOps_Curso_Completo.zip`, a la raíz del repositorio.
4. En la parte inferior, selecciona **Commit directly to the main branch** y confirma la carga.
5. Ve a **Actions** y abre **Importar ZIP del curso MLOps**. Espera a que aparezca la ejecución con marca verde.

El workflow `.github/workflows/importar-curso.yml` comprueba la estructura del ZIP, lo extrae, ejecuta las seis pruebas locales del proyecto integrado y, si pasan, guarda la estructura de carpetas en GitHub.

## Estructura que aparecerá después de la importación

```text
proyecto_integrado/
  data/raw/telco.csv
  models/champion.joblib
  app/
  src/
  tests/
  dags/
  .github/workflows/
  Dockerfile
  compose.yaml
  README.md
practicas/
  01_git/
  02_github/
  03_dvc/
  04_mlflow/
  05_airflow/
  06_fastapi/
  07_docker/
  08_cicd/
  09_monitoreo/
EMPIEZA_AQUI.md
VERIFICACION_GENERAL.md
Dataset_original_aportado.zip
```

**Importante:** las nueve prácticas son independientes y por eso incluyen copias del dataset y de modelos.

## Verificación del proyecto integrado

En Windows, abre `proyecto_integrado` en VS Code y ejecuta `scripts/01_verificar_en_windows.bat`. Alternativamente, en una consola CMD en esa carpeta:

```bat
py -3.11 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest -v
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Abre `http://localhost:8000/docs` o `http://localhost:8000/` para realizar predicciones.

## CI/CD y GHCR

Una vez que la importación terminó con éxito, en **Actions** selecciona **Telco CI CD > Run workflow > Run workflow**. Ejecuta las pruebas y, si pasan, construye y publica la imagen Docker en `ghcr.io/oswar12344/telco-mlops:latest` usando `GITHUB_TOKEN`. Puede requerir ajustes de permisos del repositorio o del paquete; revisa el registro de Actions si falla.

El evento generado por el token automático al importar el paquete puede no activar otro workflow, por lo que es necesario iniciar manualmente esta primera ejecución. Los siguientes cambios normales al código en `main` sí activarán CI/CD.

## Alcance y comprobaciones pendientes

- Dataset Telco Customer Churn: **7,043 filas**, con 11 espacios vacíos en `TotalCharges`.
- Modelos: Regresión Logística, Random Forest y SVM (RBF); Champion seleccionado en validación.
- Pruebas de FastAPI y datos: **6 pruebas** comprobadas en el entorno de creación.
- Requieren validación externa: DVC, MLflow, Airflow, Docker Desktop, GHCR y Evidently.
- El dataset y el artefacto joblib son material didáctico; no son un sistema en producción. El repositorio debe permanecer privado hasta confirmar los términos de redistribución del dataset.

Para las instrucciones por herramienta, consulta `practicas/NN_nombre/GUIA_ALUMNO.md` y `GUIA_DOCENTE.md`.
