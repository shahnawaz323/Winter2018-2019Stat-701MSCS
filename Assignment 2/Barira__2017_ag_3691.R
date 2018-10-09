
library("scatterplot3d")

    dframe = data.frame(
    fert = c(100,200,300,400,500,600,700),
    rain = c(10, 20, 10, 30, 20, 20, 30),
    Yield = c(40,50,50,70,65,65,80))

      
  print(dframe)
  fit = lm(Yield ~ fert + rain, data = dframe)

  cat("\n\nSUMMARY\n")
  print(summary(fit))
  
  cat("\n\n")
  print(coefficients(fit))
  
  cat("\n\nY_hat\n")
  print(fitted(fit))
  
  cat("\n\n")
  print(anova(fit))
  
  cat("\n\n")
  rsqr = round(summary(fit)$r.squared, 3)
  sigmasqr = round(summary(fit)$sigma^2, 3)
  
  print(paste("R2 =", rsqr,
              collapse = " "))
  print(paste("MSE =", sigmasqr,
              collapse = " "))
  
  plot = scatterplot3d(dframe, type = "h", color = "red"
                       ,grid=TRUE,
                       
                       main = "Linear Regression of Fertilizer, Rainfall and Yield",
                       xlab = "Fertilizer", ylab = "Rainfall",
                       zlab = "Yield"
  )  

  cat("\n\n")
  print(vcov(fit))