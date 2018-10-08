import numpy as np
picture_Graphics = np.array([15, 17, 115, 117, 19, 111])
Color_Combinations = np.array([10, 10, 110, 110, 120, 120])
Axis_Depth = np.array([10, 10, 1100, 1100, 1400, 1400])

n = picture_Graphics.size
K = 3
Y_mean = sum(picture_Graphics)/n
X1_mean = sum(Color_Combinations)/n
X2_mean = sum(Axis_Depth)/n

print(" mean of y = ", Y_mean)
print(" mean of X1 = ", X1_mean)
print(" mean of X2 = ", X2_mean)

sum_y = np.sum(picture_Graphics)
print(" sum_y = ", sum_y)
sum_x1 = np.sum(Color_Combinations)
print(" sum_x1 = ", sum_x1)
sum_x2 = np.sum(Axis_Depth)
print(" sum_x2 = ", sum_x2)
sum_x1x1 = np.sum(Color_Combinations * Color_Combinations)
print(" sum_x1x1 = ", sum_x1x1)
sum_x2x2 = np.sum(Axis_Depth * Axis_Depth)
print(" sum_x2x2 = ", sum_x2x2)
sum_x1x2 = np.sum(Color_Combinations * Axis_Depth)
print(" sum_x1x2 = ", sum_x1x2)
sum_x1y = np.sum(Color_Combinations * picture_Graphics)
print(" sum_x1y = ", sum_x1y)
sum_x2y = np.sum(Axis_Depth * picture_Graphics)
print(" sum_x2y = ", sum_x2y)
sum_yy = np.sum(picture_Graphics * picture_Graphics)
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

Y_heat = b0 + b1 * Color_Combinations + b2 * Axis_Depth
sum_Y_heat = sum(Y_heat)
TSS = np.sum((picture_Graphics - Y_mean) ** 2)
MSS = np.sum((Y_heat - Y_mean) ** 2)
RSS = np.sum((picture_Graphics - Y_heat) ** 2)
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
