# SPEC

## Sistema actual

`backend-escuela` es una aplicacion backend para gestion escolar. En el estado actual del codigo, permite administrar estudiantes y cursos por medio de una API FastAPI y tambien por medio de un menu de consola.

El sistema usa SQLAlchemy para definir entidades y ejecutar operaciones de persistencia. La conexion a base de datos se carga desde `.env` mediante la variable `DATABASE_URL`.

## Tecnologias actuales

- Python.
- FastAPI.
- SQLAlchemy.
- Pydantic.
- python-dotenv.
- PostgreSQL/Neon segun la configuracion de `database/config.py`.
- UUID de PostgreSQL para identificadores de estudiantes y cursos.

No se detecto frontend en el repositorio.

## Arquitectura real

La organizacion actual es por capas simples:

- `app.py`: punto de entrada de la API FastAPI, configuracion CORS, creacion de tablas y registro de routers.
- `main.py`: punto de entrada CLI con menu interactivo para estudiantes y cursos.
- `database/config.py`: carga de `.env`, creacion de `engine`, `SessionLocal` y `Base`.
- `entities/`: modelos SQLAlchemy.
- `schemas/`: schemas Pydantic para contratos HTTP.
- `crud/`: operaciones de base de datos.
- `routers/`: endpoints FastAPI.

No hay evidencia de frontend ni de una arquitectura MVC formal. La separacion real es por responsabilidad tecnica: rutas, schemas, CRUD, entidades y configuracion de base de datos.

## Entidades detectadas

### Estudiante

Archivo: `entities/estudiante.py`

Campos principales:

- `id_estudiante`
- `cedula`
- `nombre`
- `apellido`
- `email`
- `sexo`
- `fecha_nacimiento`
- `no_celular`
- `fecha_creacion`

### Curso

Archivo: `entities/curso.py`

Campos principales:

- `id_curso`
- `nombre_curso`
- `fecha_creacion`

### Profesor

Archivo: `entities/profesor.py`

Modelo existente con campos de profesor y trazabilidad. No tiene router FastAPI detectado.

### Materia

Archivo: `entities/materia.py`

Modelo existente con codigo, nombre y trazabilidad. No tiene router FastAPI detectado.

### Inscripcion

Archivo: `entities/inscripcion.py`

Modelo existente para relacionar grado, asignatura, estudiante, profesor y periodo. No tiene router FastAPI detectado.

### Calificaciones

Archivo: `entities/calificaciones.py`

Modelo existente para registrar descripcion y valor de calificacion asociado a estudiante y profesor. No tiene router FastAPI detectado.

## Features implementadas

### API raiz y salud

Implementado en `app.py`.

- `GET /`: devuelve mensaje de bienvenida, version y rutas principales.
- `GET /health`: devuelve estado del servicio.

### CRUD de estudiantes por API

Implementado en `routers/estudiante.py`, `crud/estudiante_crud.py`, `schemas/estudiante_schema.py` y `entities/estudiante.py`.

Endpoints:

- `POST /estudiantes/`: registra estudiante.
- `GET /estudiantes/`: lista estudiantes.
- `GET /estudiantes/{id}`: consulta estudiante por UUID.
- `PUT /estudiantes/{id}`: actualiza estudiante.
- `DELETE /estudiantes/{id}`: elimina estudiante.

Comportamiento observado:

- Valida duplicados de email y cedula en creacion.
- Valida duplicados de email y cedula contra otros registros en actualizacion.
- Normaliza algunos textos con `strip()` y `title()`.
- Responde con `HTTPException` en errores o entidades no encontradas.

### CRUD de cursos por API

Implementado en `routers/curso.py`, `crud/curso_crud.py`, `schemas/curso_schema.py` y `entities/curso.py`.

Endpoints:

- `POST /cursos/`: registra curso.
- `GET /cursos/`: lista cursos.
- `GET /cursos/{id}`: consulta curso por UUID.
- `PUT /cursos/{id}`: actualiza curso.
- `DELETE /cursos/{id}`: elimina curso.

Comportamiento observado:

- Normaliza el nombre del curso con `strip()` y `title()`.
- Responde 404 cuando no hay cursos o no se encuentra un curso.
- Usa `CursoCrud` para persistencia.

### Menu de consola

Implementado en `main.py`.

Permite:

- Crear, listar, consultar, actualizar y eliminar estudiantes.
- Crear, listar, consultar, actualizar y eliminar cursos.
- Convertir entradas de fecha para estudiantes.
- Convertir IDs ingresados a UUID.

## Flujo de funcionamiento API

1. `app.py` importa `Base` y `engine`.
2. Ejecuta `Base.metadata.create_all(bind=engine)`.
3. Crea instancia `FastAPI`.
4. Configura CORS abierto.
5. Incluye routers de estudiantes y cursos.
6. Cada endpoint solicita una sesion mediante `get_db()`.
7. El router valida datos con Pydantic.
8. El router instancia el CRUD correspondiente.
9. El CRUD opera con SQLAlchemy y confirma transacciones.
10. La respuesta se serializa con schemas Pydantic o diccionarios.

## Flujo de funcionamiento CLI

1. `main.py` crea tablas con `Base.metadata.create_all(bind=engine)`.
2. Abre una sesion con `SessionLocal()`.
3. Instancia `EstudianteCrud` y `CursoCrud`.
4. Muestra un menu en bucle.
5. Segun la opcion, solicita datos por `input()`.
6. Ejecuta operaciones CRUD.
7. Imprime resultados en consola.

## Convenciones actuales

- Archivos por entidad y capa.
- Clases de entidades en singular y PascalCase.
- Clases CRUD en PascalCase con sufijo `Crud`.
- Schemas Pydantic con sufijos `Base`, `Create`, `Response` y `ResponseGet`.
- Routers con prefijo plural: `/estudiantes`, `/cursos`.
- Identificadores UUID para estudiantes y cursos.
- Tablas con nombres en espanol: `estudiantes`, `curso`, `profesores`, `materias`, `inscripcion`, `calificaciones`.

## Riesgos y observaciones

- No se detecto archivo `requirements.txt`, aunque el README lo menciona.
- No se detecto suite de pruebas.
- Hay cambios previos no confirmados en `routers/estudiante.py`.
- `crud/profesor_crud.py`, `crud/inscripcion_crud.py` y `crud/calificaciones_crud.py` importan desde modulos que parecen incorrectos para su ubicacion actual.
- `entities/inscripcion.py` y `entities/calificaciones.py` tienen imports duplicados o inconsistentes.
- `app.py` documenta rutas antiguas en comentarios, pero el codigo real usa `routers/estudiante.py` y `routers/curso.py`.
- CORS esta abierto para todos los origenes.

Estas observaciones no se corrigen en esta configuracion inicial porque el objetivo es integrar el metodo de trabajo sin modificar la logica existente.
