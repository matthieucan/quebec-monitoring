#!/usr/bin/env python

BANKS = {
    'RBC banque royale': 'https://www1.royalbank.com/cgi-bin/rbaccess/rbunxcgi?F6=1&F7=IB&F21=IB&F22=IB&REQUEST=ClientSignin&LANGUAGE=FRENCH',
    'TD Canada Trust': 'https://banquenetcpo.td.com/waw/idp/login.htm?execution=e1s1',
    'BDC': 'https://connex.bdc.ca/_LOGIN/BDCConnexlogin.aspx',
    'CIBC': 'https://www.cibc.com/ca/personal.html?int_id=HP_PersonalBanking',
    'Banque de Montreal': 'https://www1.bmo.com/onlinebanking/cgi-bin/netbnx/NBmain?product=6',
    'Scotiabank': 'https://www2.scotiaonline.scotiabank.com/online/authentication/authentication.bns',
    'BNC': 'https://bvi.bnc.ca',
    'Banque Laurentienne': 'https://blcweb.banquelaurentienne.ca/BLCDirect/',
    'Desjardins': 'https://accesd.desjardins.com/fr/accesd/',
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
       check_command            check_http_service!%(url)s
}
""")


def main():
    print prefix
    for bank, url in BANKS.iteritems():
        print template % {'bank': bank, 'url': url}

if __name__ == '__main__':
    main()
