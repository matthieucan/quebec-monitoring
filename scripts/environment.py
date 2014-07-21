#!/usr/bin/env python
# -*- coding: utf-8 -*-

ENVS = {
    'Niveau de grippe (Montréal)': {
        'hostname': 'env_flu_mtl',
        'command': 'check_environment_canada!http://www.meteomedia.com/api/data/caqc0363!flu_level',
        'url': 'http://www.msss.gouv.qc.ca/sujets/prob_sante/influenza/index.php?aid=29',
    },
    'Pollen (Montréal)': {
        'hostname': 'env_pollen_mtl',
        'command': 'check_environment_canada!http://www.meteomedia.com/api/data/caqc0363!pollen_adlevel',
        'url': 'http://www.meteomedia.com/plein-air/pollen/canada/quebec/montreal',
    },
    'UV (Montréal)': {
        'hostname': 'env_uv_mtl',
        'command': 'check_environment_canada_wc!http://www.meteomedia.com/api/data/caqc0363!last_uv!3!7',
        'url': 'http://www.meteomedia.com/previsions/uv/canada/quebec/montreal',
    },
    "Qualité de l'air (Montréal)": {
        'hostname': 'env_aq_mtl',
        'command': 'check_environment_canada_wc!http://www.meteomedia.com/api/data/caqc0363!aq_index!26!51',
        'url': 'http://www.meteomedia.com/previsions/qualite-air/canada/quebec/montreal',
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
       action_url               %(url)s
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
       service_description              Écologie
       check_command                    bp_rule!%(all_environments)s
       business_rule_output_template    $(x)$
       servicegroups                    group-environment
       labels                           order_0
       icon_image                       fa-tree
       notes                            Vérifie certaines métriques relatives à l'environnement.
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
                          'url': values['url'],
                          'order': order + 1,
                          }
    
    all_environments = '&'.join(all_environments)
    print business_rule % {'all_environments': all_environments}

if __name__ == '__main__':
    main()
