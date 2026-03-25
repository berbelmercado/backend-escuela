from typing import List
from uuid import UUID
from entities.curso import Curso
from sqlalchemy.orm import Session


class CursoCrud:

    def __init__(self, db: Session):
        self.db = db

    def crear_curso(
        self,
        nombre_curso: str,
    ) -> Curso:
        curso = Curso(
            nombre_curso=nombre_curso.strip().title(),
        )
        self.db.add(curso)
        self.db.commit()
        self.db.refresh(curso)
        return curso

    def obtener_curso(self, id_curso: UUID) -> Curso:
        return self.db.query(Curso).filter(Curso.id_curso == id_curso).first()

    def obtener_cursos(self) -> List[Curso]:
        return self.db.query(Curso).all()

    def actualizar_curso(self, id_curso: UUID, data: dict) -> Curso:
        curso = self.db.query(Curso).filter(Curso.id_curso == id_curso).first()

        if not curso:
            raise ValueError("No existe el curso para actualizar")

        for key, value in data.items():
            setattr(curso, key, value)

        self.db.commit()
        self.db.refresh(curso)
        return curso

    def eliminar_curso(self, id_curso: UUID) -> bool:
        curso = self.db.query(Curso).filter(Curso.id_curso == id_curso).first()

        if not curso:
            raise ValueError("No existe el curso")

        self.db.delete(curso)
        self.db.commit()
        return True
