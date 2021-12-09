# bioinformatics-cp
This is Group 6 for Bioinformatics class.   
Fresh Functions Group



# How to Install vcf2gwas
1. Install conda   
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
2. Once conda is installed, create a new environment (myenv can be changed to any name)   
```
conda create -n myenv
```
3. Next, activate your environment  
```
conda activate myenv
```
4. Next, install the vcf2gwas package  
```
conda install vcf2gwas -c conda-forge -c bioconda -c fvogt257
```  
5. Next, install wget (for refactored vcf2gwas)
```
pip install wget
```
You are now ready to run vcf2gwas  


# Running refactor vcf2gwas
Follow the prompts after using the following command
```
python3 run_vcf2gwas.py
```

# For More Detailed Instructions
Please visit https://github.com/frankvogt/vcf2gwas/blob/main/README.md
