ChemicalToolBox Docker Image
============================

The [ChemicalToolBox](https://github.com/bgruening/galaxytools/tree/master/chemicaltoolbox) (CTB) is a set of tools integrated into the [Galaxy-workflow-management](http://galaxyproject.org) system to enable researchers easy-to-use, reproducible, and transparent access to cheminformatics libraries and drug discovery tools. It includes standard applications for similarity and substructure searches, clustering of compounds, prediction of properties and descriptors, filtering, and many other tools that range from drug-likeness classification to fragmentation and fragment-merging. By combinating the various tools many more powerful applications can be designed.

ChemicalToolBox is based on open-source software, web-accessible, freely available, and easily expandable. It can be downloaded and easily deployed locally or on a large scale cluster.

With the CTB Docker Image we provide a full Galaxy installation with PostgreSQL and Apache. CTB is preinstalled with all dependencies and one example workflow to make it even more easier to install and test the future of large-scale cheminformatics. 


Usage
=====

At first you need to install docker. Please follow the instruction on https://www.docker.io/gettingstarted/#h_installation

After the successful installation, all what you need to do is:

``docker run -d -p 8080:80 -p 8000:8000 bgruening/galaxy-chemicaltoolbox``

I will shortly explain the meaning of all the parameters. For a more detailed describtion please consult the [docker manual](http://docs.docker.io/), it's really worth reading.

Let's start: ``docker run`` will run the Image/Container for you. In case you do not have the Container stored locally, docker will download it for you. ``-p 8080:80`` will make the port 80 (inside of the container) available on port 8080 on your host. Inside the container a Apache Webserver is running on port 80 and that port can be bound to a local port on your host computer. With this parameter you can access your Galaxy instance via ``http://localhost:8080`` immediately after executing the command above. ``bgruening/galaxy-chemicaltoolbox`` is the Image/Container name, that directs docker to the correct path in the [docker index](https://index.docker.io/u/bgruening/galaxy-stable/). ``-d`` will start the docker container in daemon mode. For an interactive session, you can execute:

``docker run -i -t -p 8080:80 -p 8000:8000 bgruening/galaxy-chemicaltoolbox``

and run the ``` startup ``` script by your own, to start PostgreSQL, Apache and Galaxy.

Docker images are "read-only", all your changes inside one session will be lost after restart. This mode is usefull to present Galaxy to your collegues or to run workshops with it. To install Tool Shed respositories or to save your data you need to export the calculated data to the host computer.

Fortunately, this is as easy as:

``docker run -d -p 8080:80 -p 8000:8000 -v /home/user/galaxy_storage/:/export/ bgruening/galaxy-chemicaltoolbox``

With the additional ``-v /home/user/galaxy_storage/:/export/`` parameter, docker will mount the folder ``/home/user/galaxy_storage`` into the Container under ``/export/``. A ``startup.sh`` script, that is usually starting Apache, PostgreSQL and Galaxy, will recognise the export directory with one of the following outcomes:

  - In case of an empty ``/export/`` directory, it will move the [PostgreSQL](http://www.postgresql.org/) database, the Galaxy database directory, Shed Tools and Tool Dependencies and various config scripts to /export/ and symlink back to the original location.
  - In case of a non-empty ``/export/``, for example if you continue a previouse session within the same folder, nothing will be moved, but the symlinks will be created.

This enables you to have different export folders for different sessions - means real separation of your different projects.


Users & Passwords
================

The Galaxy Admin User has the username ``admin@galaxy.org`` and the password ``admin``.
The PostgreSQL username is ``galaxy``, the password is ``galaxy`` and the database name is ``galaxy`` (I know I was really creative ;)).
If you want to create new users, please make sure to use the ``/export/`` volume. Otherwise your user will be removed after your docker session is finished.


Requirements
============

- [docker](https://www.docker.io/gettingstarted/#h_installation)


History
=======

 - 0.1: Initial release!


Support & Bug Reports
=====================

You can file an issue here https://github.com/bgruening/galaxy_recipes/issues or ask
us on the Galaxy development list http://lists.bx.psu.edu/listinfo/galaxy-dev


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
