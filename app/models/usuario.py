# app/models/usuario.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class UsuarioModel(BaseModel):
    usuario_id: int
    nombre_usuario: str
    correo: EmailStr
    contrasena: str
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    es_activo: bool = True
    correo_confirmado: bool = False
    fecha_creacion: datetime
    fecha_ultimo_acceso: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
    es_eliminado: bool = False

    class Config:
        from_attributes = True