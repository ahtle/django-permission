# django-permission

Django app with Postgres in Docker Compose for local development.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine with the Compose plugin)


## Start local development

From the project root:

```bash
docker compose up --build
```

- App: http://127.0.0.1:8000/
- Postgres is published to `localhost` on port `5432` by default (`POSTGRES_PORT_PUBLISH`).
- On each start, the `web` service runs migrations, then Django’s development server.


## Stop local development

```bash
docker compose down
```

Containers and the default network are removed. The **named Postgres volume is kept**, so data survives until you delete it deliberately.

### Remove containers and wipe the database

```bash
docker compose down -v
```

`-v` removes the `postgres_data` volume and all database data.

## Useful commands

Create a Django superuser (with the stack running):

```bash
docker compose exec web python manage.py createsuperuser
```

Run a one-off management command without starting the dev server:

```bash
docker compose run --rm web python manage.py <command>
```

View logs (after `docker compose up -d`):

```bash
docker compose logs -f web
```

## Production note

The Compose setup uses Django’s **development** server. The `Dockerfile` default command uses **Gunicorn**; use that (or another WSGI server) with appropriate settings for real deployments.
