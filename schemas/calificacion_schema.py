from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class CalificacionBase(BaseModel):
    id_estudiante: UUID
    id_profesor: UUID
    id_asignatura: int
    descripcion_nota: str = Field(..., min_length=1, max_length=200)
    valor_nota: float


class CalificacionCreate(CalificacionBase):
    pass


class CalificacionResponse(CalificacionBase):
    id: int = Field(..., alias="id_calificacion")
    message: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class CalificacionResponseGet(CalificacionResponse):
    pass
