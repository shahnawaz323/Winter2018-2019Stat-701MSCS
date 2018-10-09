install.packages("scatterplot3d") 
library("scatterplot3d") 

X_1 = c(0,0,10,10,20,20)   
X_2= c(0,0,100,100,400,400)  
Y = c(5,7,15,17,9,11) 

data_frame = data.frame(X_1,X_2,Y)


data(data_frame)
head(data_frame)
scatterplot3d(x=X_1, y=X_2, z=Y)
s3d <- scatterplot3d(data_frame, type = "p", color = "blue",
    angle=55, pch =16,grid=TRUE, box=FALSE,


              main="Multiple Linear Regression",
              xlab = "X_1",
              ylab = "X_2",
              zlab = "Y")


my.lm <- lm(Y~X_1+X_2)

s3d$plane3d(my.lm, lty.box = "solid",  draw_polygon = TRUE)

MLR<- function( X_1, X_2, Y )
{
	n = length(Y)

	mean.X_1 = mean(X_1)
	mean.X_2 = mean(X_2)
	mean.Y = mean(Y)

	
	X_1 = X_1 - mean.X_1
	X_2 = X_2 - mean.x_2