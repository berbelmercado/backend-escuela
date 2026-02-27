class GestionProfesor:

    @staticmethod
    def captura_datos_profesor() -> str:
        nombre = input("Ingrese el nombre del profesor: ").strip()
        id_profesor = int(input("Ingrese el ID del profesor: "))
        especialidad = input("Ingrese la especialidad del profesor: ").strip()
        return nombre, id_profesor, especialidad
