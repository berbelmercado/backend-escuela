import uuid
from database.config import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Curso(Base):

    __tablename__ = "curso"

    id_curso = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre_curso = Column(String(100), nullable=False)
    fecha_creacion = Column(DateTime, server_default=func.now())
