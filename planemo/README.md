Galaxy planemo Docker Image
===========================

Command-line utilities to assist in developing tools for the Galaxy project.

https://github.com/galaxyproject/planemo

Usage
=====

At first you need to install docker. Please follow the instruction on https://docs.docker.com/installation/

After the successful installation, all what you need to do is:

``docker run -v `pwd`:/export planemo lint /export/filtering.xml``

More information about planemo can be found on [github](https://github.com/galaxyproject/planemo) or the offical [planemo documentation](https://planemo.readthedocs.org.). Furthermore, you can run the following command to get command line help.

``docker run planemo``

