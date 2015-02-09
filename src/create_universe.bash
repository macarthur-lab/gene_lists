#!/bin/bash

wget ftp://ftp.ebi.ac.uk/pub/databases/genenames/locus_types/gene_with_protein_product.txt.gz
gunzip gene_with_protein_product.txt.gz
cat gene_with_protein_product.txt | cut -f2 | tail -n +2 | sort | uniq > lists/universe.tsv
