"""  Assignment # 2 : MS(CS) - Y | X1 | X2 .......Stats 701 :
Student name: Aneela Tabassum ,
AG no. 2017-ag-3643 ,
Degree and Session : MS(CS) 2017-2019 """

# Note: Firstly,I just calculation all this calculation on regresster then write this one code.
# The graphs code was taken form class mate "Arsalan Ali"



from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math as math
#  3D graph
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy import stats

#these are all data set:
# Our Data
Y = np.array([5, 7, 15, 17, 9, 11])
X1 = np.array([0, 0, 10, 10, 20, 20])
X2 = np.array([0, 0, 100, 100, 400, 400])
# Number of Observations
n = X2.size
print("\nNumber of Observations : n = ", n)

# Calculate the mean of Y , X1 , X2:
Ybar = sum(Y) / Y.size
Fbar = sum(X1) / X1.size
Rbar = sum(X2) / X2.size

print("\nY Mean : Y = ", Ybar)
print("X1 Mean : X1 = ", Fbar)
print("X2 Mean : X2 = ", Rbar)

# Let's deviate from the mean :
x1 = X1 - Fbar
x2 = X2 - Rbar
y = Y - Ybar

print("\nx1 =", x1)
print("x2 =", x2)
print("Y =", y)

# Let's take the sum of X1,X2 and Y  deviate :
Σx1 = np.sum(x1)
Σx2 = np.sum(x2)
Σy = np.sum(y)

# taking the sequre of  sums of X1,X2 and y's deviations :
square_x1 = np.sum((x1) ** 2)
square_x2 = np.sum((x2) ** 2)
square_Y = np.sum((y) ** 2)

# Just some formulas in order to get all the Betas
Σx1y = np.sum((x1 * y))
Σx1_square = np.sum((x1) ** 2)
Σx2_square = np.sum((x2) ** 2)
Σx2y = np.sum((x2 * y))
Σx1x2 = np.sum((x1 * x2))

Σx1y_Σx2_square = Σx1y * Σx2_square
Σx2y_Σx1x2 = Σx2y * Σx1x2
Σx1_square_Σx2_square = Σx1_square * Σx2_square
Σx1x2_square = (Σx1x2) ** 2
temp1 = Σx1_square_Σx2_square - Σx1x2_square

Beta1 = (Σx1y_Σx2_square - Σx2y_Σx1x2) / temp1
print("\nBeta1 = ", Beta1)

Beta2 = ((Σx2y * Σx1_square) - (Σx1y * Σx1x2)) / temp1
print("Beta2 = ", Beta2)

Beta0 = Ybar - (Beta1 * Fbar) - (Beta2 * Rbar)
print("Beta0 = ", Beta0)

# K is the Number of parameters
k = 3
print("\nNumber of Parameters from  B0, B1, B2 : k = ", k)

# Y hat is  The Y-predicted :
Y_hat = Beta0 + Beta1 * X1 + Beta2 * X2
ΣY_hat = np.sum(Beta0 + Beta1 * X1 + Beta2 * X2)
print("\nSum of All Y-hat values = ", ΣY_hat)

print("\nY = {} + {}X1 + {}X2".format(Beta0, Beta1, Beta2))

#calculate the TSS , MSS and RSS for computing the Regression Co-efficient
TSS = np.sum((Y - Ybar) ** 2)
MSS = np.sum((Y_hat - Ybar) ** 2)
RSS = np.sum((Y - Y_hat) ** 2)

print("\nTotal Sum of Squares : TSS = ", TSS)
print("Model Sum of Squares : MSS = ", MSS)
print("Residual Sum of Squares : RSS = ", RSS)

# Regression Co-efficient
R_square = MSS / TSS
print("\nR_square = ", R_square)

# Mean Square Error
MSE = RSS / (n - k)
print("\nMeans Square Error : MSE = ", MSE)

# Beta1's variances
temp2 = Σx1_square_Σx2_square - Σx1x2_square
V_Beta1 = MSE * ((Σx2_square) / temp2)
SE_Beta1 = math.sqrt(V_Beta1)
print("\nVariance of Beta1 = ", V_Beta1)
print("Standard Error of Beta1 : SE(B1) = ", SE_Beta1)

# Beta2's variances
V_Beta2 = MSE * ((Σx1_square) / temp2)
SE_Beta2 = math.sqrt(V_Beta2)
print("\nVariance of Beta2 = ", V_Beta2)
print("Standard Error of Beta2 : SE(B2) = ", SE_Beta2)


F_bar_square = Fbar ** 2
R_bar_square = Rbar ** 2
F_bar_R_bar = Fbar * Rbar

#  Beta0's variances
V_Beta0 = MSE * ((1 / n) + ((F_bar_square * Σx2_square + R_bar_square * Σx1_square - 2 * F_bar_R_bar * (Σx1x2)) / temp2))
SE_Beta0 = math.sqrt(V_Beta0)
print("\nVariance of Beta0 = ", V_Beta0)
print("Standard Error of Beta0 : SE(B0) = ", SE_Beta0)

# now goning to draw the 3'D graph
data_frame = pd.DataFrame(
    {
        "Y": Y
        , "X1": X1
        , "X2": X2

    }
)

# It will turn it into a 3D Graph
ax = plt.figure().gca(projection='3d')

# It will take the values of Y,X1,X2 and turn them into X,Y,Z Axis
ax.scatter(
    data_frame["X1"]
    , data_frame["X2"]
    , data_frame["Y"]
    , color="blue"
    , marker="o"
    , alpha=1
)


# From here....graph code is taken from class mate "Arsalan Ali"

Reg = ols(formula="Y ~ X1 + X2", data=data_frame)

Fit2 = Reg.fit()
print("\n", Fit2.summary())
print("\n", anova_lm(Fit2))

# Again plotting our Dear 3D-Graph
ax = plt.figure().gca(projection='3d')

# Creating Axis X,Y,Z out of our Data Y,X1,X2
ax.scatter(
    data_frame["X1"]
    , data_frame["X2"]
    , data_frame["Y"]
    , color="blue"
    , marker="o"
    , alpha=1
)

# Title of the graph
ax.set_title('Regression Shape in 3D \n ''Aneela Tabassum 2017-ag-3643')

# Again labelling the Axis we just created , writing duplicate code is a/an headache
ax.set_xlabel("X1 ", color="green")
ax.set_ylabel("X2 ", color="purple")
ax.set_zlabel("Y ", color="blue")


# Parameters to create Shape/Grid using X1 and X2 Data
x_surf = X1
y_surf = X2

# The purpose of meshgrid is to create a rectangular grid out of an data of x and y values
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

# To combine X and Y in order to generate Z for the surface
exog = pd.core.frame.DataFrame({
    "X1": x_surf.ravel()
    , "X2": y_surf.ravel()
})

# Generating Predicted values for the shape
out = Fit2.predict(exog=exog)

# Generating the actual Shape now on Graph
ax.plot_surface(
    x_surf
    , y_surf
    , out.values.reshape(x_surf.shape)
    , rstride=1
    , cstride=1
    , color="None"
    , alpha=0.4
)
# We all know what this does , right? The End of our Assignment comes here.
plt.show()
