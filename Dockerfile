FROM python:3-alpine3.10

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

ENV DISCORD_BOT_KEY "NjAwODY2MTM0OTI0OTg0MzIw.XS8dzw.4A42COeyGd0q43k0MH6BbsI19qk"

COPY ./app /app

ENTRYPOINT python3 /app/main.py