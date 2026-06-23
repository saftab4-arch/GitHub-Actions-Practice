#!/bin/bash

set -e

echo "Checking Project 04 containers..."
docker compose ps

echo
echo "Testing application endpoint..."
curl -f http://localhost:5000

echo
echo "Health check completed successfully."
