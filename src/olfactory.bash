#!/bin/bash

# get olfactory receptor list from Mainland et al 2015 http://www.nature.com/articles/sdata20152

wget http://files.figshare.com/1816348/Receptors.tsv
cat Receptors.tsv | tr '\r' '\n' | tail -n +3 | cut -f2 | cut -d ' ' -f1 | sort | uniq | src/update_symbols.py --hgnc gene_with_protein_product.txt > lists/olfactory_receptors.tsv