WD = $(shell pwd)

all: run

build:
	sudo docker build -t quebec .

rebuild:
	sudo docker build --no-cache=true -t quebec .

run: build
	sudo docker run -d -p 8080:80 quebec

updatable-prod: build
	(cd app && npm install)
	sudo docker run -d -t -p 8080:80 -v $(WD)/app:/srv/app -v $(WD)/etc/shinken/adagios:/etc/shinken/adagios quebec

dev: build
	(cd app && npm install)
	sudo docker run -i -t -p 8080:80 -v $(WD)/app:/srv/app -v $(WD)/etc/shinken/adagios:/etc/shinken/adagios quebec bash

dev-frontend: build
	(cd app && npm install)
	sudo docker run -d -p 8080:80 -v $(WD)/app:/srv/app quebec
