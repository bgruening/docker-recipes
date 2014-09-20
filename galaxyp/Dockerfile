# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN sed -i 's|brand.*|brand = deepTools|g' ~/galaxy-central/universe_wsgi.ini

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

# Install deepTools
RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name peptideshaker --panel-section-name PeptideShaker"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_libtool_2_4"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_qt_4_8"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_zlib_1_2_8"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name package_openms_1_11"



# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
