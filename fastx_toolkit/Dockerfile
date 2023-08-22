FROM perl:stable-slim-bullseye

# Binaries from EU from 2014
COPY binaries/* /usr/local/bin/

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    apt-get install --no-install-recommends -y libperlio-gzip-perl libgd-graph-perl && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*





