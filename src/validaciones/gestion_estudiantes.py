class GestionEstudiantes:
    @staticmethod
    def captura_datos_estudiantes() -> tuple:
        """
        Solicita los datos del estudiante: nombre, id_estudiante y edad.
        """
        print("\n--- Registro de Nuevo Estudiante ---")
        nombre = input("Ingrese el nombre completo: ")
        id_estudiante = input("Ingrese el ID del estudiante: ")

        # Usamos un try-except por si el usuario no ingresa un número en la edad
        try:
            edad = int(input("Ingrese la edad: "))
        except ValueError:
            print("Edad no válida, se asignará 0 por defecto.")
            edad = 0

        return nombre, id_estudiante, edad
