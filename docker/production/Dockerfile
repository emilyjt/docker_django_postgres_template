###############################################################################

FROM python:3.8.5 AS builder

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Set some enviroment variables and create the folders
WORKDIR /home/app
RUN mkdir -p /home/app

# Install the necessary packages to create the wheels
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3-dev \
    musl-dev

# Copy the requirements over, and create the wheels
COPY ./requirements.production.txt .
RUN python -m pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/app/wheels -r requirements.production.txt

###############################################################################

FROM python:3.8.5-slim

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# We need netcat to check if the postgres database has properly started
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a user for the app, so we don't have to use the root account
RUN groupadd -r app && useradd --no-log-init -r -g app app

# Set some enviroment variables and create the folders
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

# copy entrypoint.production.sh and give it execute permissions
COPY ./docker/production/entrypoint.production.sh $HOME
RUN chmod +x /home/app/entrypoint.production.sh

# copy the project to $APP_HOME
COPY ./src/django_template $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.production.sh
ENTRYPOINT ["/home/app/entrypoint.production.sh"]