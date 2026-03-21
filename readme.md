#  Sistema de Gestión Escolar - Backend en Python

##  Propósito del proyecto

Este proyecto tiene como objetivo desarrollar un sistema básico de gestión escolar utilizando Python.
El sistema permite registrar estudiantes, profesores, asignaturas, inscripciones y calificaciones, además de calcular promedios individuales y grupales.

El proyecto está enfocado en aplicar programación orientada a objetos (POO), organización de carpetas y trabajo colaborativo con Git y GitHub.

---

## Entidades del sistema

El sistema está basado en las siguientes entidades principales:

###  Estudiantes

Permite registrar:

* Nombre del estudiante
* Identificación
* Edad
* Sexo
* Celular

---

###  Profesor

Permite registrar:

* Nombre del profesor
* Identificación
* Edad
* Sexo
* Asignaturas que enseña

---

###  Asignaturas

Permite registrar:

* Nombre de la asignatura
* Profesor asignado
* Lista de estudiantes inscritos

---

###  Inscripción

Permite registrar:

* Qué estudiante está inscrito
* En qué asignatura está inscrito
* Fecha de inscripción

Esta entidad conecta estudiantes con asignaturas.

---

###  Calificaciones

Permite registrar:

* Notas de cada estudiante
* Notas por asignatura
* Promedio individual
* Promedio general del grupo

---

##  Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```
backend-escuela/
│
├── src/
│   └── entities/
│       ├── estudiante.py
│       ├── profesor.py
│       ├── asignatura.py
│       ├── inscripcion.py
│       └── calificaciones.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

Esta estructura permite mantener el código organizado y facilita el trabajo en equipo.

---

##  Cómo instalar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/berbelmercado/backend-escuela.git
```

---

### 2. Entrar a la carpeta del proyecto

```bash
cd backend-escuela
```

---

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

---

### 4. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

---

##  Uso de requirements.txt

Para instalar las dependencias necesarias ejecuta:

```bash
pip install -r requirements.txt
```

---

##  Uso del archivo .env

El archivo `.env` se utiliza para almacenar configuraciones del proyecto, como variables de entorno.

Ejemplo:

```
APP_NAME=Sistema Escolar
VERSION=1.0
```

---

##  Cómo ejecutar el proyecto

Después de activar el entorno virtual, ejecuta:

```bash
python main.py
```
---

##  URL del video

```

```
---


