"""
Rutas y lógica para la entidad "Estudiante".

Responsabilidades:
- Exponer endpoints CRUD para estudiantes.
- Utilizar el CRUD ya construido en EstudianteCrud.
- Proveer respuestas claras y códigos HTTP apropiados.

Endpoints:
- POST /estudiantes/        -> Crear un nuevo estudiante.
- GET  /estudiantes/        -> Listar todos los estudiantes.
- GET  /estudiantes/{id}    -> Obtener un estudiante por id.
- PUT  /estudiantes/{id}    -> Actualizar un estudiante por id.
- DELETE /estudiantes/{id}  -> Eliminar un estudiante por id.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from database.config import SessionLocal
from crud.estudiante_crud import EstudianteCrud
from schemas.estudiante_schema import (
    EstudianteCreate,
    EstudianteResponse,
    EstudianteResponseGet,
)

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


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
    response_model=EstudianteResponse,
    summary="Registrar un nuevo estudiante",
    description="""Crea un nuevo estudiante verificando que no exista otro con el mismo email o cédula.""",
    responses={
        200: {
            "description": "Datos del estudiante registrado con mensaje: Estudiante registrado exitosamente"
        },
        409: {
            "description": "Email o cédula ya existe",
            "content": {
                "application/json": {
                    "example": {"detail": "Este email ya está registrado."}
                }
            },
        },
    },
)
def create_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo estudiante en la base de datos.

    Validaciones:
    - Si ya existe un estudiante con el mismo email -> 409
    - Si ya existe un estudiante con la misma cédula -> 409

    Parámetros:
    - estudiante: EstudianteCreate (datos de entrada).
    - db: Sesión de base de datos proporcionada por get_db.

    Devuelve:
    - EstudianteResponse con los campos del estudiante creado y un mensaje.
    """
    try:
        # Validar que no exista un estudiante con el mismo email
        email_exists = (
            db.query(EstudianteCrud)
            .filter(Estudiante.email == estudiante.email)
            .first()
        )
        if email_exists:
            raise HTTPException(409, "Este email ya está registrado.")

        # Validar que no exista un estudiante con la misma cédula
        cedula_exists = (
            db.query(Estudiante).filter(Estudiante.cedula == estudiante.cedula).first()
        )
        if cedula_exists:
            raise HTTPException(409, "Esta cédula ya está registrada.")

        crud = EstudianteCrud(db)
        db_estudiante = crud.crear_estudiante(
            cedula=estudiante.cedula,
            nombre=estudiante.nombre,
            apellido=estudiante.apellido,
            email=estudiante.email,
            sexo=estudiante.sexo,
            fecha_nacimiento=estudiante.fecha_nacimiento,
            no_celular=estudiante.no_celular or "",
        )

        return EstudianteResponse(
            id=db_estudiante.id_estudiante,
            cedula=db_estudiante.cedula,
            nombre=db_estudiante.nombre,
            apellido=db_estudiante.apellido,
            email=db_estudiante.email,
            sexo=db_estudiante.sexo,
            fecha_nacimiento=db_estudiante.fecha_nacimiento,
            no_celular=db_estudiante.no_celular,
            message="Estudiante registrado exitosamente",
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(400, f"Error al crear el estudiante: {str(e)}")


@router.get(
    "/",
    response_model=list[EstudianteResponseGet],
    summary="Listar estudiantes",
    description="Se consultan todos los estudiantes registrados en el sistema.",
    responses={
        200: {"description": "Lista de estudiantes"},
        404: {
            "description": "No hay estudiantes registrados",
            "content": {
                "application/json": {
                    "example": {"detail": "No hay estudiantes registrados"}
                }
            },
        },
    },
)
def list_estudiantes(db: Session = Depends(get_db)):
    """
    Recupera la lista de estudiantes.

    Si no hay estudiantes registrados se lanza HTTPException(404).

    Devuelve:
    - Lista de EstudianteResponseGet.
    """
    try:
        crud = EstudianteCrud(db)
        estudiantes = crud.obtener_estudiantes()

        if len(estudiantes) == 0:
            raise HTTPException(404, "No hay estudiantes registrados")

        return estudiantes
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error al listar estudiantes: {str(e)}")


@router.get(
    "/{id}",
    response_model=EstudianteResponseGet,
    summary="Consultar estudiante por Id",
    description="Se consulta un estudiante con su número de Id.",
    responses={
        200: {"description": "Datos del estudiante"},
        404: {
            "description": "Estudiante no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Estudiante no encontrado"}}
            },
        },
    },
)
def get_estudiante(id: UUID, db: Session = Depends(get_db)):
    """
    Busca un estudiante por id.

    Parámetros:
    - id: UUID, identificador del estudiante.
    - db: Sesión de base de datos.

    Devuelve:
    - EstudianteResponseGet si existe, si no -> HTTPException(404).
    """
    try:
        crud = EstudianteCrud(db)
        estudiante = crud.obtener_estudiante(id)

        if not estudiante:
            raise HTTPException(404, "Estudiante no encontrado")

        return estudiante
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error al obtener el estudiante: {str(e)}")


@router.put(
    "/{id}",
    response_model=EstudianteResponse,
    summary="Actualizar estudiante por Id",
    description="Actualiza los datos de un estudiante existente.",
    responses={
        200: {"description": "Datos del estudiante actualizado"},
        404: {
            "description": "Estudiante no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Estudiante no encontrado"}}
            },
        },
        409: {
            "description": "Email o cédula ya existe en otro registro",
            "content": {
                "application/json": {
                    "example": {"detail": "Este email ya está registrado."}
                }
            },
        },
    },
)
def update_estudiante(
    id: UUID, estudiante_update: EstudianteCreate, db: Session = Depends(get_db)
):
    """
    Actualiza los datos de un estudiante por id.

    Validaciones:
    - Si no existe el estudiante -> HTTPException(404)
    - Si el nuevo email ya existe en otro estudiante -> HTTPException(409)
    - Si la nueva cédula ya existe en otro estudiante -> HTTPException(409)

    Parámetros:
    - id: UUID, identificador del estudiante.
    - estudiante_update: EstudianteCreate (datos a actualizar).
    - db: Sesión de base de datos.

    Devuelve:
    - EstudianteResponse con los datos actualizados.
    """
    try:
        crud = EstudianteCrud(db)

        # Verificar que el estudiante existe
        estudiante_existe = crud.obtener_estudiante(id)
        if not estudiante_existe:
            raise HTTPException(404, "Estudiante no encontrado")

        # Validar que el nuevo email no exista en otro estudiante
        from entities.estudiante import Estudiante

        email_exists = (
            db.query(Estudiante)
            .filter(
                Estudiante.email == estudiante_update.email,
                Estudiante.id_estudiante != id,
            )
            .first()
        )
        if email_exists:
            raise HTTPException(
                409, "Este email ya está registrado en otro estudiante."
            )

        # Validar que la nueva cédula no exista en otro estudiante
        cedula_exists = (
            db.query(Estudiante)
            .filter(
                Estudiante.cedula == estudiante_update.cedula,
                Estudiante.id_estudiante != id,
            )
            .first()
        )
        if cedula_exists:
            raise HTTPException(
                409, "Esta cédula ya está registrada en otro estudiante."
            )

        # Preparar datos para actualizar
        data_update = {
            "cedula": estudiante_update.cedula.strip(),
            "nombre": estudiante_update.nombre.strip().title(),
            "apellido": estudiante_update.apellido.strip().title(),
            "email": estudiante_update.email.strip(),
            "sexo": estudiante_update.sexo.strip().title(),
            "fecha_nacimiento": estudiante_update.fecha_nacimiento,
            "no_celular": (
                estudiante_update.no_celular.strip()
                if estudiante_update.no_celular
                else ""
            ),
        }

        estudiante_actualizado = crud.actualizar_estudiante(id, data_update)

        return EstudianteResponse(
            id=estudiante_actualizado.id_estudiante,
            cedula=estudiante_actualizado.cedula,
            nombre=estudiante_actualizado.nombre,
            apellido=estudiante_actualizado.apellido,
            email=estudiante_actualizado.email,
            sexo=estudiante_actualizado.sexo,
            fecha_nacimiento=estudiante_actualizado.fecha_nacimiento,
            no_celular=estudiante_actualizado.no_celular,
            message="Estudiante actualizado exitosamente",
        )
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        raise HTTPException(400, f"Error al actualizar el estudiante: {str(e)}")


@router.delete(
    "/{id}",
    summary="Eliminar estudiante por Id",
    description="Elimina un estudiante con su número de Id.",
    responses={
        200: {
            "description": "Estudiante eliminado",
            "content": {
                "application/json": {"example": {"message": "Estudiante eliminado"}}
            },
        },
        404: {
            "description": "Estudiante no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Estudiante no encontrado"}}
            },
        },
    },
)
def delete_estudiante(id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un estudiante por id.

    Parámetros:
    - id: UUID, identificador del estudiante.
    - db: Sesión de base de datos.

    Comportamiento:
    - Si no existe el estudiante -> HTTPException(404)
    - Si existe -> elimina y confirma con un mensaje JSON.
    """
    try:
        crud = EstudianteCrud(db)
        crud.eliminar_estudiante(id)
        return {"message": "Estudiante eliminado"}
    except ValueError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        raise HTTPException(500, f"Error al eliminar el estudiante: {str(e)}")
