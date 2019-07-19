# FROM python:3-alpine3.10
# FROM python:3
FROM python:3-slim
# FROM python:3

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install libopus0 opus-tools -y
# RUN apt-get install libopus0
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV DISCORD_BOT_KEY "key"

COPY ./app /app
# RUN cd /app/bin/opus && ./configure && make && make check
ENTRYPOINT python3 /app/main.py