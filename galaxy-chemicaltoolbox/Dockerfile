# Galaxy - ChemicalToolBox
#
# VERSION       0.1

FROM bgruening/galaxy-stable

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y wget
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libcairo2-dev

RUN sed -i 's|brand.*|brand = ChemicalToolBox|g' ~/galaxy-central/universe_wsgi.ini

# Include all needed scripts and libraries from the host
# compressed archives will be extracted automatically
ADD ./Jmoleditor.tar.bz2 /galaxy-central/

RUN rm /usr/bin/startup
ADD ./startup.sh /usr/bin/startup
RUN chmod +x /usr/bin/startup

# Install ChemicalToolBox & one example workflow
RUN service postgresql start && service apache2 start && ./run.sh --daemon && sleep 120 && python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:8080 --url http://toolshed.g2.bx.psu.edu/ -o bgruening -r c799c6211cbd --name chemicaltoolbox --tool-deps --repository-deps --panel-section-name ChemicalToolBox && python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:8080 --url http://toolshed.g2.bx.psu.edu/ -o bgruening --name chemicaltoolbox_merging_chemical_databases_workflow -r fdabd3833502 --tool-deps --repository-deps --panel-section-name ChemicalToolBox && python ./scripts/api/import_workflows_from_installed_tool_shed_repository.py --api admin -u http://toolshed.g2.bx.psu.edu -l http://localhost:8080 -o bgruening --name chemicaltoolbox_merging_chemical_databases_workflow -r fdabd3833502

# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80
# 8000 is the standard SimpleHTTPServer Server port from python
EXPOSE :8000

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
