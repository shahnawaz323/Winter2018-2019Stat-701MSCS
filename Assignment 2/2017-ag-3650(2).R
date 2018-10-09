#Programe For the Simple Linear regression and the Multiple linear regression
#Add a Library For the 3 dimensions Ploting

Fit = function() {

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
  
  # Variance of coefficients
  print(vcov(reg))
  
  cat("\nConfidence Interval")
  print(confint(regression)) #confitence interval +- values
 
}
hypothesis_test = function(){
  Fstatsval = round(summary(regression)$fstatistic[1], 3)   # Extract F stats value
  cat("\n\n")
  print(paste("Test Hypothesis\nH0: B1 = B2 = B3 = 0", "on table value", Ftestval,
              "\n where alpha = 5%...", collapse = " "))
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
                         main= "Regression Line for Yield ~ Fertilizer + Rainfall",
                         xlab = "Fertilizer",
                         ylab = "Rainfall",
                         zlab = "Yield", pch = 2, color = "blue"
    )
    plot$plane3d(regression)
  
}


#### MAIN

    dataframe = data.frame(
      
      Fertilizer = c(100,200,300,400,500,600,700),
      
      Rainfall = c(10, 20, 10, 30, 20, 20, 30),
      
      yield = c(40,50,50,70,65,65,80))
    
    Ftestval= 6.94
  
  print(dataframe)
  regression = lm(yield ~ Fertilizer + Rainfall, data = dataframe)
  plot_regression()
  Fit()
  
  cat("\n\n")
  #Hypothesis
  hypothesis_test()

  