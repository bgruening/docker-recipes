CopraRNA Docker Image
=====================

CopraRNA is a tool for sRNA target prediction.

It computes whole genome predictions by combination of distinct whole genome IntaRNA predictions. As input, CopraRNA requires 
at least 3 homologous sRNA sequences from 3 distinct organisms in FASTA format. 
Furthermore each organisms' genome has to be part of the NCBI Reference Sequence 
(RefSeq) database (i.e. it should have exactly this format NC_XXXXXX where X stands for a digit between 0 and 9). 
Depending on sequence length (target and sRNA), amount of input organisms and genome sizes, 
CopraRNA can take up to 24h to compute (in most cases it is significantly faster).

The CopraRNA Webserver can be found here:

http://rna.informatik.uni-freiburg.de/CopraRNA/Input.jsp


Usage
=====

You can use the Docker CopraRNA container with the following command.

```
docker run -v /full/path/to/seq/dir/:/transfer/ bgruening/coprarna --infile /transfer/input_sRNA.fa --upstream --downstream --region --refseq-ids NC_000913 NC_009792 NC_013716 NC_011740 --outdir /transfer/
```

```docker run``` will invoke the preconfigured CopraRNA box and ``` -v /full/path/to/seq/dir/:/transfer/ ``` will mount the host folder (```/full/path/to/seq/dir/```) into the container (``` /transfer/ ```). All arguments behind the container name ```bgruening/coprarna``` are arguments for CopraRNA. ``` --outdir ``` will specify the output directory. It should be the same as your transfer folder, where your input sequence file is stored. In your example it was ``` /tranfer/ ```.


```
docker run bgruening/coprarna --help
```

Will show you the full parameter list.


Requirements
============

- [docker](https://www.docker.io/gettingstarted/#h_installation)


History
=======

 - 0.1: Initial release!


How to cite CopraRNA
====================

-   Patrick R. Wright, Andreas S. Richter, Kai Papenfort, Martin Mann, Jörg Vogel, Wolfgang R. Hess, Rolf Backofen and Jens Georg
    [Comparative genomics boosts target prediction for bacterial small RNAs](http://www.bioinf.uni-freiburg.de//Subpages/publications.html?de#Wright_Richter_Papenfort-Compa_genom_boost-PNAS2013.abstract)
    Proc Natl Acad Sci USA, 2013, 110(37), E3487–E3496.




Bug Reports
===========

You can file an issue here https://github.com/bgruening/docker-recipes/issues.


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
