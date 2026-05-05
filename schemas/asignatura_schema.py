from pydantic import BaseModel, Field
from typing import Optional


class AsignaturaBase(BaseModel):
    nombre_asignatura: str = Field(..., min_length=1, max_length=100)
    horas_semanales: int = Field(..., ge=1)
    modalidad: str = Field(..., min_length=1, max_length=50)
    estado: bool


class AsignaturaCreate(AsignaturaBase):
    pass


class AsignaturaResponse(AsignaturaBase):
    id: int = Field(..., alias="id_asignatura")
    message: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class AsignaturaResponseGet(AsignaturaResponse):
    pass
