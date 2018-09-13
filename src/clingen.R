options(stringsAsFactors=F)
setwd('~/d/sci/src/gene_lists')

# before reading in, delete lines 1-5 and the # from the beginning of line 5
clingen = read.table('ClinGen_gene_curation_list_GRCh37.tsv',sep='\t',skip=5,comment.char='',quote='',header=T)
colnames(clingen) = gsub('[^a-z0-9_]','_',tolower(colnames(clingen)))
clingen_haploinsufficient_level_3 = clingen[clingen$haploinsufficiency_score=='3','x_gene_symbol']
write.table(clingen_haploinsufficient_level_3,'lists/clingen_level3_genes_2018_09_13.tsv',row.names=F,quote=F,col.names=F)


