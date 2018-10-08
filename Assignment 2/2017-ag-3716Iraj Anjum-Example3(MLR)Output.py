Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:\mphill Study material\3rd semester\stat 701\assignment1Stat\Assignmnt2StatExample3MLR.py 
E-Learning through video link is a web development approach which focuses on online learning through website by providing live learning interaction 
teacher and student.It will also bring ease at global level to seek knowledge at this web platform where people can learn any topic from the 
domain without attending the physical class.This system will deduct its commission from payment made bstudent to teacher and get its profit to run 
the business.Many data mining techniques are used to make complete analysis performed by using predictive analytics techniques to analyze the records
to discover the trends.Data regarding the E-learning is collected from stakeholders by considering radomly data of (2002-2017)years to evaluate the 
predictions on the yearly profit of the managment and the students who successfully passes out and do tremendous work in information communication
technology(ICT).later,these predictions will facilitate the E-learning monetarily while making beneficial effect or not.
X1=(number of students(passed the courses) , X2=number of teachers , Y=yearly profit(%)
X1= [250, 260, 600, 400, 160, 200]
Total Sum of X1 values is: 1870
X2= [5, 6, 4, 6, 7, 10]
Total Sum of X2 values is: 38
Y= [60, 70, 75, 63, 82, 70]
Total Sum of Y values is: 420
value of X1_bar is: 311.6666666666667
value of X1_bar^2 is: 97136.11111111112
value of X2_bar is: 6.333333333333333
value of X2_bar^2 is: 40.11111111111111
value of Y_bar is: 70
Value of x1=X1-X_bar is:
[-61.666666666666686]
[-61.666666666666686, -51.666666666666686]
[-61.666666666666686, -51.666666666666686, 288.3333333333333]
[-61.666666666666686, -51.666666666666686, 288.3333333333333, 88.33333333333331]
[-61.666666666666686, -51.666666666666686, 288.3333333333333, 88.33333333333331, -151.66666666666669]
[-61.666666666666686, -51.666666666666686, 288.3333333333333, 88.33333333333331, -151.66666666666669, -111.66666666666669]
Value of x2=X2-X2_bar is:
[-1.333333333333333]
[-1.333333333333333, -0.33333333333333304]
[-1.333333333333333, -0.33333333333333304, -2.333333333333333]
[-1.333333333333333, -0.33333333333333304, -2.333333333333333, -0.33333333333333304]
[-1.333333333333333, -0.33333333333333304, -2.333333333333333, -0.33333333333333304, 0.666666666666667]
[-1.333333333333333, -0.33333333333333304, -2.333333333333333, -0.33333333333333304, 0.666666666666667, 3.666666666666667]
Value of y=Y-Y_bar is:
[-10]
[-10, 0]
[-10, 0, 5]
[-10, 0, 5, -7]
[-10, 0, 5, -7, 12]
[-10, 0, 5, -7, 12, 0]
B1^=(sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
firstly calculate sigmax1.y.sigmax2^2
value of x1.y is: [616.6666666666669, -0.0, 1441.6666666666665, -618.3333333333333, -1820.0000000000002, -0.0]
sigma(x1.y) is: -380.0
value of (x2)^2 is: [1.777777777777777, 0.11111111111111091, 5.444444444444443, 0.11111111111111091, 0.44444444444444486, 13.444444444444446]
sigma(x2)^2 is: 21.333333333333332
value of (sigmax1.y.sigmax2^2) is: -8106.666666666666
 2ndly calculate sigmax2.y.sigmax1.x2
value of x2.y is: [13.33333333333333, -0.0, -11.666666666666664, 2.3333333333333313, 8.000000000000004, 0.0]
sigma(x2.y) is: 12.0
value of (x1)(x2) is: [82.22222222222223, 17.222222222222214, -672.7777777777776, -29.44444444444441, -101.11111111111117, -409.44444444444457]
sigma(x1)(x2) is: -1113.3333333333335
value of (sigmax2.y.sigmax1.x2) is: -13360.000000000002
value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is: 5253.333333333336
value of (x1)^2 is: [3802.77777777778, 2669.4444444444466, 83136.1111111111, 7802.777777777775, 23002.777777777785, 12469.444444444449]
sigma(x1)^2 is: 132883.3333333333
sigma(x2)^2 is(solved above is): 21.333333333333332
value of (sigmax1^2.sigmax2^2) is: 2834844.444444444
value of (sigma(x1x2)^2 is: 1239511.1111111115
value of (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2 is: 1595333.3333333326
value of B1^ is: 0.0032929377350605967
B2^=(sigmax2.y.sigmax1^2)-(sigmax1.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
firstly calculate (sigmax2.y.sigmax1^2)
value 0f (sigmax2.y.sigmax1^2) is: 1594599.9999999998
3rdly calculate (sigmax1.y.sigmax1.x2)
value 0f (sigmax1.y.sigmax1.x2) is: 423066.66666666674
value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is: 1171533.333333333
value of B2^ is: 0.7343501880484749
B0^=(Y_bar)-(B1^.X1_bar)-(B2^.X2_bar)
value of B0^ is: 64.32281654826578
Y^=B1^*X1+B2^*X2
1stly calculate B1^*X1
value of B1^*X is: [0.8232344337651492, 0.8561638111157551, 1.975762641036358, 1.3171750940242386, 0.5268700376096955, 0.6585875470121193]
2ndly calculate B2^*X2
value of B2^*X2 is: [3.671750940242374, 4.4061011282908495, 2.9374007521938994, 4.4061011282908495, 5.140451316339324, 7.343501880484748]
value of (B1^*X1)+(B2^*X2) is: [4.494985374007523, 5.262264939406605, 4.913163393230257, 5.723276222315088, 5.66732135394902, 8.002089427496868]
value of Y^ is: [68.8178019222733, 69.58508148767238, 69.23597994149604, 70.04609277058087, 69.9901379022148, 72.32490597576265]
TSS=sigma(Y-Y_bar)^2
calculate value of (Y-Y_bar)^2
value of (Y-Y_bar)^2 is:
[100, 0, 25, 49, 144, 0]
value of TSS is : 318
MSS=sigma(Y^-Y_bar)^2
1stly calculate value of (Y^-Y_bar)
Value of Y(i)^-Y_bar is:
[-1.1821980777266958]
[-1.1821980777266958, -0.4149185123276169]
[-1.1821980777266958, -0.4149185123276169, -0.7640200585039594]
[-1.1821980777266958, -0.4149185123276169, -0.7640200585039594, 0.046092770580870024]
[-1.1821980777266958, -0.4149185123276169, -0.7640200585039594, 0.046092770580870024, -0.009862097785202195]
[-1.1821980777266958, -0.4149185123276169, -0.7640200585039594, 0.046092770580870024, -0.009862097785202195, 2.324905975762647]
value of (Y_hat-Y_bar)^2 is: [1.3975922949806947, 0.17215737187216276, 0.5837266497963935, 0.0021245434998207174, 9.726097272489004e-05, 5.4051877961368655]
MSS=Sigma(Y^-Y_bar)^2 is: 7.560885917258663
RSS=sigma(Y-Y^)^2
1stly calculate value of (Y-Y^)
value of (Y-Y^) is: [-8.817801922273304, 0.4149185123276169, 5.764020058503959, -7.04609277058087, 12.009862097785202, -2.324905975762647]
value of (Y-Y^)^2 is: [77.75363074044678, 0.17215737187216276, 33.22392723483599, 49.647423331632, 144.23678760781758, 5.4051877961368655]
RSS=Sigma(Y-Y^)^2 is: 310.4391140827414
<^2=RSS/n-k
k=no. of parameters=3 i.e(B1,B2,B0) and n=7
n-k= 4
value of <^2 is: 77.60977852068535
V(B1^)=<^2. sigmax2^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
vaue of V(B1^) is: 0.0010378240337074519
V(B2^)=<^2. sigmax1^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
vaue of V(B2^) is: 6.464508609960557
V(B0^)=<^2. 1/n+[X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
for [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]
1stly calculate X1_bar^2.sigmax2^2
value of X1_bar^2.sigmax2^2 is: 2072237.0370370373
2ndly calculate X2_bar^2.sigmax1^2
value of X2_bar^2.sigmax1^2 is: 5330098.148148146
3rdly calculate 2X1_bar.X2_bar.sigmax1x2
value of 2X1_bar.X2_bar.sigmax1x2 is: -4395192.592592593
so value of [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2] is: 3007142.5925925905
value of VB0_hat : 157.37858881308108
This is the 2nd Assignment(example.3)of Stat701 in python.Thanku for watching :)
>>> 
