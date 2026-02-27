class Profesor:
    def __init__(self, nombre, id_profesor, especialidad):
        self.nombre = nombre
        self.id_profesor = id_profesor
        self.especialidad = especialidad
        self.materias = []

    def asignar_materia(self, materia):
        self.materias.append(materia)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID Profesor: {self.id_profesor}")
        print(f"Especialidad: {self.especialidad}")
        print("Materias asignadas:")
        for materia in self.materias:
            print(f"- {materia}")
