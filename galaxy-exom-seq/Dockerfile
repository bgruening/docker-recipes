# Galaxy - Exom Sequencing Pipeline

FROM bgruening/galaxy-ngs-preprocessing

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Exom Sequencing Pipeline

# Enable TTS installation
# RUN add-tool-shed --url 'http://testtoolshed.g2.bx.psu.edu/' --name 'Test Tool Shed'


# Install GATK2, samtools and 
RUN install-repository \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name gatk2 --panel-section-name GATK2" \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name suite_samtools_0_1_19 --panel-section-name SAMTools" \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name freebayes --panel-section-name Freebayes"

RUN install-repository \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_pysam_0_7_7" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_scipy_0_12" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_matplotlib_1_2" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_bx_python_12_2013"

RUN install-repository \
    "--url https://toolshed.g2.bx.psu.edu/ --name variant_select --owner devteam"\
    "--url https://toolshed.g2.bx.psu.edu/ --name variant_filtration --owner devteam"

RUN install-repository \
    "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name deeptools --panel-section-name deepTools" \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name data_manager_bwa_index_builder" \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bwa_wrappers --panel-section-name Mapping" \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bwa  --panel-section-name Mapping"


RUN install-repository \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name vt_variant_tools --panel-section-name VCFtools" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name suite_vcflib_tools_2_0 --panel-section-name VCFtools" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name snpeff --panel-section-name SNPEff"

# Install GEMINI and BED tools
RUN install-repository \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_tabix_0_2_6" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_bedtools_2_19" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_grabix_0_1_3" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_gemini_0_10_0" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name data_manager_gemini_database_downloader" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name gemini --panel-section-name VariantSelection" \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name bedtools --panel-section-name BEDtools"

# RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o crs4 --name kggseq_variant_selection --panel-section-name VariantSelection"


# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
