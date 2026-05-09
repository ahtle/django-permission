# django-permission

A Django-based authorization framework demonstrating composable permissions, group-based access control, and declarative API authorization.

The project uses:

Django
Django REST Framework
PostgreSQL
Docker

This repository is intended for local development and experimentation.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine with the Compose plugin)
- Python 3.12+


---
## Start local development

1. Start the application

From the project root:

```bash
docker compose up --build
```

This will:

- build the Docker image
- start PostgreSQL
- install Python dependencies from requirements.txt
- run Django migrations
- start the Django development server

Application URLs:

Django app: http://localhost:8000/
Django admin: http://localhost:8000/admin/
PostgreSQL: localhost:5432

2. Create a Django superuser (with the stack running):

```bash
docker compose exec web python manage.py createsuperuser
```

## Stop local development

```bash
docker compose down
```

### Remove containers and wipe the database

```bash
docker compose down -v
```

---
## Local Python Environment

The application runs fully inside Docker, but can run on local machine as well.

Create local virtual environment, activate, and install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then configure your IDE to use:

```bash
./.venv/bin/python
```

---
## Useful commands

```bash
# Run a one-off management command without starting the dev server:
docker compose run --rm web python manage.py <command>
```

```bash
docker compose logs -f web
```

```bash
docker compose exec web python manage.py makemigrations
```

```bash
docker compose exec web python manage.py migrate
```

```bash
docker compose exec web python manage.py shell -v 2
```

---
## Test

```bash
docker compose run --rm web python manage.py test
```