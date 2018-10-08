Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:\mphill Study material\3rd semester\stat 701\assignment1Stat\Assignmnt2StatExample1.py 
X1= [100, 200, 300, 400, 500, 600, 700]
Total Sum of X1 values is: 2800
X2= [10, 20, 10, 30, 20, 20, 30]
Total Sum of X2 values is: 140
Y= [40, 50, 50, 70, 65, 65, 80]
Total Sum of Y values is: 420
value of X1_bar is: 400
value of X1_bar^2 is: 160000
value of X2_bar is: 20
value of X2_bar^2 is: 400
value of Y_bar is: 60
Value of x1=X1-X_bar is:
[-300]
[-300, -200]
[-300, -200, -100]
[-300, -200, -100, 0]
[-300, -200, -100, 0, 100]
[-300, -200, -100, 0, 100, 200]
[-300, -200, -100, 0, 100, 200, 300]
Value of x2=X2-X2_bar is:
[-10]
[-10, 0]
[-10, 0, -10]
[-10, 0, -10, 10]
[-10, 0, -10, 10, 0]
[-10, 0, -10, 10, 0, 0]
[-10, 0, -10, 10, 0, 0, 10]
Value of y=Y-Y_bar is:
[-20]
[-20, -10]
[-20, -10, -10]
[-20, -10, -10, 10]
[-20, -10, -10, 10, 5]
[-20, -10, -10, 10, 5, 5]
[-20, -10, -10, 10, 5, 5, 20]
B1^=(sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
firstly calculate sigmax1.y.sigmax2^2
value of x1.y is: [6000, 2000, 1000, 0, 500, 1000, 6000]
sigma(x1.y) is: 16500
value of (x2)^2 is: [100, 0, 100, 100, 0, 0, 100]
sigma(x2)^2 is: 400
value of (sigmax1.y.sigmax2^2) is: 6600000
 2ndly calculate sigmax2.y.sigmax1.x2
value of x2.y is: [200, 0, 100, 100, 0, 0, 200]
sigma(x2.y) is: 600
value of (x1)(x2) is: [3000, 0, 1000, 0, 0, 0, 3000]
sigma(x1)(x2) is: 7000
value of (sigmax2.y.sigmax1.x2) is: 4200000
value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is: 2400000
value of (x1)^2 is: [90000, 40000, 10000, 0, 10000, 40000, 90000]
sigma(x1)^2 is: 280000
sigma(x2)^2 is(solved above is): 400
value of (sigmax1^2.sigmax2^2) is: 112000000
value of (sigma(x1x2)^2 is: 49000000
value of (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2 is: 63000000
value of B1^ is: 0.0380952380952381
B2^=(sigmax2.y.sigmax1^2)-(sigmax1.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
firstly calculate (sigmax2.y.sigmax1^2)
value 0f (sigmax2.y.sigmax1^2) is: 168000000
2ndly calculate (sigmax1.y.sigmax1.x2)
value 0f (sigmax1.y.sigmax1.x2) is: 115500000
value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is: 52500000
value of B2^ is: 0.8333333333333334
B0^=(Y_bar)-(B1^.X1_bar)-(B2^.X2_bar)
value of B0^ is: 28.09523809523809
Y^=B1^*X1+B2^*X2
1stly calculate B1^*X1
value of B1^*X is: [3.8095238095238098, 7.6190476190476195, 11.428571428571429, 15.238095238095239, 19.04761904761905, 22.857142857142858, 26.666666666666668]
2ndly calculate B2^*X2
value of B2^*X2 is: [8.333333333333334, 16.666666666666668, 8.333333333333334, 25.0, 16.666666666666668, 16.666666666666668, 25.0]
value of (B1^*X1)+(B2^*X2) is: [12.142857142857144, 24.28571428571429, 19.761904761904763, 40.23809523809524, 35.71428571428572, 39.523809523809526, 51.66666666666667]
value of Y^ is: [40.238095238095234, 52.38095238095238, 47.857142857142854, 68.33333333333333, 63.80952380952381, 67.61904761904762, 79.76190476190476]
TSS=sigma(Y-Y_bar)^2
calculate value of (Y-Y_bar)^2
value of (Y-Y_bar)^2 is:
[400, 100, 100, 100, 25, 25, 400]
value of TSS is : 1150
MSS=sigma(Y^-Y_bar)^2
1stly calculate value of (Y^-Y_bar)
Value of Y(i)^-Y_bar is:
[-19.761904761904766]
[-19.761904761904766, -7.61904761904762]
[-19.761904761904766, -7.61904761904762, -12.142857142857146]
[-19.761904761904766, -7.61904761904762, -12.142857142857146, 8.333333333333329]
[-19.761904761904766, -7.61904761904762, -12.142857142857146, 8.333333333333329, 3.80952380952381]
[-19.761904761904766, -7.61904761904762, -12.142857142857146, 8.333333333333329, 3.80952380952381, 7.61904761904762]
[-19.761904761904766, -7.61904761904762, -12.142857142857146, 8.333333333333329, 3.80952380952381, 7.61904761904762, 19.76190476190476]
value of (Y_hat-Y_bar)^2 is: [390.53287981859427, 58.04988662131521, 147.4489795918368, 69.44444444444437, 14.512471655328802, 58.04988662131521, 390.532879818594]
MSS=Sigma(Y^-Y_bar)^2 is: 1128.5714285714284
RSS=sigma(Y-Y^)^2
1stly calculate value of (Y-Y^)
value of (Y-Y^) is: [-0.2380952380952337, -2.3809523809523796, 2.142857142857146, 1.6666666666666714, 1.1904761904761898, -2.6190476190476204, 0.2380952380952408]
value of (Y-Y^)^2 is: [0.056689342403626025, 5.668934240362805, 4.59183673469389, 2.7777777777777937, 1.4172335600907013, 6.859410430839009, 0.056689342403629404]
RSS=Sigma(Y-Y^)^2 is: 21.428571428571455
<^2=RSS/n-k
k=no. of parameters=3 i.e(B1,B2,B0) and n=7
n-k= 4
value of <^2 is: 5.357142857142864
V(B1^)=<^2. sigmax2^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
vaue of V(B1^) is: 3.401360544217691e-05
V(B2^)=<^2. sigmax1^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
vaue of V(B2^) is: 0.02380952380952384
V(B0^)=<^2. 1/n+[X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2
for [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]
1stly calculate X1_bar^2.sigmax2^2
value of X1_bar^2.sigmax2^2 is: 64000000
2ndly calculate X2_bar^2.sigmax1^2
value of X2_bar^2.sigmax1^2 is: 112000000
3rdly calculate 2X1_bar.X2_bar.sigmax1x2
value of 2X1_bar.X2_bar.sigmax1x2 is: 112000000
so value of [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2] is: 288000000
value of VB0_hat : 25.255102040816357
This is the 2nd Assignment(example.1)of Stat701 in python.Thanku for watching :)
>>> 
