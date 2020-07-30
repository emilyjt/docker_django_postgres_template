###############################################################################

FROM python:3.8.5 AS builder

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

WORKDIR /home/app

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3-dev \
    musl-dev

COPY ./requirements.production.txt .

RUN python -m pip install --upgrade pip

# install dependencies to the local user directory (eg. /root/.local)
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/app/wheels -r requirements.production.txt

###############################################################################

FROM python:3.8.5-slim

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r app && useradd --no-log-init -r -g app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/django
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# copy only the dependencies installation from the 1st stage image
RUN python -m pip install --upgrade pip
COPY --from=builder /home/app/wheels /wheels
COPY --from=builder /home/app/requirements.production.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.production.sh
COPY ./docker/production/entrypoint.production.sh $APP_HOME
RUN chmod +x /home/app/django/entrypoint.production.sh

COPY ./src/django_template $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.production.sh
ENTRYPOINT ["/home/app/django/entrypoint.production.sh"]