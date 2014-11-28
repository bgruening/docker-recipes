# Galaxy - DESeq2
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND DESeq2

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh

RUN sleep 3 && ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_deseq2_1_6_1"

RUN sleep 3 && ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name deseq2"

RUN sleep 3 && ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o lparsons --name htseq_count"


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
