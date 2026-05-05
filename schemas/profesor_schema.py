from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class ProfesorBase(BaseModel):
    cedula: str = Field(..., min_length=1, max_length=20)
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    sexo: str = Field(..., min_length=1, max_length=20)
    edad: int = Field(..., ge=0)


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorResponse(ProfesorBase):
    id: UUID = Field(..., alias="id_profesor")
    message: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class ProfesorResponseGet(ProfesorResponse):
    pass
