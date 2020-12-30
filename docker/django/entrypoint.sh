#!/bin/sh

# Check if the database has started
# We could also use ${POSTGRES_PORT:-5432} to provide a default value
if [ -n "$POSTGRES_HOST" ] && [ -n "$POSTGRES_PORT" ]
then
    /usr/local/bin/wait-for-it.sh "$POSTGRES_HOST:$POSTGRES_PORT" --strict --timeout=300
fi

python manage.py makemigrations
python manage.py migrate

# We do not want to run collectstatic during development, as we are probably
# using the django dev server
if [ "$DJANGO_SETTINGS_MODULE" != "config.settings.development" ]
then
    python manage.py collectstatic --noinput
fi

exec "$@"