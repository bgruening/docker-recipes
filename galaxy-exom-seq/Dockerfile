# Galaxy - Exom Sequencing Pipeline
#
# VERSION       0.1

FROM galaxy

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

ENV GALAXY_CONFIG_BRAND Exom Sequencing Pipeline

WORKDIR /galaxy-central
ADD ./install_repo_wrapper.sh /galaxy-central/install_repo_wrapper.sh
RUN chmod +x ./install_repo_wrapper.sh


# Install GATK2, samtools and 
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name gatk2 --panel-section-name GATK2"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name suite_samtools_0_1_19 --panel-section-name SAMTools"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name freebayes --panel-section-name Freebayes"

# Bowtie & FASTQC
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bowtie2 --panel-section-name Mapping"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name fastqc --panel-section-name QualityControl"

RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_pysam_0_7_7"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name package_libpng_1_6_7"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_freetype_2_4"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_numpy_1_7"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_scipy_0_12"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_matplotlib_1_2"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_bx_python_12_2013"



RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name deeptools --panel-section-name deepTools"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name data_manager_bwa_index_builder"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o devteam --name bwa_wrappers --panel-section-name Mapping"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o crs4 --name bwa_mem  --panel-section-name Mapping"


RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name vt_variant_tools --panel-section-name VCFtools"

RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o anton --name suite_vcflib_tools_2_0 --panel-section-name VCFtools"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name snpeff --panel-section-name SNPEff"

# Install GEMINI and BED tools
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_tabix_0_2_6"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_bedtools_2_19"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_grabix_0_1_3"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name package_gemini_0_10_0"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name data_manager_gemini_database_downloader"
RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o iuc --name gemini --panel-section-name VariantSelection"
RUN ./install_repo_wrapper.sh \
    "--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name bedtools --panel-section-name BEDtools"

RUN ./install_repo_wrapper.sh \
    "--url http://toolshed.g2.bx.psu.edu/ -o crs4 --name kggseq_variant_selection --panel-section-name VariantSelection"


# Mark one folders as imported from the host.
VOLUME ["/export/"]

# Expose port 80 to the host
EXPOSE :80

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
