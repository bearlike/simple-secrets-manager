# syntax=docker/dockerfile:1.0

FROM python:3.13-slim-bookworm

LABEL org.opencontainers.image.title="Simple Secrets Manager"
LABEL org.opencontainers.image.version="1.2.2"
LABEL org.opencontainers.image.authors="Krishnakanth Alagiri"
LABEL org.opencontainers.image.url="https://github.com/bearlike/simple-secrets-manager"
LABEL org.opencontainers.image.source="https://github.com/bearlike/simple-secrets-manager"
LABEL org.opencontainers.image.description="Secure storage, and delivery for tokens, passwords, API keys, and other secrets."

ARG DEBIAN_FRONTEND=noninteractive
ARG LANG=C.UTF-8

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

ENV PORT 5000
ENV CONNECTION_STRING "mongodb://root:password@mongo:27017"
CMD [ "python3", "server.py" ]
