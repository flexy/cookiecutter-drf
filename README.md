# cookiecutter-drf
[![Build Status](https://travis-ci.com/fndrz/cookiecutter-drf.svg?token=qdpTcWC2mqQPPSZNoKk1&branch=master)](https://travis-ci.com/fndrz/cookiecutter-drf)
[![codecov](https://codecov.io/gh/fndrz/cookiecutter-drf/branch/master/graph/badge.svg?token=aG2CYaPmQ0)](https://codecov.io/gh/fndrz/cookiecutter-drf)


## Getting Started
1. [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html).
2. Generate your project from cookiecutter-drf:
```bash
cookiecutter gh:fndrz/cookiecutter-drf
```


## Features
### Architecture:
* Containerized with Docker
* Python 3.7
* Django 2.1
* Web server: Gunicorn and Uvicorn
* Databases: PostgreSQL 9.6, Redis 4.0.11
* Dependency and python version management (Pipenv)

### Utilities:
* Better settings (django-environ, django-configurations)
* Better logging (logutils)
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

### Testing:
* pytest with pytest-django
* Easy API testing (django-rest-assured)
* Factories (factory-boy)
* django-debug-toolbar available locally
* Code quality (Flake8)
* Code coverage (pytest-cov)
* CI integration (Travis CI)

### Continuous Deployment:
* Heroku


## Upcoming Features
* Email verification
* Better permissions


## Development
### Generate the project
```bash
cookiecutter . --no-input --overwrite-if-exists
```
