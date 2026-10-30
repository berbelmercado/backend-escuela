from typing import List
from uuid import UUID

from entities.profesor import Profesor
from sqlalchemy.orm import Session


class ProfesorCrud:
    def __init__(self, db: Session):
        self.db = db

    def crear_profesor(
        self, cedula: str, nombre: str, apellido: str, sexo: str, edad: int
    ) -> Profesor:
        profesor = Profesor(
            cedula=cedula.strip(),
            nombre=nombre.strip().title(),
            apellido=apellido.strip().title(),
            sexo=sexo.strip().title(),
            edad=edad,
        )
        self.db.add(profesor)
        self.db.commit()
        self.db.refresh(profesor)
        return profesor

    def obtener_profesor(self, id_profesor: UUID) -> Profesor:
        return self.db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()

    def obtener_profesores(self) -> List[Profesor]:
        return self.db.query(Profesor).all()

    def actualizar_profesor(self, id_profesor: UUID, data: dict) -> Profesor:
        profesor = self.obtener_profesor(id_profesor)
        if not profesor:
            raise ValueError("No existe el profesor para actualizar")

        for key, value in data.items():
            setattr(profesor, key, value)

        self.db.commit()
        self.db.refresh(profesor)
        return profesor

    def eliminar_profesor(self, id_profesor: UUID) -> bool:
        profesor = self.obtener_profesor(id_profesor)
        if not profesor:
            raise ValueError("No existe el profesor")

        self.db.delete(profesor)
        self.db.commit()
        return True
