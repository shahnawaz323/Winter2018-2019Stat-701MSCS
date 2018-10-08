# from matplotlib import pyplot as plt
import numpy as np
# import pandas as pd
# import math as math
# from statsmodels.formula.api import ols
# from statsmodels.stats.anova import anova_lm

Y = np.array([5, 7, 15, 17, 9, 11])
X1 = np.array([0, 0, 10, 10, 20, 20])
X2 = np.array([0, 0, 100, 100, 400, 400])

n = Y.size
K = 3
Y_mean = sum(Y)/n
X1_mean = sum(X1)/n
X2_mean = sum(X2)/n

print(" mean of y = ", Y_mean)
print(" mean of X1 = ", X1_mean)
print(" mean of X2 = ", X2_mean)

sum_y = np.sum(Y)
print(" sum_y = ", sum_y)
sum_x1 = np.sum(X1)
print(" sum_x1 = ", sum_x1)
sum_x2 = np.sum(X2)
print(" sum_x2 = ", sum_x2)
sum_x1x1 = np.sum(X1 * X1)
print(" sum_x1x1 = ", sum_x1x1)
sum_x2x2 = np.sum(X2 * X2)
print(" sum_x2x2 = ", sum_x2x2)
sum_x1x2 = np.sum(X1 * X2)
print(" sum_x1x2 = ", sum_x1x2)
sum_x1y = np.sum(X1 * Y)
print(" sum_x1y = ", sum_x1y)
sum_x2y = np.sum(X2 * Y)
print(" sum_x2y = ", sum_x2y)
sum_yy = np.sum(Y * Y)
print(" sum_yy = ", sum_yy)

S_x1x1 = float(sum_x1x1-sum_x1 ** 2/n)
S_x2x2 = (sum_x2x2-(sum_x2 ** 2/n))
S_x1y = (sum_x1y-(sum_x1*sum_y/n))
S_x2y = (sum_x2y-(sum_x2*sum_y/n))
S_x1x2 = (sum_x1x2-(sum_x1*sum_x2/n))
S_yy = (sum_yy-(sum_y ** 2/n))

b1 = float((S_x2x2*S_x1y-S_x1x2*S_x2y)/(S_x1x1*S_x2x2-S_x1x2 ** 2))
b2 = float((S_x1x1*S_x2y-S_x1x2*S_x1y)/(S_x1x1*S_x2x2-S_x1x2 ** 2))
b0 = float(Y_mean-(b1*X1_mean)-(b2*X2_mean))

Y_heat = b0 + b1 * X1 + b2 * X2
sum_Y_heat = sum(Y_heat)
TSS = np.sum((Y - Y_mean) ** 2)
MSS = np.sum((Y_heat - Y_mean) ** 2)
RSS = np.sum((Y - Y_heat) ** 2)
R2 = float(RSS / TSS)
sigma_heat2 = RSS / (n - K)

variance_B1_hat = sigma_heat2*(S_x2x2/(S_x1x1*S_x2x2-S_x1x2 ** 2))
variance_B2_hat = sigma_heat2*(S_x1x1/(S_x1x1*S_x2x2-S_x1x2 ** 2))
v_B0 = sigma_heat2*((1/n)+((X1_mean ** 2*S_x2x2+X2_mean ** 2*S_x1x1-2*X1_mean*X2_mean*S_x1x2)/(S_x1x1*S_x2x2-S_x1x2 ** 2)))

print("b0 = ", b0)
print("b1 = ", b1)
print("b2 = ", b2)
print("Y = ", b0, " + ", b1, "X1", b2, "X2")
print("sum of all y values = ", sum_Y_heat)
print("TSS = ", TSS)
print("MSS = ", MSS)
print("RSS = ", RSS)
print("R2 = ", R2)
print("sigma.heat2 = ", sigma_heat2)
print("variance of B1.hat =", variance_B1_hat)
print("variance of B2.hat =", variance_B2_hat)
print("variance of B0.hat =", v_B0)
