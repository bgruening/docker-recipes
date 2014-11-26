# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Mummer 3

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o peterjc --name mummer  --panel-section-name MUMmer"

# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
