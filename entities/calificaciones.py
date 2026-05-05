from database.config import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Calificaciones(Base):
    __tablename__ = "calificaciones"

    id_calificacion = Column(Integer, primary_key=True, index=True)
    id_estudiante = Column(
        UUID(as_uuid=True), ForeignKey("estudiantes.id_estudiante"), nullable=False
    )
    id_profesor = Column(
        UUID(as_uuid=True), ForeignKey("profesores.id_profesor"), nullable=False
    )
    id_asignatura = Column(
        Integer, ForeignKey("asignatura.id_asignatura"), nullable=False
    )
    descripcion_nota = Column(String(200), nullable=False)
    valor_nota = Column(Float, nullable=False)
    estudiante = relationship("Estudiante", back_populates="calificaciones")
    profesor = relationship("Profesor", back_populates="calificaciones")
    asignatura = relationship("Asignatura", back_populates="calificaciones")
