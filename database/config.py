"""
Configuración de la base de datos utilizando SQLAlchemy y Neon como proveedor de base de datos.
Este módulo establece la conexión a la base de datos, define la sesión y la clase base para los modelos.
Requiere que la variable de entorno DATABASE_URL esté configurada con la URL de conexión a la base de
datos.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

DATABASE_URL = getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Se requiere DATABASE_URL en las variables de entorno")

engine = create_engine(
    DATABASE_URL,
    echo=False,  # Cambiar a True para ver consultas SQL
    pool_pre_ping=True,  # Verificar conexión antes de usar
    pool_recycle=300,  # Reciclar conexiones cada 5 minutos
    connect_args={"sslmode": "require"},  # Requerir SSL para Neon
)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la clase base para los modelos
Base = declarative_base()
