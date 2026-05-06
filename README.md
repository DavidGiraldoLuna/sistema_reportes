# Sistema de Reportes de Infraestructura Universitaria
**Universidad del Magdalena — Seminario III**

Sistema web para la gestión de reportes de daños en la infraestructura del campus universitario. Permite a estudiantes reportar daños, a administradores gestionarlos y asignar técnicos, y a técnicos atender y actualizar el estado de los reportes.

---

## Tecnologías
- Python 3.13
- Django 6.0
- PostgreSQL 18
- Bootstrap 5.3
- Bootstrap Icons

---

## Requisitos previos
- Python 3.11+
- PostgreSQL instalado y corriendo
- Git

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/DavidGiraldoLuna/sistema_reportes.git
cd sistema_reportes
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install django psycopg2-binary pillow
```

### 4. Configurar la base de datos en PostgreSQL
Abre pgAdmin y ejecuta esto en la base de datos `postgres`:
```sql
CREATE DATABASE sistema_reportes;
CREATE USER reportes_user WITH PASSWORD 'reportes1234';
GRANT ALL PRIVILEGES ON DATABASE sistema_reportes TO reportes_user;
```

Luego conéctate a `sistema_reportes` y ejecuta:
```sql
GRANT ALL ON SCHEMA public TO reportes_user;
ALTER SCHEMA public OWNER TO reportes_user;
```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Cargar datos iniciales
```bash
python manage.py shell
```
Dentro del shell pega esto:
```python
from usuarios.models import Rol
from reportes.models import Estado, TipoDano

Rol.objects.create(nombre='Solicitante')
Rol.objects.create(nombre='Administrador')
Rol.objects.create(nombre='Técnico')

Estado.objects.create(nombre='Pendiente')
Estado.objects.create(nombre='Validado')
Estado.objects.create(nombre='Rechazado')
Estado.objects.create(nombre='Asignado')
Estado.objects.create(nombre='Solucionado')
Estado.objects.create(nombre='Cerrado')
Estado.objects.create(nombre='Sin solucionar')
Estado.objects.create(nombre='Reasignado')

TipoDano.objects.create(nombre='Eléctrico')
TipoDano.objects.create(nombre='Plomería')
TipoDano.objects.create(nombre='Estructura')
TipoDano.objects.create(nombre='Mobiliario')
TipoDano.objects.create(nombre='Otro')
exit()
```

### 7. Crear superusuario
```bash
python manage.py createsuperuser
```

### 8. Ejecutar el servidor
```bash
python manage.py runserver
```

Abre el navegador en **http://127.0.0.1:8000**

---

## Roles del sistema
| Rol | Descripción |
|-----|-------------|
| Solicitante | Estudiante que crea y hace seguimiento de reportes |
| Administrador | Valida, rechaza, asigna técnicos y cierra reportes |
| Técnico | Atiende y actualiza el estado de los reportes asignados |

---

## Autores
- David de Jesús Giraldo Luna
- Gabriel Gómez Enrique Maestre

**Docente:** Luis del Cristo Garrido Barrios