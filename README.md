<h1 align="center"><a href="#"><img alt="Simple Secrets Manager" src="docs/img/gh_banner.png" /></a></h1>
<p align="center">
    <a href="https://hub.docker.com/r/krishnaalagiri/ssm"><img alt="Docker Image Latest Version" src="https://img.shields.io/docker/v/krishnaalagiri/ssm?logo=docker&sort=semver"></a>
    <a href="https://hub.docker.com/r/krishnaalagiri/ssm"><img alt="Docker Image Architecture" src="https://img.shields.io/badge/architecture-arm64v8%20%7C%20x86__64-blue?logo=docker"></a>
    <a href="https://github.com/bearlike/simple-secrets-manager/actions/workflows/ci.yml"><img alt="GitHub Repository" src="https://img.shields.io/github/workflow/status/bearlike/simple-secrets-manager/Build%20and%20deploy%20multiarch%20image?logo=github"></a>
    <a href="/LICENSE"><img alt="License" src="https://img.shields.io/github/license/bearlike/simple-secrets-manager"></a>
</p>

Secure storage, and delivery for tokens, passwords, API keys, and other secrets using HTTP API, Swagger UI or Python Package.
> `TL;DR`: Poor Man's Hashi Corp Vault

## Why does this exist?

Hashi Corp Vault works well but it was meant for enterprises. Therefore, it was heavy and non-portable (atleast difficult) for my homelab setup. So I wanted to build a Secrets Manager intended for small scale setups that could also scale well.

## Goals

- A lightweight system that sucks less power out of the wall. Therefore, minimal background jobs and reduced resource utilizations.
- Should be compatible on both `x86-64` and `arm64v8` (mainly Raspberry Pi 4).
- High stability, availability and easy scalability.

## Available secret engines

| Secret Engine | Description                                           |
|---------------|-------------------------------------------------------|
| `kv`          | Key-Value engine is used to store arbitrary secrets.  |

## Available authentication methods

| Auth Methods      | Description                                                               |
|-------------------|---------------------------------------------------------------------------|
| `userpass`        | Allows users to authenticate using a username and password combination.   |
| `token`           | Allows users to authenticate using a token. Token generation requires users to be authenticated via `userpass`                               |

## Future

- Secret engines for certificates (PKI), SSH and databases.
- Encrypting secrets before writing to a persistent storage, so gaining access to the raw storage isn't enough to access your secrets.

## Getting started

### Automated Install: [`docker-compose`](https://docs.docker.com/compose/install/) (Recommended)

1. Run the [stack](docker-compose.yml) by executing `docker-compose up -d`.

### Manual Install

1. Clone our repository and run

    ```bash
    git clone --depth 1 https://github.com/bearlike/simple-secrets-manager simple-secrets-manager
    cd "simple-secrets-manager"
    ```

2. Start a Mongo database server.
3. Create a `.env` file in the project root with the following values

    ```sh
    CONNECTION_STRING=mongodb://username:password@mongo.hostname:27017
    ```

4. Install the required python packages by executing `pip3 install -r requirements.txt`
5. You will need atleast `python3.9`. Start the server by running `server.py`.
6. Visit the application via `http://server_hostname:5000/api` (default port is `5000`) to visit the Swagger UI.
