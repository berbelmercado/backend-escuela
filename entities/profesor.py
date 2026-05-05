import uuid
from database.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    cedula = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    sexo = Column(String(20), nullable=False)
    edad = Column(Integer, nullable=False)
    inscripciones = relationship("Inscripcion", back_populates="profesor")
    calificaciones = relationship("Calificaciones", back_populates="profesor")
