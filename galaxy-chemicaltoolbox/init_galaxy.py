from scripts.db_shell import *
from galaxy.util.bunch import Bunch
from galaxy.security import GalaxyRBACAgent
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
import argparse
bunch = Bunch( **globals() )
engine = create_engine('postgres://galaxy:galaxy@localhost:5432/galaxy')
bunch.session = sessionmaker(bind=engine)
# For backward compatibility with "model.context.current"
bunch.context = sessionmaker(bind=engine)

security_agent = GalaxyRBACAgent( bunch )
security_agent.sa_session = sa_session
import sys
import os
import shutil
import subprocess

PG_DATA_DIR_DEFAULT = "/var/lib/postgresql/9.1/main"
PG_DATA_DIR_HOST = "/var/lib/postgresql/9.1/main_host"
PG_BIN = "/usr/lib/postgresql/9.1/bin/"
PG_CONF = '/etc/postgresql/9.1/main/postgresql.conf'

def add_user(email, password, key=None):
    """
        Add Galaxy User.
        From https://gist.github.com/jmchilton/4475646
    """
    query = sa_session.query( User ).filter_by( email=email )
    if query.count() > 0:
        return query.first()
    else:
        user = User(email)
        user.set_password_cleartext(password)
        sa_session.add(user)
        sa_session.flush()

        security_agent.create_private_user_role( user )
        if not user.default_permissions:
            security_agent.user_set_default_permissions( user, history=True, dataset=True )

        if key is not None:
            api_key = APIKeys()
            api_key.user_id = user.id
            api_key.key = key
            sa_session.add(api_key)
            sa_session.flush()
        return user

def pg_ctl( database_path, mod = 'start' ):
    """
        Start/Stop PostgreSQL with variable data_directory.
        mod = [start, end, restart, reload]
    """
    new_data_directory = "'%s'" % database_path
    cmd = 'sed -i "s|data_directory = .*|data_directory = %s|g" %s' % (new_data_directory, PG_CONF)
    subprocess.call(cmd, shell=True)
    subprocess.call('service postgresql %s' % (mod), shell=True)

def set_pg_permission( database_path ):
    """
        Set the correct permissions for a newly created PostgreSQL data_directory.
    """
    subprocess.call('chown -R postgres:postgres %s' % database_path, shell=True)
    subprocess.call('chmod -R 700 %s' % database_path, shell=True)

def create_db(user, password, database, database_path):
    """
        Initialize PostgreSQL Database, add database user und create the Galaxy Database.
    """
    if not os.path.exists( database_path ):
        os.makedirs( database_path )
        set_pg_permission( database_path )
        # create new postgres database directory
        subprocess.call('sudo -u postgres %s --auth=trust --pgdata=%s' % (os.path.join(PG_BIN, 'initdb'), database_path), shell=True)

        os.symlink('/etc/ssl/certs/ssl-cert-snakeoil.pem', os.path.join(database_path, 'server.crt'))
        os.symlink('/etc/ssl/private/ssl-cert-snakeoil.key', os.path.join(database_path, 'server.key'))

        pg_ctl( database_path, 'start' )
        password = "'%s'" % ('galaxy')
        subprocess.call( 'sudo -u postgres psql --command "CREATE USER galaxy WITH SUPERUSER PASSWORD %s;"' % (password), shell=True )

        subprocess.call('sudo -u postgres createdb -O %s %s' % (user, database), shell=True)

def _make_dir( directory ):
    if not os.path.exists( directory ):
        os.makedirs( directory )

def change_config_file( config_file_path ):
    """
        #file_path = database/files
        #job_working_directory = database/job_working_directory
        #object_store_cache_path = database/files/
    """
    universe_wsgi_tmp = open('/tmp/universe_wsgi.ini', 'w+')
    _make_dir('/galaxy-central/database_host/files')
    _make_dir('/galaxy-central/database_host/job_working_directory')

    for line in open( config_file_path ):
        if line.startswith('#file_path'):
            universe_wsgi_tmp.write('file_path = database_host/files\n')
        elif line.startswith('#job_working_directory'):
            universe_wsgi_tmp.write('job_working_directory = database_host/job_working_directory\n')
        elif line.startswith('#object_store_cache_path'):
            universe_wsgi_tmp.write('object_store_cache_path = database_host/files\n')
        else:
            universe_wsgi_tmp.write( line )
    universe_wsgi_tmp.close()
    os.unlink( config_file_path )
    shutil.move('/tmp/universe_wsgi.ini', config_file_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Initializing a complete Galaxy Database with Tool Shed Tools.')

    parser.add_argument("--dbuser", required=True,
                    help="Username of the Galaxy Database Administrator. That name will be specified in the universe_wsgi.xml file.")

    parser.add_argument("--dbpassword", required=True,
                    help="Password of the Galaxy Database Administrator. That name will be specified in the universe_wsgi.xml file.")

    parser.add_argument("--db-name", dest='db_name', required=True,
                    help="Galaxy Database name. That name will be specified in the universe_wsgi.xml file.")

    parser.add_argument("--dbpath", default="/var/lib/postgresql/9.1/main_host",
                    help="Galaxy Database path.")

    parser.add_argument("--docker-build", dest='docker_build', action="store_true", default=False,
                    help="If true the database will be build from scratch. That is usually only needed via Dockerfile build.")

    parser.add_argument("--mode", default = 'HOST',
                    help="Define different modes. In 'HOST' mode Docker will export the Galaxy databases to the Host. ")

    parser.add_argument("--guser", required=True,
                    help="Username, it should be an email address.")

    parser.add_argument("--gpassword", required=True,
                    help="Password.")

    parser.add_argument("--gkey", help="API-Key.")

    options = parser.parse_args()

    if options.docker_build:
        """
            Initialize the Galaxy Database, add a User and Install packages from the Tool Shed.
            This database is the default one, created by the Dockerfile. 
            The user can set GALAXY_DOCKER_MODE=HOST to get a persistent database.
        """
        database_path = PG_DATA_DIR_DEFAULT
        create_db(options.dbuser, options.dbpassword, options.db_name, database_path)
        # start Galaxy and create the database tables
        subprocess.call('./create_db.sh', cwd="/galaxy-central/", shell=True)
        subprocess.call('./run.sh --daemon', cwd="/galaxy-central/", shell=True)
        # wait until Galaxy ist started
        subprocess.call(['sleep', '60'])
        add_user(options.guser, options.gpassword, options.gkey)

        # Install from Tool Shed
        cmd = 'python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:8080 --url http://toolshed.g2.bx.psu.edu/ -o bgruening -r b223268cc050 --name chemicaltoolbox --tool-deps --repository-deps --panel-section-name ChemicalToolBox'
        subprocess.call(cmd, cwd="/galaxy-central/", shell=True)
        pg_ctl( database_path, 'stop' )
    else:
        if options.mode.lower() == 'host':
            database_path = PG_DATA_DIR_HOST
            change_config_file( '/galaxy-central/universe_wsgi.ini' )
        else:
            database_path = PG_DATA_DIR_DEFAULT
        if 'PG_VERSION' not in os.listdir( database_path ):
            # User given dbpath, usually a directory from the host machine
            # copy the postgresql data folder to the new location
            subprocess.call('cp -R %s/* %s' % (PG_DATA_DIR_DEFAULT, database_path), shell=True)
            # copytree needs an non-existing dst dir, how annoying :(
            #shutil.copytree(PG_DATA_DIR_DEFAULT, PG_DATA_DIR_HOST)
            set_pg_permission( database_path )

    pg_ctl( database_path, 'start' )
