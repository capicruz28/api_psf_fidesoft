@echo off
cd /d D:\fastapi_service
call venv\Scripts\activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
