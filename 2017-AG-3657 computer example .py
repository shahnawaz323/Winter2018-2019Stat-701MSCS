from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as dd
import numpy as np
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm



b= dd.DataFrame({"CPU": [10,20,30,40,50,60,70,80], "Monitor": [100, 200, 100, 300, 200, 200, 300, 400], "Mouse": [45, 55, 55, 75, 70, 75, 85, 95]})
result = smf.ols(formula="CPU ~ Monitor + Mouse", data=b).fit()
print(result.summary())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(b['Monitor'],
           b['CPU'], b['Monitor'],
           c='r', marker='o')
ab, ba = np.meshgrid(b['CPU'],
                     b['Monitor'])
exog = dd.core.frame.DataFrame({'CPU':ab.ravel(),
                                'Monitor':ba.ravel()}
                               )
out = result.predict(exog=exog)
ax.plot_surface(ab, ba, out.values.reshape(ab.shape), rstride=1, cstride=1, alpha='0.4', color='None')
ax.set_xlabel("CPU")
ax.set_ylabel("Monitor")
ax.set_zlabel("Mouse")
plt.show()

