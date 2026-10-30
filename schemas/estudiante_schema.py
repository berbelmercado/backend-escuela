"""
Schemas Pydantic para la entidad "Estudiante".

Este módulo define las estructuras de validación y serialización que usa FastAPI
para recibir y devolver datos relacionados con estudiantes.

Clases públicas:
- EstudianteBase: campos comunes a los esquemas de estudiante (entrada y salida).
- EstudianteCreate: esquema de entrada para crear un estudiante (hereda de EstudianteBase).
- EstudianteResponse: esquema de respuesta que incluye el id y mensaje adicional.
- EstudianteResponseGet: esquema de respuesta para métodos Get que incluye toda la información del estudiante.
"""

from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime
from uuid import UUID
from typing import Optional


class EstudianteBase(BaseModel):
    """
    Esquema base con los campos básicos de un estudiante.

    Atributos:
    - cedula (str): Número de cédula del estudiante.
    - nombre (str): Nombre del estudiante.
    - apellido (str): Apellido del estudiante.
    - email (EmailStr): Correo electrónico único del estudiante.
    - sexo (str): Sexo del estudiante (M/F u otro).
    - fecha_nacimiento (date): Fecha de nacimiento.
    - no_celular (str | None): Número de celular (opcional).
    """

    cedula: str = Field(..., min_length=1, max_length=20)
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    sexo: str = Field(..., min_length=1, max_length=8)
    fecha_nacimiento: date
    no_celular: Optional[str] = Field(None, max_length=20)


class EstudianteCreate(EstudianteBase):
    """
    Esquema de entrada para crear un estudiante.
    Hereda todos los campos de EstudianteBase.
    """

    pass


class EstudianteResponse(EstudianteBase):
    """
    Esquema de respuesta usado cuando la API inserta o actualiza la información de un estudiante.
    Incluye el id y un mensaje opcional.
    """

    id: UUID
    message: Optional[str] = None

    class Config:
        from_attributes = True


class EstudianteResponseGet(BaseModel):
    """
    Esquema de respuesta usado cuando la API consulta la información de uno o todos los estudiantes.
    """

    id: UUID = Field(..., alias="id_estudiante")
    cedula: str
    nombre: str
    apellido: str
    email: str
    sexo: str
    fecha_nacimiento: date
    no_celular: Optional[str] = None
    fecha_creacion: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True
