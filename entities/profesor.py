from math import prod
import uuid
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

# Esta línea conecta tu tabla con la configuración de Neon que hizo tu compañero
from database.config import Base


class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    cedula = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)

    # --- TRAZABILIDAD OBLIGATORIA (Punto 2.2 del Examen) ---
    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_edicion = Column(DateTime, onupdate=func.now())
    id_usuario_creacion = Column(String(50), nullable=True)  # Quién lo creó
    id_usuario_edita = Column(String(50), nullable=True)  # Quién lo editó
