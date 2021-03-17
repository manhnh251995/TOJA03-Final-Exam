docker build -t nodejsfinal:latest -f  DockerfileNodejs .
docker tag nodejsfinal:latest manhnh1995/nodejsfinal:latest
docker login -u manhnh1995 -p $PASSWORD_DOCKER_HUB
docker push manhnh1995/nodejsfinal:$VERSION
