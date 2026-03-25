from database.config import SessionLocal, Base, engine
from crud.estudiante_crud import EstudianteCrud
from crud.curso_crud import CursoCrud
from datetime import datetime
from uuid import UUID

Base.metadata.create_all(bind=engine)


def mostrar_menu():
    print("\n===== MENÚ =====")
    print("--- Estudiantes ---")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("--- Cursos ---")
    print("6. Crear curso")
    print("7. Listar cursos")
    print("8. Buscar curso por ID")
    print("9. Actualizar curso")
    print("10. Eliminar curso")
    print("0. Salir")


def main():
    db = SessionLocal()
    estudiante_crud = EstudianteCrud(db)
    curso_crud = CursoCrud(db)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # ── ESTUDIANTES ────────────────────────────────────────────

        # Creacion estudiante
        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            sexo = input("Sexo: ")
            fecha_str = input("Fecha nacimiento (YYYY-MM-DD): ")
            celular = input("Celular: ")

            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

            estudiante = estudiante_crud.crear_estudiante(
                cedula, nombre, apellido, email, sexo, fecha, celular
            )

            print(
                f" Creado con ID: {estudiante.id_estudiante}, nombre: {estudiante.nombre} apellido: {estudiante.apellido}"
            )

        # Consultar todo
        elif opcion == "2":
            estudiantes = estudiante_crud.obtener_estudiantes()

            for e in estudiantes:
                print(
                    f" Id: {e.id_estudiante}  Cedula: {e.cedula} | Nombre: {e.nombre} {e.apellido} | Correo: {e.email} | Celular: {e.no_celular}"
                )

        # Consultar uno
        elif opcion == "3":
            id_est = UUID(input("Ingrese ID: "))
            estudiante = estudiante_crud.obtener_estudiante(id_est)

            if estudiante:
                print(f"{estudiante.nombre} {estudiante.apellido} - {estudiante.email}")
            else:
                print(" No encontrado")

        # actualizar estudiante
        elif opcion == "4":
            id_est = UUID(input("Ingrese ID a actualizar: "))
            campo = input("Campo a actualizar (nombre, email, etc): ")
            valor = input("Nuevo valor: ")

            estudiante = estudiante_crud.actualizar_estudiante(id_est, {campo: valor})
            print(" Actualizado:", estudiante.nombre)

        # Eliminar estudiante
        elif opcion == "5":
            id_est = UUID(input("Ingrese ID a eliminar: "))
            estudiante_crud.eliminar_estudiante(id_est)
            print(" Eliminado")

        # ── CURSOS ─────────────────────────────────────────────────

        # Crear curso
        elif opcion == "6":
            nombre_curso = input("Nombre del curso: ")

            curso = curso_crud.crear_curso(nombre_curso)
            print(f" Creado con ID: {curso.id_curso}, nombre: {curso.nombre_curso}")

        # Consultar todos los cursos
        elif opcion == "7":
            cursos = curso_crud.obtener_cursos()

            if cursos:
                for c in cursos:
                    print(
                        f" Id: {c.id_curso} | Nombre: {c.nombre_curso} | Creado: {c.fecha_creacion}"
                    )
            else:
                print(" No hay cursos registrados")

        # consultar uno
        elif opcion == "8":
            id_curso = UUID(input("Ingrese ID del curso: "))
            curso = curso_crud.obtener_curso(id_curso)

            if curso:
                print(
                    f" Id: {curso.id_curso} | Nombre: {curso.nombre_curso} | Creado: {curso.fecha_creacion}"
                )
            else:
                print(" No encontrado")

        # Actualizar curso
        elif opcion == "9":
            id_curso = UUID(input("Ingrese ID del curso a actualizar: "))
            campo = input("Campo a actualizar (nombre_curso): ")
            valor = input("Nuevo valor: ")

            curso = curso_crud.actualizar_curso(id_curso, {campo: valor})
            print(" Actualizado:", curso.nombre_curso)

        # Eliminar curso
        elif opcion == "10":
            id_curso = UUID(input("Ingrese ID del curso a eliminar: "))
            curso_crud.eliminar_curso(id_curso)
            print(" Eliminado")

        # Salir
        elif opcion == "0":
            print(" Saliendo...")
            break

        else:
            print(" Opción inválida")


if __name__ == "__main__":
    main()
