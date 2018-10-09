import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pd.read_csv('Data.csv')
x = data.iloc[:,[0]].values
y = data.iloc[:,[1]].values

x_t = np.transpose(x)
first_inv = np.matmul(x_t, x)
second = np.matmul(x_t, y)
first = np.linalg.inv(first_inv)
theta = np.matmul(first, second)
y_prad = theta*x

regressor = LinearRegression()
regressor.fit(x, y)
y_prad2 = regressor.predict(x)
plt.scatter(x, y)
plt.plot(x, y_prad, 'red')
plt.plot(x, y_prad2, 'green')
