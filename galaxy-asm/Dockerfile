# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN sed -i 's|brand.*|brand = Allele specific mapping|g' ~/galaxy-central/universe_wsgi.ini

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y build-essential gfortran
# TODO: tabix is/can be installed via the Tool Shed
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y tabix
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove -y
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

# Install suspenders & labels
RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name labels --panel-section-name ASM"
RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name suspenders --panel-section-name ASM"

# Install bowtie2, fastqc & tophat
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bowtie2 --panel-section-name ASM"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name fastqc --panel-section-name NGS_QC"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name package_tophat2_2_0_9 --panel-section-name ASM"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name tophat2 --panel-section-name ASM"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_tabix_0_2_6"

# Installing deepTools
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name deeptools --panel-section-name deepTools"


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
