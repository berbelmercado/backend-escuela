from typing import List
from uuid import UUID

from entities.inscripcion import Inscripcion
from sqlalchemy.orm import Session


class InscripcionCrud:
    def __init__(self, db: Session):
        self.db = db

    def crear_inscripcion(
        self,
        id_curso: UUID,
        id_asignatura: int,
        id_estudiante: UUID,
        id_profesor: UUID,
        periodo: str,
    ) -> Inscripcion:
        inscripcion = Inscripcion(
            id_curso=id_curso,
            id_asignatura=id_asignatura,
            id_estudiante=id_estudiante,
            id_profesor=id_profesor,
            periodo=periodo.strip(),
        )
        self.db.add(inscripcion)
        self.db.commit()
        self.db.refresh(inscripcion)
        return inscripcion

    def obtener_inscripcion(self, id_inscripcion: int) -> Inscripcion:
        return (
            self.db.query(Inscripcion)
            .filter(Inscripcion.id_inscripcion == id_inscripcion)
            .first()
        )

    def obtener_inscripciones(self) -> List[Inscripcion]:
        return self.db.query(Inscripcion).all()

    def actualizar_inscripcion(self, id_inscripcion: int, data: dict) -> Inscripcion:
        inscripcion = self.obtener_inscripcion(id_inscripcion)
        if not inscripcion:
            raise ValueError("No existe la inscripcion para actualizar")

        for key, value in data.items():
            setattr(inscripcion, key, value)

        self.db.commit()
        self.db.refresh(inscripcion)
        return inscripcion

    def eliminar_inscripcion(self, id_inscripcion: int) -> bool:
        inscripcion = self.obtener_inscripcion(id_inscripcion)
        if not inscripcion:
            raise ValueError("No existe la inscripcion")

        self.db.delete(inscripcion)
        self.db.commit()
        return True
