#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

from gene_list_utils import *

'''
Parses the drug target gene list from:
Nelson MR, Wegmann D, Ehm MG, Kessner D, St Jean P, Verzilli C,
   Shen J, Tang Z, Bacanu SA, Fraser D, Warren L, Aponte J,
   Zawistowski M, Liu X, Zhang H, Zhang  Y, Li J, Li Y, 
   Li L, Woollard P, Topp S, Hall MD, Nangle K, Wang J, 
   Abecasis G, Cardon LR, Zollner S, Whittaker JC, Chissoe SL, 
   Novembre J, Mooser V. An abundance of rare functional variants 
   in 202 drug target genes sequenced in 14,002 people. 
   Science. 2012 Jul 6;337(6090):100-4. doi: 10.1126/science.1217876. 
   Epub 2012 May 17. PubMed PMID: 22604722; 
   PubMed Central PMCID: PMC4319976."
'''
def parse_nelson(table_path,hgnc):
    genes = {} # dictionary of genes
    with open(table_path) as f:
        colnames = f.readline().strip().split("\t")
        for line in f.readlines():
            gene_data = dict(zip(colnames,line.strip().split("\t")))
            gene_symbol_as_of_2012 = gene_data['Gene37']
            # try to find an updated symbol
            if hgnc.has_key(gene_symbol_as_of_2012):
                current_symbol = hgnc[gene_symbol_as_of_2012] 
            else:
                sys.stderr.write("Could not find a current approved gene symbol for %s, skipping.\n"%(gene_symbol_as_of_2012))
                continue
            genes[current_symbol] = gene_data
    return genes

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt",mode='update')
    nelson = parse_nelson('nelson_fixed.txt',hgnc)
    with open('lists/drug_targets_nelson.tsv',mode='w') as f:
        print_list(nelson.keys(),f)

