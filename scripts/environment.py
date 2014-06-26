#!/usr/bin/env python
# -*- coding: utf-8 -*-

ENVS = {
    'Flu level (Montreal)': {
        'hostname': 'env_flu_mtl',
        'command': 'check_env_canada!http://www.meteomedia.com/api/data/caqc0363!flu_level',
    },
    'Pollen (Montreal)': {
        'hostname': 'env_pollen_mtl',
        'command': 'check_env_canada!http://www.meteomedia.com/api/data/caqc0363!pollen_adlevel',
    },
    'UV (Montreal)': {
        'hostname': 'env_uv_mtl',
        'command': 'check_env_canada_wc!http://www.meteomedia.com/api/data/caqc0363!last_uv!3!7',
    },
    'Air quality (Montreal)': {
        'hostname': 'env_aq_mtl',
        'command': 'check_env_canada_wc!http://www.meteomedia.com/api/data/caqc0363!aq_index!26!51',
    },
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
       servicegroups            group-environment
       labels                   order_%(order)d
}

""")

business_rule = (
"""
define host {
       use                            generic-host
       host_name                      Environment
       alias                          Environment
       check_command                  check_dummy!0!OK
}
define service {
       use                              generic-service
       host_name                        Environment
       service_description              Environment
       check_command                    bp_rule!%(all_environments)s
       business_rule_output_template    $(x)$
       servicegroups                    group-environment
       labels                           order_0
       icon_image                       fa-tree
       notes_url                        <a href="http://www.meteomedia.com/meteo/canada/quebec/montreal">Meteomedia</a>
}

""")



def main():
    all_environments = []
    for order, (name, values) in enumerate(ENVS.iteritems()):
        all_environments.append('%s,%s' % (values['hostname'], values['hostname']))
        print template % {'name': name,
                          'hostname': values['hostname'],
                          'command': values['command'],
                          'order': order + 1,
                          }
    
    all_environments = '&'.join(all_environments)
    print business_rule % {'all_environments': all_environments}

if __name__ == '__main__':
    main()
