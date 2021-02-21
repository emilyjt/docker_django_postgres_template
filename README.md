# docker django postgres templa
te

[![GitHub license](https://img.shields.io/github/license/emilyjt/docker_django_postgres_template)](https://github.com/emilyjt/docker_django_postgres_template/blob/main/LICENSE)

This template is for django. The django project is contained within docker and is ready for development. The django project already has a non-modified [custom user model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project). It is set up for use with PostgreSQL which is also included as a docker container. An example production deployment is included, which includes NGINX, and Redis.

I have also created and included several [alternative custom user models](https://github.com/emilyjt/docker_django_postgres_template/tree/main/www/django/src/templates_django/templates_django/account/alternative%20user%20models), and included them in this project:

- Login with an email address

  - [with a username field](https://github.com/emilyjt/docker_django_postgres_template/tree/main/www/django/src/templates_django/templates_django/account/alternative%20user%20models/Log%20in%20with%20email%20address/Username%20field)
  - [without a username field](https://github.com/emilyjt/docker_django_postgres_template/tree/main/www/django/src/templates_django/templates_django/account/alternative%20user%20models/Log%20in%20with%20email%20address/No%20username%20field)

- [Username is no longer case sensitive](https://github.com/emilyjt/docker_django_postgres_template/tree/main/www/django/src/templates_django/templates_django/account/alternative%20user%20models/Username%20is%20not%20case%20sensitive)


## Getting Started
### Requirements
- [Docker](https://docs.docker.com/engine/install/)

Start by cloning the project:

```sh
$ git clone https://github.com/emilyjt/docker_django_postgres_template.git <your-project>
$ cd <your-project>
```

I have included an [initialisation script](https://github.com/emilyjt/docker_django_postgres_template/blob/main/django_init.py) (written in Python) that: generates new secrets, and renames the project files automatically.

Run the script:

```sh
$ docker run -it --rm --name init-django -v ${PWD}:/usr/src/myapp -w /usr/src/myapp python:3 python django_init.py
```

Which will generate an output similar to below:

```sh
Unable to find image 'python:3' locally
3: Pulling from library/python
0ecb575e629c: Pull complete
7467d1831b69: Pull complete
feab2c490a3c: Pull complete
f15a0f46f8c3: Pull complete
937782447ff6: Pull complete
e78b7aaaab2c: Pull complete
b68a1c52a41c: Pull complete
ddcd772f47ec: Pull complete
0753beeb7344: Pull complete
Digest: sha256:942bc4201d0fe995d18dcf8ca50745cfe3d16c253f54366af10cae18a2bfe7f6
Status: Downloaded newer image for python:3

Please enter either: a project name, or the domain name this project will be deployed to:
$ example.co.uk
9 files have been updated, and 2 directories have been renamed.
```

The project is now ready for development.

### I want a local virtual environment for black/flake8/etc...

```sh
$ cd ./www/django/
```

#### Poetry

```sh
$ poetry install
$ poetry shell
```

#### venv

```sh
$ python -m venv .venv
$ ./.venv/Scripts/activate
(venv) $ pip install -r requirements.development.txt
```

## Useful commands

To start the development server:

```sh
$ docker-compose -f docker-compose.dev.yml up -d
```

To stop the development server:

```sh
$ docker-compose -f docker-compose.dev.yml down
```

To run a command using django `manage.py`:

(On the development server, the container name is extrapolated from the project name/domain name entered on my initialisation script - which is the SERVICENAME var in .env)

```sh
$ docker exec example_django python manage.py <command>
```

To get a permanent shell inside the container:

```sh
$ docker exec -it example_django /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"
```

## Authors

- [**emilyjt**](https://github.com/emilyjt)

See also the list of [contributors](https://github.com/emilyjt/django_template/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- spookylukey - [Django Views — The Right Way](https://spookylukey.github.io/django-views-the-right-way/the-pattern.html)
- [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)
- Claudio Jolowicz - [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
- Vitor Freitas - [How to Use Django's Built-in Login System](https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html)
- [calmcode](https://calmcode.io/)