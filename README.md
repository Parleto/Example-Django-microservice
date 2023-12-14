## About

This repository is an example microservice made in Django with minimal configuration.
Useful for creating microservices that don't need all features of Django.
This example shows the implementation of simple endpoint with added test in [pytest](https://docs.pytest.org/) and preconfigured translations.

## Info

Tested on Python 3.11. This will probably work on other versions too.

## How to run

### Run project setup

Creates a python env, upgrades pip and installs required python packages.

```bash
./run -s
# or
./run --setup
```

### Run dev server

Starts project in development mode with hot-reloading.

```bash
./run -d
# or
./run --dev
# change default port
./run -d 8000
# change default address and port
./run -d 192.168.0.8:8000
```

### Run tests

Starts all tests.

```bash
./run -t
# or
./run --tests
```

### Translations

#### Generate translations (make messages)

Searches for all strings marked for translation and generates \*.po files
for each language. See [makemessages](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemessages) for more details.

```bash
./run -mm
# or
./run --messages-make
```

#### Compile translations

Compiles \*.po files to use in translations. See [compilemessages](https://docs.djangoproject.com/en/5.0/ref/django-admin/#compilemessages)

```bash
./run -mc
# or
./run --messages-compile
```

#### Gunicorn example

To start microservice with gunicorn:

```bash
# install gunicorn
source backend/.venv/bin/activate
pip install gunicorn
# run
gunicorn --bind 127.0.0.1:8000 --chdir backend/project wsgi:application
```

