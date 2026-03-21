rayko15-feature-login
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

import uuid
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

# Esta línea conecta tu tabla con la configuración de Neon que hizo tu compañero
from database.configuracion import Base


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
    prod
