import uuid
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from database.configuracion import Base


class Materia(Base):
    __tablename__ = "materias"

    id_materia = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    codigo = Column(String(20), unique=True, nullable=False)
    nombre_materia = Column(String(100), nullable=False)

    # --- TRAZABILIDAD OBLIGATORIA (Punto 2.2 del Examen) ---
    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_edicion = Column(DateTime, onupdate=func.now())
    id_usuario_creacion = Column(String(50), nullable=True)
    id_usuario_edita = Column(String(50), nullable=True)
