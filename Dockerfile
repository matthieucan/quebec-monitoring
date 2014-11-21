FROM ubuntu:trusty

MAINTAINER Matthieu Caneill <matthieu.caneill@savoirfairelinux.com>

ENV DEBIAN_FRONTEND noninteractive

### Init

RUN apt-get update

### Utils

RUN apt-get install -y git python-pip emacs curl nodejs nodejs-legacy npm
RUN npm install -g bower

### Other .deb sources

RUN curl http://download.opensuse.org/repositories/home:/kaji-project/xUbuntu_14.04/Release.key | apt-key add -
RUN echo 'deb http://download.opensuse.org/repositories/home:/kaji-project/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/kaji.list

RUN curl http://download.opensuse.org/repositories/home:/sfl-monitoring:/monitoring-tools/xUbuntu_14.04/Release.key | apt-key add -
RUN echo 'deb http://download.opensuse.org/repositories/home:/sfl-monitoring:/monitoring-tools/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/shinkenplugins.list

RUN apt-get update

### Shinken

RUN apt-get install -y shinken-common
RUN apt-get install -y shinken-mod-livestatus
RUN apt-get install -y shinken-mod-pickle-retention-file-generic
RUN apt-get install -y shinken-mod-simple-log
RUN apt-get install -y shinken-mod-booster-nrpe
RUN apt-get install -y shinken-mod-logstore-sqlite

### Plugins

RUN apt-get install -y nagios-plugins
RUN apt-get install -y plugin-check-amt-montreal plugin-check-bixi-montreal plugin-check-emergency-rooms-quebec plugin-check-environment-canada plugin-check-http2 plugin-check-quebecrencontrescom plugin-check-reseaucontactcom plugin-check-stm-metro-montreal plugin-check-hydro-quebec

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

#RUN cd /var && git clone https://github.com/matthieucan/adagios.git
#RUN cd /var/adagios && git checkout feature-view-engine-rebased && make trad && python setup.py install
RUN pip install git+git://github.com/pynag/pynag.git
RUN pip install git+git://github.com/opinkerfi/adagios.git


### Configuration

## Docker

# makes `df` work
#RUN ln -s /proc/mounts /etc/mtab

# run permissions for user `shinken`
RUN chmod u+s /usr/lib/nagios/plugins/check_icmp
RUN chmod u+s /bin/ping
RUN chmod u+s /bin/ping6

## Shinken, Apache, Adagios

ADD app /srv/app

RUN chown -R shinken: /etc/adagios
RUN chown -R shinken: /etc/shinken

## Shinken hosts/services configuration
RUN apt-get install -y python-bs4 python-requests
ADD scripts /scripts
RUN mkdir /etc/shinken/adagios
RUN scripts/banks.py > etc/shinken/adagios/banks.cfg
RUN scripts/dns.py > etc/shinken/adagios/dns.cfg
RUN scripts/websites.py > etc/shinken/adagios/websites.cfg
RUN scripts/hospitals.py > etc/shinken/adagios/hospitals.cfg
RUN scripts/transports.py > etc/shinken/adagios/transports.cfg
RUN scripts/dating.py > etc/shinken/adagios/dating.cfg
RUN scripts/isp.py > etc/shinken/adagios/isp.cfg
RUN scripts/environment.py > etc/shinken/adagios/environment.cfg
RUN scripts/energy.py > etc/shinken/adagios/energy.cfg

# APP
RUN cd /srv/app && yes | bower install --allow-root

# fixed upstream, should be fixed in newer Debian packages
RUN mv /etc/shinken/logstore_sqlite.cfg/logstore_sqlite.cfg /etc/shinken/modules/
RUN sed -i 's/logstore-sqlite/logsqlite/g' /etc/shinken/modules/logstore_sqlite.cfg
RUN sed -i 's/Livestatus/livestatus/g' /etc/shinken/brokers/broker.cfg
RUN sed -i 's/Livestatus/livestatus/g' /etc/shinken/modules/livestatus.cfg
RUN sed -i 's/NrpeBooster/booster-nrpe/g' /etc/shinken/modules/booster_nrpe.cfg/booster_nrpe.cfg
RUN sed -i 's/SimpleLog/simple-log/g' /etc/shinken/brokers/broker.cfg
RUN sed -i 's/Graphite/graphite/g' /etc/shinken/brokers/broker.cfg
RUN sed -i 's/BoosterNrpe/booster-nrpe/g' /etc/shinken/brokers/broker.cfg
RUN sed -i 's/NrpeBooster/booster-nrpe/g' /etc/shinken/pollers/poller.cfg

RUN sed -i 's/WebUI/livestatus/g' /etc/shinken/brokers/broker.cfg

# Allow ssh connection from host
# ADD id_rsa.pub /root/home/.ssh/authorized_keys

# temporary fix while we wait for https://github.com/shinken-monitoring/mod-livestatus/pull/26
ADD mod-livestatus-labels.patch /mod-livestatus-labels.patch
RUN cd /usr/share/pyshared/shinken/modules/livestatus && git apply /mod-livestatus-labels.patch

ADD etc /etc

EXPOSE 80
EXPOSE 8083
EXPOSE 22

CMD ["/usr/bin/supervisord"]
