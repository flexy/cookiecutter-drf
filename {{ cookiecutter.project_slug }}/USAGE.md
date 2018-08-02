# {{ cookiecutter.project_name }} Usage


## Setup

1. Install dependencies:
  ```bash
  pipenv install
  ```

2. Launch the project environment:
  ```bash
  pipenv shell
  ```

3. Create an environment configuration file (.env) with the following contents:
  ```
  DJANGO_ALLOWED_HOSTS=*
  DJANGO_SECRET_KEY=local
  DJANGO_CORS_ORIGIN_WHITELIST=(localhost:8080)
  ```

4. Run the project:
  ```bash
  docker-compose up
  ```

5. In a new shell, create a super user:
  ```bash
  docker-compose run --rm web ./manage.py createsuperuser
  ```


# Travis CI Setup
1. Enable the repository on Travis CI: [read their tutorial](https://docs.travis-ci.com/user/getting-started/).
2. In the Travis project settings, set the following environment variables:

| Key | Value |
| --- | --- |
| DJANGO_SECRET_KEY | A unique, unpredictable value |


# Continuous Deployment Setup

Add the following environment variables to your Travis project settings:

| Key | Value |
| --- | --- |
| DEPLOY_DEV_ENABLED | `true` (`false` to explicitly disable) |
| DEPLOY_DEV_BRANCH | `develop` (or your dev branch) |
| DEPLOY_DEV_REGISTRY_URL | `registry.heroku.com` |
| DEPLOY_DEV_APP_URL | `registry.heroku.com/<Heroku Dev App Slug>/web` |
| DEPLOY_PROD_ENABLED | `true` (`false` to explicitly disable) |
| DEPLOY_PROD_BRANCH | `master` (or your prod branch) |
| DEPLOY_PROD_REGISTRY_URL | `registry.heroku.com` |
| DEPLOY_PROD_APP_URL | `registry.heroku.com/<Heroku Prod App Slug>/web` |
| DOCKER_USERNAME | *Docker username* |
| DOCKER_PASSWORD | *Docker password* |


# OAuth Setup
1. Visit the project in your web browser: http://localhost:8000/
2. Login with an admin user.
3. Register a new application via the OAuth application endpoint: http://localhost:8000/api/v1/auth/oauth/applications/


# Other Tasks
* Build the project:
  ```bash
  docker-compose build
  ```

* Run a command inside Docker:
  ```bash
  docker-compose run --rm web <command>
  ```

* Destroy the project's Docker containers, networks, volumes, and images:
  ```bash
  docker-compose down
  ```
