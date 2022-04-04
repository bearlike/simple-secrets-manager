# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

LABEL title="Secrets Manager"
LABEL version="1.0"
LABEL author.name="Krishnakanth Alagiri"
LABEL author.github="https://github.com/bearlike"
LABEL repository="https://github.com/bearlike/secrets-manager"
LABEL description="Secure storage, and delivery for tokens, passwords, \
API keys, and other secrets using HTTP API, Swagger UI or Python Package."

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV PORT 5000
CMD [ "python3", "server.py" ]