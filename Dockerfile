FROM python:3.12.1-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/code 

# create directory for the app user
RUN mkdir -p $HOME  \
    && addgroup --system app \
    && adduser --system --group app 

WORKDIR $HOME

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . $HOME

# Change the owner of app home
RUN chown -R app:app $HOME
USER app

