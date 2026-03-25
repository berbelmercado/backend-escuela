from sqlalchemy.orm import Session
from inscripcion_crud import Inscripcion


def crear_inscripcion(db: Session, inscripcion: Inscripcion):
    db.add(inscripcion)
    db.commit()
    db.refresh(inscripcion)
    return inscripcion


def obtener_inscripciones(db: Session):
    return db.query(Inscripcion).all()


def obtener_inscripcion_por_id(db: Session, id_inscripcion: int):
    return (
        db.query(Inscripcion)
        .filter(Inscripcion.id_inscripcion == id_inscripcion)
        .first()
    )


def actualizar_inscripcion(db: Session, id_inscripcion: int, datos):
    inscripcion = (
        db.query(Inscripcion)
        .filter(Inscripcion.id_inscripcion == id_inscripcion)
        .first()
    )

    if inscripcion:
        inscripcion.id_grado = datos.id_grado
        inscripcion.id_asignatura = datos.id_asignatura
        inscripcion.id_estudiante = datos.id_estudiante
        inscripcion.id_profesor = datos.id_profesor
        inscripcion.periodo = datos.periodo

        db.commit()
        db.refresh(inscripcion)

    return inscripcion


def eliminar_inscripcion(db: Session, id_inscripcion: int):
    inscripcion = (
        db.query(Inscripcion)
        .filter(Inscripcion.id_inscripcion == id_inscripcion)
        .first()
    )

    if inscripcion:
        db.delete(inscripcion)
        db.commit()

    return inscripcion
