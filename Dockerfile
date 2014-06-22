FROM ubuntu:trusty

MAINTAINER Matthieu Caneill <matthieu.caneill@savoirfairelinux.com>

ENV DEBIAN_FRONTEND noninteractive

### Init

RUN apt-get update

### Utils

RUN apt-get install -y git python-pip emacs curl

### Kaji sources

RUN curl http://download.opensuse.org/repositories/home:/kaji-project/xUbuntu_14.04/Release.key | apt-key add -
RUN echo 'deb http://download.opensuse.org/repositories/home:/kaji-project/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/kaji.list
RUN apt-get update

### Shinken

RUN apt-get install -y shinken-common
RUN apt-get install -y shinken-module-graphite
RUN apt-get install -y shinken-module-livestatus
RUN apt-get install -y shinken-module-pickle-retention-file-generic
RUN apt-get install -y shinken-module-simple-log
RUN apt-get install -y shinken-module-booster-nrpe
RUN apt-get install -y shinken-module-logstore-sqlite

RUN apt-get install -y python-openssl # required for $plugin
RUN apt-get install -y python-lxml # required by scrapers plugins

### Plugins

RUN apt-get install -y nagios-plugins

### SSH

RUN apt-get install -y openssh-server

### Apache

RUN apt-get install -y apache2 libapache2-mod-wsgi

### Supervisor

RUN apt-get -y install supervisor

### Pynag/Adagios

RUN apt-get install -y python-simplejson coffeescript gettext make
# We need an old version of Django for Adagios
RUN pip install django\<1.5 python-geoip python-geoip-geolite2
RUN ln -s /usr/bin/django-admin /usr/bin/django-admin.py

RUN cd /var && git clone https://github.com/matthieucan/adagios.git
RUN cd /var/adagios && git checkout feature-view-engine-newstuff && make trad && python setup.py install
RUN pip install git+git://github.com/pynag/pynag.git

### Configuration

## Docker

# makes `df` work
#RUN ln -s /proc/mounts /etc/mtab

# run permissions for user `shinken`
RUN chmod u+s /usr/lib/nagios/plugins/check_icmp
RUN chmod u+s /bin/ping
RUN chmod u+s /bin/ping6

## Shinken, Apache, Adagios

ADD etc /etc
ADD plugins /usr/lib/nagios/plugins
ADD templates/html /usr/local/lib/python2.7/dist-packages/adagios/status/templates/custom_views/templates
ADD templates/media /usr/local/lib/python2.7/dist-packages/adagios/media

RUN chown -R shinken: /etc/adagios
RUN chown -R shinken: /etc/shinken

RUN mv /etc/shinken/logstore_sqlite.cfg/logstore_sqlite.cfg /etc/shinken/modules/
RUN sed -i 's/logstore-sqlite/logsqlite/g' /etc/shinken/modules/logstore_sqlite.cfg
RUN sed -i 's/Livestatus/livestatus/g' /etc/shinken/brokers/broker.cfg
RUN sed -i 's/Simple-log/simple-log/g' /etc/shinken/brokers/broker.cfg
RUN sed -i 's/NrpeBooster/booster-nrpe/g' /etc/shinken/pollers/poller.cfg

# Allow ssh connection from host
# ADD id_rsa.pub /root/home/.ssh/authorized_keys

EXPOSE 80
EXPOSE 22

CMD ["/usr/bin/supervisord"]
