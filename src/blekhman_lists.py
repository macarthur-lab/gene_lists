#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

from gene_list_utils import *
import re

'''
Parses the gene list from the Supplementary Materials of Blekhman et al, 2008 into a dict
Suggested input:
    wget http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2474766/bin/NIHMS57219-supplement-02.xls
    # Open Excel and convert xls to tab-delimited text. Then use the next line to convert \r to \n:
    at NIHMS57219-supplement-02.txt | tr '\r' '\n' > blekhman_supplement_02.txt
Citation for this dataset:
    Blekhman R, Man O, Herrmann L, Boyko AR, Indap A, Kosiol C, Bustamante CD,
    Teshima KM, Przeworski M. Natural selection on genes that underlie human
    disease  susceptibility. Curr Biol. 2008 Jun 24;18(12):883-9.
    doi: 10.1016/j.cub.2008.04.074.
    PubMed PMID: 18571414;
    PubMed Central PMCID: PMC2474766.
'''
def parse_blekhman(table_path,hgnc):
    genes = {} # dictionary of genes
    with open(table_path) as f:
        colnames = f.readline().strip().split("\t")
        for line in f.readlines():
            gene_data = dict(zip(colnames,line.strip().split("\t")))
            # make sure we use the current gene symbol.
            # note this is incredibly inefficient right now but for 19K genes it is fast enough
            gene_symbol_as_of_2008 = gene_data['HUGO']
            # try to find an updated symbol
            if hgnc.has_key(gene_symbol_as_of_2008):
                current_symbol = hgnc[gene_symbol_as_of_2008] 
            else:
                sys.stderr.write("Could not find a current approved gene symbol for %s, skipping.\n"%(gene_symbol_as_of_2008))
                continue
            genes[current_symbol] = gene_data
    return genes

'''
Takes a dictionary from the above function and returns a list of genes
meeting filters specified in the dictionary, filters. In that dictionary,
every key should be a column from the supplement, and every value
should be a value that column has to be equal to, e.g.
{'ModeInher': 'AD'} returns only autosomal dominant genes.
'''
def get_genes(blekhman,filters):
    genes = []
    for gene in blekhman.keys():
        include = True
        for filterkey in filters.keys():
            if blekhman[gene][filterkey] != filters[filterkey]:
                include = False
                break
        if include:
            genes.append(gene)
    return genes

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt",mode='update')
    blekhman = parse_blekhman('blekhman_supplement_02.txt',hgnc)
    ad_genes = get_genes(blekhman, {'ModeInher': 'AD'})
    with open('lists/blekhman_ad.tsv',mode='w') as f:
        print_list(ad_genes,f)
    ar_genes = get_genes(blekhman, {'ModeInher': 'AR'})
    with open('lists/blekhman_ar.tsv',mode='w') as f:
        print_list(ar_genes,f)
    x_genes = get_genes(blekhman, {'ModeInher': 'X'})
    with open('lists/blekhman_x.tsv',mode='w') as f:
        print_list(x_genes,f)

