from typing import List

from entities.asignatura import Asignatura
from sqlalchemy.orm import Session


class AsignaturaCrud:
    def __init__(self, db: Session):
        self.db = db

    def crear_asignatura(
        self, nombre_asignatura: str, horas_semanales: int, modalidad: str, estado: bool
    ) -> Asignatura:
        asignatura = Asignatura(
            nombre_asignatura=nombre_asignatura.strip().title(),
            horas_semanales=horas_semanales,
            modalidad=modalidad.strip().title(),
            estado=estado,
        )
        self.db.add(asignatura)
        self.db.commit()
        self.db.refresh(asignatura)
        return asignatura

    def obtener_asignatura(self, id_asignatura: int) -> Asignatura:
        return (
            self.db.query(Asignatura)
            .filter(Asignatura.id_asignatura == id_asignatura)
            .first()
        )

    def obtener_asignaturas(self) -> List[Asignatura]:
        return self.db.query(Asignatura).all()

    def actualizar_asignatura(self, id_asignatura: int, data: dict) -> Asignatura:
        asignatura = self.obtener_asignatura(id_asignatura)
        if not asignatura:
            raise ValueError("No existe la asignatura para actualizar")

        for key, value in data.items():
            setattr(asignatura, key, value)

        self.db.commit()
        self.db.refresh(asignatura)
        return asignatura

    def eliminar_asignatura(self, id_asignatura: int) -> bool:
        asignatura = self.obtener_asignatura(id_asignatura)
        if not asignatura:
            raise ValueError("No existe la asignatura")

        self.db.delete(asignatura)
        self.db.commit()
        return True
