# Integración GitHub Actions — Telco MLOps

Repositorio de la práctica: `Oswar12344/telco-mlops`.

## Flujo de integración continua
1. Al cambiar cualquier archivo dentro de `proyecto_integrado/` en `main`, GitHub Actions ejecuta `.github/workflows/cicd.yml`.
2. El job `pruebas` configura Python 3.11, instala `requirements.txt` y ejecuta `python -m pytest -v`.
3. Si todas las pruebas pasan, el job `imagen_docker` construye la imagen del `Dockerfile` y la publica en GitHub Container Registry (GHCR) con etiquetas `latest` y el SHA del commit.

## Dónde verificar el resultado
- GitHub → repositorio → pestaña **Actions** → workflow **Telco CI CD**.
- Cada ejecución incluye los jobs `pruebas` e `imagen_docker`.
- La imagen esperada es `ghcr.io/oswar12344/telco-mlops:latest`; si el paquete queda privado, su descarga externa requiere autenticación.

## Probar localmente con Docker Desktop
En PowerShell o CMD, después de arrancar Docker Desktop:

```powershell
docker pull ghcr.io/oswar12344/telco-mlops:latest
docker run --rm -p 8000:8000 ghcr.io/oswar12344/telco-mlops:latest
```

Abrir `http://localhost:8000/docs` y `http://localhost:8000/health`.

## Observaciones
- Publicar una imagen no significa que esté desplegada automáticamente en un servidor externo.
- La primera publicación puede depender de los permisos del repositorio y de GitHub Packages.
- Las comprobaciones de DVC, MLflow, Airflow y Evidently se realizan en prácticas separadas.
