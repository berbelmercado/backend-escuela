"""
Schemas Pydantic para la entidad "Curso".

Este módulo define las estructuras de validación y serialización que usa FastAPI
para recibir y devolver datos relacionados con cursos.

Clases públicas:
- CursoBase: campos comunes a los esquemas de curso (entrada y salida).
- CursoCreate: esquema de entrada para crear un curso (hereda de CursoBase).
- CursoResponse: esquema de respuesta que incluye el id y mensaje adicional.
- CursoResponseGet: esquema de respuesta para métodos Get que incluye toda la información del curso.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from typing import Optional


class CursoBase(BaseModel):
    """
    Esquema base con los campos básicos de un curso.

    Atributos:
    - nombre (str): Nombre del curso.
    """

    nombre: str = Field(..., min_length=1, max_length=100)


class CursoCreate(CursoBase):
    """
    Esquema de entrada para crear un curso.
    Hereda todos los campos de CursoBase.
    """

    pass


class CursoResponse(CursoBase):
    """
    Esquema de respuesta usado cuando la API inserta la información de un curso.
    Incluye el id y un mensaje opcional.
    """

    id: UUID
    message: Optional[str] = None

    class Config:
        from_attributes = True


class CursoResponseGet(BaseModel):
    """
    Esquema de respuesta usado cuando la API consulta la información de uno o todos los cursos.
    """

    id: UUID = Field(..., alias="id_curso")
    nombre: str = Field(..., alias="nombre_curso")
    fecha_creacion: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True
