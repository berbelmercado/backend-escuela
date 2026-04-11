"""
app.py
------
Punto de entrada de la API "Backend Escuela".

Responsabilidades principales:
- Crear las tablas en la base de datos a partir de los modelos declarativos.
- Instanciar la aplicación FastAPI y centralizar metadata (título, descripción).
- Registrar (incluir) los routers que exponen los endpoints para estudiantes y cursos.

Dependencias del workspace:
- Base (declarative_base) y engine (sqlalchemy) en database.py:
  -> [`Base`](database.py), [`engine`](database.py)
- Routers con los endpoints:
  -> Estudiantes: [`router`](routers/estudiante_routes.py) en [routers/estudiante_routes.py](routers/estudiante_routes.py)
  -> Cursos: [`router`](routers/curso_routes.py) en [routers/curso_routes.py](routers/curso_routes.py)

Notas de despliegue:
- La configuración de conexión está en database.py. Para desarrollo local usa
  la base de datos SQLite o PostgreSQL según sea configurado.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.config import Base, engine
from routers import estudiante, curso

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend Escuela",
    description="""API para gestionar estudiantes y cursos en una institución educativa.
    Incluye endpoints para:
    - Registrar, consultar, actualizar y eliminar estudiantes.
    - Registrar, consultar, actualizar y eliminar cursos.
    - Gestionar relaciones entre estudiantes y cursos.
    """,
    version="1.0.0",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(estudiante.router)
app.include_router(curso.router)


@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.
    """
    return {
        "message": "Bienvenido a Backend Escuela API",
        "version": "1.0.0",
        "endpoints": {
            "estudiantes": "/estudiantes",
            "cursos": "/cursos",
            "documentación": "/docs",
        },
    }


@app.get("/health", tags=["Health"])
def health_check():
    """
    Endpoint para verificar el estado de la API.
    """
    return {"status": "ok", "service": "Backend Escuela API"}
