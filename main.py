from database.config import SessionLocal, Base, engine
from crud.estudiante_crud import EstudianteCrud
from datetime import date

Base.metadata.create_all(bind=engine)

db = SessionLocal()

obj_estudiante = EstudianteCrud(db)

nuevo = obj_estudiante.crear_estudiante(
    cedula="3245345",
    nombre="Camilo",
    apellido="Pelaez",
    email="camiloPelaez@test.com",
    sexo="M",
    fecha_nacimiento=date(1997, 1, 12),
    no_celular="554323898",
)

print("Creado:", nuevo.id_estudiante)

# consultar estudiantes
list_estudiante = obj_estudiante.obtener_estudiantes()

for i in list_estudiante:
    print(
        f"""cedula: {i.cedula} nombre: {i.nombre} apellido: {i.apellido} email: {i.email} sexo: {i.sexo} fecha de nacimiento: {i.fecha_nacimiento} Numero De Celular: {i.no_celular}"""
    )

# Consultar 1 solo estudiante
list_estudiante = obj_estudiante.obtener_estudiante(
    id_estudiante="9314ed91-c587-491f-a452-22a88dc6e089"
)

print(
    f"""cedula: {list_estudiante.cedula} nombre: {list_estudiante.nombre} apellido: {list_estudiante.apellido} email: {list_estudiante.email} sexo: {list_estudiante.sexo} fecha de nacimiento: {list_estudiante.fecha_nacimiento} Numero De Celular: {list_estudiante.no_celular}"""
)

# Eliminar 1 dato
obj_estudiante.eliminar_estudiante(id_estudiante="d2533c1e-5d26-446b-bac2-f4404a5034aa")
