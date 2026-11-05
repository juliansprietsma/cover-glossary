FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
COPY . /app

# Disable development dependencies
ENV UV_NO_DEV=1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]