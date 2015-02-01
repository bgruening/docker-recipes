# Galaxy - RNA workbench
#
# VERSION       0.1

FROM bgruening/galaxy-stable:dev

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Galaxy for RNA Research

WORKDIR /galaxy-central

# TODO: rnashapes is currently not in the ToolShed install it via PPA
RUN apt-get -qq update && apt-get install --no-install-recommends -y apt-transport-https software-properties-common && \
    apt-add-repository -y ppa:bibi-help/bibitools && \
    apt-get -qq update && \
    apt-get install --no-install-recommends -y rnashapes &&\
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN install-repository "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name rnabob --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name trna_prediction --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o rnateam --name blockclust --panel-section-name RNATools" \
    "--url https://testtoolshed.g2.bx.psu.edu/ -o rnateam --name cofold --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name infernal --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o lionelguy --name rnammer --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name rnaz --panel-section-name RNATools" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name suite_mirdeep_2_0 --panel-section-name RNATools" \

    "--url https://toolshed.g2.bx.psu.edu/ -o devteam --name emboss_5 --panel-section-name EMBOSS" \
    "--url https://toolshed.g2.bx.psu.edu/ -o bgruening --name text_processing --panel-section-name 'Text manipulation'" \
    "--url https://toolshed.g2.bx.psu.edu/ -o iuc --name bedtools --panel-section-name 'BED tools'"

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
