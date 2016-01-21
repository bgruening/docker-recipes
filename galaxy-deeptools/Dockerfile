# Galaxy - deepTools
#
# VERSION       dev

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND deepTools
ENV GALAXY_CONFIG_ENABLE_BETA_TOOL_COMMAND_ISOLATION True
ENV GALAXY_CONFIG_SERVE_XSS_VULNERABLE_MIMETYPES True

RUN add-tool-shed --url 'https://testtoolshed.g2.bx.psu.edu/' --name 'Test Tool Shed'

# Install deepTools
RUN install-repository \
    "--url https://testtoolshed.g2.bx.psu.edu/ -o bgruening --name suite_deeptools --panel-section-name deepTools"

# Install bowtie2, fastqc
RUN install-repository \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name bowtie2 --panel-section-id solexa_tools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name data_manager_bowtie2_index_builder" \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name data_manager_fetch_genome_dbkeys_all_fasta" \
    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name fastqc --panel-section-id NGS_QC"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
