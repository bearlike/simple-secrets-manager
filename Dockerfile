# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

LABEL com.ssm.title="Simple Secrets Manager"
LABEL com.ssm.version="1.1.1"
LABEL com.ssm.author.name="Krishnakanth Alagiri"
LABEL com.ssm.author.github="https://github.com/bearlike"
LABEL com.ssm.repo="https://github.com/bearlike/simple-secrets-manager"
LABEL com.ssm.description="Secure storage, and delivery for tokens, passwords, \
API keys, and other secrets."

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV PORT 5000

CMD [ "python3", "server.py" ]