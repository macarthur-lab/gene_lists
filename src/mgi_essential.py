#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

from gene_list_utils import *

'''
First, obtain a copy of dbNSFP from https://sites.google.com/site/jpopgen/dbNSFP
Then extract the human gene symbols of genes whose mouse orthologs are considered
to be essential:
cat dbNSFP2.6_gene | awk -v FS="\t" '$32 == "E" {print $1}' > mouse_essential.txt
'''
def parse_mgi_essential(table_path,hgnc):
    genes = [] # list of genes
    with open(table_path) as f:
        colnames = f.readline().strip().split("\t")
        for line in f.readlines():
            gene_symbol_as_of_2013 = line.strip()
            # try to find an updated symbol
            if hgnc.has_key(gene_symbol_as_of_2013):
                current_symbol = hgnc[gene_symbol_as_of_2013] 
            else:
                sys.stderr.write("Could not find a current approved gene symbol for %s, skipping.\n"%(gene_symbol_as_of_2013))
                continue
            genes.append(current_symbol)
    return genes

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt",mode='update')
    genes = parse_mgi_essential('mouse_essential.txt',hgnc)
    with open('lists/mgi_essential.tsv',mode='w') as f:
        print_list(genes,f)

