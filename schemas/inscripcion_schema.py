from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class InscripcionBase(BaseModel):
    id_curso: UUID
    id_asignatura: int
    id_estudiante: UUID
    id_profesor: UUID
    periodo: str = Field(..., min_length=1, max_length=50)


class InscripcionCreate(InscripcionBase):
    pass


class InscripcionResponse(InscripcionBase):
    id: int = Field(..., alias="id_inscripcion")
    message: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class InscripcionResponseGet(InscripcionResponse):
    pass
