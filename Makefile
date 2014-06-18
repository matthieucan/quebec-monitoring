all: conf run

run:
	docker.io build -t quebec .
	docker.io run -d -t quebec

conf: banks dns websites hospitals transports dating

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
