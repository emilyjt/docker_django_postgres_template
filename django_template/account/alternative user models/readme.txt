To use a custom user model, copy and paste the files to the "src/django_template/apps/account" folder.

The original files are contained within the "default" folder. After swapping to a new user model, do not
forget to "py manage.py makemigrations" and then "py manage.py migrate".