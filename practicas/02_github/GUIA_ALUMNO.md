# Práctica 2 — GitHub

**Duración:** 120 minutos. **Modalidad:** individual, Windows + VS Code.

**Objetivo:** conocer y utilizar GitHub sin escribir de nuevo el modelo de ML. El CSV del proyecto es el original facilitado por el docente.

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

## Bloque 1 (0–25 min): preparar Git local

```bat
git init -b main
git config user.name "Tu Nombre"
git config user.email "tu-correo@example.com"
git add .
git commit -m "Proyecto inicial Telco"
```

## Bloque 2 (25–50 min): crear repositorio en GitHub

1. Entra a `https://github.com/new` e inicia sesión.
2. Nombre: `telco-curso-github`. Déjalo **Private** si no has verificado los términos de redistribución del CSV de Kaggle.
3. **No marques** README ni .gitignore; ya están incluidos.
4. Copia tu URL HTTPS y sustituye `TU_USUARIO`:

```bat
git remote add origin https://github.com/TU_USUARIO/telco-curso-github.git
git push -u origin main
```

**Comprueba:** README, `src`, `data` y `models` aparecen en el repositorio remoto.

## Bloque 3 (50–80 min): Pull Request

```bat
git switch -c feature/metricas
```

Agrega al final de README una frase sobre F1 y ROC-AUC. Después:

```bat
git add README.md
git commit -m "docs: explicar metricas"
git push -u origin feature/metricas
```

En GitHub usa **Compare & pull request** → crea un Pull Request a `main` → revisa **Files changed** → usa **Create a merge commit** (no squash) y confirma.

## Bloque 4 (80–105 min): sincronizar

```bat
git switch main
git pull origin main
git log --graph --oneline --all
```

## Bloque 5 (105–120 min): clonar en otra carpeta

En CMD, primero sitúate en una carpeta distinta (por ejemplo la carpeta `Documentos`):

```bat
cd %USERPROFILE%\Documents
git clone https://github.com/TU_USUARIO/telco-curso-github.git telco-clon
cd telco-clon
git status
```

**Entrega:** URL del repo privado o público según indicación docente; capturas de PR integrado, `git pull` y clon. Si el repo es privado, da acceso al docente por GitHub en vez de hacerlo público.

---

**Entrega:** adjunta capturas de los resultados indicados y un párrafo explicando qué problema resuelve la herramienta.
**Importante:** cuando aparezca un error, registra el mensaje completo antes de cambiar algo.
