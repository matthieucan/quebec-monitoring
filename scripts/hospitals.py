#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The list can be found here:
# http://www.informa.msss.gouv.qc.ca/Listes.aspx?Name=y9M4IcKgjFYapz02jKwkUg==&Key=hhKpcdsNkJS+eg2gWNwm7A==&OrderByClause=8jnVPckjxX8dPG+Ajs/DlA==&idDimension=hqx1rRlrkPQ=
# However not everything is usable, since many sites use PDFs

# IPs are fake, and just here to show the geographical location for maps

HOSPITALS = {
    'Bas_St_Laurent': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//div[@id="etat-des-urgences"]/table//th[@class="darkfirst"]/following-sibling::th[1]//text()',
        'occupied': '//div[@id="etat-des-urgences"]/table//th[@class="darkfirst"]/following-sibling::th[2]//text()',
        'ip': 'A',
        },
    'Quebec': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '//td[contains(text(), "Ensemble de la r")]/following-sibling::td[1]/text()',
        'occupied': '//td[contains(text(), "Ensemble de la r")]/following-sibling::td[2]/text()',
        'ip': 'A',
        },
    # No totals in the table
    # 'Mauricie': {
    #     'url': 'http://www.agencesss04.qc.ca/Siurge/Siurge.htm',
    #     'functional': '',
    #     'occupied': '',
    #     'ip': 'A',
    #     }
    'Montreal': {
        # this url uses an iframe (link below)
        #'url': 'http://agence.santemontreal.qc.ca/espace-medias/donnees-urgences-et-chirurgies/releve-quotidien-de-la-situation-des-salles-durgence/',
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//td/div[text()="Total"]/../following-sibling::td[2]/div/text()',
        'occupied': '//td/div[text()="Total"]/../following-sibling::td[3]/div/text()',
        'ip': 'A',
        },
    'Chaudiere-Appalaches': {
        'url': 'http://www.agencesss12.gouv.qc.ca/situation-dans-les-urgences/',
        'functional': '//td[contains(text(), "Ensemble de la r")]/following-sibling::td[1]/text()',
        'occupied': '//td[contains(text(), "Ensemble de la r")]/following-sibling::td[2]/text()',
        'ip': 'A',
        },
    'Monteregie': {
        # this url uses an iframe (link below)
        #'url': 'http://www.santemonteregie.qc.ca/champlaincharleslemoyne/services/salle-urgence/situation-dans-les-urgences.fr.html#.U6CY93X7FhE',
        'url': 'http://www.santemonteregie.qc.ca/userfiles/file/Agence/Situationdanslesurgences/Relevequotidien.htm',
        'functional': '/html//table//tr[last()-1]/td[3]/text()',
        'occupied': '/html//table//tr[last()-1]/td[4]/text()',
        'ip': 'A',
        },
}
                
        
template = (
"""define host {
       use                      generic-host
       host_name                %(region)s
       address                  %(ip)s
       alias                    %(region)s
       display_name             %(region)s
       hostgroups               group-hospitals
       notes                    order_%(order)d
       check_command            check_emergency_occupation!%(url)s!%(functional)s!%(occupied)s
}
""")

business_rule = (
"""
define host {
       use                            generic-host
       host_name                      Hospitals
       hostgroups                     group-hospitals
       # check_command                  bp_rule!g:group_banks
       check_command                  bp_rule!%(all_hospitals)s
       business_rule_output_template  $(x)$
       notes                          order_0
       icon_image                     fa-h-square
}
""")

def main():
    # all_hospitals is a workaround while we wait for g:group-hospitals to work
    all_hospitals = []
    for order, (region, values) in enumerate(HOSPITALS.iteritems()):
        all_hospitals.append('%s' % region)
        print template % {'region': region,
                          'ip': values['ip'],
                          'url': values['url'],
                          'functional': values['functional'],
                          'occupied': values['occupied'],
                          'order': order + 1,
                          }
    
    all_hospitals = '&'.join(all_hospitals)
    print business_rule % {'all_hospitals': all_hospitals}

if __name__ == '__main__':
    main()
