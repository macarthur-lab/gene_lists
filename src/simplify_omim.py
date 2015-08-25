"""
Parses omim_table.tsv to yield simplified gene lists
"""

__author__ = 'ericminikel'

import argparse
import os

def main(args):
    #### parse the omim data
    omim_data = {} # keys will be gene symbols, values will be dictionaries of info about the genes
    with open(args.omim,mode='r') as f:
        header = f.readline()
        colnames = header.strip('\n').split('\t')
        for line in f.readlines():
            colvalues = line.strip('\n').split('\t')
            data = dict(zip(colnames, colvalues))
            if data['gene'] != '':
                genes = data['gene'].split(',')
                inheritance_modes = []
                if data['phenotypeInheritance'] != 'NA':
                    inheritance_modes = data['phenotypeInheritance'].split(';')
                phenotypes = []
                if data['phenotype'] != 'NA':
                    phenotypes.append(data['phenotype'])
                for gene in genes:
                    omim_data.setdefault(gene, {}).setdefault('phenotype', set()).update(phenotypes)
                    omim_data[gene].setdefault('inheritance_modes', set()).update(set(inheritance_modes))
    #### now write out lists and tables of interest
    # just a list of all omim genes
    with open(os.path.join(args.output_dir,'lists','omim_all.tsv'), mode='wb') as f:
        for gene in sorted(omim_data.keys()):
            f.write(gene+'\n')
    # list of dominant genes
    with open(os.path.join(args.output_dir,'lists','omim_ad.tsv'), mode='wb') as f:
        for gene in sorted(omim_data.keys()):
            if 'Autosomal dominant' in omim_data[gene]['inheritance_modes']:
                f.write(gene+'\n')
    # list of recessive genes
    with open(os.path.join(args.output_dir,'lists','omim_ar.tsv'), mode='wb') as f:
        for gene in sorted(omim_data.keys()):
            if 'Autosomal recessive' in omim_data[gene]['inheritance_modes']:
                f.write(gene+'\n')
    # table of gene to phenotype(s)
    with open(os.path.join(args.output_dir,'other_data','omim_gene_to_phenotype.tsv'), mode='wb') as f:
        f.write('gene\tphenotypes\n')
        for gene in sorted(omim_data.keys()):
            f.write(gene + '\t' + ';'.join(omim_data[gene]['phenotype']) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # for now just assuming the gene symbols have already been updated with the thesaurus in omim_api.py
    #parser.add_argument('--hgnc', dest='hgnc', help='Path to gene thesaurus file.')
    parser.add_argument('--omim', dest='omim', help='Path to omim_table.tsv, which is output of omim_api.py')
    parser.add_argument('-o', '--output_dir', dest='output_dir', help='Directory to save new lists')
    args = parser.parse_args()
    main(args)
