from sqlalchemy.orm import Session
from calificaciones_crud import Calificaciones


def crear_calificacion(db: Session, calificacion: Calificaciones):
    db.add(calificacion)
    db.commit()
    db.refresh(calificacion)
    return calificacion


def obtener_calificaciones(db: Session):
    return db.query(Calificaciones).all()


def obtener_calificacion_por_id(db: Session, id_calificaciones: int):
    return (
        db.query(Calificaciones)
        .filter(Calificaciones.id_calificaciones == id_calificaciones)
        .first()
    )


def actualizar_calificacion(db: Session, id_calificaciones: int, datos):
    calificacion = (
        db.query(Calificaciones)
        .filter(Calificaciones.id_calificaciones == id_calificaciones)
        .first()
    )

    if calificacion:
        calificacion.id_estudiante = datos.id_estudiante
        calificacion.id_profesor = datos.id_profesor
        calificacion.descripcion = datos.descripcion
        calificacion.valor = datos.valor

        db.commit()
        db.refresh(calificacion)

    return calificacion


def eliminar_calificacion(db: Session, id_calificaciones: int):
    calificacion = (
        db.query(Calificaciones)
        .filter(Calificaciones.id_calificaciones == id_calificaciones)
        .first()
    )

    if calificacion:
        db.delete(calificacion)
        db.commit()

    return calificacion
