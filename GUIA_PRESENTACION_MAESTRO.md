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
