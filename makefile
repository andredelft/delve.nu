HOST_PORT=80
IMAGE_TAG=delve
ENV_FILE=.env

build:
	docker build -t $(IMAGE_TAG) .

run:
	touch $(ENV_FILE)
	docker run --env DEBUG=0 --env-file $(ENV_FILE) -p $(HOST_PORT):8000 --detach $(IMAGE_TAG)
