#!/usr/bin/env python

DNS = {
    # Cogeco Cable (Trois-rivieres) 
    'cogeco': ['205.151.69.200','205.151.68.200'],
    
    # Sympatico.ca (BELL)
    'sympatico': ['198.235.216.110', '209.226.175.224', '206.47.244.90',
                  '206.47.244.53', '206.47.244.54', '198.235.216.1',
                  '198.235.216.2', '198.235.216.130', '198.235.216.131'],
    
    # Telus
    'telus': ['142.169.1.16', '199.84.242.22'],
    
    # Videotron.CA 
    'videotron.ca': ['205.151.222.250', '205.151.222.251', '24.200.241.2',
                  '24.200.241.6', '24.200.241.10', '24.200.243.234',
                  '24.200.243.242', '24.200.243.250', '24.201.245.106',
                  '24.201.245.114'],
    
    # Videotron.NET
    'videotron.net': ['205.151.222.254', '205.151.222.253'],
    
    # Colbanet
    'colbanet': ['216.252.64.75', '216.252.64.76', '69.28.239.8',
                 '74.116.184.9', '69.28.239.9', '74.116.184.8'],

    # Cooptel
    'cooptel': ['216.144.115.241', '216.144.115.242'],

    # Fido
    'fido': ['204.92.15.211', '204.92.15.212', '64.71.255.205', '64.71.255.253']
    }


prefix = (
"""define host {
       use                      generic-host
       host_name                DNS
       alias                    DNS
}
""")

template = (
"""define service {
       use                      generic-service
       host_name                DNS
       service_description      Check DNS for %(host)s_%(ip)s
       alias                    %(host)s_%(ip)s
       check_command            check_dig_service!%(ip)s
}
""")


def main():
    print prefix
    for host, ips in DNS.iteritems():
        for ip in ips:
            print template % {'host': host, 'ip': ip}
        

if __name__ == '__main__':
    main()
