from database.config import SessionLocal, Base, engine
from crud.estudiante_crud import EstudianteCrud
from datetime import datetime
from uuid import UUID

Base.metadata.create_all(bind=engine)


def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("0. Salir")


def main():
    db = SessionLocal()
    crud = EstudianteCrud(db)

    try:
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            # 🔹 CREATE
            if opcion == "1":
                cedula = input("Cédula: ")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")
                sexo = input("Sexo: ")
                fecha_str = input("Fecha nacimiento (YYYY-MM-DD): ")
                celular = input("Celular: ")

                fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

                estudiante = crud.crear_estudiante(
                    cedula, nombre, apellido, email, sexo, fecha, celular
                )

                print(
                    f"✅ Creado con ID: {estudiante.id_estudiante}, nombre:{estudiante.nombre} apellido: {estudiante.apellido}"
                )

            # 🔹 READ ALL
            elif opcion == "2":
                estudiantes = crud.obtener_estudiantes()

                for e in estudiantes:
                    print(
                        f" Id: {e.id_estudiante}  Cedula: {e.cedula} | Nombre:{e.nombre} {e.apellido} | Correo: {e.email} | Celular{e.no_celular}"
                    )

            # 🔹 READ ONE
            elif opcion == "3":
                id_est = UUID(input("Ingrese ID: "))
                estudiante = crud.obtener_estudiante(id_est)

                if estudiante:
                    print(
                        f"{estudiante.nombre} {estudiante.apellido} - {estudiante.email}"
                    )
                else:
                    print("❌ No encontrado")

            # 🔹 UPDATE
            elif opcion == "4":
                id_est = UUID(input("Ingrese ID a actualizar: "))

                campo = input("Campo a actualizar (nombre, email, etc): ")
                valor = input("Nuevo valor: ")

                estudiante = crud.actualizar_estudiante(id_est, {campo: valor})

                print("✅ Actualizado:", estudiante.nombre)

            # 🔹 DELETE
            elif opcion == "5":
                id_est = UUID(input("Ingrese ID a eliminar: "))
                crud.eliminar_estudiante(id_est)
                print("🗑️ Eliminado")

            # 🔹 EXIT
            elif opcion == "0":
                print("👋 Saliendo...")
                break

            else:
                print("❌ Opción inválida")

    finally:
        db.close()


if __name__ == "__main__":
    main()
