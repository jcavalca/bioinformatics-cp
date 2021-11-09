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

    GEMMA_Options()

    return 1

def GEMMA_Options():
    print("Here are the questions regarded about GEMMA models:")
    print("What model do you want to run?")
    print("     (1) Linear Model Analysis")
    print("     (2) Linear Mixed Model Analysis")
    print("     (3) Bayesian Sparse Linear Mixed Model Analysis")
    print("Please enter 1, 2, or 3: ", end=" ")
    model_type = input()

    if (model_type == "1"):
        command = "-p 1 -lm"
    elif (model_type == "2"):
        # still need to fix what if only one phenotype is given
        print("What phenotypes do you want to run?")
        print("For example, if you want to run CD8 (1st column), MCH (2nd column), and avrRpm (4th column) phenotype independently," +
            "you can enter CD8 MCH avrRpm, or you can enter 1 2 4")
        print("Please enter name of phenotype(s) listed on your phenotype file or coloumn(s) of the phenotype(s): ", end=" ")
        number_of_phenotypes = input().split(" ")
        number_of_phenotypes = " -p ".join(number_of_phenotypes)
        command = f"-p {number_of_phenotypes} -lmm --multi"
        print(command)
    # elif (model_type == "3"):
        
    return 1

if __name__ == "__main__":
    main()
