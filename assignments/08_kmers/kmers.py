#!/usr/bin/env python3
"""
Author : wliu <wliu@localhost>
Date   : 2021-10-25
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
def count_kmers(infile, kmers):
    """ Count k-mers in string """

    words = {}

    for line in infile:
        for word in line.split():
            for kmer in find_kmers(word, kmers):
                if kmer in words:
                    words[kmer] += 1
                else:
                    words[kmer] = 1
    return words


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words1 = count_kmers(args.file1, args.kmer)
    words2 = count_kmers(args.file2, args.kmer)

    common = sorted(set(words1) & set(words2))
    for n in common:
        print(f'{n:<10}{words1.get(n):>6}{words2.get(n):>6}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
