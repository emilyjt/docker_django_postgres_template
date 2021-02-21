FROM python:3-buster AS builder

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# # Install the necessary packages to create the wheels
# RUN apt-get update \
#     && DEBIAN_FRONTEND=noninteractive apt-get install -y \
#     python3-dev \
#     musl-dev

# Set some enviroment variables and create the folders
WORKDIR /app

RUN mkdir -p /app

# Copy the requirements over, and create the wheels
ARG REQUIREMENTS
COPY ./django/$REQUIREMENTS ./
RUN python -m pip install --upgrade pip \ 
    && pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r $REQUIREMENTS

###############################################################################

FROM python:3-slim as runner

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set some enviroment variables and create the folders
ENV APP_HOME=/app/django
RUN mkdir -p $APP_HOME \
    && mkdir $APP_HOME/staticfiles \
    && mkdir $APP_HOME/mediafiles

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/$REQUIREMENTS $HOME

RUN python -m pip install --upgrade pip \
    && pip install --no-cache /wheels/* \
    && rm -rf /wheels

# copy entrypoint.sh and give it execute permissions
COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# copy wait-for-it.sh and give it execute permissions
COPY ./docker/wait-for-it /wait-for-it
RUN sed -i 's/\r$//g' /wait-for-it
RUN chmod +x /wait-for-it

# copy the project to $APP_HOME
ARG SERVICENAME
COPY ./django/src/$SERVICENAME $APP_HOME

WORKDIR $APP_HOME

# run entrypoint.sh
ENTRYPOINT ["/entrypoint"]