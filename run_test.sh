#/bin/bash
docker-compose down
docker-compose up --build
docker-compose exec jiba-python-back_server_1 "pytest"
docker-compose down