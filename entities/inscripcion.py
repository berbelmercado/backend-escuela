from database.config import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Inscripcion(Base):
    __tablename__ = "inscripcion"

    id_inscripcion = Column(Integer, primary_key=True, index=True)
    id_curso = Column(UUID(as_uuid=True), ForeignKey("curso.id_curso"), nullable=False)
    id_asignatura = Column(
        Integer, ForeignKey("asignatura.id_asignatura"), nullable=False
    )
    id_estudiante = Column(
        UUID(as_uuid=True), ForeignKey("estudiantes.id_estudiante"), nullable=False
    )
    id_profesor = Column(
        UUID(as_uuid=True), ForeignKey("profesores.id_profesor"), nullable=False
    )
    periodo = Column(String(50), nullable=False)
    curso = relationship("Curso", back_populates="inscripciones")
    asignatura = relationship("Asignatura", back_populates="inscripciones")
    estudiante = relationship("Estudiante", back_populates="inscripciones")
    profesor = relationship("Profesor", back_populates="inscripciones")
