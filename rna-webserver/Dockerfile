# RNA - webserver
#
# VERSION       0.1

FROM debian:wheezy

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

# make sure the package repository is up to date
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update


RUN apt-get update
RUN apt-get install -y openjdk-7-jre tomcat7
RUN apt-get install -y gridengine-client gridengine-master


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :8080


ADD run.sh /root/run.sh
RUN chmod +x /root/run.sh


CMD ["/root/run.sh"]
