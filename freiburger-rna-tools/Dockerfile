# RNA - webserver
#
# VERSION       3.4.0

FROM debian:wheezy

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com & Martin Mann, mmann@informatik.uni-freiburg.de

# make sure the package repository is up to date
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y openjdk-7-jre-headless tomcat7
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y gridengine-master gridengine-exec gridengine-common gridengine-qmon gridengine-client
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y ghostscript wget graphicsmagick graphicsmagick-imagemagick-compat
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y r-base-core
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y cpanminus
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y sudo nano less vim procps

RUN mkdir -p /usr/local/user/

RUN wget -qO- http://rna.informatik.uni-freiburg.de/Docker-deploy/FRT/3.4.0/FRT-3.4.0-ExpaRNA.tgz | tar -zxf - -C /usr/local/user/
RUN wget -qO- http://rna.informatik.uni-freiburg.de/Docker-deploy/FRT/3.4.0/FRT-3.4.0-CARNA.tgz | tar -zxf - -C /usr/local/user/
RUN wget -qO- http://rna.informatik.uni-freiburg.de/Docker-deploy/FRT/3.4.0/FRT-3.4.0-LocARNA.tgz | tar -zxf - -C /usr/local/user/
RUN wget -qO- http://rna.informatik.uni-freiburg.de/Docker-deploy/FRT/3.4.0/FRT-3.4.0-IntaRNA.tgz | tar -zxf - -C /usr/local/user/

# Installing the webapp
RUN wget -qO- http://rna.informatik.uni-freiburg.de/Docker-deploy/FRT/3.4.0/FRT-3.4.0.tgz | tar -zxf - -C /var/lib/tomcat7/webapps/

RUN rm /var/lib/tomcat7/webapps/ROOT -rf
RUN ln -s /var/lib/tomcat7/webapps/FRT-3.4.0/ /var/lib/tomcat7/webapps/ROOT

RUN Rscript -e 'install.packages("evir", dependencies=TRUE, repos="http://cran.us.r-project.org")'
RUN Rscript -e 'install.packages("seqinr", dependencies=TRUE, repos="http://cran.us.r-project.org")'

RUN useradd bisge001 --create-home
RUN adduser bisge001 sudo
RUN adduser bisge001 tomcat7
RUN mkdir -p /FRT-3.4.0/results/
RUN chmod a+rwx /FRT-3.4.0/ -R
RUN chown bisge001:bisge001 /FRT-3.4.0/ -R

RUN echo 'tomcat7	ALL=(bisge001)	NOPASSWD: ALL' >> /etc/sudoers

ADD exec_host /exec_host
# Set maximum of available memory - this is avaiable memory - 1GB
RUN sed -i "s|complex_values        NONE|complex_values        h_vmem=`grep 'MemTotal' /proc/meminfo | awk '{print ($2 - 1000000)}'`k|g" /exec_host

ADD host_group_entry /host_group_entry
ADD queue /queue

USER root
# Expose port 8080 to the host
EXPOSE :8080

ADD run.sh /root/run.sh
RUN chmod +x /root/run.sh

# trick to execute startup commands and run the bash without exiting
CMD bash -C '/root/run.sh';'bash'
