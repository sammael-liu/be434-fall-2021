#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-11-01
Purpose: Split interleaved/paired reads
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        basename = os.path.basename(fh.name)
        root, ext = os.path.splitext(basename)
        if not os.path.exists(args.outdir):
            os.makedirs(args.outdir)
        ind = 0
        with open(os.path.join(args.outdir, root + '_1' + ext),
                  'wt',
                  encoding='utf8') as out1:
            with open(os.path.join(args.outdir, root + '_2' + ext),
                      'wt',
                      encoding='utf8') as out2:
                for rec in SeqIO.parse(fh.name, 'fasta'):
                    ind += 1
                    if ind % 2 == 1:
                        out1.write(">" + rec.description + "\n" +
                                   str(rec.seq) + "\n")
                    else:
                        out2.write(">" + rec.description + "\n" +
                                   str(rec.seq) + "\n")
    print(f'Done, see output in "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
