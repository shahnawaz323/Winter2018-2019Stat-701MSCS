import statistics
print("E-Learning through video link is a web development approach which focuses on online learning through website by providing live learning interaction ") 
print("teacher and student.It will also bring ease at global level to seek knowledge at this web platform where people can learn any topic from the ") 
print("domain without attending the physical class.This system will deduct its commission from payment made bstudent to teacher and get its profit to run ")
print("the business.Many data mining techniques are used to make complete analysis performed by using predictive analytics techniques to analyze the records")
print("to discover the trends.Data regarding the E-learning is collected from stakeholders by considering radomly data of (2002-2017)years to evaluate the ")
print("predictions on the yearly profit of the managment and the students who successfully passes out and do tremendous work in information communication")
print("technology(ICT).later,these predictions will facilitate the E-learning monetarily while making beneficial effect or not.")
print("values_listX=(number of students(passed the courses) , Y=yearly profit(%)")
values_listX= [250,260,600,400,160,200]
print("X=", values_listX)
SumX=sum(values_listX)
print("Total Sum of X values is:", SumX)
#for X bar............
X_bar= statistics.mean(values_listX)
print("value of X_bar is:", X_bar)
#for Y........
values_listY= [60,70,75,63,82,70]
print("Y=", values_listY )
SumY=sum(values_listY)
print("Total Sum of Y values is:", SumY)
#for Y bar...........
Y_bar= statistics.mean(values_listY)
print("value of Y_bar is:", Y_bar)
#for X(i)-X bar.......
print("Value of X(i)-X_bar is:")
newValue_list=[]
for i in range(len(values_listX)):
    newValue_list.append(values_listX[i]-X_bar)
    print(newValue_list)
#for Y(i)-Y bar.........
print("Value of Y(i)-Y_bar is:")
newValue_list2=[]
for i in range(len(values_listY)):
    newValue_list2.append(values_listY[i]-Y_bar)
    print(newValue_list2)
#for (X(i)-X bar)*(Y(i)-Y bar)......
XY= [a*b for a,b in zip (newValue_list,newValue_list2)]
print("value of (X(i)-X_bar)*(Y(i)-Y_bar) is:", XY)
#for sigma(X(i)-X_bar)(Y(i)-Y_bar)..........
SumXY=sum(XY)
print("Sigma(X(i)-X_bar)(Y(i)-Y_bar) is:", SumXY)
#for (X(i)-X_bar)^2.........
XX=[a*b for a,b in zip(newValue_list,newValue_list)]
print("value of (X(i)-X_bar)^2 is:", XX)
#for sigma(X(i)-X_bar)^2..........
SumXX=sum(XX)
print("Sigma(X(i)-X_bar)(X(i)-X_bar) is:", SumXX)
#for the value of B1^...........
print("So as we know that B1^=Sigma(X(i)-X_bar)(Y(i)-Y_bar)/(X(i)-X_bar)^2")
B1_hat=float(SumXY/SumXX)
print("Value of B1^ is :", B1_hat)
#for the value of B0^...........
print("So as we know that B0^=Y_bar-B1^*X_bar")
B0_hat=Y_bar-B1_hat*X_bar
print("value of B0_hat is:", B0_hat)
#for (Y(i)-Y_bar)^2.........
YY=[a*b for a,b in zip(newValue_list2,newValue_list2)]
print("value of (Y(i)-Y_bar)^2 is:", YY)
#for sigma (Y(i)-Y_bar)^2.............
SumYY=sum(YY)
print("Sigma(Y(i)-Y_bar)^2 is:", SumYY)
#for (Y(i)^-Y_bar)^2...........
#so the 1st step is to calculate B1^*X
print("now calculate (Y(i)^-Y_bar)^2 for which 1stly calculate B1^*X")
B1_hatX=[i*B1_hat for i in values_listX]
print("value of B1^*X is:", B1_hatX)
#2ndly calculate Y^......
print("we know that for Y(i)^,2ndly calculate Y^=B0^+B1^*X")
Y_hat=[i+B0_hat for i in B1_hatX]
print("value of Y^ is:", Y_hat)
#3rdly calculate Y(i)^-Y_bar.....................
print("now 3rdly calculate Y(i)^-Y_bar")
#for Y(i)_hat-Y bar.........
print("Value of Y(i)^-Y_bar is:")
Value_listYi_hat=[]
for i in range(len(Y_hat)):
    Value_listYi_hat.append(Y_hat[i]-Y_bar)
    print(Value_listYi_hat)
#then finally for (Y(i)^-Y_bar)^2........
    Yi_hat=[a*b for a,b in zip(Value_listYi_hat,Value_listYi_hat)]
print("value of (Y(i)_hat-Y_bar)^2 is:", Yi_hat)
#for sigma (Y(i)^-Y_bar)^2.............
SumYi_hat=sum(Yi_hat)
print("Sigma(Y(i)^-Y_bar)^2 is:", SumYi_hat)
print("This is the 2nd assignment(example.3SLR done in python.Thankyou :)")
    

