"""
Rutas y lógica para la entidad "Curso".

Responsabilidades:
- Exponer endpoints CRUD para cursos.
- Utilizar el CRUD ya construido en CursoCrud.
- Proveer respuestas claras y códigos HTTP apropiados.

Endpoints:
- POST /cursos/        -> Crear un nuevo curso.
- GET  /cursos/        -> Listar todos los cursos.
- GET  /cursos/{id}    -> Obtener un curso por id.
- PUT  /cursos/{id}    -> Actualizar un curso por id.
- DELETE /cursos/{id}  -> Eliminar un curso por id.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from database.config import SessionLocal
from crud.curso_crud import CursoCrud
from schemas.curso_schema import CursoCreate, CursoResponse, CursoResponseGet

router = APIRouter(prefix="/cursos", tags=["Cursos"])


def get_db():
    """
    Dependencia para obtener una sesión de base de datos.

    Crea una nueva sesión de base de datos y la cierra al finalizar la operación.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=CursoResponse,
    summary="Registrar un nuevo curso",
    description="""Crea un nuevo curso usando el CRUD construido.""",
    responses={
        200: {
            "description": "Datos del curso registrado con mensaje: Curso registrado exitosamente"
        },
        400: {
            "description": "Error en los datos de entrada",
            "content": {
                "application/json": {"example": {"detail": "Error al crear el curso"}}
            },
        },
    },
)
def create_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo curso en la base de datos.

    Parámetros:
    - curso: CursoCreate (datos de entrada).
    - db: Sesión de base de datos proporcionada por get_db.

    Devuelve:
    - CursoResponse con los campos del curso creado y un mensaje.
    """
    try:
        crud = CursoCrud(db)
        db_curso = crud.crear_curso(nombre_curso=curso.nombre)

        return CursoResponse(
            id=db_curso.id_curso,
            nombre=db_curso.nombre_curso,
            message="Curso registrado exitosamente",
        )
    except Exception as e:
        raise HTTPException(400, f"Error al crear el curso: {str(e)}")


@router.get(
    "/",
    response_model=list[CursoResponseGet],
    summary="Listar cursos",
    description="Se consultan todos los cursos registrados en el sistema.",
    responses={
        200: {"description": "Lista de cursos"},
        404: {
            "description": "No hay cursos registrados",
            "content": {
                "application/json": {"example": {"detail": "No hay cursos registrados"}}
            },
        },
    },
)
def list_cursos(db: Session = Depends(get_db)):
    """
    Recupera la lista de cursos.

    Si no hay cursos registrados se lanza HTTPException(404).

    Devuelve:
    - Lista de CursoResponseGet.
    """
    try:
        crud = CursoCrud(db)
        cursos = crud.obtener_cursos()

        if len(cursos) == 0:
            raise HTTPException(404, "No hay cursos registrados")

        return cursos
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error al listar cursos: {str(e)}")


@router.get(
    "/{id}",
    response_model=CursoResponseGet,
    summary="Consultar curso por Id",
    description="Se consulta un curso con su número de Id.",
    responses={
        200: {"description": "Datos del curso"},
        404: {
            "description": "Curso no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Curso no encontrado"}}
            },
        },
    },
)
def get_curso(id: UUID, db: Session = Depends(get_db)):
    """
    Busca un curso por id.

    Parámetros:
    - id: UUID, identificador del curso.
    - db: Sesión de base de datos.

    Devuelve:
    - CursoResponseGet si existe, si no -> HTTPException(404).
    """
    try:
        crud = CursoCrud(db)
        curso = crud.obtener_curso(id)

        if not curso:
            raise HTTPException(404, "Curso no encontrado")

        return curso
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error al obtener el curso: {str(e)}")


@router.put(
    "/{id}",
    response_model=CursoResponse,
    summary="Actualizar curso por Id",
    description="Actualiza los datos de un curso existente.",
    responses={
        200: {"description": "Datos del curso actualizado"},
        404: {
            "description": "Curso no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Curso no encontrado"}}
            },
        },
        400: {
            "description": "Error en los datos de entrada",
            "content": {
                "application/json": {
                    "example": {"detail": "Error al actualizar el curso"}
                }
            },
        },
    },
)
def update_curso(id: UUID, curso_update: CursoCreate, db: Session = Depends(get_db)):
    """
    Actualiza los datos de un curso por id.

    Validaciones:
    - Si no existe el curso -> HTTPException(404)

    Parámetros:
    - id: UUID, identificador del curso.
    - curso_update: CursoCreate (datos a actualizar).
    - db: Sesión de base de datos.

    Devuelve:
    - CursoResponse con los datos actualizados.
    """
    try:
        crud = CursoCrud(db)

        # Verificar que el curso existe
        curso_existe = crud.obtener_curso(id)
        if not curso_existe:
            raise HTTPException(404, "Curso no encontrado")

        # Actualizar el curso
        data_update = {"nombre_curso": curso_update.nombre.strip().title()}
        curso_actualizado = crud.actualizar_curso(id, data_update)

        return CursoResponse(
            id=curso_actualizado.id_curso,
            nombre=curso_actualizado.nombre_curso,
            message="Curso actualizado exitosamente",
        )
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        raise HTTPException(400, f"Error al actualizar el curso: {str(e)}")


@router.delete(
    "/{id}",
    summary="Eliminar curso por Id",
    description="Elimina un curso con su número de Id.",
    responses={
        200: {
            "description": "Curso eliminado",
            "content": {
                "application/json": {"example": {"message": "Curso eliminado"}}
            },
        },
        404: {
            "description": "Curso no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Curso no encontrado"}}
            },
        },
    },
)
def delete_curso(id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un curso por id.

    Parámetros:
    - id: UUID, identificador del curso.
    - db: Sesión de base de datos.

    Comportamiento:
    - Si no existe el curso -> HTTPException(404)
    - Si existe -> elimina y confirma con un mensaje JSON.
    """
    try:
        crud = CursoCrud(db)
        crud.eliminar_curso(id)
        return {"message": "Curso eliminado"}
    except ValueError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        raise HTTPException(500, f"Error al eliminar el curso: {str(e)}")
