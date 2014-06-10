#!/usr/bin/env python

import re

import requests
from bs4 import BeautifulSoup

template = (
"""define service {
       use                      generic-service
       host_name                qc.ca
       service_description      Check http for %s.qc.ca
       check_command            check_http
}
""")

def get_hosts_list():
    url = 'http://gouv.qc.ca/portail/quebec/pgs/commun/gouv/minorg/?lang=fr'
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    hosts = soup.find_all('a', href=re.compile('.qc.ca'))
    res = set()
    for host in hosts:
        r = re.search('://((.*).qc.ca)', host['href'])
        if r is not None:
            res.add(r.group(2))
    
    return res

def main():
    for host in get_hosts_list():
        print template % host

if __name__ == '__main__':
    main()
