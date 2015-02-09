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
Prints unique values from a dictionary, alphabetically, each only once.
'''
def print_values(a_dictionary,dest=sys.stdout):
    unique_values = sorted(set(a_dictionary.values()))
    for unique_value in unique_values:
        if unique_value is not None:
            dest.write((unique_value + "\n").encode('utf8'))

'''
Prints unique values from a list, alphabetically, each only once.
'''
def print_list(a_list,dest=sys.stdout):
    unique_values = sorted(set(a_list))
    for unique_value in unique_values:
        if unique_value is not None:
            dest.write((unique_value + "\n").encode('utf8')) 

'''
Takes a dictionary in which gene symbols are keys and dictionaries
of info about each gene are the values. 
Returns a list of genes meeting filters specified in the dictionary
called "filters". For instance, for the Blekhman 2008 dataset, 
get_genes(blekhman,{'ModeInher': 'AD'}) returns only autosomal dominant genes.
'''
def get_genes(gene_dict,filters):
    genes = []
    for gene in gene_dict.keys():
        include = True
        for filterkey in filters.keys():
            if gene_dict[gene][filterkey] != filters[filterkey]:
                include = False
                break
        if include:
            genes.append(gene)
    return genes

'''
Parse the HGNC database to get current gene symbol for all 19,000 genes with protein products
Suggested input:
    wget ftp://ftp.ebi.ac.uk/pub/databases/genenames/locus_types/gene_with_protein_product.txt.gz
    gunzip gene_with_protein_product.txt.gz
Note for some reason the file from EBI seems to be unreadable by zcat but can still be gunzipped. Not sure why.
Behavior depends on mode.
If mode = 'id', returns a dictonary mapping HGNC ids (e.g. "HGNC:5") to all HGNC info, including approved gene symbol (e.g. "A1BG")
If mode = 'update', returns a dictionary mapping any previous symbols or synonyms (e.g. "ACF") to current approved HGNC symbol (e.g. "AC1F")
'''
def parse_hgnc(hgnc_path, mode='id'):
    hgnc = {}
    with open(hgnc_path) as hgnc_file:
        header = hgnc_file.readline()
        colnames = header.strip().split('\t')
        for line in hgnc_file.readlines():
            cols = line.split('\t')
            if mode == 'id':
                hgnc_id = cols[colnames.index('HGNC ID')]
                hgnc[hgnc_id] = dict(zip(colnames,line.split('\t')))
            if mode == 'update':
                all_possible_names_and_symbols = map(str.strip,cols[colnames.index('Previous Symbols')].split(',') + 
                    cols[colnames.index('Approved Symbol')].split(',') + 
                    cols[colnames.index('Synonyms')].split(','))
                for symbol in all_possible_names_and_symbols:
                    if symbol != '': # skip blanks
                        hgnc[symbol] = cols[colnames.index('Approved Symbol')]
    return hgnc
