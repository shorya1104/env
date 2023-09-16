#!bin/bash
set -e

#Pull the docker image
docker pull shoryasngh/env:latest

#run docker container 
docker container run -d -p 3000:3000 -name ENV env:latest