#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-09-12
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int',
                        metavar='INT',
                        nargs='+',
                        type=int,
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    int_arg = args.int
    num = len(int_arg)

    if num == 1:
        print(f'{int_arg[0]} = {int_arg[0]}')
    else:
        int_to_string = [str(int) for int in int_arg]
        left = ' + '.join(int_to_string)
        right = sum(int_arg)
        print(f'{left} = {right}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
