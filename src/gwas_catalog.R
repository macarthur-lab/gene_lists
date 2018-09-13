options(stringsAsFactors=F)
setwd('~/d/sci/src/gene_lists')
gwahits = data.frame(read.table('gwas_catalog_v1.0-associations_e93_r2018-08-28.tsv',header=TRUE,sep='\t',quote="",comment.char="",as.is=TRUE))


# note that the Lek 2016 (PMID: 27535533) supplement (p. 68) says that the 
# definition of GWAS genes used in that paper was:
# "Closest gene 3' and 5' of GWAS hits in the NHGRI GWAS catalog (genome.gov/gwastudies/) accessed 02/09/2015."

# the current EBI GWAS catalog has a MAPPED_GENE column defined as:
# MAPPED GENE(S)*: Gene(s) mapped to the strongest SNP. If the SNP is located within a gene, that gene is listed. If the SNP is intergenic, the upstream and downstream genes are listed, separated by a hyphen.
# (from http://www.ebi.ac.uk/gwas/docs/fileheaders)

# that sounds most relevant

mapped_genes = trimws(unlist(strsplit(gwahits$MAPPED_GENE[gwahits$P.VALUE < 5e-8],' -')),which='both')
head(mapped_genes)
length(unique(mapped_genes))

write.table(mapped_genes,'lists/mapped_genes_raw.tsv',sep='\t',row.names=F,quote=F,col.names=T)
