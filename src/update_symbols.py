#!/usr/bin/env python

import argparse
from gene_list_utils import *

# usage: update_symbols.py --hgnc gene_with_protein_product.txt < raw_list.tsv > updated_list.tsv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get current HGNC symbols for a possibly-outdated list of gene symbols. Also removes dups.')
    parser.add_argument('--hgnc', dest='hgnc', action='store',
                        help='Path to the file "gene_with_protein_product.txt" downloaded from HGNC', type=str)
    args = parser.parse_args()
    hgnc = parse_hgnc(args.hgnc,mode='update')
    current_symbols = set()
    for line in sys.stdin.readlines():
        old_symbol = line.strip()
        if old_symbol in hgnc:
            current_symbols.add(hgnc[old_symbol])
    for symbol in sorted(current_symbols):
        sys.stdout.write(symbol + '\n')
