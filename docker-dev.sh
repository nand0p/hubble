#!/bin/sh -ex

docker network create -d bridge nasa 2> /dev/null || true

docker build -t nasa-dev \
	     -f Dockerfile \
	     --build-arg "DATE=$(date)" \
	     --build-arg "REVISION=$(git rev-parse HEAD)" \
	     .

docker kill nasa-dev 2> /dev/null || true
sleep 2

docker run --rm --name nasa-dev -d --network=nasa -p 5005:5000 nasa-dev
sleep 5
docker ps

echo "docker run --rm --name nasa-dev -ti -p 5005:5000 nasa-dev bash"
docker logs nasa-dev
echo "docker exec -ti nasa-dev bash"
