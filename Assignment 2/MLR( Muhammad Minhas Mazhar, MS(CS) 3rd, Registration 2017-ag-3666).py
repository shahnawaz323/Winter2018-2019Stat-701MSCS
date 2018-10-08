# Muhammad Minhas Mazhar, MS(CS) 3rd, Registration 2017-ag-3666
import numpy as np
from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt
Yield_graph = {
    'Yield': [5, 7, 15, 17, 9, 11],
    'Fertilizer': [0, 0, 10, 10, 20, 20],
    'Rainfall': [0,0,100,100,400,400]
    }
y=np.array([5, 7, 15, 17, 9, 11])
x = np.array([
     [0, 0, 10, 10, 20, 20],
     [0,0,100,100,400,400]])
X = x.T
X = np.c_[X, np.ones(X.shape[0])]
beta_hat = np.linalg.lstsq(X,y)[0]
print(beta_hat)
df = DataFrame(Yield_graph, columns=['Yield', 'Fertilizer', 'Rainfall'])

plt.scatter(df['Fertilizer'], df['Yield'], color='red')
plt.title('Yield Vs Fertilizer', fontsize=14)
plt.xlabel('Fertilizer', fontsize=14)
plt.ylabel('Yield', fontsize=14)
plt.grid(True)
plt.show()
plt.scatter(df['Rainfall'], df['Yield'], color='red')
plt.title('Yield Vs Rainfall', fontsize=14)
plt.xlabel('Rainfall', fontsize=14)
plt.ylabel('Yield', fontsize=14)
plt.grid(True)
plt.show()



