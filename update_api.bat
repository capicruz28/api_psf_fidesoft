@echo off
cd /d D:\fastapi_service
net stop FastAPI_Service
git pull
call venv\Scripts\activate
pip install -r requirements.txt
net start FastAPI_Service
echo Actualización completada.
pause
