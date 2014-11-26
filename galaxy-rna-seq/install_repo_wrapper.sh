#!/bin/sh

service postgresql start
service apache2 start
./run.sh --daemon

sleep 60
python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:8080 --tool-deps --repository-deps $1
exit_code=$?

if [ $exit_code != 0 ] ; then
    exit $exit_code
fi

./run.sh --stop-daemon
service postgresql stop
service apache2 stop
