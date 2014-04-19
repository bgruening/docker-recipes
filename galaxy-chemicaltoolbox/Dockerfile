# Galaxy - ChemicalToolBox
#
# VERSION       0.1

FROM debian:wheezy

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

# make sure the package repository is up to date
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update

# Set Apache User and Group
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# Install all requirements that are recommend by the Galaxy project
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y autoconf
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y automake
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y cmake
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y git-core
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libatlas-base-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libblas-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y liblapack-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y mercurial
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y subversion
#RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y python-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y pkg-config
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y openjdk-7-jre
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y postgresql
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y apache2
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libapache2-mod-xsendfile
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y sudo

# Load required Apache Modules
RUN a2enmod xsendfile
RUN a2enmod proxy
RUN a2enmod proxy_balancer
RUN a2enmod proxy_http
RUN a2enmod rewrite

# Download and update Galaxy to the latest stable release
RUN hg clone https://bitbucket.org/galaxy/galaxy-central/
WORKDIR /galaxy-central
RUN hg pull
RUN hg update stable

# Configure Galaxy to use the Tool Shed
RUN cp ~/galaxy-central/universe_wsgi.ini.sample ~/galaxy-central/universe_wsgi.ini
RUN mkdir ~/shed_tools
RUN mkdir ~/galaxy-central/tool_deps

# TODO: use a prepared and tuned config file
RUN sed -i 's|#database_connection.*|database_connection = postgres://galaxy:galaxy@localhost:5432/galaxy|g' ~/galaxy-central/universe_wsgi.ini
RUN sed -i 's|#tool_dependency_dir = None|tool_dependency_dir = ./tool_deps|g' ~/galaxy-central/universe_wsgi.ini
RUN sed -i 's|#tool_config_file|tool_config_file|g' ~/galaxy-central/universe_wsgi.ini
RUN sed -i 's|#tool_path|tool_path|g' ~/galaxy-central/universe_wsgi.ini
RUN sed -i 's|#admin_users = None|admin_users = admin@galaxy.org|g' ~/galaxy-central/universe_wsgi.ini
RUN sed -i 's|#master_api_key=changethis|master_api_key=HSNiugRFvgT574F43jZ7N9F3|g' ~/galaxy-central/universe_wsgi.ini
RUN sed -i 's|#brand = None|brand = ChemicalToolBox|g' ~/galaxy-central/universe_wsgi.ini

# Fetching all Galaxy python dependencies
RUN python scripts/fetch_eggs.py

# Define the default postgresql database path
# If you want to save your data locally you need to set GALAXY_DOCKER_MODE=HOST
ENV PG_DATA_DIR_DEFAULT /var/lib/postgresql/9.1/main/

# Include all needed scripts from the host
ADD ./init_galaxy.py /galaxy-central/init_galaxy.py
ADD ./ctb.apache /tmp/ctb.apache
ADD ./startup.sh /usr/bin/startup.sh
RUN chmod +x /galaxy-central/init_galaxy.py
RUN chmod +x /usr/bin/startup.sh
RUN cp /tmp/ctb.apache /etc/apache2/sites-available/

RUN a2ensite ctb.apache
RUN service apache2 restart
RUN service postgresql stop

# Configure PostgreSQL
# 1. Remove all old configuration
# 2. Create DB-user 'galaxy' with password 'galaxy' in database 'galaxy'
# 3. Create Galaxy Admin User 'admin@galaxy.org' with password 'admin' and API key 'admin'
RUN rm $PG_DATA_DIR_DEFAULT -rf
RUN python ./init_galaxy.py --dbuser galaxy --dbpassword galaxy --db-name galaxy --guser admin@galaxy.org --gpassword admin --gkey admin --dbpath $PG_DATA_DIR_DEFAULT --docker-build

# Mark two folders as imported from the host.
# Here we will store the data if the User set GALAXY_DOCKER_MODE=HOST
VOLUME ["/var/lib/postgresql/9.1/main_host", "/galaxy-central/database_host/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup.sh"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

