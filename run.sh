#/bin/bash
docker-compose -f runtime-docker-compose.yml down
docker-compose -f runtime-docker-compose.yml up --build 