# AGENTS.md

Agente identificado: Codex.

Este repositorio debe trabajarse con el metodo Planificar -> Ejecutar -> Iterar.
El proyecto no inicia desde cero: ya existe una aplicacion backend de gestion escolar con codigo, estructura, tecnologias y logica implementada.

## Contexto del proyecto

- Proyecto principal: `backend-escuela`.
- Lenguaje: Python.
- Framework API: FastAPI.
- Persistencia: SQLAlchemy con URL de conexion `DATABASE_URL` cargada desde `.env`.
- Base de datos esperada: PostgreSQL/Neon, usando SSL en `database/config.py`.
- Capas existentes: `routers/`, `crud/`, `entities/`, `schemas/`, `database/`.
- Entradas actuales: `app.py` para API HTTP y `main.py` para menu de consola.

## Reglas de trabajo

1. Antes de implementar cambios, revisar la estructura y los patrones existentes.
2. Mantener las tecnologias actuales salvo instruccion explicita del usuario.
3. Mantener la organizacion actual por capas:
   - `routers/` para endpoints FastAPI.
   - `schemas/` para modelos Pydantic de entrada/salida.
   - `crud/` para operaciones de persistencia.
   - `entities/` para modelos SQLAlchemy.
   - `database/` para configuracion de conexion y sesiones.
4. Evitar refactors grandes sin aprobacion.
5. Si se detectan malas practicas, documentarlas o reportarlas antes de cambiarlas.
6. No sobrescribir documentacion existente; complementarla cuando haga falta.
7. Actualizar `docs/SPEC.md` cuando una feature real cambie.

## Flujo Planificar -> Ejecutar -> Iterar

1. Brainstorming: aclarar objetivo, alcance, restricciones y riesgos.
2. Spec: registrar comportamiento esperado y estado actual en `docs/SPEC.md`.
3. Plan: dividir el trabajo en pasos verificables.
4. Ejecucion: implementar siguiendo la estructura y estilo existentes.
5. Iteracion: verificar, ajustar y actualizar la SPEC con lo realmente entregado.

## Convenciones observadas

- Nombres de modulos en minusculas y, cuando aplica, sufijo por capa: `_crud.py`, `_schema.py`.
- Clases de entidades y CRUD en PascalCase: `Estudiante`, `Curso`, `EstudianteCrud`, `CursoCrud`.
- Endpoints agrupados por entidad mediante `APIRouter(prefix=..., tags=...)`.
- Dependencia `get_db()` local en routers para abrir y cerrar sesiones SQLAlchemy.
- UUID como identificador principal en estudiantes y cursos.
- Normalizacion basica de strings en CRUD: `strip()` y `title()`.

## Restricciones actuales

- No existe `requirements.txt` en el estado revisado del proyecto.
- No hay suite de pruebas detectada.
- Existen cambios previos no confirmados en `routers/estudiante.py`; no deben revertirse sin autorizacion.
- Algunos modulos secundarios parecen incompletos o con imports inconsistentes. No corregir sin una tarea explicita.
