# Instructions for custom user models

Navigate to the folder containing the custom user model files you would like to use.

Each of the custom user model templates should contain four files:

- admin.py
- forms.py
- managers.py
- models.py

Copy these files into the directory `www/django/src/templates_django/templates_django/account` replacing the files that are already there (replace `templates_django` with your project name where appropriate).

Open up your new `www/django/src/templates_django/templates_django/account/admin.py` and find the following line:

```python
# @admin.register(User) # <-- this line will need to uncommented
```

You will need to uncomment this line, like so:

```python
@admin.register(User) # <-- this line will need to uncommented
```

Finally, do not forget to `makemigrations` and `migrate`:

```sh
$ docker exec example_django python manage.py makemigrations
$ docker exec example_django python manage.py migrate
```