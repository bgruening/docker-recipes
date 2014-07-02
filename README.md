various Dockerfiles for Bio- & Cheminformatics
==============================================

A collection of Chem- & Bioinformatic related Dockerfiles.

- Galaxy-stable: Base [Galaxy](http://www.galaxyproject.org) Image to provide the infrastructure for other projects. It contains a full-fledged Galaxy instance with [Apach2](http://httpd.apache.org/), [PostgreSQL](http://www.postgresql.org/) and a mechanism to save all data to the host system
- Galaxy-chemicaltoolbox: [ChemicalToolBox](https://github.com/bgruening/galaxytools/tree/master/chemicaltoolbox) Image, based on the Galaxy-stable Image with ChemicalToolBox installed
- Galaxy-deepTools: deepTools Image, based on the Galaxy-stable Image with [deepTools](http://deeptools.github.io/) installed
- CopraRNA: A tool for sRNA target prediction from Patrick R. Wright (Bioinformatic Group in Freiburg)
- Galaxy-docker: Proof of principal for running docker in galaxy in docker.

A detailed description can be found in the project specific readme files.


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
