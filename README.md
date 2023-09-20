# Django Wordpress Import

## Setup

### Clone the repo

```bash
git clone git@github.com:wagtail-packages/django-wordpress-import.git
```

### Run with docker

```bash
docker-compose up -d --build
```

## Django import site

### Running an import

Start by entering the running container with:

```bash
docker-compose exec app bash
```

The first time you run it you will need to run the migrations and create a superuser:

```bash
./manage.py migrate
./manage.py createsuperuser
```

Then activate the poetry shell with:

```bash
poetry install && poetry shell
```

Then run the following commands to import the data:

```bash
dj authors
dj categories
dj tags
dj posts
dj pages
dj media
dj comments
```

or to run all of them

```bash
dj complete
```

## View/edit the imported data

You can view the imported data by going to the following url:

<http://localhost:8000/import-admin> and logging in with the superuser you created.

## View the API

You can view the API endpoints by going to the following url:

<http://localhost:8000/api/>
