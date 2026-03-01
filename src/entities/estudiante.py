class Estudiante:
    def __init__(self, nombre: str, id_estudiante: str, edad: int) -> None:
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.edad = edad
        self.notas = {}  # Usaremos un diccionario: {"Materia": nota}

    def registrar_nota(self, materia: str, nota: float) -> None:
        self.notas[materia] = nota
        print(f"Nota {nota} registrada en {materia} para {self.nombre}")

    def mostrar_info(self) -> None:
        print(f"Estudiante: {self.nombre}")
        print(f"ID: {self.id_estudiante}")
        print(f"Edad: {self.edad}")
        print("Calificaciones:")
        for materia, nota in self.notas.items():
            print(f"- {materia}: {nota}")

    def calcular_promedio(self) -> float:
        if not self.notas:
            return 0.0
        promedio = sum(self.notas.values()) / len(self.notas)
        return round(promedio, 2)