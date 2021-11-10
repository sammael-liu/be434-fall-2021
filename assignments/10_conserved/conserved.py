#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-11-08
Purpose: Find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    seqs = []
    for line in args.file:
        seqs.extend(line.split())
        print(line, end='')

    check = ''
    for i in range(len(seqs[0])):
        bases = []
        for seq in seqs:
            bases += seq[i]

        check += '|' if all(element == bases[0] for element in bases) else 'X'
    print(check)


# --------------------------------------------------
if __name__ == '__main__':
    main()
