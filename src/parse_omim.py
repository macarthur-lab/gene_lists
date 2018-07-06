"""
Pulls down gene list and associated disease information from OMIM via HTTP API.
"""

__author__ = 'bernie'

import urllib
import urllib2
import re
import json
import argparse
import sys
from collections import defaultdict
from gene_list_utils import *


def get_gene_thesaurus(filename):
	"""
	Returns mapping from gene symbol to list of synonymous, approved gene symbols 
	ideally, there should only be one approved synonym for any given symbol, but the file has lines where
	a non-approved symbol will appear in the approved column and thus will be mapped to itself
	e.g. FRAXA NA
	"""
	thesaurus = defaultdict(list)
	with open(filename, 'r') as lines:
		for line in lines:
			line = line.strip().split("\t")
			approved = line[0]
			synonyms = line[1].split(",")
			thesaurus[approved].append(approved)
			if synonyms != "NA":
				for word in synonyms:
					thesaurus[word].append(approved)
	return thesaurus


def main(args):
	if args.chrom:
		chromosomes = [args.chrom]
	else:
		chromosomes = (x for x in range(1,23) + ['X', 'Y'])
	
	# set parameters for HTTP request
	request_data = {}
	request_data['apiKey'] = 'tjqbNLkIQOOiXFd2ctwLGw'
	request_data['format'] = 'json'
	request_data['chromosome'] = chromosomes.next()
	request_data['limit'] = 100
	request_data['chromosomeSort'] = 1

	if args.output == sys.stdout:
		o = sys.stdout
	else:
		o = open(args.output, 'w')

	header = ['genes', 'hgnc_synonyms', 'hgnc_genes', 'phenotype', 'phenotypeInheritance', 
			  'geneMimNumber','phenotypeMimNumber', 'chromosome', 'comments']
	o.write('\t'.join(header) + '\n')
	header = dict(zip(header, range(len(header))))

	t = get_gene_thesaurus(args.hgnc)
	sys.stdout.write("\rOn chromosome %s .. " % request_data['chromosome'])
	sys.stdout.flush()
	while True:
		url = 'http://api.omim.org/api/geneMap'
		# add parameters to url string
		url_values = urllib.urlencode(request_data)
		url = url + '?' + url_values
		# query OMIM 
		try:
			response = urllib2.urlopen(url)
		except urllib2.HTTPError:
			raise SystemExit, "Failed to access OMIM API, may be time to register for a new key"
		# read in response
		result = json.loads(response.read())		
		geneMapList = result['omim']['listResponse']['geneMapList']
		
		# check if chromosome is done
		num_genes = len(geneMapList)
		if num_genes == 0:
			# try moving to next chromosome
			try:
				request_data['chromosome'] = chromosomes.next()
				sys.stdout.write("\rOn chromosome %s .." % request_data['chromosome'])
				sys.stdout.flush()
			# if no chromosomes are left, break out of loop .. we're done here
			except StopIteration:
				break

			request_data['chromosomeSort'] = 1
			continue

		# write response data
		for g in geneMapList:
			line = ['']*len(header.keys())
			geneMap = g['geneMap']
			genes = re.sub(' ', '', geneMap['geneSymbols']).split(',')
			hgnc_genes = [','.join(t[gene]) if t[gene] else 'NA' for gene in genes]
			if args.use and all(map(lambda g:g == 'NA', hgnc_genes)):
				continue

			line[header['hgnc_synonyms']] = '|'.join(hgnc_genes)
			tmp = reduce(lambda a, b: a + ',' + b, hgnc_genes)
			hgnc_genes = set(filter(lambda x:x != 'NA', tmp.split(',')))
			if not hgnc_genes: 
				hgnc_genes = 'NA'
			else:
				hgnc_genes = ','.join(hgnc_genes)

			line[header['genes']] = '|'.join(genes)
			line[header['hgnc_genes']] = hgnc_genes
			line[header['chromosome']] = geneMap['chromosomeSymbol']
			line[header['geneMimNumber']] = geneMap['mimNumber']
			
			if 'comments' in geneMap:
				line[header['comments']] = geneMap['comments']
			else:
				line[header['comments']] = 'NA'

			if 'phenotypeMapList' in geneMap:
				phenotypeMapList = geneMap['phenotypeMapList']
				for p in phenotypeMapList:
					phenotypeMap = p['phenotypeMap']
					for key in ['phenotype', 'phenotypeInheritance', 'phenotypeMimNumber']:
						if key in phenotypeMap:
							if key == 'phenotype':
								value = re.sub('[{}\[\]]', '', phenotypeMap[key])
							else:
								value = phenotypeMap[key]
						else:
							value = 'NA'
						line[header[key]] = value

					line = map(str, line)
					o.write('\t'.join(line) + '\n')
			elif args.use:
				continue
			else:
				line[header['phenotype']] = 'NA'
				line[header['phenotypeInheritance']] = 'NA'
				line[header['phenotypeMimNumber']] = 'NA'
				line = map(str, line)
				o.write('\t'.join(line) + '\n')
		
		request_data['chromosomeSort'] += 100
	
	o.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--hgnc', dest='hgnc', help='Path to gene thesaurus file.', required=True)
	parser.add_argument('-o', '--output', dest='output', default=sys.stdout)
	parser.add_argument('--chrom', help='Only get data for given chromosome.')
	parser.add_argument('--use', action='store_true', help='Only output entries with a gene AND '
														   'associated phenotype AND WHERE '
														   'the gene can be matched to an HGNC-approved symbol.')
	args = parser.parse_args()

	main(args)

# e.g python parse_omim.py --hgnc gene_symbol_thesaurus.txt --simplify_genes --output omim_table.txt



