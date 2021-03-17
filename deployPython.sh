docker login -u manhnh1995 -p $PASSWORD_DOCKER_HUB
docker pull manhnh1995/pythonfinal:$VERSION
docker run -d -p 5000:5000 -e VERSION=$VERSION -e HOSTNAME=$(hostname) manhnh1995/pythonfinal:$VERSION
