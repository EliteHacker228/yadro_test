#!/bin/bash

image_name="yadro_test:latest"

echo "Building Docker image..."
docker build . -t $image_name

echo "Running the Docker container..."
container_id=$(docker run -d $image_name)

echo "Waiting for the container to finish..."
docker wait "$container_id"

echo "Checking logs..."
logs=$(docker logs $container_id)

info_count=$(echo "$logs" | grep -c '\[INFO\]')
error_count=$(echo "$logs" | grep -c '\[ERROR\]')

echo "INFO lines found: $info_count as expected"
echo "ERROR lines found: $error_count as expected"

if [[ "$info_count" -ne 5 ]]; then
  echo "ERROR: Expected 4 lines with [INFO], but found $info_count. Script failed"
  exit 1
fi

if [[ "$error_count" -ne 2 ]]; then
  echo "ERROR: Expected 3 lines with [ERROR], but found $error_count. Script failed"
  exit 1
fi

echo "Script worked correctly!"
exit 0
