# Galaxy - BLAST+ suite
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND NCBI BLAST+ Suite

WORKDIR /galaxy-central

# Install NCBI Blast+

RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus --panel-section-name BLAST+"
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o peterjc --name blastxml_to_top_descr --panel-section-name BLAST+"
RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o peterjc --name blast_rbh --panel-section-name BLAST+"


# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
