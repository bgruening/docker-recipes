#!/bin/bash

/etc/init.d/gridengine-master start
/etc/init.d/gridengine-exec start
sudo -u sgeadmin qconf -am bisge001
sudo -u bisge001 qconf -au bisge001 users
sudo -u bisge001 qconf -Ae /exec_host
sudo -u bisge001 qconf -Ahgrp /host_group_entry
sudo -u bisge001 qconf -aattr hostgroup hostlist frtwebserver @allhosts
sudo -u bisge001 qconf -Aq /queue
sudo -u bisge001 qconf -aattr queue hostlist @allhosts main.q
sudo -u bisge001 qconf -as frtwebserver

/etc/init.d/tomcat7 start

# The container will run as long as the script is running, that's why
# we need something long-lived here
exec tail -f /var/log/tomcat7/catalina.out
