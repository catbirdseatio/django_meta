FROM python:3.12.1-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/home/app \
    APP_HOME=/home/app/web

# create directory for the app user
RUN mkdir -p $HOME  \
    && addgroup --system app \
    && adduser --system --group app \
    && mkdir $APP_HOME \
    && mkdir $APP_HOME/staticfiles 

WORKDIR $APP_HOME

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . $APP_HOME

# Change the owner of app home
RUN chown -R app:app $APP_HOME
USER app

