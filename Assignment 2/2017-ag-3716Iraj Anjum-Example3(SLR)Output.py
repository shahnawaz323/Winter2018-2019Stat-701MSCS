Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:\mphill Study material\3rd semester\stat 701\assignment1Stat\Assignment2StatExample3SLR.py 
E-Learning through video link is a web development approach which focuses on online learning through website by providing live learning interaction 
teacher and student.It will also bring ease at global level to seek knowledge at this web platform where people can learn any topic from the 
domain without attending the physical class.This system will deduct its commission from payment made bstudent to teacher and get its profit to run 
the business.Many data mining techniques are used to make complete analysis performed by using predictive analytics techniques to analyze the records
to discover the trends.Data regarding the E-learning is collected from stakeholders by considering radomly data of (2002-2017)years to evaluate the 
predictions on the yearly profit of the managment and the students who successfully passes out and do tremendous work in information communication
technology(ICT).later,these predictions will facilitate the E-learning monetarily while making beneficial effect or not.
values_listX=(number of students(passed the courses) , Y=yearly profit(%)
X= [250, 260, 600, 400, 160, 200]
Total Sum of X values is: 1870
value of X_bar is: 311.6666666666667
Y= [60, 70, 75, 63, 82, 70]
Total Sum of Y values is: 420
value of Y_bar is: 70
Value of X(i)-X_bar is:
[-61.666666666666686]
[-61.666666666666686, -51.666666666666686]
[-61.666666666666686, -51.666666666666686, 288.3333333333333]
[-61.666666666666686, -51.666666666666686, 288.3333333333333, 88.33333333333331]
[-61.666666666666686, -51.666666666666686, 288.3333333333333, 88.33333333333331, -151.66666666666669]
[-61.666666666666686, -51.666666666666686, 288.3333333333333, 88.33333333333331, -151.66666666666669, -111.66666666666669]
Value of Y(i)-Y_bar is:
[-10]
[-10, 0]
[-10, 0, 5]
[-10, 0, 5, -7]
[-10, 0, 5, -7, 12]
[-10, 0, 5, -7, 12, 0]
value of (X(i)-X_bar)*(Y(i)-Y_bar) is: [616.6666666666669, -0.0, 1441.6666666666665, -618.3333333333333, -1820.0000000000002, -0.0]
Sigma(X(i)-X_bar)(Y(i)-Y_bar) is: -380.0
value of (X(i)-X_bar)^2 is: [3802.77777777778, 2669.4444444444466, 83136.1111111111, 7802.777777777775, 23002.777777777785, 12469.444444444449]
Sigma(X(i)-X_bar)(X(i)-X_bar) is: 132883.3333333333
So as we know that B1^=Sigma(X(i)-X_bar)(Y(i)-Y_bar)/(X(i)-X_bar)^2
Value of B1^ is : -0.0028596513232158538
So as we know that B0^=Y_bar-B1^*X_bar
value of B0_hat is: 70.89125799573561
value of (Y(i)-Y_bar)^2 is: [100, 0, 25, 49, 144, 0]
Sigma(Y(i)-Y_bar)^2 is: 318
now calculate (Y(i)^-Y_bar)^2 for which 1stly calculate B1^*X
value of B1^*X is: [-0.7149128308039634, -0.743509344036122, -1.7157907939295123, -1.1438605292863415, -0.45754421171453663, -0.5719302646431708]
we know that for Y(i)^,2ndly calculate Y^=B0^+B1^*X
value of Y^ is: [70.17634516493165, 70.14774865169949, 69.1754672018061, 69.74739746644927, 70.43371378402108, 70.31932773109244]
now 3rdly calculate Y(i)^-Y_bar
Value of Y(i)^-Y_bar is:
[0.17634516493164654]
[0.17634516493164654, 0.14774865169948725]
[0.17634516493164654, 0.14774865169948725, -0.8245327981938999]
[0.17634516493164654, 0.14774865169948725, -0.8245327981938999, -0.2526025335507285]
[0.17634516493164654, 0.14774865169948725, -0.8245327981938999, -0.2526025335507285, 0.4337137840210801]
[0.17634516493164654, 0.14774865169948725, -0.8245327981938999, -0.2526025335507285, 0.4337137840210801, 0.31932773109244295]
value of (Y(i)_hat-Y_bar)^2 is: [0.031097617194769618, 0.0218296640790164, 0.6798543352974624, 0.06380803995624691, 0.1881076464498841, 0.10197019984464756]
Sigma(Y(i)^-Y_bar)^2 is: 1.086667502822027
This is the 2nd assignment(example.3SLR done in python.Thankyou :)
>>> 
