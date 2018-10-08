# from matplotlib import pyplot as plt
import numpy as np
# import pandas as pd
# import math as math
# from statsmodels.formula.api import ols
# from statsmodels.stats.anova import anova_lm

Yield = np.array([40, 50, 50, 70, 65, 65, 80])
fertilizer = np.array([100, 200, 300, 400, 500, 600, 700])
rainfall = np.array([10, 20, 10, 30, 20, 20, 30])

n = Yield.size
K = 3
Y_mean = sum(Yield)/n
X1_mean = sum(fertilizer)/n
X2_mean = sum(rainfall)/n

print(" mean of y = ", Y_mean)
print(" mean of X1 = ", X1_mean)
print(" mean of X2 = ", X2_mean)

sum_y = np.sum(Yield)
print(" sum_y = ", sum_y)
sum_x1 = np.sum(fertilizer)
print(" sum_x1 = ", sum_x1)
sum_x2 = np.sum(rainfall)
print(" sum_x2 = ", sum_x2)
sum_x1x1 = np.sum(fertilizer * fertilizer)
print(" sum_x1x1 = ", sum_x1x1)
sum_x2x2 = np.sum(rainfall * rainfall)
print(" sum_x2x2 = ", sum_x2x2)
sum_x1x2 = np.sum(fertilizer * rainfall)
print(" sum_x1x2 = ", sum_x1x2)
sum_x1y = np.sum(fertilizer * Yield)
print(" sum_x1y = ", sum_x1y)
sum_x2y = np.sum(rainfall * Yield)
print(" sum_x2y = ", sum_x2y)
sum_yy = np.sum(Yield * Yield)
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

Y_heat = b0 + b1 * fertilizer + b2 * rainfall
sum_Y_heat = sum(Y_heat)
TSS = np.sum((Yield - Y_mean) ** 2)
MSS = np.sum((Y_heat - Y_mean) ** 2)
RSS = np.sum((Yield - Y_heat) ** 2)
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
