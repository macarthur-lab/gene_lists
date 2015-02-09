#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

from gene_list_utils import *

'''
Parses the gene list from the Supplementary Materials of Berg et al, 2013 into a dict
Suggested input:
    wget http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3538953/bin/NIHMS424944-supplement-Supplemental_Tables_1-3.xls
    # Open Excel and convert the second worksheet, Table S1, xls to tab-delimited text as berg_2013_table_s1.txt
    # Then use the next line to convert \r to \n:
    cat berg_2013_table_s1.txt | tr '\r' '\n' > berg_2013_table_s1_fixed.txt
Citation for this dataset:
    Berg JS, Adams M, Nassar N, Bizon C, Lee K, Schmitt CP, Wilhelmsen KC, 
    Evans JP. An informatics approach to analyzing the incidentalome. 
    Genet Med. 2013 Jan;15(1):36-44. doi: 10.1038/gim.2012.112. 
    Epub 2012 Sep 20. PubMed PMID: 22995991; PubMed Central 
    PMCID: PMC3538953.
'''

def parse_berg(table_path,hgnc):
    genes = {} # dictionary of genes
    with open(table_path) as f:
        colnames = f.readline().strip().split("\t")
        for line in f.readlines():
            gene_data = dict(zip(colnames,line.strip().split("\t")))
            symbols_as_of_2013 = gene_data['symbol'].strip('"').split(",")
            current_symbol = None
            for symbol in symbols_as_of_2013:
                if hgnc.has_key(symbol):
                    current_symbol = hgnc[symbol]
            if current_symbol is None:
                sys.stderr.write("Could not find a current approved gene symbol for %s, skipping.\n"%(symbols_as_of_2013))
                continue
            genes[current_symbol] = gene_data
    return genes

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt",mode='update')
    berg = parse_berg('berg_2013_table_s1_fixed.txt',hgnc)
    with open('lists/berg_ad.tsv',mode='w') as f:
        print_list(get_genes(berg, {'inheritance': 'AD'}),f)
    with open('lists/berg_ar.tsv',mode='w') as f:
        print_list(get_genes(berg, {'inheritance': 'AR'}),f)
    with open('lists/berg_xd.tsv',mode='w') as f:
        print_list(get_genes(berg, {'inheritance': 'XD'}),f)
    with open('lists/berg_xr.tsv',mode='w') as f:
        print_list(get_genes(berg, {'inheritance': 'XR'}),f)