#dummy data
set.seed(123)
#phenotype
phenotype <- data.frame(
  a_menopause=sample(c(0,1),10,replace=TRUE),
  country=sample(letters[1:3],10,replace=TRUE))
#genotype
genotype <- 
  read.table(text="SNP1   SNP2    SNP3    SNP4
             1   0   1   1
             2    0   2   1
             0    0   0   1
             0    0   0   1
             0    1   0   1
             1    1   0   1
             1    2   0   1
             1    2   1   2
             0    0   0   1
             0    1   0   1
             ",header=TRUE)
#data for lm
fitDat <- cbind(phenotype,genotype)

#get fit for all SNPs
fitAllSNPs <-
  lapply(colnames(fitDat)[3:6], function(SNP){
    fit <- lm(paste("a_menopause ~ country + ", SNP), 
              data=fitDat)
  })

#extract coef for each SNP
lapply(fitAllSNPs,coef)