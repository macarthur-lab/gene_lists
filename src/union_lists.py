#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

from gene_list_utils import *
from berg_lists import *
from blekhman_lists import *

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt",mode='update')
    berg = parse_berg('berg_2013_table_s1_fixed.txt',hgnc)
    blekhman = parse_blekhman('blekhman_supplement_02.txt',hgnc)
    all_ad = list(set(get_genes(blekhman, {'ModeInher': 'AD'})) | set(get_genes(berg, {'inheritance': 'AD'})))
    with open('lists/all_ad.tsv',mode='w') as f:
        print_list(all_ad,f)
    all_ar = list(set(get_genes(blekhman, {'ModeInher': 'AR'})) | set(get_genes(berg, {'inheritance': 'AR'})))
    with open('lists/all_ar.tsv',mode='w') as f:
        print_list(all_ar,f)