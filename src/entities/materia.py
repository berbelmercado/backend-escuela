class Materia:
    def __init__(
        self, nombre_asignatura: str, horas_semana: int, modalidad: str, estado: str
    ) -> None:
        self.nombre_asignatura = nombre_asignatura
        self.horas_semana = horas_semana
        self.modalidad = modalidad
        self.estado = estado

    def __str__(self) -> str:
        return f"Materia: {self.nombre_asignatura}, Horas por semana: {self.horas_semana}, Modalidad: {self.modalidad}, Estado: {self.estado}"

    def registrar_asignatura(
        self, nombre_asignatura: str, horas_semana: int, modalidad: str, estado: str
    ) -> None:
        self.nombre_asignatura = nombre_asignatura
        self.horas_semana = horas_semana
        self.modalidad = modalidad
        self.estado = estado

    def actualizar_estado(self, nuevo_estado: str) -> None:
        self.estado = nuevo_estado
