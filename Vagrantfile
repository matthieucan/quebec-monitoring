# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
     vb.customize ["modifyvm", :id, "--memory", "2048"]
  end
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  # Enable provisioning with CFEngine. CFEngine Community packages are
  # automatically installed. For example, configure the host as a
  # policy server and optionally a policy file to run:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.am_policy_hub = true
  #   # cf.run_file = "motd.cf"
  # end
  #
  # You can also configure and bootstrap a client to an existing
  # policy server:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.policy_server_address = "10.0.2.15"
  # end

  # Enable provisioning with Puppet stand alone.  Puppet manifests
  # are contained in a directory path relative to this Vagrantfile.
  # You will need to create the manifests directory and a manifest in
  # the file default.pp in the manifests_path directory.
  #
  # config.vm.provision "puppet" do |puppet|
  #   puppet.manifests_path = "manifests"
  #   puppet.manifest_file  = "default.pp"
  # end

  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
  #
  # config.vm.provision "chef_solo" do |chef|
  #   chef.cookbooks_path = "../my-recipes/cookbooks"
  #   chef.roles_path = "../my-recipes/roles"
  #   chef.data_bags_path = "../my-recipes/data_bags"
  #   chef.add_recipe "mysql"
  #   chef.add_role "web"
  #
  #   # You may also specify custom JSON attributes:
  #   chef.json = { mysql_password: "foo" }
  # end

  # Enable provisioning with chef server, specifying the chef server URL,
  # and the path to the validation key (relative to this Vagrantfile).
  #
  # The Opscode Platform uses HTTPS. Substitute your organization for
  # ORGNAME in the URL and validation key.
  #
  # If you have your own Chef Server, use the appropriate URL, which may be
  # HTTP instead of HTTPS depending on your configuration. Also change the
  # validation key to validation.pem.
  #
  # config.vm.provision "chef_client" do |chef|
  #   chef.chef_server_url = "https://api.opscode.com/organizations/ORGNAME"
  #   chef.validation_key_path = "ORGNAME-validator.pem"
  # end
  #
  # If you're using the Opscode platform, your validator client is
  # ORGNAME-validator, replacing ORGNAME with your organization name.
  #
  # If you have your own Chef Server, the default validation client name is
  # chef-validator, unless you changed the configuration.
  #
  #   chef.validation_client_name = "ORGNAME-validator"
  config.vm.provision :shell, :inline => "sudo apt-get update"
  config.vm.provision :shell, :inline => "sudo apt-get upgrade -y"
  config.vm.provision :shell, :inline => "sudo apt-get install -y git python-pip curl nodejs nodejs-legacy npm vim wget aptitude htop openssh-server apache2 libapache2-mod-wsgi python-bs4 python-requests"
  config.vm.provision :shell, :inline => "npm install -g bower"
  config.vm.provision :shell, :inline => "sudo gpg --recv-keys  --keyserver pgp.mit.edu 2320E8F8 && gpg --export --armor 2320E8F8 | apt-key add -"
  config.vm.provision :shell, :inline => "sudo echo 'deb http://deb.kaji-project.org/ubuntu14.04/ amakuni main' >> /etc/apt/sources.list.d/kaji.list"
  config.vm.provision :shell, :inline => "sudo echo 'deb http://deb.kaji-project.org/ubuntu14.04/ plugins main' >> /etc/apt/sources.list.d/kaji.list"
  config.vm.provision :shell, :inline => "sudo apt-get update"
#  config.vm.provision :shell, :inline => "debconf-set-selections <<< 'postfix postfix/mailname string your.hostname.com'"
#  config.vm.provision :shell, :inline => "debconf-set-selections <<< 'postfix postfix/main_mailer_type string \'Internet Site\''"
  config.vm.provision :shell, :inline => "debconf-set-selections <<< 'postfix postfix/mailname string your.hostname.com'"
  config.vm.provision :shell, :inline => "debconf-set-selections <<< \"postfix postfix/main_mailer_type string 'Internet Site'\""
  config.vm.provision :shell, :inline => "debconf-set-selections <<< \"nagvis nagvis/monitoring_system string icinga\""
  config.vm.provision :shell, :inline => "apt-get install -y postfix"
  config.vm.provision :shell, :inline => "apt-get install -y nagvis"
  config.vm.provision :shell, :inline => "apt-get install -y kaji"
  config.vm.provision :shell, :inline => "apt-get install -y nagios-plugins"
  config.vm.provision :shell, :inline => "apt-get install -y monitoring-plugins-sfl-check-amt-montreal monitoring-plugins-sfl-check-bixi-montreal monitoring-plugins-sfl-check-emergency-rooms-quebec monitoring-plugins-sfl-check-environment-canada monitoring-plugins-sfl-check-http2 monitoring-plugins-sfl-check-quebecrencontrescom monitoring-plugins-sfl-check-reseaucontactcom monitoring-plugins-sfl-check-stm-metro-montreal monitoring-plugins-sfl-check-hydro-quebec"
  config.vm.provision :shell, :inline => "chmod u+s /bin/ping"
  config.vm.provision :shell, :inline => "chmod u+s /bin/ping6"
  config.vm.provision :shell, :inline => "mkdir /etc/shinken/adagios/ -p"
  config.vm.provision :shell, :inline => "/scripts/banks.py > /etc/shinken/adagios/banks.cfg"
  config.vm.provision :shell, :inline => "/scripts/dns.py > /etc/shinken/adagios/dns.cfg"
  config.vm.provision :shell, :inline => "/scripts/websites.py > /etc/shinken/adagios/websites.cfg"
  config.vm.provision :shell, :inline => "/scripts/hospitals.py > /etc/shinken/adagios/hospitals.cfg"
  config.vm.provision :shell, :inline => "/scripts/transports.py > /etc/shinken/adagios/transports.cfg"
  config.vm.provision :shell, :inline => "/scripts/dating.py > /etc/shinken/adagios/dating.cfg"
  config.vm.provision :shell, :inline => "/scripts/isp.py > /etc/shinken/adagios/isp.cfg"
  config.vm.provision :shell, :inline => "/scripts/environment.py > /etc/shinken/adagios/environment.cfg"
  config.vm.provision :shell, :inline => "/scripts/energy.py > /etc/shinken/adagios/energy.cfg"
  config.vm.provision :shell, :inline => "cd /srv/app && yes | bower install --allow-root"
  config.vm.synced_folder "app/", "/srv/app"
  config.vm.synced_folder "scripts/", "/scripts"
  config.vm.synced_folder "etc/", "/tmp/etc"
  config.vm.provision :shell, :inline => "cp -r /tmp/etc/* /etc/"
#  config.vm.provision "file", source: "etc/adagios/adagios.conf", destination: "/etc/adagios/adagios.conf"
#  config.vm.provision "file", source: "etc/adagios/userdata/anonymous.json", destination: "/etc/adagios/userdata/anonymous.json"
#  config.vm.provision "file", source: "etc/apache2/sites-enabled/adagios.conf", destination: "/etc/apache2/sites-enabled/adagios.conf"
#  config.vm.provision "file", source: "etc/apache2/sites-enabled/quebec247.conf", destination: "/etc/apache2/sites-enabled/quebec247.conf"
#  config.vm.provision "file", source: "etc/shinken/shinken.cfg", destination: "/etc/shinken/shinken.cfg"
#  config.vm.provision "file", source: "etc/shinken/templates.cfg", destination: "/etc/shinken/templates.cfg"
#  config.vm.provision "file", source: "etc/shinken/adagios/commands.cfg", destination: "/etc/shinken/adagios/commands.cfg"
#  config.vm.provision "file", source: "etc/shinken/adagios/resources.cfg", destination: "/etc/shinken/adagios/resources.cfg"
#  config.vm.provision "file", source: "etc/shinken/adagios/timeperiods.cfg", destination: "/etc/shinken/adagios/timeperiods.cfg"
#  config.vm.provision "file", source: "etc/shinken/brokers/broker.cfg", destination: "/etc/shinken/brokers/broker.cfg"

  config.vm.provision :shell, :inline => "sudo bash /usr/sbin/kaji-finish-install"
  config.vm.provision :shell, :inline => "rm /etc/shinken/hosts/localhost.cfg"
  config.vm.provision :shell, :inline => "service shinken-arbiter restart"
end
