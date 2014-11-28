# Galaxy - Exom Sequencing Pipeline
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


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
