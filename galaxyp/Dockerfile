# Galaxy - GalaxyP
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Galaxy for Proteomic Research

WORKDIR /galaxy-central

RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name peptideshaker --panel-section-name PeptideShaker"
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name package_openms_latest"
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name openms --panel-section-name OpenMS"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
