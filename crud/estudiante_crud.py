from typing import List, Optional
from uuid import UUID
from entities.estudiante import Estudiante
from sqlalchemy.orm import Session
from datetime import date


class Estudiante_crud:

    def __init__(self, db: Session):
        self.db = db

    def crear_estudiante(
        self,
        cedula: str,
        nombre: str,
        apellido: str,
        email: str,
        sexo: str,
        fecha_nacimiento: date,
        no_celular: str,
    ) -> Estudiante:
        estudiante = Estudiante(
            cedula=cedula.strip(),
            nombre=nombre.strip().capitalize(),
            apellido=apellido.strip().capitalize(),
            email=email.strip(),
            sexo=sexo.strip().capitalize(),
            fecha_nacimiento=fecha_nacimiento,
            no_celular=no_celular.strip(),
        )
        self.db.add(estudiante)
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante

    def obtener_estudiante(self, id_estudiante=UUID):
        return (
            self.db.query(Estudiante)
            .filter(Estudiante.id_estudiante == id_estudiante)
            .first()
        )

    def obtener_estudiantes(
        self,
    ) -> List[Estudiante]:
        return self.db.query(Estudiante).all()

    def actualizar_estudiante(self, estudiante_id, data: dict):
        estudiante = (
            self.db.query(Estudiante)
            .filter(Estudiante.id_estudiante == estudiante_id)
            .first()
        )

        if not estudiante:
            raise ValueError("No existe el estudiante para actualizar")

        for key, value in data.items():
            setattr(estudiante, key, value)

        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante
