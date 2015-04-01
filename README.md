### List of gene lists

Often in bioinformatics we want a list of genes so that we can ask, "are genes in this list more X than other genes?" or "are genes in this list enriched in this other list?" and so on. There are many useful lists out there, but many of them are in an Excel file supplement to a paper, or an XML format with loads of other info you don't need, or use outdated gene symbols. For one reason or another, it often takes a lot of work to wrestle them into a format you can use. This repository is the MacArthur Lab's effort to collect all the lists we find useful into one place, with each formatted as just a single-column text file listing the current gene symbols.

Here is a guide to the lists we currently have in this repo:

| List | Count | Description | Please cite |
| ---- | ---- | ---- | ---- |
| [Universe](lists/universe.tsv) | 18,991 | Approved symbols for 18,991 protein-coding genes according to HGNC as of Feb 9, 2015. For details see [src/create_universe.bash](src/create_universe.bash). This list is the "universe" of which all subsequent lists are subsets. | See [genenames.org/about/overview](http://www.genenames.org/about/overview). Users are asked to web reference "HUGO Gene Nomenclature Committee at the European Bioinformatics Institute" (http://www.genenames.org/) if possible. |
| [FDA-approved drug targets](lists/fda_approved_drug_targets.tsv) | 286 | Genes whose protein products are known to be the mechanistic targets of FDA-approved drugs. For details on the exact criteria we used for inclusion in this list, see [src/drug_targets.py](src/drug_targets.py) | See [drugbank.ca/about](http://www.drugbank.ca/about). Please cite [[Law 2014], [Knox 2011], [Wishart 2008] and/or [Wishart 2006]]. | 
| [Drug targets by Nelson et al 2012](lists/drug_targets_nelson.tsv) | 201 | Drug targets according to Nelson et al 2012, with reference to Russ & Lampel 2005. | [[Nelson 2012], [Russ & Lampel 2005]] |
| [Autosomal dominant genes by Blekhman et al 2008](lists/blekhman_ad.tsv) | 307 | OMIM disease genes deemed to follow autosomal dominant inheritance according to extensive manual curation by Molly Przeworski's group. | [[Blekhman 2008]] |
| [Autosomal dominant genes by Berg et al 2013](lists/berg_ad.tsv) | 631 | OMIM disease genes (as of June 2011) deemed to follow autosomal dominant inheritance according Berg et al, 2013. | [[Berg 2013]] |
| [Autosomal recessive genes by Blekhman et al 2008](lists/blekhman_ar.tsv) | 529 | OMIM disease genes deemed to follow autosomal recessive inheritance according to extensive manual curation by Molly Przeworski's group. | [[Blekhman 2008]] |
| [Autosomal recessive genes by Berg et al 2013](lists/berg_ar.tsv) | 1073 | OMIM disease genes (as of June 2011) deemed to follow autosomal recessive inheritance according Berg et al, 2013. | [[Berg 2013]] |
| [X-linked genes by Blekhman et al 2008](lists/blekhman_x.tsv) | 66 | OMIM disease genes deemed to follow X-linked inheritance (dominant/recessive not specified) according to extensive manual curation by Molly Przeworski's group. | [[Blekhman 2008]] |
| [X-linked recessive genes by Berg et al 2013](lists/berg_xr.tsv) | 102 | OMIM disease genes (as of June 2011) deemed to follow X-linked recessive inheritance according Berg et al, 2013. | [[Berg 2013]] |
| [X-linked dominant genes by Berg et al 2013](lists/berg_xd.tsv) | 34 | OMIM disease genes (as of June 2011) deemed to follow X-linked dominant inheritance according Berg et al, 2013. | [[Berg 2013]] |
| [All dominant genes](lists/all_ad.tsv) | 709 | Currently the union of the Berg and Blekhman dominant lists, may add more lists later. | [[Blekhman 2008], [Berg 2013]] |
| [All recessive genes](lists/all_ar.tsv) | 1183 | Currently the union of the Berg and Blekhman recessive lists, may add more lists later. | [[Blekhman 2008], [Berg 2013]] |
| [Essential in culture](lists/core_essentials_hart.tsv) | 285 | Genes deemed essential in multiple cultured cell lines based on shRNA screen data | [[Hart 2014]] |
| [Essential in mice](lists/mgi_essential.tsv) | 2,454 | Genes where homozygous knockout in mice results in pre-, peri- or post-natal lethality. The mouse phenotypes were reported by Jackson Labs [[Blake 2011]], then essential gene list was extracted via manual review of phenotypes by [[Georgi 2013]], and the essential/non-essential flag was put into dbNSFP [[Liu 2013]]. We extracted the genes from dbNSFP. | [[Blake 2011], [Georgi 2013], and [Liu 2013]] | 
| [Genes nearest to GWAS peaks](lists/gwascatalog.tsv) | 3,762 | Closest gene 3' and 5' of GWAS hits in the NHGRI GWAS catalog as of Feb 9, 2015 | See instructions [here](http://www.genome.gov/gwastudies/). Cite [[Welter 2014]] and include a web reference to [genome.gov/gwastudies/](http://www.genome.gov/gwastudies/). |
| [DNA Repair Genes, WoodRD](lists/DRG_WoodRD.tsv) | 178 | An updated inventory of human DNA repair genes. (Last modified on Tuesday 15th April 2014). For details see [src/DRG_WoodRD.R](src/DRG_WoodRD.R) | Cite [[Wood 2005]] and include a web reference to [this URL](http://sciencepark.mdanderson.org/labs/wood/dna_repair_genes.html). |
| [DNA Repair Genes, KangJ](lists/DRG_KangJ.tsv) | 151 | Supplementary Table 1. 151 DNA repair genes. DNA repair genes from DNA repair pathways: ATM, BER, FA/HR, MMR, NHEJ, NER, TLS, XLR, RECQ, and other. | Cite [[Kang 2012]] |
| [ClinGen haploinsufficient genes](lists/clingen_level3_genes_2015_03_31.tsv) | 221 | Genes with sufficient evidence for dosage pathogenicity (level 3) as determined by the ClinGen Dosage Sensitivity Map as of Feb 27, 2015 | See [http://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/](http://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/) |

We welcome pull requests for adding additional lists, provided they are licensed for redistribution. If possible, please provide the source code used to extract the list from its original source, and an appropriate description for this readme.

[Law 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24203711 "Law V, Knox C, Djoumbou Y, Jewison T, Guo AC, Liu Y, Maciejewski A, Arndt D, Wilson M, Neveu V, Tang A, Gabriel G, Ly C, Adamjee S, Dame ZT, Han B, Zhou Y, Wishart DS. DrugBank 4.0: shedding new light on drug metabolism. Nucleic Acids Res. 2014 Jan;42(Database issue):D1091-7. doi: 10.1093/nar/gkt1068. Epub 2013 Nov 6. PubMed PMID: 24203711; PubMed Central PMCID: PMC3965102."

[Knox 2011]: http://www.ncbi.nlm.nih.gov/pubmed/21059682 "Knox C, Law V, Jewison T, Liu P, Ly S, Frolkis A, Pon A, Banco K, Mak C, Neveu V, Djoumbou Y, Eisner R, Guo AC, Wishart DS. DrugBank 3.0: a comprehensive resource for 'omics' research on drugs. Nucleic Acids Res. 2011 Jan;39(Database issue):D1035-41. doi: 10.1093/nar/gkq1126. Epub 2010 Nov 8. PubMed PMID: 21059682; PubMed Central PMCID: PMC3013709."

[Wishart 2008]: http://www.ncbi.nlm.nih.gov/pubmed/18048412 "Wishart DS, Knox C, Guo AC, Cheng D, Shrivastava S, Tzur D, Gautam B, Hassanali M. DrugBank: a knowledgebase for drugs, drug actions and drug targets.  Nucleic Acids Res. 2008 Jan;36(Database issue):D901-6. Epub 2007 Nov 29. PubMed PMID: 18048412; PubMed Central PMCID: PMC2238889."

[Wishart 2006]: http://www.ncbi.nlm.nih.gov/pubmed/16381955 "Wishart DS, Knox C, Guo AC, Shrivastava S, Hassanali M, Stothard P, Chang Z, Woolsey J. DrugBank: a comprehensive resource for in silico drug discovery and exploration. Nucleic Acids Res. 2006 Jan 1;34(Database issue):D668-72. PubMed PMID: 16381955; PubMed Central PMCID: PMC1347430."

[Blekhman 2008]: http://www.ncbi.nlm.nih.gov/pubmed/18571414 "Blekhman R, Man O, Herrmann L, Boyko AR, Indap A, Kosiol C, Bustamante CD, Teshima KM, Przeworski M. Natural selection on genes that underlie human disease  susceptibility. Curr Biol. 2008 Jun 24;18(12):883-9. doi: 10.1016/j.cub.2008.04.074. PubMed PMID: 18571414; PubMed Central PMCID: PMC2474766."

[Berg 2013]: http://www.ncbi.nlm.nih.gov/pubmed/22995991 "Berg JS, Adams M, Nassar N, Bizon C, Lee K, Schmitt CP, Wilhelmsen KC, Evans JP. An informatics approach to analyzing the incidentalome. Genet Med. 2013 Jan;15(1):36-44. doi: 10.1038/gim.2012.112. Epub 2012 Sep 20. PubMed PMID: 22995991; PubMed Central PMCID: PMC3538953."

[Nelson 2012]: http://www.ncbi.nlm.nih.gov/pubmed/22604722 "Nelson MR, Wegmann D, Ehm MG, Kessner D, St Jean P, Verzilli C, Shen J, Tang Z, Bacanu SA, Fraser D, Warren L, Aponte J, Zawistowski M, Liu X, Zhang H, Zhang  Y, Li J, Li Y, Li L, Woollard P, Topp S, Hall MD, Nangle K, Wang J, Abecasis G, Cardon LR, Zöllner S, Whittaker JC, Chissoe SL, Novembre J, Mooser V. An abundance of rare functional variants in 202 drug target genes sequenced in 14,002 people. Science. 2012 Jul 6;337(6090):100-4. doi: 10.1126/science.1217876. Epub 2012 May 17. PubMed PMID: 22604722; PubMed Central PMCID: PMC4319976."

[Russ & Lampel 2005]: http://www.ncbi.nlm.nih.gov/pubmed/16376820 "Russ AP, Lampel S. The druggable genome: an update. Drug Discov Today. 2005 Dec;10(23-24):1607-10. PubMed PMID: 16376820."

[Hart 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24987113 "Hart T, Brown KR, Sircoulomb F, Rottapel R, Moffat J. Measuring error rates in genomic perturbation screens: gold standards for human functional genomics. Mol Syst Biol. 2014 Jul 1;10:733. doi: 10.15252/msb.20145216. PubMed PMID: 24987113;  PubMed Central PMCID: PMC4299491."

[Welter 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24316577 "Welter D, MacArthur J, Morales J, Burdett T, Hall P, Junkins H, Klemm A, Flicek P, Manolio T, Hindorff L, Parkinson H. The NHGRI GWAS Catalog, a curated resource of SNP-trait associations. Nucleic Acids Res. 2014 Jan;42(Database issue):D1001-6. doi: 10.1093/nar/gkt1229. Epub 2013 Dec 6. PubMed PMID: 24316577; PubMed Central PMCID: PMC3965119."

[Georgi 2013]: http://www.ncbi.nlm.nih.gov/pubmed/23675308 "Georgi B, Voight BF, Bućan M. From mouse to human: evolutionary genomics analysis of human orthologs of essential genes. PLoS Genet. 2013 May;9(5):e1003484. doi: 10.1371/journal.pgen.1003484. Epub 2013 May 9. PubMed PMID: 23675308; PubMed Central PMCID: PMC3649967."

[Blake 2011]: http://www.ncbi.nlm.nih.gov/pubmed/21051359 "Blake JA, Bult CJ, Kadin JA, Richardson JE, Eppig JT; Mouse Genome Database Group. The Mouse Genome Database (MGD): premier model organism resource for mammalian genomics and genetics. Nucleic Acids Res. 2011 Jan;39(Database issue):D842-8. doi: 10.1093/nar/gkq1008. Epub 2010 Nov 3. PubMed PMID: 21051359;  PubMed Central PMCID: PMC3013640."

[Liu 2013]: http://www.ncbi.nlm.nih.gov/pubmed/23843252 "Liu X, Jian X, Boerwinkle E. dbNSFP v2.0: a database of human non-synonymous SNVs and their functional predictions and annotations. Hum Mutat. 2013 Sep;34(9):E2393-402. doi: 10.1002/humu.22376. Epub 2013 Jul 10. PubMed PMID: 23843252; PubMed Central PMCID: PMC4109890."

[Wood RD 2005]: http://www.ncbi.nlm.nih.gov/pubmed/15922366 "Human DNA repair genes, 2005. Wood RD1, Mitchell M, Lindahl T"

[Kang J 2012]: http://www.ncbi.nlm.nih.gov/pubmed/22505474 "A DNA repair pathway-focused score for prediction of outcomes in ovarian cancer treated with platinum-based chemotherapy."
