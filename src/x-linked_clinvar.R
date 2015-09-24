options(stringsAsFactors=FALSE)
require(sqldf)
setwd('~/d/sci/src/gene_lists')
clinvar = read.table('../clinvar/output/clinvar.tsv',sep='\t',header=T,quote='',comment.char='')
x_linked = sqldf("
select   symbol
from     clinvar
where    pathogenic = 1
and      conflicted = 0
and      all_submitters not in ('OMIM','GeneReviews','OMIM;GeneReviews')
and      chrom = 'X'
and      symbol <> '-'
group by 1
having   count(*) > 2
order by 1
;")
write.table(x_linked,'lists/x-linked_clinvar.tsv',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)
