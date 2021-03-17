import requests
import sys
import os
import datetime


def GET_DIGEST_IMAGE_DOCKER_HUB():

    token = os.environ.get("TOKEN")
    stream = os.popen('curl -s -H "Content-Type: application/json" -X POST -d \'{"username": "manhnh1995", "password": "Manhnh251995"}\' https://hub.docker.com/v2/users/login/ | jq -r .token')
    token = stream.read()
    request_dockerhub = os.popen('curl -s -H "Authorization: JWT {}" https://hub.docker.com/v2/repositories/manhnh1995/nodejsfinal/tags/latest | jq \'.images[].digest\''.format(token))
    digest_image_dockerhub = request_dockerhub.read()

    return str(digest_image_dockerhub.replace('"',''))

def GET_DIGEST_CURRENT_CONTAINER():

    stream = os.popen('docker inspect --format \'{{ .Image }}\' nodejs-frontend')
    digest_container = stream.read()

    return digest_container

def main():

    docker_hub_image_id = GET_DIGEST_IMAGE_DOCKER_HUB()
    container_current_id = GET_DIGEST_CURRENT_CONTAINER()
    date_time_now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    if docker_hub_image_id != container_current_id :
        os.system("echo '{} [INFO] Deploy new image have tag id {}..' >> /var/log/Deploy.log ".format(date_time_now,docker_hub_image_id))
        os.system("sh deployNodeJS.sh")
        os.system("echo '{} [INFO] Success deploy new image...' >> /var/log/Deploy.log ".format(date_time_now))
    else :
        os.system("echo '{} [INFO] Not Found new image.. >> /var/log/Deploy.log'".format(date_time_now))
        os.system("echo '{} [INFO] No New deployment... >> /var/log/Deploy.log'".format(date_time_now))

if __name__ == "__main__":
   main()
