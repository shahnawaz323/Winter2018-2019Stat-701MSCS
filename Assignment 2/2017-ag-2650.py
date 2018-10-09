from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import math as math
from statsmodels.stats.anova import anova_lm



def plot_reg(df, reg, strval):


        ax = plt.figure().gca(projection='3d')

        ax.scatter(

            df["x1"]
            , df["x2"]
            , df["y"]
            , color="green"

        )

        ax.set_title(strval[0])
        ax.set_xlabel(strval[1], color="blue")
        ax.set_ylabel(strval[2], color="blue")
        ax.set_zlabel(strval[3], color="blue")

        xsurf = df["x1"]
        ysurf = df["x2"]

        xsurf, ysurf = np.meshgrid(xsurf, ysurf)

        exog_ = pd.core.frame.DataFrame({

            "x1": xsurf.ravel(), "x2": ysurf.ravel()

        })

        pred = reg.predict(exog=exog_)

        ax.plot_surface(

            xsurf, ysurf
            , pred.values.reshape(xsurf.shape),
            color = None,
            alpha=0.3

        )

        plt.show()


def anova_tab(reg, y_m, y, y_hat_val, k):


    n = np.size(y_hat_val)

    df_m = k - 1
    df_r = n - k

    mss = np.sum((y_hat_val - y_m) ** 2)
    rss = np.sum((y - y_hat_val) ** 2)
    tss = mss + rss

    ms_m = mss / df_m
    ms_r = rss / df_r

    f_val = round(ms_m / ms_r, 4)
    r_sqr = round(mss / tss, 4)
    sigma_sqr = round(rss / df_r, 4)


    print("\n\nAnova Table\n", anova_lm(reg))

    print("\n\nR2 =", r_sqr)
    print("MSE = ", sigma_sqr)

    return f_val, sigma_sqr


def tesing_hypothesis(f_val, ftab):
    print("\nTesing Hypothesis...\n H0: B1 = B2 = B3 = 0 on F table value: {} at alpha = 5 %\n" .format(ftab))

    if (f_val > ftab):
        print("Since Fc = {} is greater than Ft = {}, so reject H0".format(f_val, ftab))

    else:
        print("Since Fc = {}  is greater than Ft = {, so accept H0\n\n".format(f_val))


def inputvalue():
    try:

        getval = int(input())

    except ValueError:

        print("You must enter a number")
        inputvalue()

    else:

        if getval == 1 or getval == 2:
            return getval

        else:
            print("Enter a 1 or 2")
            inputvalue()


def callmain(getval):

    if getval == 1:

        df = pd.DataFrame(
        {
                "x1": [100, 200, 300, 400, 500, 600, 700],  # Fertilizer
                "x2": [10, 20, 10, 30, 20, 20, 30],  # Rainfall
                "y": [40, 50, 50, 70, 65, 65, 80]  # Yield
            }
        )

        print(df)

        titlestring = "Linear Regression Line for Yield ~ Fertilizer + Rainfall"
        xlabstr = "Fertilizer"
        ylabstr = "Rainfall"
        zlabstr = "Yield"
        strval = [titlestring, xlabstr, ylabstr, zlabstr]

        ftab = 6.94

    else:        

        df = pd.DataFrame(
            {
                "x1": [0, 0, 10, 10, 20, 20],
                "x2": [0, 0, 100, 100, 400, 400],
                "y": [5, 7, 15, 17, 9, 11]
            }
        )
        print(df)

        titlestring = "Linear Regression Line y ~ x1 + x2"
        xlabstring = "x1"
        ylabstring = "x2"
        zlabstring = "x3"
        strval = [titlestring, xlabstring, ylabstring, zlabstring]

        ftab = 9.55

    reg = ols(formula="y ~ x1 + x2", data=df).fit()

    print("\n\n", reg.params)

    y_hat_val = reg.fittedvalues
    print("\n\nFitted Values:\n", y_hat_val)


    y_m = np.mean(df["y"])

    k = 3
    f_val, mse = anova_tab(reg, y_m, df["y"], y_hat_val, k)

    tesing_hypothesis(f_val, ftab)

    plot_reg(df, reg, strval)


print("Please Enter number: \n")
print("Enter 1 for Multiple Linear Regression (Yield)\n")
print("Enter 2 for Multiple Linear Regrsesion (y_x1_x2)\n")
getval = inputvalue()
callmain(getval)