#!/bin/bash
docker build -t pythonfinal:latest -f  DockerfilePython .
docker tag pythonfinal:latest manhnh1995/pythonfinal:latest
docker login -u manhnh1995 -p $PASSWORD_DOCKER_HUB
docker push manhnh1995/nodejsfinal:$VERSION
