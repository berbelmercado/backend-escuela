from src.entities.materia import Materia
from src.validaciones.gestion_materias import GestionMaterias

materias = []


def menu() -> None:
    print("=== Menú de Gestión de Escuela ===")
    print("1. Registrar nueva materia")
    print("2. Consultar materias registradas")
    print("3. Actualizar estado de una materia")


def main() -> None:
    opciones = [
        1,
        2,
        3,
        4,
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


if __name__ == "__main__":
    main()
