various Dockerfiles for Bio- & Cheminformatics
==============================================

A collection of Chem- & Bioinformatic related Dockerfiles.

- Galaxy-stable: Base [Galaxy](http://www.galaxyproject.org) Image to provide the infrastructure for other projects. It contains a full-fledged Galaxy instance with [Apach2](http://httpd.apache.org/), [PostgreSQL](http://www.postgresql.org/) and a mechanism to save all data to the host system
- Galaxy-chemicaltoolbox: [ChemicalToolBox](https://github.com/bgruening/galaxytools/tree/master/chemicaltoolbox) Image, based on the Galaxy-stable Image with ChemicalToolBox installed
- Galaxy-deepTools: deepTools Image, based on the Galaxy-stable Image with [deepTools](http://deeptools.github.io/) installed

A detailed description can be found in the project specific readme files.
