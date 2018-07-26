# FNDRZ Template Usage


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
| DEV_REGISTRY_URL | `registry.heroku.com` |
| DEV_APP_URL | `registry.heroku.com/<Heroku Dev App Slug>/web` |
| PROD_REGISTRY_URL | `registry.heroku.com` |
| PROD_APP_URL | `registry.heroku.com/<Heroku Prod App Slug>/web` |
| DOCKER_USERNAME | *Docker username* |
| DOCKER_PASSWORD | *Docker password* |


# OAuth Setup
1. Visit the project in your web browser: http://localhost:8000/
2. Login with an admin user.
3. Register a new OAuth application:
  * Visit the application registration endpoint: http://localhost:8000/api/v1/oauth/applications/register/

  * Use the following settings:
    * Client Type: `Public`
    * Authorization Grant Type: `Implicit`


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
