# CopraRNA 1.2.7
#
# VERSION       0.1

FROM ubuntu:12.04
MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN echo "deb http://archive.ubuntu.com/ubuntu precise multiverse" >> /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update

RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y blast2
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y r-base-core
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y cpanminus
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y bioperl
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y liblist-moreutils-perl
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libparallel-forkmanager-perl
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libgetopt-long-descriptive-perl
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libsoap-lite-perl
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y libhttp-cookies-perl
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y emboss
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y clustalw
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y embassy-phylip
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y imagemagick
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y lftp
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y wget
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y gfortran
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y tcl-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y python2.7

RUN Rscript -e 'install.packages("evir", dependencies=TRUE, repos="http://cran.us.r-project.org")'
RUN Rscript -e 'install.packages("seqinr", dependencies=TRUE, repos="http://cran.us.r-project.org")'

RUN mkdir coprarna
WORKDIR coprarna

RUN wget http://search.cpan.org/CPAN/authors/id/F/FA/FANGLY/Statistics-R-0.26.tar.gz
RUN cpanm Statistics-R-0.26.tar.gz
RUN rm Statistics-R-0.26.tar.gz

# Install ViennaRNA
RUN wget http://www.tbi.univie.ac.at/RNA/ViennaRNA-1.8.5.tar.gz
RUN tar -zxvf ViennaRNA-1.8.5.tar.gz
RUN rm ViennaRNA-1.8.5.tar.gz
RUN cd ViennaRNA-1.8.5 && ./configure && make && make install

# Install IntaRNA
RUN wget http://www.bioinf.uni-freiburg.de/Software/IntaRNA/intarna-1.2.5.tar.gz
RUN tar -zxvf intarna-1.2.5.tar.gz
RUN rm intarna-1.2.5.tar.gz
RUN cd intarna-1.2.5 && ./configure && make && make install

ADD coprarna_1.2.7.tar.bz2 /coprarna/
ADD run_coprarna.py /coprarna/
RUN chmod +x /coprarna/run_coprarna.py

# link the coprarna main program to /coprarna/ ... the python wrapper assumes the executable under /coprarna/homology_intaRNA.pl
RUN ln -s /coprarna/1.2.7/homology_intaRNA.pl /coprarna/homology_intaRNA.pl

ENTRYPOINT ["/coprarna/run_coprarna.py"]

# Cleanup
RUN DEBIAN_FRONTEND=noninteractive apt-get purge -y build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get purge -y gfortran
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

