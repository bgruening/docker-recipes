#!/usr/bin/env python

"""
    Add a convenient commandline interface to CopraRNA.
"""

import os
import sys
import argparse
import subprocess

def main( args ):
    """
        Run CopraRNA in its own directory.
    """

    cmd = "/coprarna/homology_intaRNA.pl %s %s %s %s %s" % (args.infile, args.upstream, args.downstream, args.region, ' '.join(args.refseq_ids))
    subprocess.call( cmd, shell=True, cwd=args.outdir )

class IntRange( object ):
    def __init__(self, start, stop):
        self.start, self.stop = start, stop

    def __call__(self, value):
        value = int(value)
        if value < self.start or value > self.stop:
            raise argparse.ArgumentTypeError('Value outside of range [%s - %s].' % (self.start, self.stop))
        return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser("CopraRNA: a tool for sRNA target prediction.")

    parser.add_argument('-i', '--infile', required=True,
        help="Specify sRNA's in FASTA format")
    parser.add_argument('-u', '--upstream', type=IntRange(1, 3000), required=True,
        help="This parameter specifies the number of nucleotides (nt) upstream of your start or stop codon (depending which one you selected). If you selected start codon, and have prior knowledge about average 5'UTR lengths in your input organisms then it is sensible to set nt up to this number in order to increase prediction quality. The sum of nt up and nt down must be at least 140.")

    parser.add_argument('-d', '--downstream', type=IntRange(1, 3000), required=True,
        help="This parameter specifies the number of nucleotides (nt) downstream of your start or stop codon (depending which one you selected). If you selected stop codon, and have prior knowledge about average 3'UTR lengths in your input organisms then it is sensible to set nt down to this number in order to increase prediction quality. The sum of nt up and nt down must be at least 140.")

    parser.add_argument('-r', '--region', choices=['5utr', '3utr', 'cds'], required=True,)
    parser.add_argument('-q', '--refseq-ids', dest="refseq_ids", nargs='*', required=True,
        help="RefSeq IDs")

    parser.add_argument('-o', '--outdir', help="Output directory")
    args = parser.parse_args()
    main( args )

