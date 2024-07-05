#!/bin/bash
# run_docker.sh - Script to build and run the application using Docker

# Build the Docker image and start the container as specified in docker-compose.yml
echo "Building the Docker image and starting the container..."
docker-compose up --build