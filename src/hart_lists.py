#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

from gene_list_utils import *

'''
Parses the list of cell culture essential genes from:
Hart T, Brown KR, Sircoulomb F, Rottapel R, Moffat J. Measuring error rates 
    in genomic perturbation screens: gold standards for human functional genomics. 
    Mol Syst Biol. 2014 Jul 1;10:733. doi: 10.15252/msb.20145216. 
    PubMed PMID: 24987113;  PubMed Central PMCID: PMC4299491."
First, download Table S1 in Excel format:
Navigate to http://onlinelibrary.wiley.com/doi/10.15252/msb.20145216/suppinfo
Download msb145216-sup-0001-DatasetS1.xlsx
Open in Excel, copy third column into its own text file
Save as hart-supplement-1-core-essentials.txt
'''
def parse_hart(table_path,hgnc):
    genes = {} # dictionary of genes
    with open(table_path) as f:
        colnames = f.readline().strip().split("\t")
        for line in f.readlines():
            gene_data = dict(zip(colnames,line.strip().split("\t")))
            gene_symbol_as_of_2014 = gene_data['CoreEssentials-24of48screens']
            # try to find an updated symbol
            if hgnc.has_key(gene_symbol_as_of_2014):
                current_symbol = hgnc[gene_symbol_as_of_2014] 
            else:
                sys.stderr.write("Could not find a current approved gene symbol for %s, skipping.\n"%(gene_symbol_as_of_2014))
                continue
            genes[current_symbol] = gene_data
    return genes

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt",mode='update')
    genes = parse_hart('hart-supplement-1-core-essentials.txt',hgnc)
    with open('lists/core_essentials_hart.tsv',mode='w') as f:
        print_list(genes.keys(),f)

