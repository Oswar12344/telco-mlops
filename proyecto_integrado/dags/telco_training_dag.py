"""DAG Airflow 3 para el proyecto montado en /opt/airflow/project."""
from datetime import datetime, timezone
from airflow.sdk import dag, task

@dag(dag_id="telco_training_pipeline", start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
     schedule=None, catchup=False, tags=["telco", "mlops"])
def telco_training_pipeline():
    @task
    def validar_datos():
        from src.check_data import validate
        validate()

    @task
    def entrenar_modelos():
        from src.train_models import train_and_select
        return train_and_select()["champion"]

    @task
    def registrar_mlflow(champion):
        import os
        from src.mlflow_tracking import track_models
        selected=track_models(os.environ.get("MLFLOW_TRACKING_URI", "http://mlflow:5000"))
        assert selected == champion

    @task
    def generar_reporte():
        from src.make_monitoring_data import generate
        generate()

    validar = validar_datos()
    ganador = entrenar_modelos()
    track = registrar_mlflow(ganador)
    monitor = generar_reporte()
    validar >> ganador >> track >> monitor

telco_training_pipeline()
