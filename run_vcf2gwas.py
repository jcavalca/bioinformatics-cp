import os


def main():
    print("Please enter genotype file: ")
    genotype = input()
    print("Please enter phenotype file: ")
    phenotype = input()

    try:
        file_genotype = open(genotype)
        file_phenotype = open(phenotype)
    except:
        print("One or more files cannot be found")
        return


    return 1

if __name__ == "__main__":
    main()