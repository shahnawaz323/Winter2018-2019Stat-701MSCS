A1 = c(0,0,10,10,20,20)
A2 = c(0,0,100,100,400,400)
B = c(5,7,15,17,9,11)
num = length(B)
TA1 = 0
TA2 = 0
A1mean = 0
A2mean = 0
Bmean = 0
TB = 0
for(I in 1:num){
  TA1 = TA1 + A1[I]
  TA2 =TA2 + A2[I]
  TB = TB + B[I]
}
A1mean = TA1/num
A2mean = TA2/num
Bmean = TB/num
Ta12 = 0
Ta22 = 0
Ta1b = 0
Ta2b = 0
Ta1a2 = 0
for(J in 1:num){
  Ta12 = Ta12 + ((A1[J] - A1mean) ^ 2)
  Ta22 = Ta22 + ((A2[J] - A2mean) ^ 2)
  Ta1b = Ta1b + ((A1[J] - A1mean) * (B[J] - Bmean))
  Ta2b = Ta2b + ((A2[J] - A2mean) * (B[J] - Bmean))
  Ta1a2 = Ta1a2 + ((A1[J] - A1mean) * (A2[J] - A2mean))
}
b1 = ((Ta22 * Ta1b) - (Ta1a2 * Ta2b)) / ((Ta12 * Ta22) - (Ta1a2 ^ 2))
b2 = ((Ta12 * Ta2b) - (Ta1a2 * Ta1b)) / ((Ta12 * Ta22) - (Ta1a2 ^ 2))
b0 = Bmean - (b1 * A1mean) - (b2 * A2mean)
RSS = 0
for(I in 1:num){
  Pvalue = b0 + (b1 * A1[I]) + (b2 * A2[I])
  RSS = RSS + (B[I] - Pvalue) ^ 2
}
MSE = RSS/(num-3)
VB1 = MSE * (Ta22 / (Ta12 * Ta22 - (Ta1a2 ^ 2)))
VB2 = MSE * (Ta12 / (Ta12 * Ta22 - (Ta1a2 ^ 2)))
VB0 = MSE * (1/num + ((A1mean ^ 2 * Ta22) + (A2mean ^ 2 * Ta12) - (2 * A1mean * A2mean * Ta1a2)) / ((Ta12 * Ta22) - Ta1a2 ^ 2))
cat("\nb0 = " , b0)
cat("\nb1 = " , b1)
cat("\nb2 = " , b2)
cat("\nEquation: B = " , b0, " + ",b1,"(A1) + ", b2 , "(A2)")
cat("\nMSE = " , MSE)
cat("\nV(B0) = " , VB0)
cat("\nV(B1) = " , VB1)
cat("\nV(B2) = " , VB2)