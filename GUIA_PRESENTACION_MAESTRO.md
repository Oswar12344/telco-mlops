# Guía de presentación al maestro — Telco MLOps

**Repositorio:** https://github.com/Oswar12344/telco-mlops  
**Entorno de la demostración:** Windows, PowerShell de VS Code, Docker Desktop.  
**Importante:** no mostrar ni compartir el token de GitHub. La imagen GHCR puede requerir acceso porque el paquete es privado.

## 1. Qué hace el proyecto

Se trabaja con el dataset Telco Customer Churn (7043 registros) para predecir si un cliente podría abandonar el servicio. El proyecto integra un modelo de clasificación, FastAPI, Docker, GitHub y GitHub Actions. Las herramientas DVC, MLflow, Airflow y Evidently tienen prácticas específicas.

La predicción no es certeza ni sistema comercial; es un ejercicio educativo.

## 2. Preparar la computadora antes de la exposición

1. Abrir **Docker Desktop** y comprobar que el motor esté funcionando.
2. Abrir **Visual Studio Code** > **Terminal** > **New Terminal** (PowerShell).
3. Comprobar Docker:

```powershell
docker --version
docker info
```

4. Ver los contenedores disponibles (opcional):

```powershell
docker ps -a
```

## 3. Encender la aplicación que ya está instalada

En la computadora donde ya ejecutamos la práctica, el contenedor se llama `telco-api` y utiliza el puerto **8001**.

```powershell
docker start telco-api
```

Comprobar que está activo:

```powershell
docker ps
```

Abrir:
- Formulario: http://localhost:8001/
- Documentación FastAPI (Swagger): http://localhost:8001/docs
- Salud de la API: http://localhost:8001/health

La respuesta de `/health` debe ser:

```json
{"status":"ok","model_loaded":true}
```

## 4. Demostrar una predicción

Ingresar en el formulario:

| Campo | Valor |
| --- | --- |
| Antigüedad (meses) | 2 |
| Cargo mensual ($) | 85 |
| Cargo total ($) | 170 |
| Contrato | Month-to-month |
| Servicio de internet | Fiber optic |

Pulsar **Calcular predicción**.

Resultado obtenido en la comprobación del equipo:

```json
{
  "prediction": 1,
  "churn_probability": 0.702736,
  "risk_level": "Alto",
  "message": "Se predice abandono"
}
```

**Cómo explicarlo:** `prediction=1` significa que el modelo predice abandono para este ejemplo. La probabilidad estimada fue **70.27 %**, clasificada como **riesgo alto** según los umbrales didácticos de la aplicación.

## 5. Apagar o reiniciar

Detener sin borrar:

```powershell
docker stop telco-api
```

Volver a encender más adelante:

```powershell
docker start telco-api
```

Consultar registros si no abre la página:

```powershell
docker logs telco-api
```

## 6. Si hay que preparar otra computadora desde cero

1. Instalar y abrir Docker Desktop.
2. Si la imagen GHCR es privada, crear un **Personal Access Token (classic)** con el permiso mínimo `read:packages` en https://github.com/settings/tokens . **No activar `write:packages` para descargar.**
3. Ejecutar este comando, y cuando aparezca `Password:`, pegar el token sin ponerlo directamente en la línea del comando:

```powershell
docker login ghcr.io -u Oswar12344
```

4. Descargar la imagen:

```powershell
docker pull ghcr.io/oswar12344/telco-mlops:latest
```

5. Crear y arrancar el contenedor usando el puerto 8001:

```powershell
docker run -d --name telco-api -p 8001:8000 ghcr.io/oswar12344/telco-mlops:latest
```

Si el nombre `telco-api` ya existe pero el contenedor está detenido, usar `docker start telco-api` en vez de `docker run`. Si el puerto 8001 está ocupado por otro programa, puede cambiarse el primer número, por ejemplo `-p 8002:8000`, y abrir `localhost:8002`.

Nunca compartir contraseñas, tokens o capturas que los expongan.

## 7. Explicar la automatización de GitHub

En https://github.com/Oswar12344/telco-mlops abrir la pestaña **Actions**.

- **Importar ZIP del curso MLOps** extrajo el proyecto y las nueve prácticas y ejecutó seis pruebas, con resultado exitoso.
- **Telco CI CD** instaló dependencias, ejecutó las pruebas, construyó la imagen Docker y la publicó en `ghcr.io/oswar12344/telco-mlops:latest`; resultado exitoso.
- La publicación de la imagen no equivale a desplegar la API en un servidor público: esta demostración funciona localmente con Docker Desktop.

Ejecución verificada: https://github.com/Oswar12344/telco-mlops/actions/runs/44101997334

## 8. Práctica 03: DVC — cómo prepararla

**Usar la práctica independiente** `practicas/03_dvc` **fuera de la carpeta de un clon Git existente**, para que `git init` cree un repositorio nuevo solo para esa práctica.

En GitHub abrir `Code > Download ZIP`, descomprimir el repositorio y copiar la carpeta `practicas/03_dvc` a una ubicación independiente (por ejemplo, `Documentos\Telco_DVC_Practica`). Abrir **esa carpeta** en VS Code y usar la terminal integrada. Comprobar:

```powershell
python --version
git --version
```

Crear el entorno, instalar dependencias y validar los datos:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\python.exe --version
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m src.check_data
```

Se espera: `Dataset válido: 7043 filas; TotalCharges vacíos: 11`.

Instalar DVC e inicializar Git/DVC (completar nombre y correo con los propios):

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-dvc.txt
git init -b main
git config user.name "Tu Nombre"
git config user.email "tu-correo@example.com"
.venv\Scripts\dvc.exe init
```

Versionar la primera copia del dataset:

```powershell
.venv\Scripts\dvc.exe add data/raw/telco.csv
git add .
git commit -m "DVC: version 1 del CSV"
```

DVC almacena el contenido del CSV en la caché; Git versiona el archivo descriptor `data/raw/telco.csv.dvc` y la configuración, no el CSV versionado por DVC.

### Pasos posteriores de DVC (realizarlos en orden)

Almacenamiento remoto local:

```powershell
mkdir ..\dvc_storage
.venv\Scripts\dvc.exe remote add -d storage ..\dvc_storage
git add .dvc/config
git commit -m "DVC: configurar remoto local"
.venv\Scripts\dvc.exe push
```

Segunda versión de ejemplo:

```powershell
.venv\Scripts\python.exe -m src.data_change
.venv\Scripts\dvc.exe status
.venv\Scripts\dvc.exe add data/raw/telco.csv
git add data/raw/telco.csv.dvc
git commit -m "DVC: version 2 del CSV"
.venv\Scripts\dvc.exe push
```

Restaurar versiones:

```powershell
git restore --source=HEAD~1 -- data/raw/telco.csv.dvc
.venv\Scripts\dvc.exe checkout
git restore --source=HEAD -- data/raw/telco.csv.dvc
.venv\Scripts\dvc.exe checkout
.venv\Scripts\dvc.exe status
```

**Durante la clase:** realizar cada bloque uno por uno; no ejecutar todos los comandos sin verificar sus salidas. Esta secuencia corresponde a la guía de `practicas/03_dvc/GUIA_ALUMNO.md`.


### Evidencia real de la práctica completada en Windows (18/11/2026)

Se ejecutó en `C:\Users\Admin\Downloads\03_dvc` con **Python 3.11.9** y **DVC 3.67.1**. La validación inicial devolvió `Dataset válido: 7043 filas; TotalCharges vacíos: 11`.

- Commit inicial: `26238cb` — `DVC: version 1 del CSV` (valor inicial de `MonthlyCharges` en la primera fila: **29.85**).
- Commit de configuración: `ed99cb3` — `DVC: configurar remoto local`.
- `dvc push` de la primera versión: **`1 file pushed`**.
- Script de modificación: `MonthlyCharges fila 1: 29.85 -> 31.85`.
- `dvc status` tras modificar: `modified: data\\raw\\telco.csv`.
- Commit de segunda versión: `4fcf38a` — `DVC: version 2 del CSV`.
- `dvc push` de la segunda versión: **`1 file pushed`**.
- Tras restaurar el descriptor de la versión 1 y ejecutar `dvc checkout`, la verificación de Python mostró **29.85**.
- Tras restaurar el descriptor de la versión 2 y ejecutar `dvc checkout`, la verificación mostró **31.85**.
- Comprobación final: **`Data and pipelines are up to date.`**

Para verificar el valor del primer registro durante la presentación:

```powershell
.\.venv\Scripts\python.exe -c "import pandas as pd; df=pd.read_csv('data/raw/telco.csv'); print('MonthlyCharges fila 1:', df.loc[0, 'MonthlyCharges'])"
```

**Estado final verificado:** versión 2 restaurada, CSV con `MonthlyCharges = 31.85` en la primera fila y DVC sincronizado. La carpeta `dvc_storage` está en `C:\Users\Admin\Downloads\dvc_storage`. Los commits citados son **locales de la práctica independiente** y no deben confundirse con los commits del repositorio remoto de GitHub.

## Práctica 04: MLflow — ejecución verificada en Windows (18/11/2026)

En `C:\Users\Admin\Downloads\04_mlflow`, con Python 3.11.9 y MLflow 3.18.0, se verificó el dataset: **7043 filas, 11 TotalCharges vacíos**.

Para iniciar el servidor, abrir una terminal de VS Code y dejarla activa:

```powershell
.\.venv\Scripts\python.exe -m mlflow server --host 127.0.0.1 --port 5000
```

Abrir http://127.0.0.1:5000. En una **segunda terminal**, ejecutar:

```powershell
.\.venv\Scripts\python.exe -m src.mlflow_tracking
```

El código original falló al registrar los modelos porque MLflow 3.18.0 requiere autorización para tipos usados por `skops`. En `src/mlflow_tracking.py`, la llamada a `mlflow.sklearn.log_model(...)` se corrigió incluyendo:

```python
skops_trusted_types=["numpy.dtype", "sklearn.tree._tree.Tree"]
```

**Solo confiar en estos tipos para modelos de procedencia conocida**; los archivos de la práctica son artefactos locales confiados por el usuario.

**Resultados reales confirmados:** se registraron `logistic`, `forest` y `svm`, sin excepción final. MLflow creó el modelo registrado **`TelcoChurnClassifier`**, versión **1**, alias **`champion`**, y seleccionó **`forest` (Random Forest)**. Mensaje: `Champion: forest | Registry: TelcoChurnClassifier v1 alias champion`.

La advertencia de MLflow sobre inferencia del esquema con columnas enteras y posibles valores ausentes es informativa para esta ejecución; no impidió el registro, pero debe revisarse si se usan entradas con valores faltantes en producción. Los intentos fallidos previos pueden aparecer en el historial del experimento y no deben confundirse con los tres registros exitosos de la última ejecución.

## 9. Mini-guion para presentar

> «Este proyecto muestra un proceso MLOps con datos reales de Telco Churn. El código y las prácticas están en GitHub. GitHub Actions ejecuta pruebas automáticas y publica nuestra imagen Docker. Ahora arrancaré la aplicación en Docker Desktop, mostraré la documentación de FastAPI y solicitaré una predicción de abandono. La API también tiene una ruta de salud para comprobar que el modelo está cargado. En DVC veremos cómo versionar el dataset de manera reproducible sin almacenar todas las versiones del CSV directamente en Git».

## 10. Checklist antes de exponer

- [ ] Docker Desktop abierto.
- [ ] `docker start telco-api` ejecutado.
- [ ] Formulario `http://localhost:8001/` accesible.
- [ ] `/health` devuelve `model_loaded: true`.
- [ ] Predicción de prueba completada.
- [ ] GitHub Actions disponible para mostrar evidencia.
- [ ] Carpeta DVC independiente abierta en VS Code si se presentará esa práctica.
- [ ] Al finalizar, ejecutar `docker stop telco-api`.


## Práctica 05 — Airflow y MLflow en Docker (verificado 19/11/2026)

**Entorno:** Windows, VS Code, carpeta independiente `C:\Users\Admin\Downloads\05_airflow`, Docker Desktop Linux.

1. `docker info` confirmó Docker Engine 29.9.2, Docker Compose 5.6.1 y modo `desktop-linux`.
2. `docker compose up -d --build` construyó e inició los servicios `airflow` y `mlflow`. `docker compose ps` confirmó Airflow en puerto **8080** y MLflow saludable en puerto **5000**.
3. Abrir http://localhost:8080. La instalación utiliza `SimpleAuthManager`; las credenciales generadas se consultaron dentro del contenedor con `docker compose exec airflow cat /opt/airflow/simple_auth_manager_passwords.json.generated`. **No divulgar contraseñas.**
4. En Airflow localizar `telco_training_pipeline` (etiquetas `mlops`, `telco`) y sus cuatro tareas: `validar_datos`, `entrenar_modelos`, `registrar_mlflow`, `generar_reporte`.
5. **Primer fallo observado:** `registrar_mlflow` devolvió HTTP 403 `Invalid Host header - possible DNS rebinding attack detected`. Se corrigió `compose.yaml` añadiendo al servicio `mlflow`:

   ```yaml
   environment:
     MLFLOW_SERVER_ALLOWED_HOSTS: "mlflow:5000,localhost:*,127.0.0.1:*"
   ```

   Aplicar con `docker compose up -d --force-recreate mlflow` (sin `down -v`). Comprobaciones: `docker compose ps`, `docker compose exec airflow python -c "import urllib.request; r=urllib.request.urlopen('http://mlflow:5000/health'); print(r.status)"` devolvió **200** y `docker compose exec airflow python -c "import mlflow; mlflow.set_tracking_uri('http://mlflow:5000'); print([e.name for e in mlflow.search_experiments()])"` devolvió **['Default']** sin error 403.
6. **Segundo fallo observado:** el registro de modelos rechazó el tipo `numpy.dtype` en `skops`. En `src/mlflow_tracking.py`, dentro de `mlflow.sklearn.log_model(...)`, se añadió:

   ```python
   skops_trusted_types=["numpy.dtype", "sklearn.tree._tree.Tree"]
   ```

   Autorizar estos tipos **solo con modelos de origen confiable**. El archivo `src` está montado como volumen; no hizo falta reconstruir imágenes. Se verificó con `docker compose exec airflow grep -n skops_trusted_types /opt/airflow/project/src/mlflow_tracking.py`.
7. **Resultado confirmado por el usuario:** al volver a activar el DAG, **las cuatro tareas aparecieron en verde (éxito)**. Esta es la ejecución que se debe mostrar en la exposición. Las ejecuciones anteriores fallidas sirven para explicar depuración y recuperación.

**Para presentar:** «Airflow orquesta la validación, el entrenamiento, el registro de modelos en MLflow y la generación del reporte. Corregimos dos errores reales de integración y comprobamos una ejecución completa con las cuatro tareas exitosas».

**Cierre:** desde `05_airflow`, `docker compose down` detiene los servicios conservando los volúmenes. No utilizar `docker compose down -v`.


## Práctica 06 — FastAPI + HTML (verificado 19/11/2026)

**Entorno:** Windows, VS Code, `C:\Users\Admin\Downloads\06_fastapi`, Python 3.11.9.

1. Crear entorno virtual: `python -m venv .venv`. Instalar dependencias: `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.
2. Verificar dataset: `.\.venv\Scripts\python.exe -m src.check_data` → **`Dataset válido: 7043 filas; TotalCharges vacíos: 11`**.
3. Al iniciar Uvicorn en el puerto predeterminado 8000, Windows devolvió **`[WinError 10013] Intento de acceso a un socket no permitido por sus permisos de acceso`**. Se resolvió usando el puerto **8001**:
   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
   ```
   Confirmado: `Application startup complete`. Mantener la terminal abierta durante las pruebas.
4. Formulario HTML: http://127.0.0.1:8001/ — accesible y operativo. Documentación Swagger: http://127.0.0.1:8001/docs — `POST /predict` visible.
5. Solicitud válida en Swagger y en el formulario:
   ```json
   {"tenure":5,"MonthlyCharges":85.5,"TotalCharges":427.5,"Contract":"Month-to-month","InternetService":"Fiber optic"}
   ```
   **HTTP 200**; ambos devolvieron la misma respuesta:
   ```json
   {"prediction":1,"churn_probability":0.711133,"risk_level":"Alto","message":"Se predice abandono"}
   ```
   Interpretación: probabilidad estimada de abandono **71.11 %**, riesgo **Alto**. El formulario advierte que las probabilidades y bandas son didácticas, no un sistema comercial.
6. Health check: http://127.0.0.1:8001/health → **`{"status":"ok","model_loaded":true}`**.
7. Validación: repetir la solicitud con `"tenure":-10` → **HTTP 422**; respuesta: `Input should be greater than or equal to 0` para `body.tenure`. FastAPI rechaza el valor inválido.
8. Pruebas automatizadas en segunda terminal:
   ```powershell
   .\.venv\Scripts\python.exe -m pytest -q
   ```
   Resultado real: **`6 passed, 1 warning in 2.32s`**. La única advertencia es `DeprecationWarning` de `starlette.testclient` / AnyIO; no fallaron pruebas.
9. Detener servidor con **Ctrl+C** en la primera terminal: `Application shutdown complete`, `Finished server process` y `Stopping reloader process` confirmados.

**Para presentar:** «Con FastAPI publicamos el modelo de abandono de clientes como API REST y formulario web. Probamos la predicción por Swagger y HTML, comprobamos la carga del modelo mediante /health, validamos entradas incorrectas con HTTP 422 y ejecutamos seis pruebas automáticas exitosas. El puerto 8000 estaba restringido en Windows, por lo que usamos 8001».

**Estado:** funcionamiento principal verificado. Las actividades opcionales de editar el encabezado HTML y cambiar temporalmente el umbral de riesgo no se realizaron; no presentarlas como verificadas.
