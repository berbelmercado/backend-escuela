from database.config import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class Asignatura(Base):
    __tablename__ = "asignatura"

    id_asignatura = Column(Integer, primary_key=True, index=True)
    nombre_asignatura = Column(String(100), nullable=False)
    horas_semanales = Column(Integer, nullable=False)
    modalidad = Column(String(50), nullable=False)
    estado = Column(Boolean, nullable=False)
    inscripciones = relationship("Inscripcion", back_populates="asignatura")
    calificaciones = relationship("Calificaciones", back_populates="asignatura")
