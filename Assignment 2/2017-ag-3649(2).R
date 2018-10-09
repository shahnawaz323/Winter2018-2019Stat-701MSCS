dframe = data.frame(
  
  fer = c(100,200,300,400,500,600,700),
  rain_fall = c(10, 20, 10, 30, 20, 20, 30),
  yield = c(40,50,50,70,65,65,80)
)


print(dframe)
fitmodel = lm(yield ~ fer + rain_fall, data = dframe)

print(summary(fitmodel))
cat("\n\n")
print(coefficients(fitmodel)) 
cat("\nY_hat\n")
print(fitted(fitmodel))
cat("\n\n")
print(anova(fitmodel))
cat("\n\n")
R2 = round(summary(fitmodel)$r.squared, 3)
sigma2 = round(summary(fitmodel)$sigma^2, 3)
print(paste("R^2 =", R2,
            collapse = " "))
print(paste("MSE =", sigma2,
            collapse = " "))

# Var of coefficients
print(vcov(fitmodel))

cat("\nConfidence Interval")
print(confint(fitmodel)) #confitence interval +- values

scatter_plot = scatterplot3d(dframe, 
                     main= "Linear reg Line",
                     xlab = "fer",
                     ylab = "rain_fall",
                     zlab = "Yield", color = "red"
)
scatter_plot$plane3d(fitmodel)