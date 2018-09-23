# Galaxy - Stable
#
# VERSION       0.1

FROM debian:stretch

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

# make sure the package repository is up to date
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install --no-install-recommends -y git-core mercurial build-essential \
        python-xappy python-xapian pkg-config postgresql python-dev ca-certificates python-psycopg2 python-sqlalchemy

RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

# Download and update Galaxy to the latest stable release
RUN git clone https://github.com/KerstenDoering/PubMed2Go.git
WORKDIR /PubMed2Go

# Define the default postgresql database path
# If you want to save your data locally you need to set GALAXY_DOCKER_MODE=HOST
ENV PG_DATA_DIR_DEFAULT /var/lib/postgresql/9.6/main/

# Include all needed scripts from the host
ADD ./setup_postgresql.py /PubMed2Go/setup_postgresql.py
ADD ./export_user_files.py /PubMed2Go/export_user_files.py
ADD ./startup.sh /usr/bin/startup

RUN chmod +x /usr/bin/startup

# Configure PostgreSQL
# 1. Remove all old configuration
# 2. Create DB-user 'parser' with password 'parser' in database 'pubmed'
RUN service postgresql stop
RUN rm $PG_DATA_DIR_DEFAULT -rf
RUN python setup_postgresql.py --dbuser parser --dbpassword parser --db-name pubmed --dbpath $PG_DATA_DIR_DEFAULT --db-schema pubmed
RUN service postgresql start && \
    echo "Waiting for PostgreSQL" && \
    sleep 2m && \
    python PubMedDB.py -d pubmed && \
    service postgresql stop
RUN echo "host    all             all             0.0.0.0/0            md5" >> /etc/postgresql/9.6/main/pg_hba.conf
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.6/main/postgresql.conf

# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :5432

# Autostart script that is invoked during container start
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/bin/startup"]
