# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND deepTools

WORKDIR /galaxy-central

RUN apt-get -qq update && apt-get install --no-install-recommends -y openssl

# Install deepTools



RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_python_2_7"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_atlas_3_10"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_gdbm_1_11"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_bzlib_1_0"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_xz_5_0_5"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_readline_6_2"

RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_numpy_1_9"
RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_scipy_0_14"
#RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_samtools_0_1_19"
#RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o devteam --name package_freetype_2_5_2"
#RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_matplotlib_1_4"
#RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_pysam_0_8_1"
#RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_bx_python_0_7_2"

RUN install-repository "--url https://testtoolshed.g2.bx.psu.edu/ -o bgruening --name upload_testing --panel-section-name deepTools"

# Install bowtie2, fastqc
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name bowtie2 --panel-section-id solexa_tools"
RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name fastqc --panel-section-id NGS_QC"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001
# 8000 is the standard SimpleHTTPServer Server port from python
EXPOSE :8000

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
