from sqlalchemy.orm import Session
from profesor_crud import Profesor


def crear_profesor(db: Session, profesor: Profesor):
    db.add(profesor)
    db.commit()
    db.refresh(profesor)
    return profesor


def obtener_profesores(db: Session):
    return db.query(Profesor).all()


def obtener_profesor_por_id(db: Session, id_profesor: int):
    return db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()


def actualizar_profesor(db: Session, id_profesor: int, datos):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()

    if profesor:
        profesor.nombre_profesor = datos.nombre_profesor
        profesor.apellido_profesor = datos.apellido_profesor
        profesor.sexo_profesor = datos.sexo_profesor
        profesor.edad = datos.edad

        db.commit()
        db.refresh(profesor)

    return profesor


def eliminar_profesor(db: Session, id_profesor: int):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()

    if profesor:
        db.delete(profesor)
        db.commit()

    return profesor
