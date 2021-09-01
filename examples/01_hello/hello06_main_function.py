#!/usr/bin/env python3
# Purpose: Say hello

import argparse

def main():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    args = parser.parse_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__': 
    main()
#you can change the main(), ex. run(), but __main__ will still be the same

#use main() instead of line 13 and 14 can also work in the current situation,
#but it is better to have line 13, 14 when using this script as library.
