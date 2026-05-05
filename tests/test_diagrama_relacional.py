from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class DiagramaRelacionalTest(unittest.TestCase):
    def test_nuevas_entidades_siguen_diagrama(self):
        asignatura = read("entities/asignatura.py")
        inscripcion = read("entities/inscripcion.py")
        calificacion = read("entities/calificaciones.py")

        self.assertIn('__tablename__ = "asignatura"', asignatura)
        for column in [
            "id_asignatura",
            "nombre_asignatura",
            "horas_semanales",
            "modalidad",
            "estado",
        ]:
            self.assertIn(column, asignatura)

        self.assertIn("id_curso", inscripcion)
        self.assertIn('ForeignKey("curso.id_curso")', inscripcion)
        self.assertIn('ForeignKey("asignatura.id_asignatura")', inscripcion)
        self.assertIn('ForeignKey("estudiantes.id_estudiante")', inscripcion)
        self.assertIn('ForeignKey("profesores.id_profesor")', inscripcion)

        self.assertIn("id_calificacion", calificacion)
        self.assertIn("descripcion_nota", calificacion)
        self.assertIn("valor_nota", calificacion)
        self.assertIn('ForeignKey("asignatura.id_asignatura")', calificacion)

    def test_schemas_y_routers_nuevos_existen_y_se_registran(self):
        for path in [
            "schemas/profesor_schema.py",
            "schemas/asignatura_schema.py",
            "schemas/inscripcion_schema.py",
            "schemas/calificacion_schema.py",
            "routers/profesor.py",
            "routers/asignatura.py",
            "routers/inscripcion.py",
            "routers/calificaciones.py",
        ]:
            self.assertTrue((ROOT / path).exists(), path)

        app = read("app.py")
        for router_name in ["profesor", "asignatura", "inscripcion", "calificaciones"]:
            self.assertIn(router_name, app)
            self.assertIn(f"app.include_router({router_name}.router)", app)


if __name__ == "__main__":
    unittest.main()
