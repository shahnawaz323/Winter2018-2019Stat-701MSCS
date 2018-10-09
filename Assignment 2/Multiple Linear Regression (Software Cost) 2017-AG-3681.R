Data = data.frame(
  X1 = c(2,3,7,9,11),
  X2 = c(4,8,14,16,10),
  Y = c(42,63,80,85,90),
  stringsAsFactors = FALSE
)
n = length(Data[[1]])
sumOfX1 = 0
sumOfX2 = 0
sumOfY = 0
for(k in 1:n){
  sumOfX1 = sumOfX1 + Data[k,1]
  sumOfX2 = sumOfX2 + Data[k,2]
  sumOfY = sumOfY + Data[k,3]
}
meanOfX1 = sumOfX1/n
meanOfX2 = sumOfX2/n
meanOfY = sumOfY/n
sumOfx12 = 0
sumOfx22 = 0
sumOfx1y = 0
sumOfx2y = 0
sumOfx1x2 = 0
temp = 0
for(k in 1:n){
  temp = (Data[k,1] - meanOfX1) ^ 2
  Data$"(x1)2"[[k]] =  temp
  sumOfx12 = sumOfx12 + temp
  temp = (Data[k,2] - meanOfX2) ^ 2
  Data$"(x2)2"[[k]] =  temp
  sumOfx22 = sumOfx22 + temp
  temp = ((Data[k,1] - meanOfX1) * (Data[k,3] - meanOfY))
  Data$"(x1y)"[[k]] =  temp
  sumOfx1y = sumOfx1y + temp
  temp = ((Data[k,2] - meanOfX2) * (Data[k,3] - meanOfY))
  Data$"(x2y)"[[k]] =  temp
  sumOfx2y = sumOfx2y + temp
  temp = ((Data[k,1] - meanOfX1) * (Data[k,2] - meanOfX2))
  Data$"(x1x2)"[[k]] =  temp
  sumOfx1x2 = sumOfx1x2 + temp
}
b1 = ((sumOfx22 * sumOfx1y) - (sumOfx1x2 * sumOfx2y)) / ((sumOfx12 * sumOfx22) - (sumOfx1x2 ^ 2))
b2 = ((sumOfx12 * sumOfx2y) - (sumOfx1x2 * sumOfx1y)) / ((sumOfx12 * sumOfx22) - (sumOfx1x2 ^ 2))
b0 = meanOfY - (b1 * meanOfX1) - (b2 * meanOfX2)
SSE = 0
SSR = 0
SST = 0
sumOfYhat = 0;
for(k in 1:n){
  temp = b0 + (b1 * as.numeric(Data[k,1])) + (b2 * as.numeric(Data[k,2]))
  sumOfYhat = sumOfYhat + temp
  Data$"Y-Hat"[[k]] =  temp
  temp = (as.numeric(Data[k,3]) - (b0 + (b1 * as.numeric(Data[k,1])) + (b2 * as.numeric(Data[k,2])))) ^ 2
  Data$"(Y-Y-Hat)2"[[k]] =  temp
  SSE = SSE + as.numeric(temp)
  temp = ((as.numeric(Data[k,3])) - meanOfY) ^ 2
  Data$"(Y-Ymean)2"[[k]] =  temp
  SST = SST + temp
  temp = ((as.numeric(Data[k,9])) - meanOfY) ^ 2
  Data$"(Y_hat-Ymean)2"[[k]] =  temp
  SSR = SSR + as.numeric(temp)
}
SS = data.frame(
  X1 = paste("Sum = ",sumOfX1),
  X2 = paste("Sum = ",sumOfX2),
  Y = paste("Sum = ",sumOfY),
  "(x1)2" = paste("Sum = ",sumOfx12),
  "(x2)2" = paste("Sum = ",sumOfx22),
  "(x1y)" = paste("Sum = ",sumOfx1y),
  "(x2y)" = paste("Sum = ",sumOfx2y),
  "(x1x2)" = paste("Sum = ",sumOfx1x2),
  "Y-hat" = paste("Sum = ", sumOfYhat),
  "(Y-Y-hat)2" = paste("Sum = ",SSE),
  "(Y-Ymean)2" = paste("Sum = ",SST),
  "(Y_hat-Ymean)2" = paste("Sum = ",SSR),
  stringsAsFactors = FALSE
)
for(j in 1:12){
  Data[8,j] = SS[1,j]
}
R2 = (SSR/SST) * 100
MSE = SSE/(n-3);
VB1 = MSE * (sumOfx22 / (sumOfx12 * sumOfx22 - (sumOfx1x2 ^ 2)))
VB2 = MSE * (sumOfx12 / (sumOfx12 * sumOfx22 - (sumOfx1x2 ^ 2)))
VB0 = MSE * (1/n + ((meanOfX1 ^ 2 * sumOfx22) + (meanOfX2 ^ 2 * sumOfx12) - (2 * meanOfX1 * meanOfX2 * sumOfx1x2)) / ((sumOfx12 * sumOfx22) - sumOfx1x2 ^ 2))
cat("\n\nb0: ",b0)
cat("\nb1: ",b1)
cat("\nb2: ",b2)
cat("\nY = ",b0," + ",b1," (X1) + ",b2," (X2)")
cat("\nSST: ",SST)
cat("\nSSR: ",SSR)
cat("\nSSE: ",SSE)
cat("\nR2: ",R2)
cat("\nMSE: ",MSE)
cat("\nV(B0): ",VB0)
cat("\nV(B1): ",VB1)
cat("\nV(B2): ",VB2)