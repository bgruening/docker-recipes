# Galaxy - ChemicalToolBox
#
# VERSION       0.1

FROM quay.io/bgruening/galaxy:16.01

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    apt-get install --no-install-recommends -y wget libcairo2-dev && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV GALAXY_CONFIG_BRAND ChemicalToolBox \
GALAXY_CONFIG_SERVE_XSS_VULNERABLE_MIMETYPES True \
GALAXY_CONFIG_CONDA_AUTO_INSTALL True \
GALAXY_CONFIG_CONDA_AUTO_INIT True \
GALAXY_CONFIG_CONDA_ENSURE_CHANNELS r,bioconda

# Include all needed scripts and libraries from the host
# compressed archives will be extracted automatically
ADD ./Jmoleditor.tar.bz2 /galaxy-central/

# ToDo: run simpleHTTPServer from startup
#RUN rm /usr/bin/startup
#ADD ./startup.sh /usr/bin/startup
#RUN chmod +x /usr/bin/startup

# Install deepTools
ADD chemicaltoolbox_tools.yml $GALAXY_ROOT/tools.yaml
RUN install-tools $GALAXY_ROOT/tools.yaml


# install unique wrapper
#RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name unique --panel-section-id filter"

# Install sed wrapper
#RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o bjoern-gruening --name sed_wrapper --panel-section-id textutil"

# Install workflow
#RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name chemicaltoolbox_merging_chemical_databases_workflow --panel-section-name ChemicalToolBox"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9002 (supervisor webui)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9002
# 8000 is the standard SimpleHTTPServer Server port from python
EXPOSE :8000

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
