#liBRARIES IMPORT FOR WORKING
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
import pandas as pd

#1 way to combine data
#Upload excel file
#figure=pd.read_csv("add.csv")
#figure.head()
fig = plt.figure()
axes = fig.add_subplot(111, projection='3d')
Fert = np.array([ 100, 200, 300, 400, 500, 600, 700])
Rainfall = np.array([10,20,10,30,20,20,30])
Yield=np.array([40,50,50,70,65,65,80])
#Second Way to Combine data
figure = pd.DataFrame({
        "Yield": Yield
        , "Fertilizer": Fert
        , "Rainfall": Rainfall }
)
print("Data for Multiple Linear Regression")
print(figure)
Reg2 = ols(formula = "Yield ~ Fert + Rainfall", data = figure)
rt = Reg2.fit()
print("Values of regression coefficients and intercept")
print(rt.params)
gt=np.array(rt.fittedvalues)

#Mean value yield
num.items = len(Yield)
mean = sum(Yield) / num.items

#TOTAL SS
differences = [Yield - mean for Yield in Yield]
sq_differences = [d ** 2 for d in differences]
op = np.sum(sq_differences)
print('The  TOTAL sum of square(TSS) is =',op)
#Regression SS
d = np.array([gt - 60])
jk = np.array([d ** 2 for d in d])
ikl = np.sum(jk)