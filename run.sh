#/bin/bash
docker-compose down -f runtime-docker-compose.yml
docker-compose up -f runtime-docker-compose.yml  --build