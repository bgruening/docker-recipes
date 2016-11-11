#!/bin/bash

cd /PubMed2Go/
# If /export/ is mounted, export_user_files file moving all data to /export/
# symlinks will point from the original location to the new path under /export/
# If /export/ is not given, nothing will happen in that step
python ./export_user_files.py $PG_DATA_DIR_DEFAULT
service postgresql start

if [ ! -f /export/.pubmed2go_save ]; then
    python PubMedParser.py -i /export/import_data/ -d pubmed -p 4
    cd full_text_index
    python RunXapian.py --xapian_database_path /export/ --index --db_psql pubmed --no_search
fi

touch /export/.pubmed2go_save

tail -f /var/log/postgresql/postgresql-9.1-main.log
