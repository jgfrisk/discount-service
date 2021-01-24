SERVICE_NAME=discount-service

rebuild-requirements:
	pip-compile requirements.in

build:
	docker build --tag $(SERVICE_NAME) .

start-interactive:
	docker run -it -p 127.0.0.1:5000:5000 --rm --name $(SERVICE_NAME) $(SERVICE_NAME):latest

run-shell:
	docker run -it --rm --user service $(SERVICE_NAME):latest bash

start:
	docker run --detach -p 127.0.0.1:5000:5000 --rm --name $(SERVICE_NAME) $(SERVICE_NAME):latest

stop:
	docker stop  $(SERVICE_NAME) || true

restart: stop start

run-tests-api:
	python tests/test_api.py
