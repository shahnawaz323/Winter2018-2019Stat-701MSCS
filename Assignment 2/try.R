# clear all variables in the workspace
install.packages("scatterplot3d") 
library("scatterplot3d") 
rm(list=ls(all=TRUE))
dependenty = c(5,7,15,17,9,11)
independentX1 = c(0,0,10,10,20,20)
independentX2= c(0,0,100,100,400,400)
df = data.frame(dependenty,independentX1,independentX2)
data(df)
head(df)
scatterplot3d(x=dependenty, y=independentX1, z=independentX2)
s3d <- scatterplot3d(df, type = "p", color = "blue",
                     angle=55, pch =16,grid=TRUE, box=FALSE,
                     main="Multiple Linear Regression \n By Ramsha Nazeer \n 2017-ag-3697",
                     xlab = "X1",
                     ylab = "X2",
                     zlab = "Y")

my.lm <- lm(dependenty~independentX1+independentX2)

s3d$plane3d(my.lm, lty.box = "solid",  draw_polygon = TRUE)


MLR = function(Y, X1, X2)
{
  sample.size = length(Y)
  K =3
  cat("length = ", sample.size, "\n")
  mean.Y = mean(Y)
  mean.X1 = mean(X1)
  mean.X2 = mean(X2)
  
  cat("mean of Y = ", mean.Y, "\n")
  cat("mean of X1 = ", mean.X1, "\n")
  cat("mean of X2 = ", mean.X2, "\n","\n")
  
  sumy=sum(Y)
  sumx1=sum(X1)
  sumx2=sum(X2)
  sumx1x1=sum(X1*X1)
  sumx2x2=sum(X2*X2)
  sumx1x2=sum(X1*X2)
  sumx1y=sum(X1*Y)
  sumx2y=sum(X2*Y)
  sumyy=sum(Y*Y)
  
  Sx1x1=sumx1x1-(sumx1^2/sample.size)
  Sx2x2=sumx2x2-(sumx2^2/sample.size)
  Sx1y=sumx1y-(sumx1*sumy/sample.size)
  Sx2y=sumx2y-(sumx2*sumy/sample.size)
  Sx1x2=sumx1x2-(sumx1*sumx2/sample.size)
  Syy=sumyy-(sumy^2/sample.size)
  
  
  b1=(Sx2x2*Sx1y-Sx1x2*Sx2y)/(Sx1x1*Sx2x2-Sx1x2^2)
  b2=(Sx1x1*Sx2y-Sx1x2*Sx1y)/(Sx1x1*Sx2x2-Sx1x2^2)
  b0=mean.Y-(b1*mean.X1)-(b2*mean.X2)
  
  Y.heat= b0+b1*X1+b2*X2
  sumY.heat=sum(Y.heat)
  TSS=sum((Y-mean.Y)^2)
  MSS=sum((Y.heat-mean.Y)^2)
  RSS=sum((Y-Y.heat)^2)
  R2=RSS/TSS
  sigma.heat2=RSS/(sample.size - K)
  variance.B1.hat=sigma.heat2*(Sx2x2/(Sx1x1*Sx2x2-Sx1x2^2))
  variance.B2.hat=sigma.heat2*(Sx1x1/(Sx1x1*Sx2x2-Sx1x2^2))
  variance.B0.hat=sigma.heat2*((1/sample.size)+((mean.X1^2*Sx2x2+mean.X2^2*Sx1x1-2*mean.X1*mean.X2*Sx1x2)/(Sx1x1*Sx2x2-Sx1x2^2)))
 
  cat("sum y = ", sumy, "\n")
  cat("sum x1 = ", sumx1, "\n")
  cat("sum x2 = ", sumx2, "\n")
  cat("sum x1x1 = ", sumx1x1, "\n")
  cat("sum x2x2 = ", sumx2x2, "\n")
  cat("sum x1x2 = ", sumx1x2, "\n")
  cat("sum x1y = ", sumx1y, "\n")
  cat("sum x2y = ", sumx2y, "\n")
  cat("sum yy = ", sumyy, "\n")
  
  cat("Sx1x1 = ", Sx1x1, "\n")
  cat("Sx2x2 = ", Sx2x2, "\n")
  cat("Sx1y = ", Sx1y, "\n")
  cat("Sx2y = ", Sx2y, "\n")
  cat("Sx1x2 = ", Sx1x2, "\n")
  cat("Syy = ", Syy, "\n","\n")
  
  cat("b0 = ", b0, "\n")
  cat("b1 = ", b1, "\n")
  cat("b2 = ", b2, "\n","\n")

  cat("Y = ", b0," + ",b1,"X1",b2,"X2", "\n")
  cat("sum of all y values = ", sumY.heat, "\n","\n")
  
  cat("TSS = ", TSS, "\n")
  cat("MSS = ", MSS, "\n")
  cat("RSS = ", RSS, "\n")
  cat("R2 = ", R2, "\n")
  cat("sigma.heat2 = ", sigma.heat2, "\n")
  cat("variance of B1.hat =",variance.B1.hat,"\n")
  cat("variance of B2.hat =",variance.B2.hat,"\n")
  cat("variance of B0.hat =",variance.B0.hat,"\n")
 
}

Exp.data = cbind(dependenty, independentX1, independentX2)
colnames(Exp.data) = c('dependenty', 'independentX1', 'independentX2')
Exp.data

# let's conduct simple linear regression on data by calling our function
Exp.regression <- MLR(dependenty, independentX1, independentX2)
Exp.regression






