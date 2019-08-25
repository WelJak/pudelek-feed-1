#!/bin/bash
echo "Clean pudelek-feed infrastracture"
docker-compose -f docker-compose.yml down -v
