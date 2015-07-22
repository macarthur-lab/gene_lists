#!/bin/bash

wget http://www.guidetopharmacology.org/DATA/targets_and_families.csv
cat targets_and_families.csv | cut -d ',' -f 11 | sed 's/"//g' | tail -n +2 | sort | uniq | python src/update_symbols.py --hgnc gene_with_protein_product.txt > lists/gpcr.tsv