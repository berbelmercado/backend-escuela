from src.entities.materia import Materia
from src.validaciones.gestion_materias import GestionMaterias
from src.validaciones.gestion_profesor import GestionProfesor
from src.entities.profesor import Profesor
from src.entities.estudiante import Estudiante
from src.validaciones.gestion_estudiantes import GestionEstudiantes

materias = []
profesores = []
estudiantes = []


def menu() -> None:
    print("=== Menú de Gestión de Escuela ===")
    print("1. Registrar nueva materia")
    print("2. Consultar materias registradas")
    print("3. Actualizar estado de una materia")
    print("4. Crear nuevo profesor")
    print("5. Mostrar profesores registrados")
    print("6. Registrar nuevo estudiante")
    print("7. Mostrar estudiantes registrados")


def main() -> None:
    opciones = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
    ]
    while True:

        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion not in opciones:

            break
        if opcion == 1:
            obj_materias = Materia(
                *GestionMaterias.captura_datos_materias(),
            )
            materias.append(obj_materias)
            print("Materia registrada exitosamente.")

        if opcion == 2:
            for materia in materias:
                print(materia.consultar_asingaturas())

        if opcion == 4:
            obj_profesor = Profesor(*GestionProfesor.captura_datos_profesor())
            profesores.append(obj_profesor)
            print("Profesor registrado exitosamente.")
        if opcion == 5:
            for profesor in profesores:
                profesor.mostrar_info()

        if opcion == 6:
            obj_estudiante = Estudiante(
                *GestionEstudiantes.captura_datos_estudiantes(),
            )
            estudiantes.append(obj_estudiante)
            print("Estudiante registrado exitosamente.")

        if opcion == 7:
            if not estudiantes:
                print("No hay estudiantes registrados.")
            for estudiante in estudiantes:
                estudiante.mostrar_info()


if __name__ == "__main__":
    main()
