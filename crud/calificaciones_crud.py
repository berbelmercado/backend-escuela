from typing import List
from uuid import UUID

from entities.calificaciones import Calificaciones
from sqlalchemy.orm import Session


class CalificacionesCrud:
    def __init__(self, db: Session):
        self.db = db

    def crear_calificacion(
        self,
        id_estudiante: UUID,
        id_profesor: UUID,
        id_asignatura: int,
        descripcion_nota: str,
        valor_nota: float,
    ) -> Calificaciones:
        calificacion = Calificaciones(
            id_estudiante=id_estudiante,
            id_profesor=id_profesor,
            id_asignatura=id_asignatura,
            descripcion_nota=descripcion_nota.strip(),
            valor_nota=valor_nota,
        )
        self.db.add(calificacion)
        self.db.commit()
        self.db.refresh(calificacion)
        return calificacion

    def obtener_calificacion(self, id_calificacion: int) -> Calificaciones:
        return (
            self.db.query(Calificaciones)
            .filter(Calificaciones.id_calificacion == id_calificacion)
            .first()
        )

    def obtener_calificaciones(self) -> List[Calificaciones]:
        return self.db.query(Calificaciones).all()

    def actualizar_calificacion(self, id_calificacion: int, data: dict) -> Calificaciones:
        calificacion = self.obtener_calificacion(id_calificacion)
        if not calificacion:
            raise ValueError("No existe la calificacion para actualizar")

        for key, value in data.items():
            setattr(calificacion, key, value)

        self.db.commit()
        self.db.refresh(calificacion)
        return calificacion

    def eliminar_calificacion(self, id_calificacion: int) -> bool:
        calificacion = self.obtener_calificacion(id_calificacion)
        if not calificacion:
            raise ValueError("No existe la calificacion")

        self.db.delete(calificacion)
        self.db.commit()
        return True
