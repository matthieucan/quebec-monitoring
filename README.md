quebec-monitoring
=================

Dockerfile all-in-the-box, plugins and templates to monitor various metrics in Québec.

Let's monitor Quebec! This work is inspired by
http://iceland.adagios.org by @palli.


# How to: run at home

The only dependency is Docker, on Debian- or Ubuntu-based distros you
can:
'''
sudo apt-get install docker.io
'''

After cloning the repository, just do:
'''
sudo make run
'''

## Is it THAT simple?

Yes.

# How to: contribute

Everything here is based on:
* back-end: the monitoring engine Shinken,
* front-end: the Django applicatin Adagios,
* all-in-the-box: the container manager Docker.

If you want to add a metric in an existing category, you can add
relevant information in scripts/<category>.py.

If you want to create a new category, add a script in
scripts/<your-cool-idea>.py, and a line in the Makefile.

*Pull requests, patches, bug reports, feedback and pizzas are always
 welcome!*
 