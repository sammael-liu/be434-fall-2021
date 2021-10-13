#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-10-12
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))
    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=[sys.stdout])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    set1 = set(args.file1.read().split())
    set2 = set(args.file2.read().split())
    both = sorted(set1.intersection(set2))
    for word in both:
        if args.outfile != [sys.stdout]:
            print(word, file=args.outfile)
        else:
            print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
