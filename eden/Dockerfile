# EDeN Docker container
#
# VERSION       0.1.0

FROM ubuntu:14.04

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com and Fabrizio Costa

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && apt-get install --no-install-recommends -y apt-transport-https \
    python-dev libc-dev python-pip gfortran libfreetype6-dev libpng-dev python-openbabel pkg-config \
    build-essential libblas-dev liblapack-dev git-core wget software-properties-common python-pygraphviz && \
    add-apt-repository ppa:bibi-help/bibitools && add-apt-repository ppa:j-4/vienna-rna && \
    apt-get -qq update && \
    apt-get install --no-install-recommends -y rnashapes vienna-rna &&\
    pip install distribute --upgrade && \
    pip install numpy biopython scipy matplotlib scikit-learn pandas \
        sklearn-pandas dill networkx && \
    apt-get remove -y --purge libzmq-dev python-dev software-properties-common libc-dev build-essential libreadline-dev && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN git clone https://github.com/fabriziocosta/pyEDeN.git

ENV PYTHONPATH $PYTHONPATH:/pyEDeN/
ENV PATH $PATH:/pyEDeN/eden/bin/

WORKDIR /pyEDeN/eden/bin/
ENTRYPOINT [""]
