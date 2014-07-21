all: conf run

run:
	docker.io build -t quebec .
	docker.io run -d -p 8080:80 quebec

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
