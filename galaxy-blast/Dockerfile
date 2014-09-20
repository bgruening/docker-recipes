# Galaxy - Exom Sequencing Pipeline
#
# VERSION       0.1

FROM bgruening/galaxy-stable:latest_2014.08.11

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN sed -i 's|brand.*|brand = NCBI BLAST+ Suite|g' ~/galaxy-central/universe_wsgi.ini

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh


# Install NCBI Blast+

RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_blast_plus_2_2_26"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_blast_plus_2_2_28"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_blast_plus_2_2_29"


#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r d375502056f1 --panel-section-name BLAST+"
#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 643338ac83c0 --panel-section-name BLAST+"
#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 9d5beacae92b --panel-section-name BLAST+"
#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 393a7a35383c --panel-section-name BLAST+"
#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 4ce66a5401d0 --panel-section-name BLAST+"
#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 1f546099212f --panel-section-name BLAST+"
#RUN ./install_repo_wrapper.sh \
#    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 9dabbfd73c8a --panel-section-name BLAST+"


RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 70e7dcbf6573 --panel-section-name BLAST+"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 4c4a0da938ff --panel-section-name BLAST+"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 6560192c5098 --panel-section-name BLAST+"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name ncbi_blast_plus -r 623f727cdff1 --panel-section-name BLAST+"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o peterjc --name blastxml_to_top_descr --panel-section-name BLAST+"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o peterjc --name blast_rbh --panel-section-name BLAST+"




# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
