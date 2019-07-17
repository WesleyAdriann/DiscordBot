FROM python:3-alpine3.10

COPY ./app /app

RUN python /app/main.py