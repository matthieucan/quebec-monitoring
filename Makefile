all: banks dns qcca hospitals

banks:
	scripts/banks.py > etc/shinken/adagios/banks.cfg

dns:
	scripts/dns.py > etc/shinken/adagios/dns.cfg

qcca:
	scripts/qc.ca.py > etc/shinken/adagios/qc.ca.cfg

hospitals:
	scripts/hospitals.py > etc/shinken/adagios/hospitals.cfg
