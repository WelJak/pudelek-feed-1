#!/bin/bash

buildStorageService(){
    cd ./storage-service;
    ./bin/build-app.sh
    cd ../
}

echo "Deploy pudelek-feed locally"
buildStorageService
docker-compose -f docker-compose.yml build --force-rm
docker-compose -f docker-compose.yml up -d
echo "Use bin/clean-local-stack.sh to stop local stack."
