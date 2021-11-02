import wget


# downloading source files (genotype and phenotype)

phenotype_file_url = "https://raw.githubusercontent.com/frankvogt/vcf2gwas/main/files/Comparison/dataset/mouse_hs1940.csv"
genotype_file_url = "https://raw.githubusercontent.com/frankvogt/vcf2gwas/main/files/Comparison/dataset/mouse_hs1940.vcf.gz"
phenotype_file = wget.download(phenotype_file_url)
genotype_file = wget.download(genotype_file_url)