#!/bin/bash

cd /galaxy-central
# After executing init_galaxy, postgresql should be up and running
# If GALAXY_DOCKER_MODE is not HOST the defaul PostgreSQL database is located in /var/lib/postgresql/9.1/main/.
# Otherwise, PostgreSQL data will be stored in /var/lib/postgresql/9.1/main_host/ and 
# Galaxy data in /galaxy-central/database_host/
python ./init_galaxy.py --dbuser galaxy --dbpassword galaxy --db-name galaxy --guser admin@galaxy.org --gpassword admin --gkey admin --mode ${GALAXY_DOCKER_MODE-TESTMODE}
# start Galaxy
./run.sh --daemon
# start the Webserver that is needed for Jmoleditor 
python -m SimpleHTTPServer &
# start Apache in Foreground, that is needed for Docker
apache2 -D FOREGROUND
