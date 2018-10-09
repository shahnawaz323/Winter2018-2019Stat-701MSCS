#########################################
### """  Assignment # 2 : MS(CS) - Y | X1 | X2 .......Stats 701 :
Student name: Aneela Tabassum ,
AG no. 2017-ag-3643 ,
Degree and Session : MS(CS) 2017-2019 """

# Note: Firstly,I just calculation all this calculation on regresster then write this one code.
# The graphs code was taken form class mate "Arsalan Ali"

#########################################

#Installing packages for 3D-graph
install.packages("scatterplot3d") 
library("scatterplot3d") 

#########################################
###			 DATA
#########################################

Fertilizer = c(100, 200, 300, 400, 500, 600, 700)   
Rainfall = c(10, 20, 10, 30, 20, 20, 30) 
Yield = c(40, 50, 50, 70, 65, 65, 80)  
#Making Data-frame
df = data.frame(Fertilizer,Rainfall,Yield)

#########################################
###			3D GRAPH CODE
#########################################

# Code for the 3D-plot 
data(df)
head(df)
#scatterplot3d(x=Fertilizer, y=Rainfall, z=Yield)
s3d <- scatterplot3d(df, type = "h", color = "blue",
    angle=55, pch = 16,grid=TRUE, box=FALSE,


              main="Multiple Linear Regression \n 
               By Aneela Tabassum\n 2017-ag-3643",
              xlab = "Fertilizer (Pound)",
              ylab = "Rainfall (Inches)",
              zlab = "Yield (Bushel)")

# Using Pre-defined MLR function for the 3D-graph
my.lm <- lm(Yield~Fertilizer+Rainfall)
s3d$plane3d(my.lm)


#############################################



###				FUNCTION



#############################################

#This is the Custom MLR function
MLR<- function( X1, X2, Y )
{

	# Size of the input, 
	n = length(Y)

	# Mean of X1, X2 and Y
	mean.X1 = mean(X1)
	mean.X2 = mean(X2)
	mean.Y = mean(Y)


	x1 = X1 - mean.X1
	x2 = X2 - mean.X2
	y = Y - mean.Y
	

	Sum_x1 = sum(x1)
	Sum_x2 = sum(x2)
	Sum_y = sum(y)

		x1_square = sum((x1)^2)
	x2_square = sum((x2)^2)
	y_square = sum((y)^2)

		Sum_x1y = sum((x1*y))
	Sum_x1_square = sum((x1)^2)
	Sum_x2_square = sum((x2)^2)
	Sum_x2y = sum((x2*y))
	Sum_x1x2 = sum((x1*x2))

	Sum_x1y_Sum_x2_square = Sum_x1y*Sum_x2_square
	Sum_x2y_Sum_x1x2 = Sum_x2y*Sum_x1x2
	Sum_x1_square_Sum_x2_square = Sum_x1_square*Sum_x2_square
	Sum_x1x2_square = (Sum_x1x2)^2

	Beta1 = (Sum_x1y_Sum_x2_square - Sum_x2y_Sum_x1x2) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square)

	Beta2 = ((Sum_x2y*Sum_x1_square) - (Sum_x1y*Sum_x1x2)) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square)

	Beta0 = mean.Y - (Beta1*mean.X1) - (Beta2*mean.X2)

	# Number of parameters e.g, All the Betas
	k = 3	

	#  Y Hat: The Y-predicted
	Y_hat = Beta0 + Beta1*Fertilizer + Beta2*Rainfall
	Sum_Y_hat = sum(Beta0 + Beta1*Fertilizer + Beta2*Rainfall)


	TSS = sum((Yield - mean.Y)^2)
	MSS = sum((Y_hat - mean.Y)^2)
	RSS = sum((Yield - Y_hat)^2)

	# The one and only Regression Co-efficient
	R_square = MSS / TSS

	# Mean Square Error
	MSE = RSS / (n - k)

	# Beta1
	V_Beta1 = MSE*((Sum_x2_square) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square))
	SE_Beta1 = sqrt(V_Beta1)

	# Beta2
	V_Beta2 = MSE*((Sum_x1_square) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square))
	SE_Beta2 = sqrt(V_Beta2)

	#  Beta0
	mean.X1_square = mean.X1^2
	mean.X2_square = mean.X2^2
	mean.X1_mean.X2 = mean.X1*mean.X2

	# Biggest secret of all from Beta0's side
	V_Beta0 = MSE*((1 / n) + ((mean.X1_square*Sum_x2_square + mean.X2_square*Sum_x1_square - 2*mean.X1_mean.X2*(Sum_x1x2)) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square)))
	SE_Beta0 = sqrt(V_Beta0)

	# These are all the Outputs:

	cat("Mean of X1 = ", mean.X1, "\n")
	cat("Mean of X2 = ", mean.X2, "\n")
	cat("Mean of Y = ", mean.Y, "\n")
	cat("\n")
	cat("Sum of Deviations of X1 = " ,Sum_x1, "\n")
	cat("Sum of Deviations of X2 = " ,Sum_x2, "\n")
	cat("Sum of Deviations of Y = " ,Sum_y, "\n")
	cat("\n")
	cat("Sum of Square of X1 : Sum_x1 = " ,x1_square, "\n")
	cat("Sum of Square of X2 : Sum_x2 = " ,x2_square, "\n")
	cat("Sum of Square of Y : Sum_y = " ,y_square, "\n")
	cat("\n")
	cat("Beta1  = " ,Beta1, "\n")
	cat("Beta2  = " ,Beta2, "\n")
	cat("Beta0  = " ,Beta0, "\n")
	cat("\n")
	cat("Sum of Y-hat = ", Sum_Y_hat , "\n")
	cat("\n")
	cat("Total Sum of Squares : TSS = ", TSS , "\n")
	cat("Model Sum of Squares : MSS = ", MSS , "\n")	
	cat("Residual Sum of Squares : RSS = ", RSS , "\n")
	cat("\n")
	cat("Regression Co-efficient : R^2 = ", R_square, "\n")
	cat("\n")
	cat("Mean Square Error : MSE = ",MSE,"\n")
	cat("\n")
	cat("Variance of Beta1 = ",V_Beta1, "\n")
	cat("Standard Error of Beta1 = ",SE_Beta1, "\n")
	cat("\n")
	cat("Variance of Beta2 = ",V_Beta2,"\n")
	cat("Standard Error of Beta2 = ",SE_Beta2, "\n")
	cat("\n")
	cat("Variance of Beta0 = ",V_Beta0,"\n")
	cat("Standard Error of Beta0 = ",SE_Beta0, "\n")

	df2 = data.frame(X1,X2,Y)

	# Since i can't do Anova etc manually so here's the pre-defined ones
	fit <- lm(Y ~ X1 + X2, data=df2)
	summary(fit)

	}

# Combines the Data-set of Fertilizer , Rainfall and Yield
Exp.data = cbind(Fertilizer , Rainfall , Yield)


colnames(Exp.data) = c('Fertilizer' , 'Rainfall' , 'Yield')

# Calls the Table-Data function to generate Table
Exp.data

# This will load the entire Regression-Calculation process

Exp.regression<- MLR( Fertilizer, Rainfall, Yield )

# Executes the above function
Exp.regression

