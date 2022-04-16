#!/usr/bin/env bash
# Takes about 5-10 minutes to run. 
# You have to be logged in to dockerhub before running this script
# $ docker login -u <username>
#
# We try to follow [SemVer v2.0.0](https://semver.org/)
VERSION="1.2.0"
# If $VERSION = "1.2.3"
# ${VERSION::3} will be "1.2"
# ${VERSION::1} will be "1"
#
# Docker build and tag for different architectures
docker buildx create --platform linux/arm64,linux/arm/v8 --name ssm-builder
docker buildx build --no-cache --builder ssm-builder --push --platform linux/amd64,linux/arm64/v8 \
    -t krishnaalagiri/ssm:latest \
    -t krishnaalagiri/ssm:$VERSION \
    -t krishnaalagiri/ssm:${VERSION::3} \
    -t krishnaalagiri/ssm:${VERSION::1} .