#!/bin/bash
echo "Building storage service"
./mvnw clean install -Dmaven.test.skip=true