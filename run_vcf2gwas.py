import wget
import subprocess
import os
import re

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
    print("Please enter VFC file (.vcf or .vcf.gz): ")
    vcf_file = input()

    x = re.search(".vcf|.vcf.gz", vcf_file)
    while x == None:
        print("Invalid vcf file")
        print("Please enter VFC file (.vcf or .vcf.gz): ")
        vcf_file = input()
        x = re.search(".vcf|.vcf.gz", vcf_file)
    
    print("Please enter phenotype file (.csv): ")
    phenotype = input()

    x = re.search(".csv", phenotype)
    while x == None:
        print("Invalid Phenotype file")
        print("Please enter phenotype file (.csv): ")
        phenotype = input()
        x = re.search(".csv", phenotype)

    

    try:
        file_genotype = open(vcf_file)
        file_phenotype = open(phenotype)
    except:
        print("One or more files cannot be found")
        print("Running GWAS on mouse1940 data using lmm ...")
        run_mouse1940()
        return

    #command  = f"vcf2gwas -v {genotype} -pf {phenotype} {flags}"
    #subprocess.run(command.split())

    complete = GEMMA_Options(vcf_file, phenotype)
    if complete == 1:
        print("\nvcf2gwas Analysis Complete!\n")
    else:
        print("\nUnable to Run vcf2gwas Analysis\n")

    return 1

def GEMMA_Options(vcf_file, phenotype):
    print()
    print("Here are the questions regarded about GEMMA models:")
    print("What model do you want to run?")
    print("     (1) Linear Model Analysis")
    print("     (2) Linear Mixed Model Analysis")
    print("     (3) Bayesian Sparse Linear Mixed Model Analysis")
    print("     (4) Multivariate Linear Mixed Model Analysis")
    print("Please enter 1, 2, 3, or 4: ", end=" ")
    model_type = input()

    if (model_type == "1"):
        print("\nWhat phenotypes do you want to run?")
        print("For example, if you want to run CD8 (1st column), MCH (2nd column), \nand avrRpm (4th column) phenotype independently," +
            "you can enter CD8 MCH avrRpm, or you can enter 1 2 4")
        print("Please enter name of phenotype(s) listed on your phenotype file or coloumn(s) of the phenotype(s): ", end=" ")
        number_of_phenotypes = input().split(" ")
        number_of_phenotypes = " -p ".join(number_of_phenotypes)

        print("\nSpecify which Frequentist Test to use for Linear Model")
        print("(1) wald test")
        print("(2) likelihood ratio test")
        print("(3) score test")
        print("(4) all three tests")
        test = input()
        command = f"vcf2gwas -v {vcf_file} -pf {phenotype} -p {number_of_phenotypes} -lm {test}"
        subprocess.run(command.split())
        return 1
    elif (model_type == "2"):
        # still need to fix what if only one phenotype is given
        print("\nWhat phenotypes do you want to run?")
        print("For example, if you want to run CD8 (1st column), MCH (2nd column), \nand avrRpm (4th column) phenotype independently," +
            "you can enter CD8 MCH avrRpm, or you can enter 1 2 4")
        print("Please enter name of phenotype(s) listed on your phenotype file or coloumn(s) of the phenotype(s): ", end=" ")
        number_of_phenotypes = input().split(" ")
        number_of_phenotypes = " -p ".join(number_of_phenotypes)

        print("\nSpecify which Frequentist Test to use for Linear Mixed Model")
        print("(1) wald test")
        print("(2) likelihood ratio test")
        print("(3) score test")
        print("(4) all three tests")
        test = input()
        command = f"vcf2gwas -v {vcf_file} -pf {phenotype} -p {number_of_phenotypes} -lmm {test}"
        print(command)
        subprocess.run(command.split())
        return 1
    elif (model_type == "3"):
        print("\nWhat phenotypes do you want to run?")
        print("For example, if you want to run CD8 (1st column), MCH (2nd column), \nand avrRpm (4th column) phenotype independently," +
            "you can enter CD8 MCH avrRpm, or you can enter 1 2 4")
        print("Please enter name of phenotype(s) listed on your phenotype file or coloumn(s) of the phenotype(s): ", end=" ")
        number_of_phenotypes = input().split(" ")
        number_of_phenotypes = " -p ".join(number_of_phenotypes)

        print("\nSpecify which Frequentist Test to use for Bayesian Sparse Linear Mixed Model")
        print("(1) wald test")
        print("(2) likelihood ratio test")
        print("(3) score test")
        print("(4) all three tests")
        test = input()
        command = f"vcf2gwas -v {vcf_file} -pf {phenotype} -p {number_of_phenotypes} -bslmm {test}"
        subprocess.run(command.split())
        return 1
    elif (model_type == "4"):
        print("\nWhat phenotypes do you want to run?")
        print("For example, if you want to run CD8 (1st column), MCH (2nd column), \nand avrRpm (4th column) phenotype independently," +
            "you can enter CD8 MCH avrRpm, or you can enter 1 2 4")
        print("Please enter name of phenotype(s) listed on your phenotype file or coloumn(s) of the phenotype(s): ", end=" ")
        number_of_phenotypes = input().split(" ")
        number_of_phenotypes = " -p ".join(number_of_phenotypes)

        print("\nSpecify which Frequentist Test to use for Multivariate Linear Mixed Model")
        print("(1) wald test")
        print("(2) likelihood ratio test")
        print("(3) score test")
        print("(4) all three tests")
        test = input()
        command = f"vcf2gwas -v {vcf_file} -pf {phenotype} -p {number_of_phenotypes} -lmm {test} -m"
        print(command)
        subprocess.run(command.split())
        return 1
        
    return 0

if __name__ == "__main__":
    main()
