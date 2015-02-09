#!/broad/software/free/Linux/redhat_5_x86_64/pkgs/python_2.7.1-sqlite3-rtrees/bin/python

import gzip
import xml.etree.ElementTree as ET
import sys

'''
Prints key-value pairs from a dictionary, subbing in "" if the value is None.
Note that the .encode('utf8') is necessary only if writing to a file (not to sys.stdout)
and even then only for a single drug in the whole dataset (dihomo-γ-linolenic acid)
which contains a Greek gamma (u'\u03b3').
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

'''
Parse the drugbank XML dump and use an HGNC dictionary to get a mapping of drug generic name to approved human gene symbol.
Suggested input:
    wget http://www.drugbank.ca/system/downloads/current/drugbank.xml.zip
    unzip drugbank.xml.zip
And before you use the drugbank.xml file, use sed or a text editor to delete 'xmlns="http:///www.drugbank.ca"' from the second line.
Otherwise you need to reference the namespace every time you access any node.
This output only includes 1) approved drugs with 2) known mechanisms of action with 3) human targets with 4) value gene symbols.
Note that annotations exist for other groups as well, but we are only addressing approved drugs here:
$ cat drugbank.xml | grep "<group>" | sort | uniq -c
# 1757     <group>approved</group>
# 5064     <group>experimental</group>
#  186     <group>illicit</group>
# 1231     <group>investigational</group>
#   89     <group>nutraceutical</group>
#  179     <group>withdrawn</group>
'''
def parse_drugbank(drugbank_path,hgnc,debug=False):
    drug_gene = {} # keys will be drug generic names, values will be gene symbols
    tree = ET.parse('drugbank.xml')
    root = tree.getroot()
    drugs = root.findall("drug")
    for drug in drugs:
        # get its common name
        name = drug.find("name")
        if name is None:
            continue
        generic_name = name.text.lower()
        # figure out if approved
        is_approved = False
        groups = drug.find("groups")
        if groups is not None:
            for group in groups.findall("group"):
                if group.text == "approved":
                    is_approved = True
        if not is_approved:
            continue
        if debug:
            sys.stderr.write(generic_name+"\t")
        gene_symbol = None
        targets_element = drug.find("targets")
        if targets_element is not None:
            targets = targets_element.findall("target")
            for target in targets:
                # not all targets have a position, but for those that do,
                # only take the top-ranked target association
                if target.attrib.has_key("position"):
                    if target.attrib["position"] != '1':
                        continue
                known_action = target.find("known-action")
                if known_action.text != "yes":
                    continue
                polypeptide = target.find("polypeptide")
                if polypeptide is None:
                    continue
                organism = polypeptide.find("organism")
                if organism.text != "Human":
                    continue
                extids = polypeptide.find("external-identifiers")
                for extid in extids.findall("external-identifier"):
                    if extid.find("resource").text == "HUGO Gene Nomenclature Committee (HGNC)":
                        hgnc_id = extid.find("identifier").text
                if hgnc_id is not None:
                    if hgnc.has_key(hgnc_id):
                        gene_symbol = hgnc[hgnc_id]['Approved Symbol']
                        break
            drug_gene[generic_name] = gene_symbol # add key-value pair to dictionary
            if debug:
                if gene_symbol is None:
                    print ""
                else:
                    print gene_symbol
    return drug_gene

if __name__ == '__main__':
    hgnc = parse_hgnc("gene_with_protein_product.txt")
    drug_gene = parse_drugbank("drugbank.xml",hgnc,debug=False)
    with open('other_data/drug_gene_match.tsv',mode='w') as f:
        print_dict(drug_gene,f)
    with open('lists/fda_approved_drug_targets.tsv',mode='w') as f:
        print_values(drug_gene,f)
