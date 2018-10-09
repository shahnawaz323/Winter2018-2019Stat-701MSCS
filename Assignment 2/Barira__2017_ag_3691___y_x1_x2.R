# BARIRA HABIB
# 17-AG-3671
# MSCS

library("scatterplot3d")

    dframe = data.frame(
      x1 = c(0, 0, 10, 10, 20, 20),
      
      x2 = c(0, 0, 100, 100, 400, 400),
      
      y = c(5, 7, 15, 17, 9, 11))

      
  print(dframe)
  fit = lm(y ~ x1 + x2, data = dframe)

  cat("\n\nSUMMARY\n")
  print(summary(fit))
  
  cat("\n\n")
  print(coefficients(fit))
  
  cat("\n\nY_hat\n")
  print(fitted(fit))
  
  cat("\n\n")
  print(anova(fit))
  
  cat("\n\n")
  rsqr = summary(fit)$r.squared
  sigmasqr = summary(fit)$sigma^2
  
  print(paste("R2 =", rsqr,
              collapse = " "))
  print(paste("MSE =", sigmasqr,
              collapse = " "))
  
  plot = scatterplot3d(dframe, type = "h", color = "red"
                       ,grid=TRUE,
                       
                       main = "Linear Regression of x1, x2 and y",
                       xlab = "X1", ylab = "x2",
                       zlab = "y"
  )  

  cat("\n\n")
  print(vcov(fit))