#!/bin/sh

# We need to start postgresql with the init system and not with supervisor,
# because we need to install into the system wide database. supervisor will try
# to start a database located under /export/
/etc/init.d/postgresql start
/usr/bin/supervisord
sleep 60
python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:9010 --tool-deps --repository-deps $1
exit_code=$?

if [ $exit_code != 0 ] ; then
    exit $exit_code
fi

supervisorctl stop all
/etc/init.d/postgresql stop
