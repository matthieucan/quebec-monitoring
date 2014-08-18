WD = $(shell pwd)

all: run

build: conf
	sudo docker build -t quebec .

run: build
	sudo docker run -d -p 8080:80 quebec

dev: build
	(cd app && npm install)
	sudo docker run -i -t -p 8080:80 -v $(WD)/app:/srv/app quebec bash

# configuration
conf: banks dns websites hospitals transports dating isp environment

banks:
	scripts/banks.py > etc/shinken/adagios/banks.cfg

dns:
	scripts/dns.py > etc/shinken/adagios/dns.cfg

websites:
	scripts/websites.py > etc/shinken/adagios/websites.cfg

hospitals:
	scripts/hospitals.py > etc/shinken/adagios/hospitals.cfg

transports:
	scripts/transports.py > etc/shinken/adagios/transports.cfg

dating:
	scripts/dating.py > etc/shinken/adagios/dating.cfg

isp:
	scripts/isp.py > etc/shinken/adagios/isp.cfg

environment:
	scripts/environment.py > etc/shinken/adagios/environment.cfg
