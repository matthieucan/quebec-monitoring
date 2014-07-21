#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The list can be found here:
# http://www.informa.msss.gouv.qc.ca/Listes.aspx?Name=y9M4IcKgjFYapz02jKwkUg==&Key=hhKpcdsNkJS+eg2gWNwm7A==&OrderByClause=8jnVPckjxX8dPG+Ajs/DlA==&idDimension=hqx1rRlrkPQ=
# However not everything is usable, since many sites use PDFs

HOSPITALS = {
    # Bas St Laurent
    'CSSS des Basques': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[4]/td[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[4]/td[3]/span/text()',
        '2d_coords': '-69.0879919,48.0285321',
        },
    'Hôpital Notre-Dame-de-Fatima': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[5]/th[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[5]/th[3]/span/text()',
        '2d_coords': '-70.026989,47.372822',
        },
    "Hôpital d'Amqui": {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[6]/td[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[6]/td[3]/span/text()',
        '2d_coords': '-67.4367035,48.4852365',
        },
    'CSSS de la Mitis': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[7]/th[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[7]/th[3]/span/text()',
        '2d_coords': '-68.203639,48.57935',
        },
    'Hôpital de Matane': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[8]/td[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[8]/td[3]/span/text()',
        '2d_coords': '-67.5236893,48.8427506',
        },
    'Hôpital régional de Rimouski': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[9]/th[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[9]/th[3]/span/text()',
        '2d_coords': '-68.532497,48.44701',
        },
    'Centre hospitalier régional du Grand-Portage': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[10]/td[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[10]/td[3]/span/text()',
        '2d_coords': '-69.539466,47.818659',
        },
    'Hôpital de Notre-Dame du Lac': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[11]/th[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[11]/th[3]/span/text()',
        '2d_coords': '-68.7987429,47.6122581',
        },
    'CLSC de Pohénégamook': {
        'url': 'http://www.agencesssbsl.gouv.qc.ca/index.php?id=179',
        'functional': '//*[@id="etat-des-urgences"]/table//tr[12]/td[2]/span/text()',
        'occupied': '//*[@id="etat-des-urgences"]/table//tr[12]/td[3]/span/text()',
        '2d_coords': '-69.2809799,47.4896336',
        },

    # Quebec
    'Hôpital St-Sacrement': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[4]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[4]/td[3]/text()',
        '2d_coords': '-71.2456991,46.7995852',
        },
    "Hôpital l'Enfant-Jésus": {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[5]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[5]/td[3]/text()',
        '2d_coords': '-71.225341,46.8372805',
        },
    'CHUL': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[6]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[6]/td[3]/text()',
        '2d_coords': '-71.2824852,46.7689108',
        },
    "Hôpital St-François-d'Assise": {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[7]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[7]/td[3]/text()',
        '2d_coords': '-71.2363095,46.8277795',
        },
    "L'Hôtel-Dieu de Québec": {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[8]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[8]/td[3]/text()',
        '2d_coords': '-71.2112364,46.815538',
        },
    'IUCPQ': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[10]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[10]/td[3]/text()',
        '2d_coords': '-71.2971556,46.7789928',
        },
    'Hôpital Jeffery Hale': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[13]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[13]/td[3]/text()',
        '2d_coords': '-71.2522067,46.7957725',
        },
    'Centre hospitalier Chauveau': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[15]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[15]/td[3]/text()',
        '2d_coords': '-71.3699268,46.8532654',
        },
    'Hôpital Ste-Anne-de-Beaupré': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[16]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[16]/td[3]/text()',
        '2d_coords': '-70.9000043,47.0428429',
        },
    'Hôpital de la Malbaie': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[18]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[18]/td[3]/text()',
        '2d_coords': '-70.1520273,47.6560911',
        },
    'Hôpital de Baie St-Paul': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[19]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[19]/td[3]/text()',
        '2d_coords': '-70.5081202,47.4363402',
        },
    'Centre hospitalier Portneuf (Saint-Raymond)': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[21]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[21]/td[3]/text()',
        '2d_coords': '-71.8151825,46.8921373',
        },
    'Centre de santé de Portneuf (Saint-Marc-des-Carrières)': {
        'url': 'http://www.rrsss03.gouv.qc.ca/urgence/fra/asp/urgence3.asp',
        'functional': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[22]/td[2]/text()',
        'occupied': '/html/body/form/table//tr[3]/td/table//tr/td[2]/table//tr[2]/td/table//tr/td/table//tr/td/div/table[2]//tr[2]/td/table//tr[22]/td[3]/text()',
        '2d_coords': '-72.0455289,46.6814792',
        },

    # Mauricie et centre du Québec
    # iframe
    'Centre-de-la-Mauricie	': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[2]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[2]/td[3]/text()',
        '2d_coords': '-72.74316799999997,46.525346',
        },
    'CHRTR': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[3]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[3]/td[3]/text()',
        '2d_coords': '-72.56166000000002,46.354888',
        },
    'Cloutier-du-Rivage	': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[4]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[4]/td[3]/text()',
        '2d_coords': '-72.5048130314911,46.364991467832326',
        },
    'CLSC de Fortierville': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[5]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[5]/td[3]/text()',
        '2d_coords': '-72.03099800000003,46.486844599999294',
        },
    'CSSS de Maskinonge': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[6]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[6]/td[3]/text()',
        '2d_coords': '-72.9519932,46.2550447',
        },
    'CSSS du Haut-Saint-Maurice': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[7]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[7]/td[3]/text()',
        '2d_coords': '-72.78516860000002,47.4285936',
        },
    'Hopital du Christ-Roi': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[8]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[8]/td[3]/text()',
        '2d_coords': '-72.62641200000002,46.231292',
        },
    'Hopital Sainte-Croix': {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[9]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[9]/td[3]/text()',
        '2d_coords': '-72.47710999999998,45.880218',
        },
    "Hotel Dieu D'Arthabaska": {
        'url': 'http://www.agencesss04.qc.ca/Siurge/Data.htm',
        'functional': '//*[@id="GridView1"]//tr[10]/td[2]/text()',
        'occupied': '//*[@id="GridView1"]//tr[10]/td[3]/text()',
        '2d_coords': '-71.91476312195128,46.04052590997372',
        },

    # Montréal
    'Centre hospitalier de St. Mary': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[4]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[4]/td[4]/div/text()',
        '2d_coords': '-73.62431400000003,45.494957',
        },
    'Hôpital de Lachine (CUSM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[5]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[5]/td[4]/div/text()',
        '2d_coords': '-73.67699466004946,45.44072755448131',
        },
    'Hôpital de LaSalle': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[6]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[6]/td[4]/div/text()',
        '2d_coords': '-73.62337300000002,45.420926',
        },
    'Hôpital de Verdun': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[7]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[7]/td[4]/div/text()',
        '2d_coords': '-73.584722,45.442175',
        },
    'Hôpital du Sacré-Coeur de Montréal': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[8]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[8]/td[4]/div/text()',
        '2d_coords': '-73.714271,45.532751',
        },
    'Hôpital Fleury': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[9]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[9]/td[4]/div/text()',
        '2d_coords': '-73.65026699999999,45.572056',
        },
    'Hôpital général de Montréal (CUSM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[10]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[10]/td[4]/div/text()',
        '2d_coords': '-73.58011963558198,45.49634623978591',
        },
    'Hôpital général du Lakeshore': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[11]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[11]/td[4]/div/text()',
        '2d_coords': '-73.83277541779097,45.45043811836126',
        },
    'Hôpital général Juif SMB': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[12]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[12]/td[4]/div/text()',
        '2d_coords': '-73.62867159999996,45.4977149',
        },
    'Hôpital Jean-Talon': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[13]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[13]/td[4]/div/text()',
        '2d_coords': '-73.60968540740964,45.545877729284925',
        },
    'Hôpital Maisonneuve-Rosemont': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[14]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[14]/td[4]/div/text()',
        '2d_coords': '-73.55969900000002,45.57415',
        },
    'Hôpital Notre-Dame (CHUM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[15]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[15]/td[4]/div/text()',
        '2d_coords': '-73.56266337301633,45.525691692226275',
        },
    'Hôpital Royal-Victoria (CUSM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[16]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[16]/td[4]/div/text()',
        '2d_coords': '-73.5819441398811,45.50836339853005',
        },
    'Hôpital Saint-Luc (CHUM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[17]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[17]/td[4]/div/text()',
        '2d_coords': '-73.55767081349182,45.51228129875902',
        },
    'Hôpital Santa Cabrini': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[18]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[18]/td[4]/div/text()',
        '2d_coords': '-73.57129036441803,45.58045185892201',
        },
    'Hôtel-Dieu (CHUM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[19]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[19]/td[4]/div/text()',
        '2d_coords': '-73.5779739,45.51443237393502',
        },
    'Institut de cardiologie de Montréal': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[20]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[20]/td[4]/div/text()',
        '2d_coords': '-73.578147,45.57385',
        },
    'Hôpital Louis-H. Lafontaine': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[23]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[23]/td[4]/div/text()',
        '2d_coords': '-73.54147973743439,45.58493208850593',
        },
    'Institut universitaire en santé mentale Douglas': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[24]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[24]/td[4]/div/text()',
        '2d_coords': '-73.52902599999999,45.588673',
        },
    'Pavillon Albert-Prévost': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[25]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[25]/td[4]/div/text()',
        '2d_coords': '-73.72970099999998,45.528266',
        },
    'CHU Sainte-Justine': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[28]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[28]/td[4]/div/text()',
        '2d_coords': '-73.62436000000002,45.50384',
        },
    'Hôpital de Montréal pour enfants (CUSM)': {
        'url': 'http://agence.santemontreal.qc.ca/fileadmin/asssm/rapports/urgence_quotidien_media.html',
        'functional': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[29]/td[3]/div/text()',
        'occupied': '//*[@id="oReportCell"]/table//tr[1]/td/div/table//tr[4]/td[2]/table//tr[29]/td[4]/div/text()',
        '2d_coords': '-73.58218699999998,45.488748',
        },

    ### 
    'Hôpital Anna-Laberge': {
        'url': 'http://www.santemonteregie.qc.ca/userfiles/file/Agence/Situationdanslesurgences/Relevequotidien.htm',
        'functional': '//*[@id="Relevequotidien_6419"]/table//tr[7]/td[3]/text()',
        'occupied': '//*[@id="Relevequotidien_6419"]/table//tr[7]/td[4]/text()',
        '2d_coords': '',
        },
}
                
        
template = (
"""
define host {
       use                      generic-host
       host_name                %(name)s
       alias                    %(region)s
       check_command            check_dummy!0!OK
}
define service {
       use                      generic-service
       host_name                %(name)s
       check_command            check_emergency_rooms_quebec!%(url)s!%(functional)s!%(occupied)s
       display_name             %(region)s
       service_description      %(name)s
       servicegroups            group-hospitals
       labels                   order_%(order)d
       icon_image_alt           %(2d_coords)s
       action_url               %(url)s
}
""")

business_rule = (
"""
define host {
       use                            generic-host
       host_name                      Hospitals
       alias                          Hospitals
       check_command                  check_dummy!0!OK
}
define service {
       use                            generic-service
       host_name                      Hospitals
       servicegroups                  group-hospitals
       service_description            Hôpitaux
       check_command                  bp_rule!%(all_hospitals)s
       business_rule_output_template  $(x)$
       labels                         order_0,map
       icon_image                     fa-h-square
       notes                          Vérifie le taux de remplissage des civières.
       notes_url                      <a href="http://www.informa.msss.gouv.qc.ca/Listes.aspx?Name=y9M4IcKgjFYapz02jKwkUg==&Key=hhKpcdsNkJS+eg2gWNwm7A==&OrderByClause=8jnVPckjxX8dPG+Ajs/DlA==&idDimension=hqx1rRlrkPQ=">Informa.msss.gouv.qc.ca</a>
}
""")

def main():
    # all_hospitals is a workaround while we wait for g:group-hospitals to work
    all_hospitals = []
    for order, (region, values) in enumerate(HOSPITALS.iteritems()):
        name = 'hospital_' + str(order)
        all_hospitals.append('%s,%s' % (name, name))
        print template % {'region': region,
                          '2d_coords': values['2d_coords'],
                          'url': values['url'],
                          'functional': values['functional'],
                          'occupied': values['occupied'],
                          'order': order + 1,
                          'name': name,
                          }
    
    all_hospitals = '&'.join(all_hospitals)
    print business_rule % {'all_hospitals': all_hospitals}

if __name__ == '__main__':
    main()
