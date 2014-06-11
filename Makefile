all: banks dns qcca

banks:
	scripts/banks.py > etc/shinken/adagios/banks.cfg

dns:
	scripts/dns.py > etc/shinken/adagios/dns.cfg

qcca:
	scripts/qc.ca.py > etc/shinken/adagios/qc.ca.cfg
