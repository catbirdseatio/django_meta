FROM python:3.12.1-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user named 'appuser'
RUN addgroup --system appuser && adduser --system --group appuser

# Set work directory
WORKDIR /code

RUN chown -R appuser:appuser /code
USER appuser

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
