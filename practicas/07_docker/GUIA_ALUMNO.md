# Práctica 7 — Docker

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar Docker sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

## Preparación común (CMD o PowerShell en VS Code)

1. Descomprime **este ZIP** y abre la carpeta resultante en VS Code.
2. Abre **Terminal > New Terminal**.
3. Comprueba `python --version` y `git --version` (Git solo donde se use).
4. Crea el entorno e instala dependencias (una sola vez):

```bat
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m src.check_data
```

**Debes ver:** `Dataset válido: 7043 filas; TotalCharges vacíos: 11`. El archivo real de Kaggle ya está en `data/raw/telco.csv`; no necesitas descargarlo otra vez.

**Nota:** si Windows no encuentra `python`, instala Python 3.11 y abre de nuevo la terminal. No uses la carpeta `.venv` de otra práctica.

## Bloque 1 (0–25 min): entender el problema

Comprueba que `Dockerfile`, `.dockerignore`, `app/`, `models/champion.joblib` y `templates/index.html` están incluidos. Sin un entorno Python con librerías, FastAPI no se ejecuta; Docker encapsula estas dependencias.

## Bloque 2 (25–55 min): construir imagen

Abre Docker Desktop con motor Linux y ejecuta:

```bat
docker info
docker build -t telco-api:v1 .
docker images
```

Comprueba que existe imagen `telco-api:v1`. Lee el Dockerfile y explica `FROM`, `COPY`, `RUN`, `EXPOSE`, `CMD`.

## Bloque 3 (55–80 min): contenedor y predicción

```bat
docker run -d --name telco-v1 -p 8000:8000 telco-api:v1
docker ps
docker logs telco-v1
```

Abre `http://localhost:8000/docs`, envía una predicción y comprueba `/health`.

## Bloque 4 (80–100 min): puerto distinto

```bat
docker stop telco-v1
docker rm telco-v1
docker run -d --name telco-9000 -p 9000:8000 telco-api:v1
```

Comprueba `http://localhost:9000/`.

## Bloque 5 (100–120 min): etiqueta v2

En `app/main.py` cambia el título de FastAPI a `Telco API v2`, reconstruye:

```bat
docker build -t telco-api:v2 .
docker images
docker stop telco-9000
docker rm telco-9000
docker run -d --name telco-v2 -p 9000:8000 telco-api:v2
```

Al terminar `docker stop telco-v2` y `docker rm telco-v2`. **Entrega:** imágenes v1/v2, logs y aplicación en puerto 9000.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
