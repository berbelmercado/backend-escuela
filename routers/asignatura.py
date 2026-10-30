from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.asignatura_crud import AsignaturaCrud
from database.config import SessionLocal
from schemas.asignatura_schema import (
    AsignaturaCreate,
    AsignaturaResponse,
    AsignaturaResponseGet,
)


router = APIRouter(prefix="/asignaturas", tags=["Asignaturas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AsignaturaResponse)
def create_asignatura(asignatura: AsignaturaCreate, db: Session = Depends(get_db)):
    crud = AsignaturaCrud(db)
    db_asignatura = crud.crear_asignatura(
        nombre_asignatura=asignatura.nombre_asignatura,
        horas_semanales=asignatura.horas_semanales,
        modalidad=asignatura.modalidad,
        estado=asignatura.estado,
    )
    return AsignaturaResponse(
        id_asignatura=db_asignatura.id_asignatura,
        nombre_asignatura=db_asignatura.nombre_asignatura,
        horas_semanales=db_asignatura.horas_semanales,
        modalidad=db_asignatura.modalidad,
        estado=db_asignatura.estado,
        message="Asignatura registrada exitosamente",
    )


@router.get("/", response_model=list[AsignaturaResponseGet])
def list_asignaturas(db: Session = Depends(get_db)):
    asignaturas = AsignaturaCrud(db).obtener_asignaturas()
    if not asignaturas:
        raise HTTPException(404, "No hay asignaturas registradas")
    return asignaturas


@router.get("/{id}", response_model=AsignaturaResponseGet)
def get_asignatura(id: int, db: Session = Depends(get_db)):
    asignatura = AsignaturaCrud(db).obtener_asignatura(id)
    if not asignatura:
        raise HTTPException(404, "Asignatura no encontrada")
    return asignatura


@router.put("/{id}", response_model=AsignaturaResponse)
def update_asignatura(
    id: int, asignatura_update: AsignaturaCreate, db: Session = Depends(get_db)
):
    crud = AsignaturaCrud(db)
    if not crud.obtener_asignatura(id):
        raise HTTPException(404, "Asignatura no encontrada")

    asignatura = crud.actualizar_asignatura(
        id,
        {
            "nombre_asignatura": asignatura_update.nombre_asignatura.strip().title(),
            "horas_semanales": asignatura_update.horas_semanales,
            "modalidad": asignatura_update.modalidad.strip().title(),
            "estado": asignatura_update.estado,
        },
    )
    return AsignaturaResponse(
        id_asignatura=asignatura.id_asignatura,
        nombre_asignatura=asignatura.nombre_asignatura,
        horas_semanales=asignatura.horas_semanales,
        modalidad=asignatura.modalidad,
        estado=asignatura.estado,
        message="Asignatura actualizada exitosamente",
    )


@router.delete("/{id}")
def delete_asignatura(id: int, db: Session = Depends(get_db)):
    try:
        AsignaturaCrud(db).eliminar_asignatura(id)
        return {"message": "Asignatura eliminada"}
    except ValueError as e:
        raise HTTPException(404, str(e))
