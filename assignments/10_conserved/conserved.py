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

    lines = []
    for line in args.file:
        lines.append(line.split())
        print(line, end='')

    reference = ''.join(lines[0])

    all_result = []
    for comp in lines[1:]:
        result = ''
        for i, loc in enumerate(reference):
            if loc == ''.join(comp)[i]:
                result += '|'
            else:
                result += 'X'
        all_result.append(result)

    if len(lines) == 2:
        print(result)

    if len(lines) == 3:
        result3 = ''
        for j, loc3 in enumerate(''.join(all_result[0])):
            if loc3 == ''.join(all_result[1])[j]:
                result3 += loc3
            else:
                result3 += 'X'
        print(result3)


# --------------------------------------------------
if __name__ == '__main__':
    main()
