### List of gene lists

Often in bioinformatics we want a list of genes so that we can ask, "are genes in this list more X than other genes?" or "are genes in this list enriched in this other list?" and so on. There are many useful lists out there, but many of them are in an Excel file supplement to a paper, or an XML format with loads of other info you don't need, or use outdated gene symbols. For one reason or another, it often takes a lot of work to wrestle them into a format you can use. This repository is the MacArthur Lab's effort to collect all the lists we find useful into one place, with each formatted as just a single-column text file listing the current gene symbols.

Here is a guide to the lists we currently have in this repo:

| List | Description | Please cite |
| ---- | ---- | ---- |
| [Universe](lists/universe.tsv) | All protein-coding genes according to HGNC as of Feb 9, 2015. For details see [src/create_universe.bash](src/create_universe.bash). This list is the "universe" of which all subsequent lists are subsets. | See [genenames.org/about/overview](http://www.genenames.org/about/overview). Users are asked to web reference "HUGO Gene Nomenclature Committee at the European Bioinformatics Institute" (http://www.genenames.org/) if possible. |
| FDA-approved drug targets | Genes whose protein products are known to be the mechanistic targets of FDA-approved drugs. For details on exact criteria used, see [src/drug_targets.py] | See [drugbank.ca/about](http://www.drugbank.ca/about). Please cite [[Law 2014], [Knox 2011], [Wishart 2008] and/or [Wishart 2006]]. | 


[Law 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24203711 "Law V, Knox C, Djoumbou Y, Jewison T, Guo AC, Liu Y, Maciejewski A, Arndt D, Wilson M, Neveu V, Tang A, Gabriel G, Ly C, Adamjee S, Dame ZT, Han B, Zhou Y, Wishart DS. DrugBank 4.0: shedding new light on drug metabolism. Nucleic Acids Res. 2014 Jan;42(Database issue):D1091-7. doi: 10.1093/nar/gkt1068. Epub 2013 Nov 6. PubMed PMID: 24203711; PubMed Central PMCID: PMC3965102."

[Knox 2011]: http://www.ncbi.nlm.nih.gov/pubmed/21059682 "Knox C, Law V, Jewison T, Liu P, Ly S, Frolkis A, Pon A, Banco K, Mak C, Neveu V, Djoumbou Y, Eisner R, Guo AC, Wishart DS. DrugBank 3.0: a comprehensive resource for 'omics' research on drugs. Nucleic Acids Res. 2011 Jan;39(Database issue):D1035-41. doi: 10.1093/nar/gkq1126. Epub 2010 Nov 8. PubMed PMID: 21059682; PubMed Central PMCID: PMC3013709."

[Wishart 2008]: http://www.ncbi.nlm.nih.gov/pubmed/18048412 "Wishart DS, Knox C, Guo AC, Cheng D, Shrivastava S, Tzur D, Gautam B, Hassanali M. DrugBank: a knowledgebase for drugs, drug actions and drug targets.  Nucleic Acids Res. 2008 Jan;36(Database issue):D901-6. Epub 2007 Nov 29. PubMed PMID: 18048412; PubMed Central PMCID: PMC2238889."

[Wishart 2006]: http://www.ncbi.nlm.nih.gov/pubmed/16381955 "Wishart DS, Knox C, Guo AC, Shrivastava S, Hassanali M, Stothard P, Chang Z, Woolsey J. DrugBank: a comprehensive resource for in silico drug discovery and exploration. Nucleic Acids Res. 2006 Jan 1;34(Database issue):D668-72. PubMed PMID: 16381955; PubMed Central PMCID: PMC1347430."