# Secrets Manager
Secure storage, and delivery for tokens, passwords, API keys, and other secrets using HTTP API, Swagger UI or Python Package.
`TL;DR`: Poor Man's Hashi Corp Vault 

## Why does this exist?
Hashi Corp Vault works well but it was meant for enterprises. Therefore, it was heavy and non-portable (atleast difficult) for my homelab setup. So I wanted to build a Secrets Manager intended for small scale setups that could also scale well. 

## Goals
- A lightweight system that sucks less power out of the wall. Therefore, minimal background jobs and reduced resource utilizations.
- Should be compatible on both `x86-64` and `arm64v8` (mainly Raspberry Pi 4).
- High stability, availability and easy scalability.      

## Available secret engines
- `kv` - Key-Value engine is used to store arbitrary secrets.

## Available authentication methods
- `token` - Allows users to authenticate using a token.

## Future
- Secret engines for certificates (PKI), SSH and databases.
- Encrypting secrets before writing to a persistent storage, so gaining access to the raw storage isn't enough to access your secrets.

## Getting started
### Automated Install: [`docker-compose`](https://docs.docker.com/compose/install/)
1. Adjust `docker-compose.yml` if necessary. Build the stack by executing `docker-compose build`.
2. Run the stack by executing `docker-compose up -d`.

### Manual Install
1. Clone our repository and run
```bash
git clone --depth 1 https://github.com/bearlike/secrets-manager secrets-manager
cd "secrets-manager"
```
2. Start a Mongo database server. 
3. Create a `.env` file in the project root with the following values
```
CONNECTION_STRING=mongodb://username:password@mongo.hostname:27017
```
4. Install the required python packages by executing `pip3 install -r requirements.txt`
5. You will need atleast `python3.7`. Start the server by running `server.py`.
6. Visit the application via `http://server_hostname:5000/api` (default port is `5000`) to visit the Swagger UI. 