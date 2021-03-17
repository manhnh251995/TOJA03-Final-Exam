docker login -u manhnh1995 -p $PASSWORD_DOCKER_HUB
docker pull manhnh1995/nodejsfinal:$VERSION
docker run -d -p 3000:3000 -e VERSION=$VERSION -e HOSTNAME=$(hostname) nodejsfinal:VERSION
