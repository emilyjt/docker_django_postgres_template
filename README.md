# django template

[![GitHub license](https://img.shields.io/github/license/emilyjt/django-template)](https://github.com/emilyjt/django-template/blob/master/LICENSE)

A fairly basic django template that includes a non-modified [custom user model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) and an opinionated [good folder structure](https://hynek.me/articles/testing-packaging/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### On a Windows OS

```bash
git clone https://github.com/emilyjt/django-template.git
cd django-template
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

and install the project requirements:

```bash
(venv) pip install -r requirements.txt
```

You should be able to now start the django development server and see a very basic home page with a random number and a link to log in.

```bash
(venv) cd .\src\django_template\
(venv) python manage.py makemigrations
(venv) python manage.py migrate
(venv) python manage.py runserver
```

## Authors

* [**emilyjt**](https://github.com/emilyjt)

See also the list of [contributors](https://github.com/emilyjt/django-template/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Claudio Jolowicz - [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
* Vitor Freitas - [How to Use Django's Built-in Login System](https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html)
* [calmcode](https://calmcode.io/)

