@echo off
cd /d "%~dp0.."
echo === TELCO MLOPS: verificar proyecto local ===
python -m venv .venv
if errorlevel 1 goto error
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto error
.venv\Scripts\python.exe -m src.check_data
if errorlevel 1 goto error
.venv\Scripts\python.exe -m pytest -v
if errorlevel 1 goto error
echo.
echo TODO CORRECTO: CSV original, librerias y tests locales.
pause
exit /b 0
:error
echo.
echo Error: revisa el mensaje de arriba; confirma Python 3.11+ e internet para instalar dependencias.
pause
exit /b 1
