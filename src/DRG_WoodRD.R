# About -------------------------------------------------------------------
# Date: 31/03/2015
# Extract DNA Repair Genes from WoodRD website
# http://sciencepark.mdanderson.org/labs/wood/dna_repair_genes.html

# Workspace ---------------------------------------------------------------
require(XML)
setwd("N:/Translational Cancer Genetics Team/04 Zsofia/24 COGS/007 CONCEPT projects/DNA repair and rare variants/DNA Repair Genes/V3/R")

# Data prep ---------------------------------------------------------------
WoodRD <- readHTMLTable("http://sciencepark.mdanderson.org/labs/wood/dna_repair_genes.html")

d <- WoodRD[[1]]

#convert Â to NA
d[d=="Â"] <- NA

#exclude subheader rows
d <- d[ !(is.na(d$V3) & is.na(d$V4)), ]

#exclude "Top of Page" rows
d <- d[ !(d$V2=="Top of Page" | d$V3=="Top of Page"),]

#keep Gene name, exclude names in brackets
d <- gsub("\\(|\\)","",d$V1)
d <- sort(unlist(lapply(strsplit(d," "),"[",1)))

# Output ------------------------------------------------------------------
write.table(d,"DRG_WoodRD.tsv",col.names = FALSE,row.names = FALSE,quote = FALSE)

#Tidy up
rm(list=ls())

# TESTING... --------------------------------------------------------------
# require(org.Hs.eg.db)
# GeneSymbol <- mappedkeys(org.Hs.egSYMBOL2EG)
# HGNC <- read.table("http://www.genenames.org/cgi-bin/genefamilies/download-all/tsv",sep="\t")
