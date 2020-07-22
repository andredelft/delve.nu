HOST_PORT=80
IMAGE_TAG=delve

build:
	docker build -t $(IMAGE_TAG) .

run:
	docker run --env DEBUG=0 -p $(HOST_PORT):8000 --detach $(IMAGE_TAG)
