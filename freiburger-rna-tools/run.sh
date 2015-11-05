
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

# set maximum of avaiable CPU's
sed -i "s|processors            4|processors            `num=$(grep ^processor /proc/cpuinfo | wc -l) && echo $((num-1))`|g" /queue
sed -i "s|slots                 4|slots                 `num=$(grep ^processor /proc/cpuinfo | wc -l) && echo $((num-1))`|g" /queue


/etc/init.d/tomcat7 start

# The container will run as long as the script is running, that's why
# It is handled by DockerFile CMD invokation trick