!/bin/bash
#stop container and remove
docker rm --force nodejs-frontend
#pull new image to DockerHub
docker login -u manhnh1995 -p $PASSWORD_DOCKER_HUB
docker pull manhnh1995/nodejsfinal:latest 
#ReDeploy appliation with new image
docker run --name nodejs-frontend -d -p 3000:3000 -e VERSION=latest -e HOSTNAME=$(hostname) nodejsfinal:latest
