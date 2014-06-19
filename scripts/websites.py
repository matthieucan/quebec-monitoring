#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import requests
from bs4 import BeautifulSoup

prefix = (
"""
""")

template = (
"""
define host {
       use                      generic-host
       host_name                %(host)s.qc.ca
       address                  %(host)s.qc.ca
       alias                    %(host)s.qc.ca
       check_command            check_dummy!0!OK
}
define service {
       use                      generic-service
       host_name                %(host)s.qc.ca
       check_command            check_http2!%(host)s.qc.ca
       display_name             %(host)s.qc.ca
       service_description      %(host)s.qc.ca
       servicegroups            group-websites
       notes                    order_%(order)d
}
""")

postfix = (
"""
define host {
       use                            generic-host
       host_name                      Websites
       alias                          Websites
       check_command                  check_dummy!0!OK
}
define service {
       use                            generic-service
       host_name                      Websites
       servicegroups                     group-websites
       check_command                  bp_rule!%(all_websites)s
       service_description            Websites
       business_rule_output_template  $(x)$
       notes                          order_0
       icon_image                     fa-desktop
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
    print prefix
    websites = []
    for (order, host) in enumerate(get_hosts_list()):
        print template % {'host': host,
                          'order': order + 1}
        websites.append('%(host)s.qc.ca,%(host)s.qc.ca' % {'host': host})
    all_websites = '&'.join(websites)
    print postfix % {'all_websites': all_websites}

if __name__ == '__main__':
    main()
