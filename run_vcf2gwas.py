import os
import subprocess

import wget
import subprocess
import os

# When user doesn't input valid files, it runs a GWAS analysis on 
# GEMMA's mouse1940 data
def run_mouse1940():
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

def main():
    print("Please enter genotype file: ")
    genotype = input()
    print("Please enter phenotype file: ")
    phenotype = input()
    print("Please enter command flags: ")
    flags = input()

    try:
        file_genotype = open(genotype)
        file_phenotype = open(phenotype)
    except:
        print("One or more files cannot be found")
        print("Running GWAS on mouse1940 data using lmm ...")
        run_mouse1940()
        return

    command  = f"vcf2gwas -v {genotype} -pf {phenotype} {flags}"
    subprocess.run(command.split())
    return 1

if __name__ == "__main__":
    main()