from sqlalchemy import Column, Float, ForeignKey, Integer, String

from database.config import Base
import uuid
from database.config import Base
from sqlalchemy import Column, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Calificaciones(Base):

    __tablename__ = "calificaciones"

    id_calificaciones = Column(Integer, primary_key=True, index=True)
    id_estudiante = Column(Integer, nullable=False)  # luego se puede poner ForeignKey
    id_profesor = Column(Integer, nullable=False)  # luego se puede poner ForeignKey
    descripcion = Column(String(200), nullable=False)
    valor = Column(Float, nullable=False)


id_estudiante = Column(
    Integer, ForeignKey("estudiantes.id_estudiantes"), nullable=False
)
