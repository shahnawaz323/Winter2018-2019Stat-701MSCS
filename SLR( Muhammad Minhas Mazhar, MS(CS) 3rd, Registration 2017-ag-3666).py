# Muhammad Minhas Mazhar, MS(CS) 3rd, Registration 2017-ag-3666
from scipy import stats
from matplotlib import pyplot as plt

x=[20, 30, 33, 40, 15, 13, 26, 38, 35, 43]

y=[7, 9, 8, 11, 5, 4, 8, 10, 9, 10]

gradient,intercept,r_value,p_value,std_err=stats.linregress(x,y)

print("Gradient and intercept",gradient,intercept)

gradient and intercept, 0.724084177708, 0.00398211223694

print("R-squared",r_value**2)
slope, Intercept, p_value, r_value, std_err = stats.linregress(x, y)
plt.plot(x, y, 'ro', color='black')
plt.ylabel('income')
plt.xlabel('expenditure')

plt.axes([0, 300, 0, 200])

plt.plot()
plt.show()
