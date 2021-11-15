#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-11-13
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', help='DNA text or file', metavar='str')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    """ Create RLE """
    encoding = ''

    for i, base in enumerate(seq):
        if i == 0:
            prev_base = base
            count = 1
        else:
            if base != prev_base:
                if count == 1:
                    encoding += prev_base
                else:
                    encoding += prev_base + str(count)
                count = 1
                prev_base = base
            else:
                count += 1
    if count == 1:
        encoding += prev_base
    else:
        encoding += prev_base + str(count)
    return encoding


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
