# Galaxy - MUMmer 3
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Mummer 3

WORKDIR /galaxy-central

RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o peterjc --name mummer  --panel-section-name MUMmer"

# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
