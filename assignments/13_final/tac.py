#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-12-02
Purpose: Python clone of tac
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python clone of tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.files:
        for line in reversed(list(fh)):
            print(line.rstrip(), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
