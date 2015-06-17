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


def simplify_gene_list(genes, thesaurus):
	genes = re.sub(' ', '', genes).split(',')
	new = set()
	for gene in genes:
		try:
			new.add(thesaurus[gene])
		except KeyError:
			pass
	return ','.join(new)


def get_gene_thesaurus(filename):
	thesaurus = {}
	with open(filename, 'r') as lines:
		for line in lines:
			line = line.strip().split("\t")
			approved = line[0]
			synonyms = line[1]
			thesaurus[approved] = approved
			if synonyms != "NA":
				for word in synonyms:
					thesaurus[word] = approved
	return thesaurus


def main(args):
	chromosomes = (x for x in range(1,23) + ['X', 'Y'])
	
	# set parameters for HTTP request
	request_data = {}
	request_data['apiKey'] = 'FE4125A4A6027ABC7E12CF006248ABDF86083EB6'
	request_data['format'] = 'json'
	request_data['chromosome'] = chromosomes.next()
	request_data['limit'] = 100
	request_data['chromosomeSort'] = 1

	if args.output == sys.stdout:
		o = sys.stdout
	else:
		o = open(args.output, 'a')

	header = ['phenotype', 'phenotypeInheritance', 'phenotypeMimNumber', 'chromosome', 'gene', 'geneMimNumber', 'comments']
	o.write('\t'.join(header) + '\n')
	header = dict(zip(header, range(len(header))))

	t = get_gene_thesaurus(args.hgnc)

	while True:
		url = 'http://api.omim.org/api/geneMap'
		# add parameters to url string
		url_values = urllib.urlencode(request_data)
		url = url + '?' + url_values
		# query OMIM 
		response = urllib2.urlopen(url)
		# read in response
		result = json.loads(response.read())		
		geneMapList = result['omim']['listResponse']['geneMapList']
		
		# check if chromosome is done
		num_genes = len(geneMapList)
		if num_genes == 0:
			# try moving to next chromosome
			try:
				request_data['chromosome'] = chromosomes.next()
				print request_data['chromosome']
			# if no chromosomes are left, break out of loop .. we're done here
			except StopIteration:
				break

			request_data['chromosomeSort'] = 1
			continue

		# write response data
		for g in geneMapList:
			geneMap = g['geneMap']
			
			line = ['']*len(header.keys())
			genes = simplify_gene_list(geneMap['geneSymbols'], t)
			line[header['gene']] = genes
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
	parser.add_argument('--hgnc', dest='hgnc', help='Path to gene thesaurus file.')
	parser.add_argument('--output', dest='output', default=sys.stdout)
	args = parser.parse_args()
	main(args)


