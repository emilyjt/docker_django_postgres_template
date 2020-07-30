FROM python:3.8.5

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV HOME=/home/app
ENV APP_HOME=/home/app/django
RUN mkdir -p $APP_HOME

WORKDIR $HOME
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

# copy project
COPY ./docker/development/entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY ./src/django_template ./django

WORKDIR $APP_HOME

# run entrypoint.sh
ENTRYPOINT ["/home/app/entrypoint.sh"]