@echo off
cd /d "%~dp0.."
if not exist .venv\Scripts\python.exe (
  echo Primero ejecuta scripts\01_verificar_en_windows.bat
  pause
  exit /b 1
)
echo Abre http://127.0.0.1:8000/ o http://127.0.0.1:8000/docs
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
pause
