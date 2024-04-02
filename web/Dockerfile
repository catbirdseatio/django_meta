FROM python:3.12.1-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/code/web 

# create directory for the app user and add user
RUN mkdir -p $HOME  \
    && mkdir $HOME/staticfiles \
    && addgroup --system app \
    && adduser --system --group app 

WORKDIR $HOME

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update -y \
    && apt-get install -y iputils-ping

# Copy project
COPY . $HOME

# Change the owner of app home
RUN chown -R app:app $HOME
USER app

