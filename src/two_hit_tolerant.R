setwd('~/d/sci/src/gene_lists')
source('~/d/sci/src/exac_2015/exac_constants.R')
exac_raw_data = load_exac_data(reload=F)
exac_data = subset(exac_raw_data, filter == 'PASS')

lof_data = subset(exac_data, lof_use & use)
universe = read.table('../gene_lists/lists/universe.tsv', header=F)$V1
hom_lof = subset(lof_data, ac_hom > 0)

two_hit_tolerant_genes = names(table(hom_lof$symbol)[table(hom_lof$symbol) > 1])
write.table(intersect(universe, two_hit_tolerant_genes), quote=F, row.names=F, col.names=F, file='../gene_lists/lists/homozygous_lof_tolerant_twohit.tsv')
