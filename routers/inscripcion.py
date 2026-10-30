from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.inscripcion_crud import InscripcionCrud
from database.config import SessionLocal
from entities.asignatura import Asignatura
from entities.curso import Curso
from entities.estudiante import Estudiante
from entities.profesor import Profesor
from schemas.inscripcion_schema import (
    InscripcionCreate,
    InscripcionResponse,
    InscripcionResponseGet,
)


router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validar_relaciones(inscripcion: InscripcionCreate, db: Session):
    if not db.query(Curso).filter(Curso.id_curso == inscripcion.id_curso).first():
        raise HTTPException(404, "Curso no encontrado")
    if (
        not db.query(Asignatura)
        .filter(Asignatura.id_asignatura == inscripcion.id_asignatura)
        .first()
    ):
        raise HTTPException(404, "Asignatura no encontrada")
    if (
        not db.query(Estudiante)
        .filter(Estudiante.id_estudiante == inscripcion.id_estudiante)
        .first()
    ):
        raise HTTPException(404, "Estudiante no encontrado")
    if not db.query(Profesor).filter(Profesor.id_profesor == inscripcion.id_profesor).first():
        raise HTTPException(404, "Profesor no encontrado")


@router.post("/", response_model=InscripcionResponse)
def create_inscripcion(inscripcion: InscripcionCreate, db: Session = Depends(get_db)):
    validar_relaciones(inscripcion, db)
    crud = InscripcionCrud(db)
    db_inscripcion = crud.crear_inscripcion(
        id_curso=inscripcion.id_curso,
        id_asignatura=inscripcion.id_asignatura,
        id_estudiante=inscripcion.id_estudiante,
        id_profesor=inscripcion.id_profesor,
        periodo=inscripcion.periodo,
    )
    return InscripcionResponse(
        id_inscripcion=db_inscripcion.id_inscripcion,
        id_curso=db_inscripcion.id_curso,
        id_asignatura=db_inscripcion.id_asignatura,
        id_estudiante=db_inscripcion.id_estudiante,
        id_profesor=db_inscripcion.id_profesor,
        periodo=db_inscripcion.periodo,
        message="Inscripcion registrada exitosamente",
    )


@router.get("/", response_model=list[InscripcionResponseGet])
def list_inscripciones(db: Session = Depends(get_db)):
    inscripciones = InscripcionCrud(db).obtener_inscripciones()
    if not inscripciones:
        raise HTTPException(404, "No hay inscripciones registradas")
    return inscripciones


@router.get("/{id}", response_model=InscripcionResponseGet)
def get_inscripcion(id: int, db: Session = Depends(get_db)):
    inscripcion = InscripcionCrud(db).obtener_inscripcion(id)
    if not inscripcion:
        raise HTTPException(404, "Inscripcion no encontrada")
    return inscripcion


@router.put("/{id}", response_model=InscripcionResponse)
def update_inscripcion(
    id: int, inscripcion_update: InscripcionCreate, db: Session = Depends(get_db)
):
    validar_relaciones(inscripcion_update, db)
    crud = InscripcionCrud(db)
    if not crud.obtener_inscripcion(id):
        raise HTTPException(404, "Inscripcion no encontrada")

    inscripcion = crud.actualizar_inscripcion(
        id,
        {
            "id_curso": inscripcion_update.id_curso,
            "id_asignatura": inscripcion_update.id_asignatura,
            "id_estudiante": inscripcion_update.id_estudiante,
            "id_profesor": inscripcion_update.id_profesor,
            "periodo": inscripcion_update.periodo.strip(),
        },
    )
    return InscripcionResponse(
        id_inscripcion=inscripcion.id_inscripcion,
        id_curso=inscripcion.id_curso,
        id_asignatura=inscripcion.id_asignatura,
        id_estudiante=inscripcion.id_estudiante,
        id_profesor=inscripcion.id_profesor,
        periodo=inscripcion.periodo,
        message="Inscripcion actualizada exitosamente",
    )


@router.delete("/{id}")
def delete_inscripcion(id: int, db: Session = Depends(get_db)):
    try:
        InscripcionCrud(db).eliminar_inscripcion(id)
        return {"message": "Inscripcion eliminada"}
    except ValueError as e:
        raise HTTPException(404, str(e))
