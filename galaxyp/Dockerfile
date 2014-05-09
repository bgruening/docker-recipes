# Galaxy - deepTools
#
# VERSION       0.1

FROM bgruening/galaxy-stable

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN sed -i 's|brand.*|brand = deepTools|g' ~/galaxy-central/universe_wsgi.ini

WORKDIR /galaxy-central

# Install deepTools
RUN service postgresql start && service apache2 start && ./run.sh --daemon && sleep 120 && python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:8080 --url http://testtoolshed.g2.bx.psu.edu/ -o bgruening -r b9f2cedab007 --name  peptideshaker --tool-deps --repository-deps --panel-section-name PeptideShaker

# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
