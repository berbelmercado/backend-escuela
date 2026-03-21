from sqlalchemy import Column, Integer, String

from unittest.mock import Base


from database.config import Base
import uuid
from database.config import Base
from sqlalchemy import Column, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Inscripcion(Base):
    __tablename__ = "inscripcion"

    id_inscripcion = Column(Integer, primary_key=True, index=True)
    id_grado = Column(Integer, nullable=False)
    id_asignatura = Column(Integer, nullable=False)
    id_estudiante = Column(Integer, nullable=False)
    id_profesor = Column(Integer, nullable=False)
    periodo = Column(String(50), nullable=False)
