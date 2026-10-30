from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from crud.profesor_crud import ProfesorCrud
from database.config import SessionLocal
from entities.profesor import Profesor
from schemas.profesor_schema import (
    ProfesorCreate,
    ProfesorResponse,
    ProfesorResponseGet,
)


router = APIRouter(prefix="/profesores", tags=["Profesores"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProfesorResponse)
def create_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db)):
    cedula_exists = db.query(Profesor).filter(Profesor.cedula == profesor.cedula).first()
    if cedula_exists:
        raise HTTPException(409, "Esta cedula ya esta registrada.")

    crud = ProfesorCrud(db)
    db_profesor = crud.crear_profesor(
        cedula=profesor.cedula,
        nombre=profesor.nombre,
        apellido=profesor.apellido,
        sexo=profesor.sexo,
        edad=profesor.edad,
    )
    return ProfesorResponse(
        id_profesor=db_profesor.id_profesor,
        cedula=db_profesor.cedula,
        nombre=db_profesor.nombre,
        apellido=db_profesor.apellido,
        sexo=db_profesor.sexo,
        edad=db_profesor.edad,
        message="Profesor registrado exitosamente",
    )


@router.get("/", response_model=list[ProfesorResponseGet])
def list_profesores(db: Session = Depends(get_db)):
    profesores = ProfesorCrud(db).obtener_profesores()
    if not profesores:
        raise HTTPException(404, "No hay profesores registrados")
    return profesores


@router.get("/{id}", response_model=ProfesorResponseGet)
def get_profesor(id: UUID, db: Session = Depends(get_db)):
    profesor = ProfesorCrud(db).obtener_profesor(id)
    if not profesor:
        raise HTTPException(404, "Profesor no encontrado")
    return profesor


@router.put("/{id}", response_model=ProfesorResponse)
def update_profesor(
    id: UUID, profesor_update: ProfesorCreate, db: Session = Depends(get_db)
):
    crud = ProfesorCrud(db)
    if not crud.obtener_profesor(id):
        raise HTTPException(404, "Profesor no encontrado")

    cedula_exists = (
        db.query(Profesor)
        .filter(Profesor.cedula == profesor_update.cedula, Profesor.id_profesor != id)
        .first()
    )
    if cedula_exists:
        raise HTTPException(409, "Esta cedula ya esta registrada en otro profesor.")

    profesor = crud.actualizar_profesor(
        id,
        {
            "cedula": profesor_update.cedula.strip(),
            "nombre": profesor_update.nombre.strip().title(),
            "apellido": profesor_update.apellido.strip().title(),
            "sexo": profesor_update.sexo.strip().title(),
            "edad": profesor_update.edad,
        },
    )
    return ProfesorResponse(
        id_profesor=profesor.id_profesor,
        cedula=profesor.cedula,
        nombre=profesor.nombre,
        apellido=profesor.apellido,
        sexo=profesor.sexo,
        edad=profesor.edad,
        message="Profesor actualizado exitosamente",
    )


@router.delete("/{id}")
def delete_profesor(id: UUID, db: Session = Depends(get_db)):
    try:
        ProfesorCrud(db).eliminar_profesor(id)
        return {"message": "Profesor eliminado"}
    except ValueError as e:
        raise HTTPException(404, str(e))
