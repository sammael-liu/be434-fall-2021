#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-11-21
Purpose: Python grep
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.files:
        for line in fh:
            if args.insensitive:
                if re.search(args.pattern, line, re.I) is not None:
                    if len(args.files) > 1:
                        print(f'{fh.name}:{line}', end='', file=args.outfile)
                    else:
                        print(line, end='', file=args.outfile)
            else:
                if re.search(args.pattern, line) is not None:
                    if len(args.files) > 1:
                        print(f'{fh.name}:{line}', end='', file=args.outfile)
                    else:
                        print(line, end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
