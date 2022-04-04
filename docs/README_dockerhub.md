<img alt="Simple Secrets Manager" src="https://github.com/bearlike/simple-secrets-manager/raw/main/docs/img/gh_banner.png" />
<p align="center">
    <a href="https://hub.docker.com/r/krishnaalagiri/ssm"><img alt="Docker Image Latest Version" src="https://img.shields.io/docker/v/krishnaalagiri/ssm?logo=docker&sort=semver"></a>
    <a href="https://hub.docker.com/r/krishnaalagiri/ssm"><img alt="Docker Image Architecture" src="https://img.shields.io/badge/architecture-arm64v8%20%7C%20x86__64-blue?logo=docker"></a>
    <a href="https://github.com/bearlike/simple-secrets-manager/actions/workflows/ci.yml"><img alt="GitHub Repository" src="https://img.shields.io/github/workflow/status/bearlike/simple-secrets-manager/Build%20and%20deploy%20multiarch%20image?logo=github"></a>
    <a href="https://github.com/bearlike/simple-secrets-manager"><img alt="GitHub Repository" src="https://img.shields.io/badge/GitHub-bearlike%2Fsimple--secrets--manager-blue?logo=github"></a>
    <a href="https://github.com/bearlike/simple-secrets-manager/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/bearlike/simple-secrets-manager"></a>
</p>


Secure storage, and delivery for tokens, passwords, API keys, and other secrets using HTTP API, Swagger UI or Python Package.
> `TL;DR`: Poor Man's Hashi Corp Vault 


## Supported tags and respective [Dockerfile](https://github.com/bearlike/simple-secrets-manager/blob/main/.github/workflows/ci.yml) links
- [`1.0.0`, `1.0`, `1`, `latest`](https://github.com/bearlike/simple-secrets-manager/blob/dad59e8bda7eaeddd2e14660958d3227ac035b3d/.github/workflows/ci.yml)


## Quick reference (cont.)
- Where to file issues: https://github.com/bearlike/simple-secrets-manager/issues
- Supported architectures: ([more info](https://github.com/docker-library/official-images#architectures-other-than-amd64)) `amd64`, `arm64v8`


## Why does this exist?
Hashi Corp Vault works well but it was meant for enterprises. Therefore, it was heavy and non-portable (atleast difficult) for my homelab setup. So I wanted to build a Secrets Manager intended for small scale setups that could also scale well. 


## Goals
- A lightweight system that sucks less power out of the wall. Therefore, minimal background jobs and reduced resource utilizations.
- Should be compatible on both `x86-64` and `arm64v8` (mainly Raspberry Pi 4).
- High stability, availability and easy scalability.      


## Available secret engines
| Secret Engine | Description                                          |
| ------------- | ---------------------------------------------------- |
| `kv`          | Key-Value engine is used to store arbitrary secrets. |


## Available authentication methods
| Auth Methods | Description                                 |
| ------------ | ------------------------------------------- |
| `token`      | Allows users to authenticate using a token. |


## Getting started
### Automated Install: [`docker-compose`](https://docs.docker.com/compose/install/) (Recommended)
1. Run the [stack](https://github.com/bearlike/simple-secrets-manager/blob/main/docker-compose.yml) by executing `docker-compose up -d`.

```yaml
version: '3'
services:
  mongo:
    image: mongo:4
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: password
    networks:
      - app-tier

  app:
    image: krishnaalagiri/ssm:latest
    depends_on:
      - mongo
    ports:
      - "5000:5000"
    environment:
      CONNECTION_STRING: mongodb://root:password@mongo:27017
      PORT: 5000
    networks:
      - app-tier

networks:
  app-tier:
    driver: bridge
```
