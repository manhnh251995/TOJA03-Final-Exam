#!/bin/bash
docker build -t pythonfinal:$VERSION -f  DockerfilePython .
docker tag pythonfinal:latest manhnh1995/pythonfinal:$VERSION
docker login -u manhnh1995 -p $PASSWORD_DOCKER_HUB
docker push manhnh1995/pythonfinal:$VERSION
