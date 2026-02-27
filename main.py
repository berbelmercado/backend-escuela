from src.entities.profesor import Profesor

prof1 = Profesor("Carlos Pérez", 101, "Matemáticas")
prof1.asignar_materia("Álgebra")

prof1.mostrar_info()
prof2 = Profesor("Ana Gómez", 102, "Física")
prof2.asignar_materia("Física Mecánica, termonámina y Fisica de campos")
prof2.mostrar_info()
prof3 = Profesor("Luis Martínez", 103, "Química")
prof3.asignar_materia("Química Orgánica")
prof3.mostrar_info()
