#!/bin/bash
echo "Deploy pudelek-feed locally"
docker-compose -f docker-compose.yml build --force-rm
docker-compose -f docker-compose.yml up -d
echo "Use bin/clean-local-stack.sh to stop local stack."
