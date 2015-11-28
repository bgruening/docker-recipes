# Galaxy - DESeq2

FROM bgruening/galaxy-ngs-preprocessing

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND DESeq2
ENV GALAXY_CONFIG_SERVE_XSS_VULNERABLE_MIMETYPES True

# Enable TTS installation
#RUN add-tool-shed --url 'http://testtoolshed.g2.bx.psu.edu/' --name 'Test Tool Shed'

RUN install-repository \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name deseq2" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name dexseq" \
    "--url http://toolshed.g2.bx.psu.edu/ -o lparsons --name htseq_count"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
