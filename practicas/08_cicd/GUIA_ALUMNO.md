# Práctica 8 — CI/CD con GitHub Actions

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar CI/CD con GitHub Actions sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

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

## Bloque 1 (0–25 min): comprobar proyecto local

```bat
.venv\Scripts\python.exe -m pytest -v
```

Comprueba que todas las pruebas pasan. El workflow real está en `.github/workflows/cicd.yml`.

## Bloque 2 (25–45 min): crear GitHub

Crea repositorio GitHub **vacío** `telco-churn-cicd` (privado si no has revisado términos de Kaggle). Sustituye `TU_USUARIO`:

```bat
git init -b main
git config user.name "Tu Nombre"
git config user.email "tu-correo@example.com"
git add .
git commit -m "Inicio CI CD"
git remote add origin https://github.com/TU_USUARIO/telco-churn-cicd.git
git push -u origin main
```

En **Actions** observa `test`, seguido por `docker` si el evento fue push a main. Un Pull Request ejecuta tests pero NO publica.

## Bloque 3 (45–70 min): fallo deliberado

En `tests/test_api.py` cambia `assert response.status_code == 200` de `test_health` a `== 404` y guarda:

```bat
git add tests/test_api.py
git commit -m "Ejercicio: fallo intencional"
git push origin main
```

**Comprueba:** job `test` rojo, job `docker` omitido. Corrige a `200`, guarda, commit y push:

```bat
git add tests/test_api.py
git commit -m "Corregir test"
git push origin main
```

## Bloque 4 (70–100 min): verificar GHCR

En GitHub busca el paquete publicado por el workflow. La URI estará en minúsculas:

`ghcr.io/TU_USUARIO/telco-churn-cicd:latest` (sustituye usuario y usa minúsculas).

Si es privado, requiere autenticación con permisos; si es público, no debería requerir login. GHCR puede requerir ajustes de acceso según políticas de la cuenta u organización.

## Bloque 5 (100–120 min): probar imagen publicada

```bat
docker pull ghcr.io/tu_usuario/telco-churn-cicd:latest
docker run --rm -p 8000:8000 ghcr.io/tu_usuario/telco-churn-cicd:latest
```

Abre `http://localhost:8000/docs`. **Entrega:** ejecución verde, roja, verde; GHCR y predicción en Docker.

**Nota de vocabulario:** este ejercicio implementa CI y entrega de una imagen; ejecutar el contenedor local es un despliegue manual, no Continuous Deployment automático.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
