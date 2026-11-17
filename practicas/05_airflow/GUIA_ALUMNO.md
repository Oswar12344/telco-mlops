# Práctica 5 — Apache Airflow

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar Apache Airflow sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

## Preparación especial (0–30 min)

**Requiere Docker Desktop iniciado en modo contenedores Linux**; recomendable disponer de memoria libre suficiente, porque se ejecutan Airflow y MLflow. El ZIP ya contiene `Dockerfile.airflow`, `Dockerfile.mlflow`, `compose.yaml` y el DAG.

Abre el proyecto en VS Code, inicia Docker Desktop y ejecuta:

```bat
docker info
docker compose up -d --build
docker compose ps
```

**Comprueba:** el servicio `mlflow` y `airflow` aparecen en la lista. La primera ejecución descarga imágenes, puede consumir varios GB y requiere internet.

## Bloque 2 (30–55 min): interfaz

Abre `http://localhost:8080`; busca credenciales de Airflow en `docker compose logs airflow` y sigue las indicaciones del arranque. Abre `http://localhost:5000` para MLflow.

En Airflow localiza el DAG `telco_training_pipeline`.

## Bloque 3 (55–80 min): ejecutar DAG

Presiona **Trigger** y abre la vista de tareas. Debes observar en orden:

1. `validar_datos`
2. `entrenar_modelos`
3. `registrar_mlflow`
4. `generar_reporte`

El script entrena los modelos a partir del CSV real, registra el experimento y genera los datos para el monitoreo.

## Bloque 4 (80–100 min): interpretar un error

En `dags/telco_training_dag.py`, cambia **temporalmente** el import `from src.check_data import validate` por `from src.check_data import funcion_no_existe`. Ejecuta otro DAG run y abre el log de la tarea fallida. Restaura exactamente el import original y vuelve a ejecutar.

## Bloque 5 (100–120 min): comprobar integración

En MLflow comprueba nuevos runs y el Champion. En Airflow observa los logs y los estados. Detén al terminar:

```bat
docker compose down
```

**Entrega:** DAG con 4 tareas, ejecución exitosa, log del fallo y MLflow con los runs. **Si Docker falla, guarda `docker compose logs airflow` y `docker compose logs mlflow` para revisión.**

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
