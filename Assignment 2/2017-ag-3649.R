dframe = data.frame(
  
  x1 = c(0, 0, 10, 10, 20, 20),
  x2 = c(0, 0, 100, 100, 400, 400),
  y = c(5, 7, 15, 17, 9, 11)
)


print(dframe)
fitmodel = lm(y ~ x1 + x2, data = dframe)

print(summary(fitmodel))
cat("\n\n")
print(coefficients(fitmodel))
cat("\nY_hat\n")
print(fitted(fitmodel))
cat("\n\n")
print(anova(fitmodel))
cat("\n\n")
R2 = round(summary(fitmodel)$r.squared, 3) 
mse = round(summary(fitmodel)$sigma^2, 3)
print(paste("R^2 =", R2,
            collapse = " "))
print(paste("MSE =", mse,
            collapse = " "))
print(vcov(fitmodel))

cat("\nConfidence Interval")
print(confint(fitmodel))

scatter_plot = scatterplot3d(dframe, 
                     xlab = "x1",
                     ylab = "x2",
                     zlab = "y", color = "red"
)
scatter_plot$plane3d(fitmodel)