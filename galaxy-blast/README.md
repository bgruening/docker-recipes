Galaxy Image for the BLAST+ suite
=================================

A complete and production ready Galaxy instance with installed BLAST+ tools.

 * [Installed tools](#installed-tools)
 * [Usage](#usage)
 * [Users & Passwords](#user--passowrds)
 * [Reproducibility of your search results](#reproducibility-of-your-search-results)
 * [Using large extern BLAST databases](#using-large-extern-blast-databases)
 * [Requirements](#requirements)
 * [Restarting Galaxy](#restarting-galaxy)
 * [History](#history)
 * [Support & Bug Reports](#support--bug-reports)
 * [Licence (MIT)](#license-mit)


Installed tools
===============

 * [BLAST+](http://blast.ncbi.nlm.nih.gov)

Usage
=====

At first you need to install docker. Please follow the instruction on https://docs.docker.com/installation/

After the successful installation, all what you need to do is:

```bash
docker run -d -p 8080:80 bgruening/galaxy-blast
```

I will shortly explain the meaning of all the parameters. For a more detailed describtion please consult the [docker manual](http://docs.docker.io/), it's really worth reading.

Let's start: ``docker run`` will run the Image/Container for you. In case you do not have the Container stored locally, docker will download it for you. ``-p 8080:80`` will make the port 80 (inside of the container) available on port 8080 on your host. Inside the container a Apache Webserver is running on port 80 and that port can be bound to a local port on your host computer. With this parameter you can access your Galaxy instance via ``http://localhost:8080`` immediately after executing the command above. ``bgruening/galaxy-blast`` is the Image/Container name, that directs docker to the correct path in the [docker index](https://index.docker.io/u/bgruening/galaxy-stable/). ``-d`` will start the docker container in daemon mode. For an interactive session, you can execute:

```bash
docker run -i -t -p 8080:80 bgruening/galaxy-blast
```

and run the ``` startup ``` script by your own, to start PostgreSQL, Apache and Galaxy.

Docker images are "read-only", all your changes inside one session will be lost after restart. This mode is usefull to present Galaxy to your collegues or to run workshops with it. To install Tool Shed respositories or to save your data you need to export the calculated data to the host computer.

Fortunately, this is as easy as:

```bash
docker run -d -p 8080:80 -v /home/user/galaxy_storage/:/export/ bgruening/galaxy-blast
```

With the additional ``-v /home/user/galaxy_storage/:/export/`` parameter, docker will mount the folder ``/home/user/galaxy_storage`` into the Container under ``/export/``. A ``startup.sh`` script, that is usually starting Apache, PostgreSQL and Galaxy, will recognise the export directory with one of the following outcomes:

  - In case of an empty ``/export/`` directory, it will move the [PostgreSQL](http://www.postgresql.org/) database, the Galaxy database directory, Shed Tools and Tool Dependencies and various config scripts to /export/ and symlink back to the original location.
  - In case of a non-empty ``/export/``, for example if you continue a previouse session within the same folder, nothing will be moved, but the symlinks will be created.

This enables you to have different export folders for different sessions - means real separation of your different projects.


Users & Passwords
================

The Galaxy Admin User has the username ``admin@galaxy.org`` and the password ``admin``.
The PostgreSQL username is ``galaxy``, the password is ``galaxy`` and the database name is ``galaxy`` (I know I was really creative ;)).
If you want to create new users, please make sure to use the ``/export/`` volume. Otherwise your user will be removed after your docker session is finished.


Reproducibility of your search results
======================================

BLAST databases are updated daily and are not versioned. This is a general problem for reproducibility of search results.
In Galaxy we track the program version, all settings and the input files. The underlying database can be tracked but this is usually 
very storage expensive. Note that the large NCBI BLAST databases exceeds 100 GB in size.
To enable 100% reproducibility you can simply create your own BLAST datbase with Galaxy. Download your database as FASTA file
and use the tool `NCBI BLAST+ makeblastdb` to convert your FASTA file to a proper BLAST database. These steps are reproducibly, with all settings and inputs.

If you want to use the precalculated BLAST databases from the [NCBI FTP server](ftp://ftp.ncbi.nlm.nih.gov/blast/db/) you can
configure your BLAST Galaxy instance to use those. Please have a look at [Using large extern BLAST databases](#large_databases). We have plans to make this a lot simples by using Galaxy *data managers*. You can track to progess here: https://github.com/peterjc/galaxy_blast/issues/22

Please understand that we cannot ship the NCBI BLAST databases by default in this Docker container, as we try to keep the image as small as possible.


Using large extern BLAST databases
==================================

You can get BLAST databases directly from the [NCBI server](ftp://ftp.ncbi.nlm.nih.gov/blast/db/) and include them into your Galaxy docker container.

 - Download your databases from [ftp://ftp.ncbi.nlm.nih.gov/blast/db/](ftp://ftp.ncbi.nlm.nih.gov/blast/db/).
   You can use the NCBI suggested [perl script](http://www.ncbi.nlm.nih.gov/blast/docs/update_blastdb.pl) to automatize this step.
 - Store all your BLAST databases in one directory, for example `/galaxy_store/data/blast_databases/`
 - Start your Galaxy container with `-v /galaxy_store/data/blast_databases/:/data/` to have access your databases inside of your container
 - Start your Galaxy container with ``-v /home/user/galaxy_storage/:/export/`` to export all config files to your host operating system
 - Modify your blast*.loc files under `/home/user/galaxy_storage/galaxy-central/tool-data/blast*.loc` on your host, or under `/export/galaxy-central/tool-data/blast*.loc` from within your container.
 - You need to add the paths to your blast databases. They need to look like `/export/swissprot/swissprot`
 - Restart your Galaxy instance, for example with ```docker exec <container name> supervisorctl restart galaxy:```

From now on you should see predifined BLAST databases in your Galaxy User Interface if you choose `Locally installed BLAST database`.


Requirements
============

- [docker](https://docs.docker.com/installation/)


Restarting Galaxy
=================

If you want to restart Galaxy without restarting the entire Galaxy container we can use `docker exec` (docker > 1.3).

```docker exec <container name> supervisorctl restart galaxy:```


History
=======

 - 0.1: Initial release!


Support & Bug Reports
=====================

For support, questions, or feature requests contact bjoern.gruening@gmail.com or fill bug reports at https://github.com/bgruening/galaxy_recipes/issues.


Licence (MIT)
=============

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
