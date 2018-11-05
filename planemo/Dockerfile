# planemo
#
# VERSION       0.1.0

FROM bgruening/galaxy-stable:18.05

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && apt-get install --no-install-recommends -y python-pip && \
    pip install git+https://github.com/galaxyproject/planemo.git && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV GALAXY_TEST_UPLOAD_ASYNC false
ENV GALAXY_TEST_DEFAULT_INTERACTOR api
ENV GALAXY_TEST_PORT 7777

WORKDIR /galaxy-central
ENTRYPOINT ["planemo"]
CMD ["--help"]
