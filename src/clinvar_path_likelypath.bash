#!/bin/bash

# current as of 2015-05-12
wget ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
zcat variant_summary.txt.gz | awk -v FS="\t" '$6 ~ "athogenic" {print $5}' | sort | uniq | tail -n +3 > clinvar_symbols.tsv
src/update_symbols.py --hgnc gene_with_protein_product.txt < clinvar_symbols.tsv > lists/clinvar_path_likelypath.tsv
