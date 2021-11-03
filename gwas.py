import wget
import subprocess
import os

genotype_file = "mouse_hs1940.vcf.gz"
phenotype_file = "mouse_hs1940.csv"

# downloading source files (genotype and phenotype) if not existent
if not os.path.isdir('input'):
    genotype_file_url = "https://raw.githubusercontent.com/frankvogt/vcf2gwas/main/files/Comparison/dataset/mouse_hs1940.vcf.gz"
    genotype_file = wget.download(genotype_file_url)

    phenotype_file_url = "https://raw.githubusercontent.com/frankvogt/vcf2gwas/main/files/Comparison/dataset/mouse_hs1940.csv"
    phenotype_file = wget.download(phenotype_file_url)

    command = "mkdir input"
    subprocess.run(command.split())
    command = f"mv {genotype_file} {phenotype_file} input/"
    subprocess.run(command.split())

# Association Tests with Univariate Linear Mixed Models
command  = f"vcf2gwas -v input/{genotype_file} -pf input/{phenotype_file} -p MCH -p CD8 -lmm -gf MM"
subprocess.run(command.split())