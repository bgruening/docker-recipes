# Galaxy - DESeq2
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND DESeq2

# Enable TTS installation
ENV GALAXY_CONFIG_TOOL_SHEDS_CONFIG_FILE $GALAXY_HOME/tool_sheds_conf.xml

WORKDIR /galaxy-central

RUN install-repository \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name deseq2" \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o lparsons --name htseq_count"

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
