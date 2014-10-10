# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN sed -i 's|brand.*|brand = OpenMS|g' ~/galaxy-central/universe_wsgi.ini

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

RUN sleep 7 && ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name package_openms_latest"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name openms --panel-section-name OpenMS"


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
