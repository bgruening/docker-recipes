# Galaxy - RNA-Seq
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND RNA-Seq

WORKDIR /galaxy-central

RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_deseq2_1_6_1"
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name deseq2"
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o lparsons --name htseq_count"
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o devteam --name all_cufflinks_tool_suite"

# Install bowtie2, fastqc
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bowtie2 --panel-section-id solexa_tools"
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name fastqc --panel-section-id NGS_QC"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
