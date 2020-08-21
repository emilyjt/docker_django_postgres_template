# docker django postgres template

[![GitHub license](https://img.shields.io/github/license/emilyjt/django_template)](https://github.com/emilyjt/django_template/blob/master/LICENSE)

This is a basic django template that has been designed for use with docker. The included database is postgres, also contained within docker. The django project has a non-modified [custom user model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project).

There are several alternative custom user models included in this project:

- Login with an email address

  - with a username field
  - without a username field

- Username is no longer case sensitive

_With more to come in the future_

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. You must have docker installed.

### On a Windows OS

```bash
git clone https://github.com/emilyjt/docker_django_postgres_template.git <project name>
cd <project name>
```

I have included a quick script to rename all refrences to `django_template` in the project.
So for the next step, we will:

```bash
py .\start_project.py
(input prompt) What would you like your project to be called?
<project name>
```

---

At this point now, you can immediately load the development server to check if everything is working:

```bash
docker-compose up --build -d
docker exec -it <container name/ID> /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"
```

You should now have access to a terminal window inside the django docker container. Use this
to migrate and create a super user.

---

For development, because I recommend the use of black and flake8, you can create and activate a virtual environment:

#### Poetry

```bash
poetry install
poetry shell
```

#### Venv

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

and install the project requirements:

```bash
(venv) pip install -r requirements.txt
```

## Authors

- [**emilyjt**](https://github.com/emilyjt)

See also the list of [contributors](https://github.com/emilyjt/django_template/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- spookylukey - [Django Views — The Right Way](https://spookylukey.github.io/django-views-the-right-way/the-pattern.html)
- Claudio Jolowicz - [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
- Vitor Freitas - [How to Use Django's Built-in Login System](https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html)
- [calmcode](https://calmcode.io/)
