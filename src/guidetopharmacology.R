options(stringsAsFactors=F)
setwd('~/d/sci/src/gene_lists')

data = read.table('guidetopharmacology.org_targets_and_families.csv',sep=',',quote='"',header=T)
colnames(data) = gsub('[^a-z0-9_]','_',tolower(colnames(data)))

gpcrs = data[data$type=='gpcr','hgnc_symbol']

write.table(gpcrs,'lists/gpcr.tsv',row.names=F,quote=F,col.names=F)

