# Galaxy - ASM

FROM bgruening/galaxy-ngs-preprocessing

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Allele specific mapping


# Enable TTS installation
# RUN add-tool-shed --url 'http://testtoolshed.g2.bx.psu.edu/' --name 'Test Tool Shed'

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    apt-get install --no-install-recommends -y build-essential gfortran tabix && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install suspenders & labels
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name labels --panel-section-name ASM"
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name suspenders --panel-section-name ASM"

# Install bowtie2, fastqc & tophat
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name package_tophat2_2_0_9 --panel-section-name ASM"
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name tophat2 --panel-section-name ASM"

RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_tabix_0_2_6"

# Installing deepTools
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name deeptools --panel-section-name deepTools"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
