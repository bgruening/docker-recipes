# IPython notebook Image for use with the Galaxy IPython Interactive Environment
# This Image will contain a few additional libraries used for workshops.
# The content will change a lot so not rely on this image. Take it as inspiration
# to create your own.
#
# VERSION       0.1

FROM bgruening / docker-ipython-notebook

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN pip install git+https://github.com/bgruening/EDeN.git

#RUN apt-get -qq update && apt-get install --no-install-recommends -y apt-transport-https \
#    libzmq1 libzmq-dev python-dev libc-dev pandoc python-pip \
#    build-essential libblas-dev liblapack-dev gfortran \
#    libfreetype6-dev libpng-dev net-tools procps \
#    r-base libreadline-dev && \
#    pip install distribute --upgrade && \
#    pip install pyzmq ipython==2.3 jinja2 tornado pygments numpy biopython scikit-learn pandas \
#        scipy sklearn-pandas bioblend matplotlib patsy pysam khmer dendropy ggplot mpld3 sympy rpy2 && \
#    apt-get remove -y --purge libzmq-dev python-dev libc-dev build-essential binutils gfortran libreadline-dev && \
#    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

