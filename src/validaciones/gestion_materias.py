from src.entities.materia import Materia


class GestionMaterias:

    @staticmethod
    def captura_datos_materias() -> str:
        nombre_asignatura = input("Ingrese el nombre de la asignatura: ").strip()
        horas_semana = int(input("Ingrese las horas por semana: "))
        modalidad = input("Ingrese la modalidad (presencial/virtual): ").strip()
        estado = input("Ingrese el estado (activo/inactivo): ").strip()
        return nombre_asignatura, horas_semana, modalidad, estado

    @staticmethod
    def actualizar_estado_materia(materia: Materia) -> None:
        nuevo_estado = input("Ingrese el nuevo estado (activo/inactivo): ").strip()
        materia.actualizar_estado(nuevo_estado)
        print("Estado de la materia actualizado exitosamente.")
