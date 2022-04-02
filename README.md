# Secrets Manager
Secure storage, and delivery for tokens, passwords, API keys, and other secrets using HTTP API, Swagger UI or Python Package.
`TL;DR`: Poor Man's Hashi Corp Vault 

## Why does this exist?
Hashi Corp Vault works well but it was meant for enterprises. Therefore, it was heavy and non-portable (atleast difficult) for my homelab setup. So I wanted to build a Secrets Manager intended for small scale setups that could also scale well. 

## Goals
- A lightweight system that sucks less power out of the wall. Therefore, minimal background jobs and reduced resource utilizations.
- Should be compatible on both `x86-64` and `arm64v8` (mainly Raspberry Pi 4).
- High stability, availability and easy scalability.      

## Available Secret Engines
- `kv` - Key-Value engine is used to store arbitrary secrets

## Future
- Secret engines for certificates (PKI), SSH and databases.
- Encrypting secrets before writing to a persistent storage, so gaining access to the raw storage isn't enough to access your secrets.

## Getting started
1. Start a Mongo database server. A basic `docker-compose.yml` is available for you. 
2. Create a `.env` file in the project root with the following values
```
CONNECTION_STRING=mongodb://username:password@mongo.hostname:27017
```
3. You will need atleast `python3.7`. Start the server by running `app.py`.
4. Visit the application via `http://server_hostname:5000/api` (default port is `5000`) to visit the Swagger UI. 