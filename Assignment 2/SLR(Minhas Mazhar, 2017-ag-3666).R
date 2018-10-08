# clear all variables in the workspace
rm(list=ls(all=TRUE))

Income = c(80, 100, 120, 140, 160, 180, 200, 220, 240, 260)
Exp = c(70, 65, 90, 95, 110, 115, 120, 140, 155, 150)


SLR = function(predictor, target)
{
  sample.size = length(target)
  
  mean.predictor = mean(predictor)
  mean.target = mean(target)
  
  sxx = sum((predictor - mean.predictor)^2)
  sxy = sum((predictor - mean.predictor)*(target - mean.target))
  
  beta1.hat = sxy/sxx
  beta0.hat = mean.target - beta1.hat*mean.predictor
  
  target.fitted = beta0.hat + beta1.hat*predictor
  target.residuals = target - target.fitted
  sum.squared.residuals = sum(target.residuals^2)
  tss = sum((target - mean.target)^2)
  allprecited = sum(target.fitted)
  mss = sum((target.fitted - mean.target)^2)
  rss = sum((target - target.fitted)^2)
  rsquare = mss/tss
  
  
  degree.freedom = sample.size - 2
  mean.squared.error = sum.squared.residuals/degree.freedom
  standard.error = sqrt(mean.squared.error)
  
  beta0.hat.sample.variance = mean.squared.error*(1/sample.size + mean.predictor^2/sxx)
  beta0.hat.standard.error = sqrt(beta0.hat.sample.variance)
  
  beta1.hat.sample.variance = mean.squared.error/sxx
  beta1.hat.standard.error = sqrt(beta1.hat.sample.variance)
  
  t.beta0.hat = beta0.hat/beta0.hat.standard.error
  t.beta1.hat = beta1.hat/beta1.hat.standard.error
  
  p.value.beta0.hat = 2*pt(abs(t.beta0.hat), degree.freedom, lower.tail = F)
  p.value.beta1.hat = 2*pt(abs(t.beta1.hat), degree.freedom, lower.tail = F)
  
  
  cat("Mean of X = ", mean.predictor, "\n")
  cat("Mean of Y = ", mean.target, "\n")
  cat("Y-intercept (b0) = ", beta0.hat, "\n")
  cat("Regression Co-efficient (b1) = ", beta1.hat, "\n")
  cat("Y-Predicted = ", beta0.hat," + ",beta1.hat,"X", "\n")
  cat("Sum of the Product of Deviations of X and Y (Sxy) = ", sxy , "\n")
  cat("Sum of Deviations of X (Sxx) = ", sxx, "\n")
  cat("Sum of all Y-Predicted values is = ", allprecited , "\n")
  cat("Total Sum of Squares (TSS) = ", tss, "\n")
  cat("Model/Regression Sum of Squares (MSS/SSR) = ", mss , "\n")
  cat("Residual/Error Sum of Square (RSS/SSE) = ", rss , "\n")
  cat("Co-efficient of Determination (R^2) = ", rsquare , "\n")
  
  plot(predictor ~ target,
       xlab = "Income",
       ylab = "Expenditures",
       main = "Relationship Between Income and Expenditures")
  
  lm(predictor ~ target)
  abline(lm(predictor ~ target))
  
  
}

Exp.data = cbind(Income, Exp)
colnames(Exp.data) = c('Income', 'Expenditures')
Exp.data

# let's conduct simple linear regression on data by calling our function
Exp.regression <- SLR(Income, Exp)
Exp.regression





