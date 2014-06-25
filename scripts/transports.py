#!/usr/bin/env python
# -*- coding: utf-8 -*-

TRANSPORTS = {
    'Metro in Montreal': {
        'hostname': 'stm_metro',
        'command': 'check_stm_metro!1!3',
    },
    'Bikes (Bixi) in Montreal': {
        'hostname': 'bixi_mtl',
        'command': 'check_bixi_montreal!http://montreal.bixi.com/data/bikeStations.xml!1!100',
    }
}

template = (
"""
define host {
       use                      generic-host
       host_name                %(hostname)s
       alias                    %(hostname)s
       check_command            check_dummy!0!OK
}
define service {
       use                      generic-service
       host_name                %(hostname)s
       display_name             %(name)s
       service_description      %(hostname)s
       check_command            %(command)s
       servicegroups            group-transports
       labels                   order_%(order)d
}

""")

business_rule = (
"""
define host {
       use                            generic-host
       host_name                      Transports
       alias                          Transports
       check_command                  check_dummy!0!OK
}
define service {
       use                              generic-service
       host_name                        Transports
       service_description              Transports
       # check_command                  bp_rule!g:group_banks
       check_command                    bp_rule!%(all_transports)s
       business_rule_output_template    $(x)$
       servicegroups                    group-transports
       labels                           order_0
       icon_image                       fa-arrow-circle-down
}

""")



def main():
    all_transports = []
    for order, (name, values) in enumerate(TRANSPORTS.iteritems()):
        all_transports.append('%s,%s' % (values['hostname'], values['hostname']))
        print template % {'name': name,
                          'hostname': values['hostname'],
                          'command': values['command'],
                          'order': order + 1,
                          }
    
    all_transports = '&'.join(all_transports)
    print business_rule % {'all_transports': all_transports}

if __name__ == '__main__':
    main()
