# Curso MLOps para Minería de Datos — 9 prácticas independientes

**Datos reales suministrados:** Kaggle Telco Customer Churn, 7043 filas / 21 columnas, 11 blancos en TotalCharges. **Modelo elegido:** se obtiene de ejecutar `python -m src.train_models` y ya está guardado en cada ZIP.

## Primer archivo que debe abrir el docente

Abre `proyecto_integrado/README.md`. Para cada práctica, ve a `practicas/NN_nombre/GUIA_ALUMNO.md` o entrega solo el ZIP individual.

## Plan sugerido

| Práctica | Herramienta | Tiempo | Verificación |
|---|---|---|---|
| 01 | Git | 2 h | historial de ramas/conflicto |
| 02 | GitHub | 2 h | Pull Request y clon |
| 03 | DVC | 2 h | versionar dos versiones y `dvc pull` |
| 04 | MLflow | 2 h | 3 runs y Champion |
| 05 | Airflow | 2 h | DAG con cuatro tareas |
| 06 | FastAPI | 2 h | `/docs`, `/predict`, HTML |
| 07 | Docker | 2 h | imagen v1/v2 y contenedor |
| 08 | CI/CD | 2 h | Actions, test rojo/verde y GHCR |
| 09 | Monitoreo | 2 h | reportes Evidently y logs API |

Son **18 horas**. Para ajustarlo a las **16 horas** originales, combina Git y GitHub en una sesión intensiva de 2 horas (reduciendo ejercicios). No intentes enseñar nueve prácticas completas de dos horas en ocho sesiones sin ajustes.

## Manual docente de comprobaciones

Consulta `VERIFICACION_GENERAL.md` y la guía individual. Cada ZIP contiene dataset, código, Champion y tests para funcionar independientemente.

## Límites de validación

El proyecto base se entrenó y probó en el entorno de creación. Las herramientas que requieren servidor, API de GitHub o Docker deben comprobarse en Windows con conexión a internet. Los ejemplos no son arquitectura productiva ni muestran permisos o datos reales de clientes.