# Telco Customer Churn — Proyecto de Introducción a MLOps

## Descripción del proyecto

Proyecto académico de Minería de Datos desarrollado para aplicar herramientas y buenas prácticas de MLOps (Machine Learning Operations).

El proyecto utiliza el conjunto de datos **Telco Customer Churn**, proporcionado por el docente, para desarrollar un modelo de Machine Learning capaz de predecir si un cliente de telecomunicaciones podría abandonar el servicio.

Además del entrenamiento del modelo, se implementaron herramientas para controlar versiones, automatizar procesos, publicar una API, ejecutar pruebas y monitorear las predicciones.

## Objetivo

Desarrollar y organizar un proyecto de Machine Learning aplicando las principales etapas de MLOps: versionado, experimentación, entrenamiento, automatización, despliegue, integración continua y monitoreo.

## Herramientas implementadas

| Herramienta | Implementación |
|---|---|
| Git | Control de versiones y seguimiento de cambios. |
| GitHub | Almacenamiento del código y documentación del proyecto. |
| DVC | Versionado de datos y seguimiento de cambios en el dataset. |
| MLflow | Registro de experimentos, modelos y selección del modelo champion. |
| Apache Airflow | Automatización del flujo de entrenamiento mediante un DAG. |
| FastAPI | API y formulario web para realizar predicciones. |
| Docker | Empaquetado y ejecución de la aplicación en contenedores. |
| GitHub Actions | Pruebas automáticas y construcción de imágenes Docker. |
| Evidently | Generación de reportes para analizar cambios en los datos. |

## Resultados principales

- **Dataset:** 7,043 registros de clientes.
- **Calidad de datos:** se identificaron 11 valores vacíos en `TotalCharges`.
- **Modelos evaluados:** Regresión Logística, Random Forest y SVM.
- **Modelo seleccionado:** Random Forest, registrado en MLflow con el alias `champion`.
- **API:** predicciones verificadas mediante FastAPI y su documentación interactiva.
- **Pruebas:** seis pruebas automatizadas ejecutadas correctamente.
- **Airflow:** ejecución satisfactoria del flujo de entrenamiento y sus cuatro tareas.
- **Docker:** ejecución comprobada de la aplicación mediante contenedores.
- **CI/CD:** ejecución exitosa de las etapas de pruebas y construcción de imagen Docker en GitHub Actions.
- **Monitoreo:** reportes de cambios en la distribución de los datos generados con Evidently.

Estos resultados corresponden a un proyecto académico y no representan un sistema desplegado en producción.

## Organización del repositorio

```text
telco-mlops/
├── .github/workflows/
├── practicas/
│   ├── 01_git/
│   ├── 02_github/
│   ├── 03_dvc/
│   ├── 04_mlflow/
│   ├── 05_airflow/
│   ├── 06_fastapi/
│   ├── 07_docker/
│   ├── 08_cicd/
│   └── 09_monitoreo/
├── proyecto_integrado/
├── Dataset_original_aportado.zip
├── Telco_MLOps_Curso_Completo.zip
├── EMPIEZA_AQUI.md
├── GUIA_PRESENTACION_MAESTRO.md
└── VERIFICACION_GENERAL.md
```

Las nueve prácticas están organizadas de manera independiente para facilitar su revisión y ejecución. La carpeta `proyecto_integrado` reúne los componentes principales del proyecto.

## Ejecución de la aplicación

Para ejecutar la aplicación del proyecto integrado en Windows, se requiere Python 3.11 y las dependencias indicadas en `requirements.txt`.

Desde la carpeta `proyecto_integrado`:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

Una vez iniciada, la aplicación puede consultarse en:

- Formulario web: http://127.0.0.1:8001/
- Documentación de la API: http://127.0.0.1:8001/docs
- Estado del servicio: http://127.0.0.1:8001/health

Los componentes de Airflow, MLflow, Docker y monitoreo cuentan con sus propias configuraciones y guías de ejecución.

## Repositorio y entrega

**Repositorio:** https://github.com/Oswar12344/telco-mlops

El repositorio es público y contiene el código fuente, las nueve prácticas, el proyecto integrado, las configuraciones y la documentación.

También se incluye el archivo `Telco_MLOps_Curso_Completo.zip`, que permite obtener una copia organizada del proyecto.

## Conclusión

El proyecto permitió aplicar herramientas de MLOps a un caso de predicción de abandono de clientes, desde la preparación y el versionado de datos hasta la automatización, las predicciones y el monitoreo.

Se comprobó el funcionamiento de los componentes principales y se documentaron los resultados obtenidos durante las prácticas.

**Nota:** este repositorio tiene fines exclusivamente académicos. El modelo y los datos se utilizan como material de aprendizaje y no constituyen un servicio comercial en producción.
