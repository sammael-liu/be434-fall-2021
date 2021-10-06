#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-10-04
Purpose: Translate DNA/RNA
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence', metavar='str', help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        codon_table[line.rstrip().split()[0]] = line.rstrip().split()[1]
    k = 3
    seq = args.sequence
    protein = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        protein += codon_table.get(codon.upper(), '-')

    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
