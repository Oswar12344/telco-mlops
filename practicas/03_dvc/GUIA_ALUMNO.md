# Práctica 3 — DVC

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar DVC sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

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

## Bloque 1 (0–30 min): inicialización

Instala DVC (en la misma `.venv`):

```bat
.venv\Scripts\python.exe -m pip install -r requirements-dvc.txt
git init -b main
git config user.name "Tu Nombre"
git config user.email "tu-correo@example.com"
.venv\Scripts\dvc.exe init
```

Si `dvc.exe` no aparece, cierra y vuelve a abrir terminal y usa `dvc init` con el entorno activado.

## Bloque 2 (30–50 min): versionar Kaggle

```bat
.venv\Scripts\dvc.exe add data/raw/telco.csv
git add .
git commit -m "DVC: version 1 del CSV"
```

Abre `data/raw/telco.csv.dvc`: contiene la huella del dataset, no las filas. Verifica que `data/raw/.gitignore` ignora el CSV.

## Bloque 3 (50–70 min): almacenamiento remoto local

```bat
mkdir ..\dvc_storage
.venv\Scripts\dvc.exe remote add -d storage ..\dvc_storage
git add .dvc/config
git commit -m "DVC: configurar remoto local"
.venv\Scripts\dvc.exe push
```

El 'remoto' es una carpeta fuera del proyecto; no necesita internet.

## Bloque 4 (70–95 min): segunda versión

```bat
.venv\Scripts\python.exe -m src.data_change
.venv\Scripts\dvc.exe status
.venv\Scripts\dvc.exe add data/raw/telco.csv
git add data/raw/telco.csv.dvc
git commit -m "DVC: version 2 del CSV"
.venv\Scripts\dvc.exe push
```

**Comprueba:** cambia el hash en `.dvc` y `git log` muestra los commits.

## Bloque 5 (95–120 min): recuperar versiones

```bat
git restore --source=HEAD~1 -- data/raw/telco.csv.dvc
.venv\Scripts\dvc.exe checkout
```

Comprueba `MonthlyCharges` en la primera fila, luego:

```bat
git restore --source=HEAD -- data/raw/telco.csv.dvc
.venv\Scripts\dvc.exe checkout
.venv\Scripts\dvc.exe pull
```

**Entrega:** `.dvc` de versiones 1 y 2, hash cambiado, resultados de push/pull, archivo restaurado. Si Git rechaza `git add .` por un archivo generado, revisa primero `git status`.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
