# Galaxy - ChemicalToolBox
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    apt-get install --no-install-recommends -y wget libcairo2-dev

ENV GALAXY_CONFIG_BRAND ChemicalToolBox
ENV GALAXY_CONFIG_SERVE_XSS_VULNERABLE_MIMETYPES ChemicalToolBox

# Include all needed scripts and libraries from the host
# compressed archives will be extracted automatically
ADD ./Jmoleditor.tar.bz2 /galaxy-central/

RUN rm /usr/bin/startup
ADD ./startup.sh /usr/bin/startup
RUN chmod +x /usr/bin/startup

ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

# Install ChemicalToolBox & one example workflow
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name chemicaltoolbox --panel-section-name ChemicalToolBox"

# install unique wrapper
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name unique --panel-section-id filter"

# Install sed wrapper
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o bjoern-gruening --name sed_wrapper --panel-section-id textutil"

# Install workflow
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name chemicaltoolbox_merging_chemical_databases_workflow --panel-section-name ChemicalToolBox"

# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80
# 8000 is the standard SimpleHTTPServer Server port from python
EXPOSE :8000

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
