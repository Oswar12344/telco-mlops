# Práctica 1 — Git

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar Git sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

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

## Bloque 1 (0–30 min): iniciar y guardar una versión

Antes de usar Git abre `src/train_models.py` y verifica que ya existen Logistic, Forest y SVM. No modifiques el código de entrenamiento.

```bat
git init -b main
git config user.name "Tu Nombre"
git config user.email "tu-correo@example.com"
git status
git add .
git commit -m "Inicio: clasificador Telco"
git log --oneline
```

**Comprueba:** aparece un commit y `git status` indica árbol limpio.

## Bloque 2 (30–60 min): crear ramas divergentes

```bat
git switch -c feature/documentacion
```

Abre `README.md`, agrega `Modelo SVM: clasificador de margen máximo.` al final, guarda y registra:

```bat
git add README.md
git commit -m "docs: agregar SVM"
git switch main
```

Ahora abre `GUIA_ALUMNO.md`, agrega al final `Revisión de conceptos de Git.` y registra:

```bat
git add GUIA_ALUMNO.md
git commit -m "docs: agregar revisión"
```

## Bloque 3 (60–85 min): merge no fast-forward

```bat
git merge --no-ff feature/documentacion -m "merge: documentacion"
git log --graph --oneline --all --decorate
```

**Comprueba:** hay un commit de merge con dos líneas de historial.

## Bloque 4 (85–105 min): conflicto deliberado

En `main` cambia la primera línea del `README.md` a `# Proyecto Telco — main`, guarda:

```bat
git add README.md
git commit -m "docs: titulo main"
git switch -c feature/titulo HEAD~1
```

Ahora cambia esa misma primera línea a `# Proyecto Telco — rama`, guarda y ejecuta:

```bat
git add README.md
git commit -m "docs: titulo en rama"
git switch main
git merge --no-ff feature/titulo
```

**Comprueba:** Git marca `CONFLICT` en README. En VS Code elimina los marcadores `<<<<<<<`, `=======`, `>>>>>>>`, conserva un solo título, y concluye:

```bat
git add README.md
git commit -m "merge: resolver conflicto"
```

## Bloque 5 (105–120 min): recuperar un cambio no guardado

Agrega texto temporal al README, guarda y ejecuta:

```bat
git diff
git restore README.md
git status
git log --oneline --graph --all
```

**Entrega:** captura de `git status` limpio, historial con dos merges y captura de conflicto antes de resolverlo. `git restore` descarta cambios sin commit.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
