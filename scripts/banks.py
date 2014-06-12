#!/usr/bin/env python

BANKS = {
    'RBC banque royale': {
        'protocol': 'https',
        'domain': 'www1.royalbank.com',
        'path': '/cgi-bin/rbaccess/rbunxcgi?F6=1&F7=IB&F21=IB&F22=IB&REQUEST=ClientSignin&LANGUAGE=FRENCH',
        },
    'TD Canada Trust': {
        'protocol': 'https',
        'domain': 'banquenetcpo.td.com',
        'path': '/waw/idp/login.htm?execution=e1s1',
        },
    'BDC': {
        'protocol': 'https',
        'domain':'connex.bdc.ca',
        'path': '/_LOGIN/BDCConnexlogin.aspx',
        },
    'CIBC': {
        'protocol': 'https',
        'domain': 'www.cibc.com',
        'path': '/ca/personal.html?int_id=HP_PersonalBanking',
        },
    'Banque de Montreal': {
        'protocol': 'https',
        'domain': 'www1.bmo.com',
        'path': '/onlinebanking/cgi-bin/netbnx/NBmain?product=6',
        },
    'Scotiabank': {
        'protocol': 'https',
        'domain': 'www2.scotiaonline.scotiabank.com',
        'path': '/online/authentication/authentication.bns',
        },
    'BNC': {
        'protocol': 'https',
        'domain': 'bvi.bnc.ca',
        'path': '/',
        },
    'Banque Laurentienne': {
        'protocol': 'https',
        'domain': 'blcweb.banquelaurentienne.ca',
        'path': '/BLCDirect/',
        },
    'Desjardins': {
        'protocol': 'https',
        'domain': 'accesd.desjardins.com',
        'path': '/fr/accesd/',
        },
    }

prefix = (
"""define host {
       use                      generic-host
       host_name                banks
       alias                    banks
}
""")

template = (
"""define service {
       use                      generic-service
       host_name                banks
       service_description      Check http for %(bank)s online services
       alias                    %(bank)s
       check_command            check_http_service!%(domain)s!%(path)s%(more_options)s
}
""")


def main():
    print prefix
    for bank, values in BANKS.iteritems():
        print template % {'bank': bank,
                          'domain': values['domain'],
                          'path': values['path'],
                          'more_options': '!--ssl' if values['protocol'] == 'https' else ''}

if __name__ == '__main__':
    main()
