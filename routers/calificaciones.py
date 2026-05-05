from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.calificaciones_crud import CalificacionesCrud
from database.config import SessionLocal
from entities.asignatura import Asignatura
from entities.estudiante import Estudiante
from entities.profesor import Profesor
from schemas.calificacion_schema import (
    CalificacionCreate,
    CalificacionResponse,
    CalificacionResponseGet,
)


router = APIRouter(prefix="/calificaciones", tags=["Calificaciones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validar_relaciones(calificacion: CalificacionCreate, db: Session):
    if (
        not db.query(Estudiante)
        .filter(Estudiante.id_estudiante == calificacion.id_estudiante)
        .first()
    ):
        raise HTTPException(404, "Estudiante no encontrado")
    if not db.query(Profesor).filter(Profesor.id_profesor == calificacion.id_profesor).first():
        raise HTTPException(404, "Profesor no encontrado")
    if (
        not db.query(Asignatura)
        .filter(Asignatura.id_asignatura == calificacion.id_asignatura)
        .first()
    ):
        raise HTTPException(404, "Asignatura no encontrada")


@router.post("/", response_model=CalificacionResponse)
def create_calificacion(calificacion: CalificacionCreate, db: Session = Depends(get_db)):
    validar_relaciones(calificacion, db)
    crud = CalificacionesCrud(db)
    db_calificacion = crud.crear_calificacion(
        id_estudiante=calificacion.id_estudiante,
        id_profesor=calificacion.id_profesor,
        id_asignatura=calificacion.id_asignatura,
        descripcion_nota=calificacion.descripcion_nota,
        valor_nota=calificacion.valor_nota,
    )
    return CalificacionResponse(
        id_calificacion=db_calificacion.id_calificacion,
        id_estudiante=db_calificacion.id_estudiante,
        id_profesor=db_calificacion.id_profesor,
        id_asignatura=db_calificacion.id_asignatura,
        descripcion_nota=db_calificacion.descripcion_nota,
        valor_nota=db_calificacion.valor_nota,
        message="Calificacion registrada exitosamente",
    )


@router.get("/", response_model=list[CalificacionResponseGet])
def list_calificaciones(db: Session = Depends(get_db)):
    calificaciones = CalificacionesCrud(db).obtener_calificaciones()
    if not calificaciones:
        raise HTTPException(404, "No hay calificaciones registradas")
    return calificaciones


@router.get("/{id}", response_model=CalificacionResponseGet)
def get_calificacion(id: int, db: Session = Depends(get_db)):
    calificacion = CalificacionesCrud(db).obtener_calificacion(id)
    if not calificacion:
        raise HTTPException(404, "Calificacion no encontrada")
    return calificacion


@router.put("/{id}", response_model=CalificacionResponse)
def update_calificacion(
    id: int, calificacion_update: CalificacionCreate, db: Session = Depends(get_db)
):
    validar_relaciones(calificacion_update, db)
    crud = CalificacionesCrud(db)
    if not crud.obtener_calificacion(id):
        raise HTTPException(404, "Calificacion no encontrada")

    calificacion = crud.actualizar_calificacion(
        id,
        {
            "id_estudiante": calificacion_update.id_estudiante,
            "id_profesor": calificacion_update.id_profesor,
            "id_asignatura": calificacion_update.id_asignatura,
            "descripcion_nota": calificacion_update.descripcion_nota.strip(),
            "valor_nota": calificacion_update.valor_nota,
        },
    )
    return CalificacionResponse(
        id_calificacion=calificacion.id_calificacion,
        id_estudiante=calificacion.id_estudiante,
        id_profesor=calificacion.id_profesor,
        id_asignatura=calificacion.id_asignatura,
        descripcion_nota=calificacion.descripcion_nota,
        valor_nota=calificacion.valor_nota,
        message="Calificacion actualizada exitosamente",
    )


@router.delete("/{id}")
def delete_calificacion(id: int, db: Session = Depends(get_db)):
    try:
        CalificacionesCrud(db).eliminar_calificacion(id)
        return {"message": "Calificacion eliminada"}
    except ValueError as e:
        raise HTTPException(404, str(e))
