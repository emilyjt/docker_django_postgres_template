###############################################################################

FROM python:3.9 AS builder

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
ARG requirements
COPY ./$requirements ./
RUN python -m pip install --upgrade pip
# If we are running from the development compose, we should delete the production requirements.txt and use the requirements.development.txt instead
# RUN if [ "$mode" = "development" ] ; then rm requirements.txt && cp requirements.development.txt requirements.txt ; rm requirements.development.txt ; fi
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/app/wheels -r $requirements

###############################################################################

FROM python:3.9-slim

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \ 
    dos2unix \ 
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
COPY --from=builder /home/app/$requirements .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh and give it execute permissions
COPY ./docker/entrypoint.sh $HOME
RUN dos2unix /home/app/entrypoint.sh
RUN chmod +x /home/app/entrypoint.sh

COPY ./docker/wait-for-it.sh /usr/local/bin/
RUN dos2unix /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# copy the project to $APP_HOME
COPY ./src/django_template $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/entrypoint.sh"]