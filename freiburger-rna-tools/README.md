Freiburger RNA Tools - Webserver
================================

This Docker Image provides an offline version of the [Freiburger RNA Tools webserver](http://rna.informatik.uni-freiburg.de/). It is a stripped down version of the original webserver, suited for offline lecturing or confidential data.

For the webserver please cite the following general publication. In concert with the tool specific citations in the webserver help pages.

Freiburg RNA Tools: a web server integrating INTARNA, EXPARNA and LOCARNA.
Smith C, Heyne S, Richter AS, Will S, Backofen R. ([doi: 10.1093/nar/gkq316](http://www.ncbi.nlm.nih.gov/pubmed/20444875))


Available Tools
===============

 * LocARNA
 * IntaRNA
 * CARNA
 * ExpaRNA

How to run the container
===========

To have the SGE server accessible,  hostname "frtwebserver" must be passed to the docker client with option -h

e.g.

    docker run -t -h frtwebserver -i imagename
    
If you want to watch the server output please run:

    $ tail -f /var/log/tomcat7/catalina.out

Limitations
===========

 * sending notifications and error reports is not possible
 * parallel environments are currently not configured

 

Authors
=======

 * Bjoern Gruening
 * Martin Mann


History
=======

- v3.4.0: Initial public release with webserver version 3.4.0



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
