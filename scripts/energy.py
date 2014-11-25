#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml.etree import tostring
from lxml import etree
from decimal import *
import lxml.html
import urllib
import re
from lxml.html import parse, fromstring

def chunks(l, n):
   """ Yield successive n-sized chunks from l.
   """
   for i in xrange(0, len(l), n):
      yield l[i : i + n]

def main():
   response = urllib.urlopen("http://pannes.hydroquebec.com/pannes/bilan-interruptions-service/#bis")
   page_source = response.read()
   root = lxml.html.fromstring(page_source)
   url = root.xpath('//td//@href')
   regions_list = []
   regions_list = root.xpath('//td//text()')
   regions_list = [r[0] for r in chunks(regions_list, 5)]
   regions_list = regions_list[:-1]
   regions_with_url = zip(regions_list, url)
   final_list = []
   
   for i in range(17):   
       host_name = "hydroquebec_" + str(i + 1)
       labels = "order_" + str(i + 1)
       check_command = "check_hydro_quebec!" + regions_list[i].encode("utf-8") 
       print "define host {"
       print "   use                      generic-host"
       print "   host_name               ", host_name 
       print "   alias                   ", regions_list[i].encode("utf-8")  
       print "   check_command            check_dummy!0!OK"
       print "}"
       print ""
       print "define service {"
       print "   use                      generic-service"
       print "   host_name               ", host_name
       print "   check_command           ", check_command 
       print "   display_name            ", regions_list[i].encode("utf-8") 
       print "   service_description     ", host_name 
       print "   servicegroups            energy"
       print "   labels                  ", labels
       print "   action_url              ", url[i].encode("utf-8")
       print "}"
       print ""
       
       final_list.append(host_name)
   final_list.append("hydroquebec_total")
   
   final_host = "bp_rule!"
   comma = ","
   plus = "&"

   for i in final_list:
       final_host = final_host + i + comma + i + plus
   
   final_host = final_host[:-1] 
   
   print "define host {"
   print "   use                      generic-host"
   print "   host_name                hydroquebec_total" 
   print "   alias                    Ensemble du Québec"  
   print "   check_command            check_dummy!0!OK"
   print "}"
   print ""
   print "define service {"
   print "   use                      generic-service"
   print "   host_name                hydroquebec_total"
   print "   check_command            check_hydro_quebec!Across Québec"
   print "   display_name             Ensemble du Québec"
   print "   service_description      hydroquebec_total"
   print "   servicegroups            energy"
   print "   labels                   order_18"
   print "   action_url               http://pannes.hydroquebec.com/pannes/bilan-interruptions-service/#bis" 
   print "}"
   print ""

   
   print "define host {"
   print "   use                               generic-host"
   print "   host_name                         energy" 
   print "   alias                             energy"  
   print "   check_command                     check_dummy!0!OK"
   print "}"
   print ""
   print "define service {"
   print "   use                               template_bprule"
   print "   host_name                         energy"
   print "   check_command                    ",final_host 
   print "   display_name                      Énergies"
   print "   service_description               energy"
   print "   business_rule_output_template     $(x)$"
   print "   servicegroups                     main"
   print "   icon_image                        fa-flash" 
   print "}"
   print ""
          
if __name__ == "__main__":
   main()



