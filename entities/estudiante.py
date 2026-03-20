import uuid
from database.config import Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Estudiante(Base):

    __tablename__ = "estudiantes"

    id_estudiante = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    cedula = Column(String(20), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email_estudiante = Column(String(255), unique=True, nullable=False)
    sexo_estudiante = Column(String(8), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    no_celular = Column(String(20), nullable=True)
    fecha_creacion = Column(DateTime, server_default=func.now())
