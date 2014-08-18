quebec-monitoring
=================

Dockerfile all-in-the-box, plugins and templates to monitor various metrics in Québec.

Let's monitor Quebec! This work is inspired by
http://iceland.adagios.org by @palli.


## How to: run at home

### Generate the configuration

* (not mandatory) Fill the tokens needed for certain web services
  ```
  $ cp scripts/tokens.py.copyme scripts/tokens.py
  $ <your-favourite-editor> scripts/tokens.py
  ```

### Run the Docker container

The only dependency is Docker, on Debian- or Ubuntu-based distros you
can:
```
$ sudo apt-get install docker.io
```

After cloning the repository, just do:
```
$ sudo make run
```

If you installed Docker manually, perhaps the command to run it is
`docker` instead of `docker.io`. In this case, run `sed -i
s/docker.io/docker/g Makefile`, or symlink docker.io to your docker
binary.

And now, navigate to your container IP. In order to know your
container IP, you can run `sudo docker.io inspect <container-number>`,
replacing `<container-number>` by the last line returned by the previous
command.

<dl>
  <dt>What? You really use sudo? This looks dangerous.</dt>
  <dd>In order to use Docker, admin rights are required. If you're not
  confident doing this, you can easily check that only the Ubuntu trusted image is
  downloaded, everything is built from it in the Dockerfile.</dd>
  
  <dt>What does it install on my machine?</dt>
  <dd>Nothing, except for Docker if you didn't have it
  already. Everything's installed in a container, which is more or
  less a virtual machine that you can throw away afterwards :-)</dd>

  <dt>Is it really that simple to run?</dt>
  <dd>Yes.</dd>
</dl>

#### Analytics

If you want to host this and get analytics, adapt the Piwik
configuration in apache-quebec.conf and templates/html/quebec.html

For an easy-to-setup Piwik in Docker, try
https://github.com/matthieucan/Dockerfiles/piwik


## How to: contribute

Everything here is based on:
* back-end: the monitoring engine Shinken,
* front-end: the Django application Adagios,
* all-in-the-box: the container manager Docker.

If you want to add a metric in an existing category, you can add
relevant information in `scripts/<category>.py`.

If you want to create a new category, create a script in
`scripts/<your-cool-idea>.py`, and an entry in the Makefile.

To have a nice development environment:

`make dev` will:
* generate the configuration from your scripts/ (look in the Makefile),
* bring you in an interactive Docker environment (where you can play with Shinken,
Apache, and the various scripts),
* map the frontend application from your harddrive to your container,
* map the specific Quebec247 configuration from your harddrive to your container.

Now run `service shinken start && service apache2 start` in your
container. Make changes to the `scripts/*.py` (backend) or `app/*`
(frontend), it will be automatically updated!

__Pull requests, patches, bug reports, feedback and pizzas are always
welcome!__

## How to: contact us

If Github workflows (issues, pull-requests) are not suitable for you,
or if you prefer to use traditional email, you can reach us through
[supervision@savoirfairelinux.com](mailto:supervision@savoirfairelinux.com "Say hi!").

We're looking forward to hearing from you!
