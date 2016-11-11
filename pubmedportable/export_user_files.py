import sys
import os
import shutil
import subprocess

PG_DATA_DIR_DEFAULT = sys.argv[1] or "/var/lib/postgresql/9.1/main"
PG_DATA_DIR_HOST = "/export/postgresql/9.1/main/"
PG_CONF = '/etc/postgresql/9.1/main/postgresql.conf'

if __name__ == "__main__":
    """
        If the '/export/' folder exist, meaning docker was started with '-v /home/foo/bar:/export',
        we will link every file that needs to persist to the host system. Addionaly a file (/.pubmed2go_save) is
        created that indicates all linking is already done.
        If the user re-starts (with docker start) the container the file /.pubmed2go_save is found and the linking
        is aborted.
    """
    if os.path.exists('/export/') and not os.path.exists('/export/.pubmed2go_save'):
        if not os.path.exists( PG_DATA_DIR_HOST ) or 'PG_VERSION' not in os.listdir( PG_DATA_DIR_HOST ):
            dest_dir = os.path.dirname( PG_DATA_DIR_HOST )
            if not os.path.exists( dest_dir ):
                os.makedirs(dest_dir)
            # User given dbpath, usually a directory from the host machine
            # copy the postgresql data folder to the new location
            subprocess.call('cp -R %s/* %s' % (PG_DATA_DIR_DEFAULT, PG_DATA_DIR_HOST), shell=True)
            # copytree needs an non-existing dst dir, how annoying :(
            #shutil.copytree(PG_DATA_DIR_DEFAULT, PG_DATA_DIR_HOST)
            subprocess.call('chown -R postgres:postgres /export/postgresql/', shell=True)
            subprocess.call('chmod -R 0755 /export/', shell=True)
            subprocess.call('chmod -R 0700 %s' % PG_DATA_DIR_HOST, shell=True)
    # change data_directory of PostgreSQL to the new location
    new_data_directory = "'%s'" % PG_DATA_DIR_HOST
    cmd = 'sed -i "s|data_directory = .*|data_directory = %s|g" %s' % (new_data_directory, PG_CONF)
    subprocess.call(cmd, shell=True)
