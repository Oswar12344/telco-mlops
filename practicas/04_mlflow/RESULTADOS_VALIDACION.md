# Resultado de las verificaciones ejecutadas

**Dataset de origen:** exactamente el CSV `WA_Fn-UseC_-Telco-Customer-Churn.csv` proporcionado en `Dataset.zip`.

- 7043 filas y 21 columnas.
- 11 valores vacíos en la columna `TotalCharges`.
- `Churn`: 5174 No, 1869 Yes.
- Se compararon Logistic, Forest y SVM por ROC-AUC en validación.
- Validación: Logistic `0.8446`, Forest `0.8462`, SVM `0.7759`.
- Champion: **Random Forest**.
- Test reservado: Accuracy `0.7956`, Precision `0.6547`, Recall `0.4866`, F1 `0.5583`, ROC-AUC `0.8326`.
- Ejecución de `python -m pytest -q`: **6 passed**.
- Se comprobó `python -m src.predict_example` sobre modelo Champion.
- Se generaron los datos de referencia y el cambio simulado para monitoreo.
- Se extrajo por separado el ZIP de Práctica 08 y pasaron las mismas 6 pruebas.
- Se revisó la sintaxis Python con `compileall`; se analizaron compose.yaml y CI/CD YAML.

**No comprobado aquí:** instalación de MLflow, DVC, Evidently, Docker Desktop, Airflow y publicación real en GitHub/GHCR. Este entorno no tiene Docker y no permite instalar nuevos paquetes desde PyPI. Se incluyeron instrucciones y configuraciones; es imprescindible que el docente verifique estas partes en su PC antes de dictar las clases.
