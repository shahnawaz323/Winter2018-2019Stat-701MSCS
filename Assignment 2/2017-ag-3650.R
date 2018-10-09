#Programe For the Simple Linear regression and the Multiple linear regression
#Add a Library For the 3 dimensions Ploting
library(scatterplot3d)

fit = function() {
  cat("\nSummary\n")
  print(summary(regression)) #summary for variable detail
  cat("\n\n")
  print(coefficients(regression)) #coefficent for b0 and b1,b2 values 
  cat("\nY_hat\n")
  print(fitted(regression)) #fitted for calculating Y hat values
  cat("\n\n")
  print(anova(regression)) #anova for complete anova table tells us how much depend a variable
  cat("\n\n")
  coef_det = round(summary(regression)$r.squared, 3) #$ sign for fetching the values from summary (r2 values)
  sigma = round(summary(regression)$sigma^2, 3)
  print(paste("R^2 =", coef_det,
              collapse = " ")) #for space in center
  print(paste("MSE =", sigma,
              collapse = " "))
  
  # V(b0), v(b1) and V(b2) values
  print(vcov(reg))
  
  cat("\nConfidence Interval\n")
  print(confint(regression)) #confitence interval +- values
  
}
hypothesis_test = function(){
    cat("\n\n")
  Fstatsval = round(summary(regression)$fstatistic[1], 3)   # Extract F stats value
  print(paste("Test Hypothesis\nH0: B1 = B2 = B3 = 0", "on table value",
              Ftestval,"\n where alpha = 5%...", collapse = " "))
  if(Fstatsval > Ftestval) {
    print(paste("Since Fc =", Fstatsval,
                "<", Ftestval, "so reject H0",
                collapse = " "))
  }
  else {
    print(paste("Since Fc =", Fstatsval,
                "<", Ftestval, "so accept H0",
                collapse = " "))
  }
}
plot_regression = function(){
  
  plot = scatterplot3d(dataframe, 
                       main= "Multiple Linear Regression Line for Y, X1 & X2",
                       xlab = "X1",
                       ylab = "X2",
                       zlab = "Y",
                       color = "blue",
                       box=FALSE,
                       pch = 2
  )
  plot$plane3d(regression)
  
}


#### MAIN

dataframe = data.frame(
  x1 = c(0, 0, 10, 10, 20, 20),
  
  x2 = c(0, 0, 100, 100, 400, 400),
  
  y = c(5, 7, 15, 17, 9, 11))

Ftestval= 9.55

print(dataframe)
regression = lm(y ~ x1 + x2, data = dataframe)
plot_regression()
fit()

cat("\n\n")
#Hypothesis
hypothesis_test()

