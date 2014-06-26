#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from http://listingsca.com/computing/internet/providers/#
ISPS = {
    'AOL Canada': {
        'url': 'http://www.aol.ca/',
        },
    'AT&T Canada': {
        'url': 'http://www.att.com/canada/',
        },
    'AT&T Canada Internet and E-Business Services': {
        'url': 'http://www.allstream.com/',
        },
    'Bell Canada': {
        'url': 'http://www.bell.ca/',
        },
    'Canadian Association of Internet Providers': {
        'url': 'http://www.caip.ca/',
        },
    'Rackforce': {
        'url': 'http://www.rackforce.com/',
        },
    'Dialup At Cost': {
        'url': 'http://www.dialupatcost.ca/',
        },
    'FollowMe Canada': {
        'url': 'http://www.followme.com/',
        },
    'ISP.ca': {
        'url': 'http://www.isp.ca/',
        },
    'Lycos Sympatico': {
        'url': 'http://www.sympatico.ca/',
        },
    'Netrover Inc.': {
        'url': 'http://www.netrover.com/',
        },
    'NetZero': {
        'url': 'http://www.netzero.net/',
        },
    'Primus Telecommunications Canada': {
        'url': 'http://www.primus.ca/',
        },
    'SmokeSignal': {
        'url': 'http://www.smokesignal.net/',
        },
    'Sprint Canada': {
        'url': 'http://www.rogerstelecom.ca/',
        },
    'TELUS Internet Services': {
        'url': 'http://www.telus.net/',
        },
    'Thunderstar Internet Access': {
        'url': 'http://www.thunderstar.net/',
        },
    'UNIServe Online': {
        'url': 'http://www.uniserve.com/',
        },
    'Virgin Technologies Inc': {
        'url': 'http://www.virgintechnologies.com/',
        },
}

template = (
"""define host {
       # not working yet, bug reported on Shinken:
       # https://github.com/naparuba/shinken/issues/1218#issuecomment-46223079
       use                      generic-host
       host_name                %(domain)s
       address                  %(domain)s
       alias                    %(domain)s
       check_command            check_dummy!0!OK
}
define service {
       use                      generic-service
       host_name                %(domain)s
       check_command            check_http2!%(url)s
       display_name             %(isp)s
       service_description      %(domain)s
       servicegroups            group-isp
       labels                   order_%(order)d
       action_url               %(url)s
}
""")

business_rule = (
"""
define host {
       use                            generic-host
       host_name                      ISP
       alias                          ISP
       check_command                  check_dummy!0!OK
}
define service {
       use                            generic-service
       host_name                      ISP
       servicegroups                  group-isp
       service_description            FAI
       check_command                  bp_rule!%(all_isp)s
       business_rule_output_template  $(x)$
       labels                         order_0
       icon_image                     fa-signal
       notes                          Vérifie la disponibilité des principaux fournisseurs d'accès à Internet.
}
""")

def main():
    all_isp = []
    for order, (isp, values) in enumerate(ISPS.iteritems()):
        address = values['url'].split('://')[1]
        domain = address.split('/')[0]
        all_isp.append('%s,%s' % (domain, domain))
        
        print template % {'isp': isp,
                         'domain': domain,
                         'url': values['url'],
                         'order': order + 1}
    all_isp = '&'.join(all_isp)
    print business_rule % {'all_isp': all_isp}

if __name__ == '__main__':
    main()
