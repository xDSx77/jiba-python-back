#!/bin/bash
docker-compose -f tests-docker-compose.yml down
docker volume prune
docker-compose -f tests-docker-compose.yml up --build
