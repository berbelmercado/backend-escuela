# MASTER PLAN

## Vision actual

`backend-escuela` es un backend de gestion escolar construido en Python. Actualmente combina una API FastAPI y un menu de consola para administrar informacion escolar, con persistencia mediante SQLAlchemy y una base de datos PostgreSQL/Neon configurada por `DATABASE_URL`.

La vision del proyecto debe partir de lo ya implementado: consolidar una API estable para entidades escolares, mantener la separacion por capas existente y expandir funciones solo despues de documentarlas y planificarlas.

## Estado actual del sistema

- API FastAPI disponible desde `app.py`.
- Menu de consola disponible desde `main.py`.
- CRUD funcional implementado para estudiantes y cursos.
- Modelos SQLAlchemy existentes para estudiantes, cursos, profesores, materias, inscripciones y calificaciones.
- Schemas Pydantic existentes para estudiantes y cursos.
- Routers HTTP existentes para estudiantes y cursos.
- Configuracion de base de datos centralizada en `database/config.py`.

## Subproyectos reales

### API HTTP

Responsable de exponer endpoints FastAPI. Actualmente incluye:

- `GET /`
- `GET /health`
- CRUD de `/estudiantes`
- CRUD de `/cursos`

### Persistencia y modelos

Responsable de entidades SQLAlchemy, sesiones y conexion.

- `database/config.py`
- `entities/estudiante.py`
- `entities/curso.py`
- `entities/profesor.py`
- `entities/materia.py`
- `entities/inscripcion.py`
- `entities/calificaciones.py`

### Logica CRUD

Responsable de encapsular operaciones de base de datos.

- CRUD orientado a clases para estudiantes y cursos.
- CRUD funcional parcial para profesores, inscripciones y calificaciones.

### Validacion y serializacion

Responsable de contratos de entrada y salida con Pydantic.

- `schemas/estudiante_schema.py`
- `schemas/curso_schema.py`

### CLI de administracion

Responsable de operar estudiantes y cursos desde consola.

- `main.py`

## Proximos pasos logicos

1. Definir dependencias exactas del proyecto en un archivo instalable si el equipo lo autoriza.
2. Agregar pruebas basicas para endpoints de estudiantes y cursos.
3. Revisar y corregir imports inconsistentes en CRUD secundarios, con aprobacion previa.
4. Decidir si profesores, materias, inscripciones y calificaciones tendran routers y schemas propios.
5. Unificar criterios de nombres entre tablas, campos y respuestas cuando haya una tarea especifica.
6. Documentar variables de entorno requeridas sin exponer secretos.
7. Mantener `docs/SPEC.md` actualizado por cada cambio funcional.

## Metodo de trabajo integrado

Cada mejora debe seguir este ciclo:

1. Brainstorming: definir problema, usuarios, alcance y restricciones.
2. Spec: actualizar o crear la descripcion del comportamiento esperado.
3. Plan: dividir el trabajo en pasos concretos y verificables.
4. Ejecucion: cambiar codigo manteniendo estructura y convenciones.
5. Actualizacion de SPEC: documentar lo realmente implementado y riesgos restantes.

Este metodo se integra progresivamente. No requiere detener el desarrollo ni reorganizar carpetas existentes.
