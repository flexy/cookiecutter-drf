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

3. Initialize [pre-commit](https://pre-commit.com/):
```bash
pre-commit install
```

4. Create an environment configuration file (.env) with the following contents:
```
DJANGO_ALLOWED_HOSTS=*
DJANGO_SECRET_KEY=local
```

5. Run the project:
```bash
docker-compose up
```

6. In a new shell, create a super user:
```bash
docker-compose run --rm web ./manage.py createsuperuser
```


### Travis CI Setup
1. Enable the repository on Travis CI: [read their tutorial](https://docs.travis-ci.com/user/getting-started/).
2. In the Travis project settings, set the following environment variables:

| Key | Value |
| --- | --- |
| DJANGO_SECRET_KEY | A unique, unpredictable value |


### Heroku Setup
Add the following config vars to your Heroku instance:

| Key | Value |
| --- | --- |
| ENVIRONMENT_NAME | The name of your environment (e.g. `'prod'`) |
| DJANGO_SECRET_KEY | A unique, unpredictable value |
| DJANGO_ALLOWED_HOSTS | A comma separated list of origins that can host this API (e.g. my-app.herokuapp.com) |
| DJANGO_CORS_ORIGIN_WHITELIST | A comma separated list of origins that can access this API (e.g. localhost:8080) |
| DJANGO_ADMIN_URL | The URL to use for the Django Admin (should be random for security) |
| DJANGO_CONFIGURATION | The Django settings class to use |
| DJANGO_SETTINGS_MODULE | The Python module from which to load the Django settings class |
| DJANGO_DEFAULT_FROM_EMAIL | The default sender for transactional emails |


### OAuth Setup
1. Visit the project in your web browser: http://localhost:8000/
2. Login with an admin user.
3. Register a new application via the OAuth application endpoint: http://localhost:8000/api/v1/auth/oauth/applications/


## Other Tasks
### Build Docker
This is required after every dependency change.
```bash
docker-compose build
```

### Run a command inside Docker
Note: Bash is not available in Linux Alpine, so you must use `ash` or `sh`.
```bash
docker-compose run --rm web <command>
```

### Destroy Docker
This destroys the project's Docker containers, networks, volumes, and images.
```bash
docker-compose down
```

### Run PSQL
```bash
docker-compose run --rm postgres psql postgres://postgres:@postgres:5432/postgres
```

### Get the Heroku database connection url
```bash
heroku pg:credentials:url DATABASE
```
