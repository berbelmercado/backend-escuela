from database.config import SessionLocal, Base, engine
from crud.estudiante_crud import EstudianteCrud
from datetime import date

Base.metadata.create_all(bind=engine)

db = SessionLocal()

obj_estudiante = EstudianteCrud(db)

nuevo = obj_estudiante.crear_estudiante(
    cedula="123456",
    nombre="Juan",
    apellido="Perez",
    email="juan@test.com",
    sexo="M",
    fecha_nacimiento=date(2000, 1, 1),
    no_celular="3041108410",
)

print("Creado:", nuevo.id_estudiante)
