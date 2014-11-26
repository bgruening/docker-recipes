# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND RNA-Seq

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_deseq2_1_6_1"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name deseq2"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o lparsons --name htseq_count"

RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o devteam --name cufflinks"

# Install bowtie2, fastqc
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bowtie2 --panel-section-id solexa_tools"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name fastqc --panel-section-id NGS_QC"


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
