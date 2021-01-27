#/bin/bash
docker-compose -f tests-docker-compose.yml down
docker-compose -f tests-docker-compose.yml  up --build
