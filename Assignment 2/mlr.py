import numpy as np
from scipy import stats
y = [-6,-5,-10,-5,-8,-3,-6,-8,-8]
x = np.array([[-4.95,-4.55],[-10.96,-1.08],[-6.52,-0.81],[-7.01,-4.46],[-11.54,-5.87],[-4.52,-11.64],[-3.36,-7.45],[-2.36,-7.33],[-7.65,-10.03]])
beta_hat = np.linalg.lstsq(x,y)[0]
print(beta_hat)
estimate = np.zeros((9))

for i in range(0,9):

    estimate[i] = beta_hat[0]*x[i,0]+beta_hat[1]*x[i,1]
print(stats.pearsonr(estimate,y))
