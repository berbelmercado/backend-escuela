import uuid
from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relación con la tabla de cursos (muchos a muchos)
    cursos = relationship(
        "Curso", secondary="estudiante_curso", back_populates="estudiantes"
    )

    def __repr__(self):
        return f"<Estudiante(id={self.id}, nombre={self.nombre}, apellido={self.apellido}, email={self.email})>"
