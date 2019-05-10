# cookiecutter-drf
[![Build Status](https://travis-ci.com/flexy/cookiecutter-drf.svg?token=qdpTcWC2mqQPPSZNoKk1&branch=master)](https://travis-ci.com/flexy/cookiecutter-drf)
[![codecov](https://codecov.io/gh/flexy/cookiecutter-drf/branch/master/graph/badge.svg?token=aG2CYaPmQ0)](https://codecov.io/gh/flexy/cookiecutter-drf)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Getting Started
1. [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html).
2. Generate your project from cookiecutter-drf:
```bash
cookiecutter gh:flexy/cookiecutter-drf
```


## Features
### Architecture:
* Containerized with Docker
* Python 3.7
* Django 2.2
* Web server: Gunicorn and Uvicorn
* Databases: PostgreSQL, Redis
* Dependency and python version management (Pipenv)
* Tasks: Celery and Celery Beat

### Utilities:
* Better settings (django-environ, django-configurations)
* Better logging (Sentry, logutils)
* Common model fields and mixins (django-model-utils)

### API:
* Django Rest Framework
* Swagger UI (drf-yasg)
* Redoc UI (drf-yasg)
* OpenAPI schema (drf-yasg)
* QuerySet filtering (django-filter)

### Authentication:
* Custom user model
* Authentication endpoints (djoser)
* Social authentication and OAuth2 (social-auth-app-django, django-oauth-toolkit, django-rest-framework-social-oauth2)

### Testing and Code Quality:
* pytest with pytest-django
* Easy API testing (django-rest-assured)
* Factories (factory-boy)
* django-debug-toolbar available locally
* Code quality (Flake8, Black)
* Code coverage (pytest-cov)
* CI integration (Travis CI)

### Continuous Deployment:
* Heroku


## Upcoming Features
* Email verification
* Better permissions


## Development
### Getting started
1. Install dependencies:
```bash
pipenv install
```

2. Launch the project environment:
```bash
pipenv shell
```

3. Initialize [pre-commit](https://pre-commit.com/):
```bash
pre-commit install
```

### Generate the project
```bash
cookiecutter . --no-input --overwrite-if-exists
```
