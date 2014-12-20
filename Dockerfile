FROM ubuntu:trusty

MAINTAINER Matthieu Caneill <matthieu.caneill@savoirfairelinux.com>

ENV DEBIAN_FRONTEND noninteractive

### Init

RUN apt-get update

### Utils

RUN apt-get install -y git python-pip emacs curl nodejs nodejs-legacy npm vim wget
RUN npm install -g bower

### Other .deb sources

RUN curl http://download.opensuse.org/repositories/home:/kaji-project/xUbuntu_14.04/Release.key | apt-key add -
RUN echo 'deb http://download.opensuse.org/repositories/home:/kaji-project/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/kaji.list

RUN curl http://download.opensuse.org/repositories/home:/sfl-monitoring:/monitoring-tools/xUbuntu_14.04/Release.key | apt-key add -
RUN echo 'deb http://download.opensuse.org/repositories/home:/sfl-monitoring:/monitoring-tools/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/shinkenplugins.list

RUN apt-get update

### InfluxDB

RUN wget http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb

RUN dpkg -i influxdb_latest_amd64.deb

### Shinken

RUN apt-get install -y kaji

### Plugins

RUN apt-get install -y nagios-plugins
RUN apt-get install -y plugin-check-amt-montreal plugin-check-bixi-montreal plugin-check-emergency-rooms-quebec plugin-check-environment-canada plugin-check-http2 plugin-check-quebecrencontrescom plugin-check-reseaucontactcom plugin-check-stm-metro-montreal plugin-check-hydro-quebec

### SSH

RUN apt-get install -y openssh-server

### Apache

RUN apt-get install -y apache2 libapache2-mod-wsgi

### Supervisor

RUN apt-get -y install supervisor

### Configuration

## Docker

# makes `df` work
#RUN ln -s /proc/mounts /etc/mtab

# run permissions for user `shinken`
RUN chmod u+s /bin/ping
RUN chmod u+s /bin/ping6

## Shinken, Apache, Adagios

ADD app /srv/app

## Shinken hosts/services configuration
RUN apt-get install -y python-bs4 python-requests
ADD scripts /scripts
#RUN mkdir /etc/shinken/adagios
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

# Allow ssh connection from host
#ADD id_rsa.pub /root/.ssh/authorized_keys
#RUN echo root:root | chpasswd
#RUN sed -i 's/PermitRootLogin.*/PermitRootLogin Yes/' /etc/ssh/sshd_config

ADD etc /etc

# rm useless configuration
RUN rm -f /etc/shinken/hosts/*

### Finishing installation

RUN sudo bash /usr/sbin/kaji-finish-install


EXPOSE 80
EXPOSE 8083
EXPOSE 22

CMD ["/usr/bin/supervisord"]
