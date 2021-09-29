#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-09-27
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print(f'     {line_num}\t{line.rstrip()}')
            else:
                print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
