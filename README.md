# cookiecutter-drf

[![Build Status](https://travis-ci.com/fndrz/cookiecutter-drf.svg?token=qdpTcWC2mqQPPSZNoKk1&branch=master)](https://travis-ci.com/fndrz/cookiecutter-drf)


## Requirements
- Docker
- Python 3.7
- Pipenv


## Features

### Architecture:
* Containerized (Docker)
* Dependency and python version management (Pipenv)
* Python 3.7
* Django 2.0

### Utilities:
* Better settings (django-environ, django-configurations)
* Better logging (logutils)
* Common model fields and mixins (django-model-utils)

### API:
* Django Rest Framework
* QuerySet filtering (django-filter)

### Authentication:
* Rest endpoints (django-rest-auth)
* OAuth2 support (django-oauth-toolkit)
* Social authentication (django-allauth)
* Custom user model
* Login with email instead of username

### Testing:
* pytest with pytest-django
* Easy API testing (django-rest-assured)
* Factories (factory-boy)
* django-debug-toolbar available locally
* Code quality (Flake8)
* CI integration (Travis CI)

### Continuous Deployment:
* Heroku


## Usage
See [USAGE.md](USAGE.md).
