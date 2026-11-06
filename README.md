## Setup

- Clone the repository
```console
$ git clone git@github.com:juliansprietsma/cover-glossary.git
```
- Create an environment and synchronise the dependencies
```console
$ uv venv
$ source .venv/bin/activate
$ uv sync
```
- setup the database connection. Make sure you have a postgres database running. Instructions on the postgres setup can be found here. Amend the `glossary/settings.py`, use the following setup:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'dbhost',
        'PORT': '5432'
    }
}
```
- Run the migrations
```console
$ uv run python manage.py migrate
```
These migrations create the table `Definitions` which contains the fields: Term, Defintion and Aliases. It also enables the pg_tgrm extension on the database, which allows Trigram Similarity for the fuzzy search.

- Create a superuser
```console
$ uv run python manage.py createsuperuser
```

- Run the code through docker
```console
$ docker compose up --build
```

- You can now go to `localhost:{APP_PORT}/admin` to see the admin interface, where defnitions can be added. Go to `localhost:{APP_PORT}/search?search_term="{Search_term}"` to search.