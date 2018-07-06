# About -------------------------------------------------------------------
# 28/03/2017
# BROCA genes
# - http://tests.labmed.washington.edu/BROCA


# Workspace ---------------------------------------------------------------
library(XML) # read table from website
library(biomaRt)
library(dplyr)

# Data prep ---------------------------------------------------------------
#get table from website
genes <- readHTMLTable("http://tests.labmed.washington.edu/BROCA")[[1]]
genes$Gene <- as.character(genes$Gene)

# make a list of BROCA genes
# split on space and /
geneList <- unlist(strsplit(genes$Gene, "/| "))
# remove word some words, "NEW", "Abraxas"
geneList <- geneList[!geneList %in% c("NEW", "Abraxas")]
# clean up some gene names
# "(+EPCAM)"
geneList <- sort(unique(gsub("(+EPCAM)", "EPCAM", geneList, fixed = TRUE)))

# Output ------------------------------------------------------------------
write.table(geneList, "BROCA_Cancer_Risk_Panel.tsv",
            col.names = FALSE, row.names = FALSE, quote = FALSE)

#Tidy up
rm(list = ls())
