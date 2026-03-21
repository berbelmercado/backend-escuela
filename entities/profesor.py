from sqlalchemy import Column, Integer, String

from database.config import Base
import uuid
from database.config import Base
from sqlalchemy import Column, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Profesor(Base):
    __tablename__ = "profesor"

    id_profesor = Column(Integer, primary_key=True, index=True)
    cedula_profesor = Column(String(20), unique=True, nullable=False)
    nombre_profesor = Column(String(100), nullable=False)
    apellido_profesor = Column(String(100), nullable=False)
    sexo_profesor = Column(String(10), nullable=False)
    edad = Column(Integer, nullable=False)
