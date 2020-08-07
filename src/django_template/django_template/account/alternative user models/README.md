# Instructions for custom user models

Navigate to the folder containing the custom user model files you would like to use.

Each of the custom user model templates should contain four files:

- admin.py
- forms.py
- managers.py
- models.py

Copy these files into the directory `src\django_template\django_template\account` replacing the files that are already there.

Open up `admin.py` and find the following line:

```python
# @admin.register(User) # <-- this line will need to uncommented
```

You will need to uncomment this line, like so:

```python
@admin.register(User) # <-- this line will need to uncommented
```

Finally, do not forget to `makemigrations` and `migrate`, like so:

## Docker

```bash
docker-compose up --build -d
docker exec -it <container name/ID> /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"
python manage.py makemigrations
python manage.py migrate
```

## Non-docker

```bash
python manage.py makemigrations
python manage.py migrate
```
