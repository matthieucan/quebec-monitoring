#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Checks the number of users (registered, connected) on quebecrencontres.com
"""
#
#
#     Copyright (C) 2012 Savoir-Faire Linux Inc.
#
#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, write to the Free Software
#     Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#     Projects :
#               SFL Shinken plugins
#
#     File :
#               check_quebecrencontrescom.py Checks the number of users (registered, connected) on quebecrencontres.com
#
#
#     Author: Matthieu Caneill <matthieu.caneill@savoirfairelinux.com>
#
#

# Generated with tools/create_new_plugin.sh

import getopt
import sys

import re
import urllib2
import lxml.html

PLUGIN_NAME = "check_quebecrencontrescom"
PLUGIN_VERSION = "0.1"
STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3
STATE_DEPENDENT = 4


def print_version():
    """Show plugin version
    """
    version_msg = """
%s.py v%s (sfl-shinken-plugins)

The SFL Shinken Plugins come with ABSOLUTELY NO WARRANTY. You may redistribute
copies of the plugins under the terms of the GNU General Public License.
For more information about these matters, see the file named COPYING.
""" % (PLUGIN_NAME, PLUGIN_VERSION)
    print version_msg


def print_support():
    """Show plugin support
    """
    support_msg = """
Send email to <matthieu.caneill@savoirfairelinux.com> if you have questions
regarding use of this software. To submit patches or suggest improvements,
send email to <matthieu.caneill@savoirfairelinux.com>
Please include version information with all correspondence (when
possible, use output from the --version option of the plugin itself).
"""
    print support_msg


def print_usage():
    """Show how to use this plugin
    """
    usage_msg = """
%s.py

Usage:
 -h, --help
    Print detailed help screen
 -V, --version
    Print version information
""" % PLUGIN_NAME
    print usage_msg

def get_html():
    url = 'http://www.quebecrencontres.com/'
    try:
        html = urllib2.urlopen(url)
    except Exception as e:
        print('Error while opening url: %s' % str(e))
        sys.exit(STATE_UNKNOWN)
    if html.getcode() >= 400:
        print('HTTP error: %d' % html.getcode())
        sys.exit(STATE_UNKNOWN)
    return html.read()

def get_data(args):
    """Fetch data
    """
    html = get_html()
    tree = lxml.html.fromstring(html)
    data = tree.xpath('//div[@id="top"]/h2[@class="txtlarge"]/text()')
    if len(data) == 1:
        data = data[0]
        data = data.strip().replace(' ', '')
        results = [x for x in re.split('[^0-9]', data) if x]
        try:
            results = [int(x) for x in results[:2]]
        except Exception as e:
            print('Wrong data received: %s' % results)
            
        print('OK - %d members, %d online|'
              'members=%d;;;0;; '
              'online=%d;;;0;;' % tuple(results * 2))
        sys.exit(STATE_OK)
    
    print('Wrong data received: %s [...]' % html[:100])
    sys.exit(STATE_UNKNOWN)

def main():
    """Main function
    """
    try:
        options, args = getopt.getopt(sys.argv[1:],
                        'hV',
                        ['help', 'version'])
    except getopt.GetoptError, err:
        print str(err)
        print_usage()
        sys.exit(STATE_UNKNOWN)

    args = {}

    for option_name, value in options:
        if option_name in ("-h", "--help"):
            print_version()
            print_usage()
            print_support()
            sys.exit(STATE_UNKNOWN)
        elif option_name in ("-V", "--version"):
            print_version()
            print_support()
            sys.exit(STATE_UNKNOWN)

    get_data(args)


if __name__ == "__main__":
    main()
