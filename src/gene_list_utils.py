#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

import gzip
import xml.etree.ElementTree as ET
import sys

'''
Prints key-value pairs from a dictionary, subbing in "" if the value is None.
Note that the .encode('utf8') is necessary only if writing to a file (not to sys.stdout)
and even then onlyn necssary for a single drug in the whole DrugBank dataset
(dihomo-u'\u03b3'-linolenic acid) which contains a Greek gamma (u'\u03b3').
'''
def print_dict(a_dictionary,dest=sys.stdout):
    for key in a_dictionary.keys():
        dest.write((key + "\t" + ("" if a_dictionary[key] is None else a_dictionary[key]) + "\n").encode('utf8'))

'''
Prints unique values from a dictionary, each only once.
'''
def print_values(a_dictionary,dest=sys.stdout):
    unique_values = sorted(set(a_dictionary.values()))
    for unique_value in unique_values:
        if unique_value is not None:
            dest.write((unique_value + "\n").encode('utf8'))

'''
Parse the HGNC database to get current gene symbol for all 19,000 genes with protein products
Suggested input:
    wget ftp://ftp.ebi.ac.uk/pub/databases/genenames/locus_types/gene_with_protein_product.txt.gz
    gunzip gene_with_protein_product.txt.gz
Note for some reason the file from EBI seems to be unreadable by zcat but can still be gunzipped. Not sure why.
Returns: a dictonary mapping HGNC ids (e.g. "HGNC:5") to HGNC info, such as approved gene symbol (e.g. "A1BG")
'''
def parse_hgnc(hgnc_path):
    hgnc = {}
    with open(hgnc_path) as hgnc_file:
        header = hgnc_file.readline()
        colnames = header.strip().split('\t')
        for line in hgnc_file.readlines():
            hgnc_id = line.split('\t')[0]
            hgnc[hgnc_id] = dict(zip(colnames,line.strip().split('\t')))
    return hgnc
