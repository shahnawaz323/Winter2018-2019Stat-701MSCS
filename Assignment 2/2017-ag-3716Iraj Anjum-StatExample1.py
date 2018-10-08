import statistics
X1=[100,200,300,400,500,600,700]
print("X1=",X1)
SumX1=sum(X1)
print("Total Sum of X1 values is:", SumX1)
X2=[10,20,10,30,20,20,30]
print("X2=",X2)
SumX2=sum(X2)
print("Total Sum of X2 values is:", SumX2)
Y=[40,50,50,70,65,65,80]
print("Y=",Y)
SumY=sum(Y)
print("Total Sum of Y values is:", SumY)
#for X1 bar............
X1_bar= statistics.mean(X1)
print("value of X1_bar is:", X1_bar)
#for X1_bar^2.........
X1_bar2=X1_bar*X1_bar
print("value of X1_bar^2 is:", X1_bar2)
#for X2 bar............
X2_bar= statistics.mean(X2)
print("value of X2_bar is:", X2_bar)
#for X2_bar^2.........
X2_bar2=X2_bar*X2_bar
print("value of X2_bar^2 is:", X2_bar2)
#for Y bar...........
Y_bar= statistics.mean(Y)
print("value of Y_bar is:", Y_bar)
#for x1=X1-X1_bar......
print("Value of x1=X1-X_bar is:")
x1=[]
for i in range(len(X1)):
    x1.append(X1[i]-X1_bar)
    print(x1)
#for x2=X2-X2_bar......
print("Value of x2=X2-X2_bar is:")
x2=[]
for i in range(len(X2)):
    x2.append(X2[i]-X2_bar)
    print(x2)
#for y=Y-Y_bar......
print("Value of y=Y-Y_bar is:")
y=[]
for i in range(len(Y)):
    y.append(Y[i]-Y_bar)
    print(y)  

                     #formula1.........................................
#for B1^ .........
print("B1^=(sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2")
print("firstly calculate sigmax1.y.sigmax2^2")
#for x1.y.........
x1y=[a*b for a,b in zip(x1,y)]
print("value of x1.y is:", x1y)
#for sigma(x1y)..........
Sumx1y=sum(x1y)
print("sigma(x1.y) is:", Sumx1y)
#for (x2)^2.........
xx2=[a*b for a,b in zip(x2,x2)]
print("value of (x2)^2 is:", xx2)
#for sigma(x2)^2..........
Sumxx2=sum(xx2)
print("sigma(x2)^2 is:", Sumxx2)
#for the value of (sigmax1.y.sigmax2^2)
pt1=Sumx1y*Sumxx2
print("value of (sigmax1.y.sigmax2^2) is:", pt1)
print(" 2ndly calculate sigmax2.y.sigmax1.x2")
#for sigmax2.y.........
x2y=[a*b for a,b in zip(x2,y)]
print("value of x2.y is:", x2y)
#for sigma(x2y)^2..........
Sumx2y=sum(x2y)
print("sigma(x2.y) is:", Sumx2y)
#for (x1)(x2).........
x1x2=[a*b for a,b in zip(x1,x2)]
print("value of (x1)(x2) is:", x1x2)
#for sigma(x1)(x2)..........
Sumx1x2=sum(x1x2)
print("sigma(x1)(x2) is:", Sumx1x2)
pt2=Sumx2y*Sumx1x2
print("value of (sigmax2.y.sigmax1.x2) is:", pt2)
#calculate value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2)........
part1=pt1-pt2
print("value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is:", part1)
#for value of (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2............
# for the value of (sigmax1^2.sigmax2^2)..........
#for (x1)^2.........
xx1=[a*b for a,b in zip(x1,x1)]
print("value of (x1)^2 is:", xx1)
#for sigma(x1)^2..........
Sumxx1=sum(xx1)
print("sigma(x1)^2 is:", Sumxx1)
print("sigma(x2)^2 is(solved above is):", Sumxx2)
pt3=Sumxx1*Sumxx2
print("value of (sigmax1^2.sigmax2^2) is:", pt3)
#for the value of (sigma(x1x2))^2...............
pt4=Sumx1x2*Sumx1x2
print("value of (sigma(x1x2)^2 is:", pt4)
#calculate value of (sigmax1^2.sigmax2^2)-(sigma(X1X2))^2"........
part2=pt3-pt4
print("value of (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2 is:",part2)
#for B1^............
B1_hat=float(part1/part2)
print("value of B1^ is:", B1_hat)

                    #.............formula2.........................................

#for B2^.........
print("B2^=(sigmax2.y.sigmax1^2)-(sigmax1.y.sigmax1.x2)/(sigmax1^2.sigmax2^2)-(sigma(x1x2))^2")
print("firstly calculate (sigmax2.y.sigmax1^2)")
ptt1=Sumx2y*Sumxx1
print("value 0f (sigmax2.y.sigmax1^2) is:", ptt1)
print("2ndly calculate (sigmax1.y.sigmax1.x2)")
ptt2=Sumx1y*Sumx1x2
print("value 0f (sigmax1.y.sigmax1.x2) is:", ptt2)
#calculate value of (sigmax2.y.sigmax1^2)-(sigmax1.y.sigmax1.x2)........
partt1=ptt1-ptt2
print("value of (sigmax1.y.sigmax2^2)-(sigmax2.y.sigmax1.x2) is:", partt1)
#for B2^............
#part2 is caculated above..........
B2_hat=float(partt1/part2)
print("value of B2^ is:", B2_hat)

                   #.............formula3.........................................


#for B0^..........
print("B0^=(Y_bar)-(B1^.X1_bar)-(B2^.X2_bar)")
B0_hat=Y_bar-B1_hat*X1_bar-B2_hat*X2_bar
print("value of B0^ is:",B0_hat)

                 #.............formula4...........................................
#for Y^..............
print("Y^=B1^*X1+B2^*X2")
#so the 1st step is to calculate B1^*X1
print("1stly calculate B1^*X1")
B1_hatX1=[i*B1_hat for i in X1]
print("value of B1^*X is:", B1_hatX1)
#so the 2nd step is to calculate B2^*X2
print("2ndly calculate B2^*X2")
B2_hatX2=[i*B2_hat for i in X2]
print("value of B2^*X2 is:", B2_hatX2)
B1B2_hatX1X2=[sum(a) for a in zip(B1_hatX1, B2_hatX2)]
print("value of (B1^*X1)+(B2^*X2) is:",B1B2_hatX1X2)
#2ndly calculate Y^......
Y_hat=[i+B0_hat for i in B1B2_hatX1X2]
print("value of Y^ is:", Y_hat)


              #.............formula5...........................................
#for TSS...............
print("TSS=sigma(Y-Y_bar)^2")
print("calculate value of (Y-Y_bar)^2")
print("value of (Y-Y_bar)^2 is:")
y2=[a*b for a,b in zip(y,y)]
print(y2)
#for sigma(y)(y)..........
Sumy2=sum(y2)
print("value of TSS is :", Sumy2)

              #.............formula6............................................
#for MSS...............
print("MSS=sigma(Y^-Y_bar)^2")
print("1stly calculate value of (Y^-Y_bar)")
print("Value of Y(i)^-Y_bar is:")
Value_listYi_hat=[]
for i in range(len(Y_hat)):
    Value_listYi_hat.append(Y_hat[i]-Y_bar)
    print(Value_listYi_hat)
#then finally for (Y^-Y_bar)^2........
    Yi_hat=[a*b for a,b in zip(Value_listYi_hat,Value_listYi_hat)]
print("value of (Y_hat-Y_bar)^2 is:", Yi_hat)
#for sigma (Y(i)^-Y_bar)^2.............
SumYi_hat=sum(Yi_hat)
print("MSS=Sigma(Y^-Y_bar)^2 is:", SumYi_hat)

                #.............formula7............................................
#for RSS...............
print("RSS=sigma(Y-Y^)^2")
print("1stly calculate value of (Y-Y^)")
YY_hat=[Y[i]-Y_hat[i] for i in range(min(len(Y), len(Y_hat)))]
print("value of (Y-Y^) is:",YY_hat)
#then finally for (Y-Y^)^2........
Yi_hat2=[a*b for a,b in zip(YY_hat,YY_hat)]
print("value of (Y-Y^)^2 is:", Yi_hat2)
#for sigma (Y-Y^)^2.............
RSS=sum(Yi_hat2)
print("RSS=Sigma(Y-Y^)^2 is:", RSS)

            #...................formula8.............................

#for <^2 .............
print("<^2=RSS/n-k")
print("k=no. of parameters=3 i.e(B1,B2,B0) and n=7")
k=3
n=7
nk=n-k
print("n-k=",nk)
sigma_hat2=float(RSS/nk)
print("value of <^2 is:", sigma_hat2)

              #...................formula9.............................

#for V(B1^)..............
print("V(B1^)=<^2. sigmax2^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2")
vpt1=sigma_hat2*(Sumxx2/part2)
print("vaue of V(B1^) is:",vpt1)
             #....................formula10............................

#forV(B2^)...................
print("V(B2^)=<^2. sigmax1^2)/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2")
vpt2=sigma_hat2*(Sumxx1/part2)
print("vaue of V(B2^) is:",vpt2)
             #......................formula11............................

#forV(B0^)...................
print("V(B0^)=<^2. 1/n+[X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]/ (sigmax1^2.sigmax2^2)-(sigma(x1x2))^2")
print("for [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2]")
print("1stly calculate X1_bar^2.sigmax2^2")
vpt3=X1_bar2*Sumxx2
print("value of X1_bar^2.sigmax2^2 is:",vpt3)
print("2ndly calculate X2_bar^2.sigmax1^2")
vpt4=X2_bar2*Sumxx1
print("value of X2_bar^2.sigmax1^2 is:",vpt4)
print("3rdly calculate 2X1_bar.X2_bar.sigmax1x2")
vpt5=2*X1_bar*X2_bar*Sumx1x2
print("value of 2X1_bar.X2_bar.sigmax1x2 is:",vpt5)
vpart1=vpt3+vpt4+vpt5
print("so value of [X1_bar^2.sigmax2^2+X2_bar^2.sigmax1^2+2X1_bar.X2_bar.sigmax1x2] is:", vpart1)
vb1=float(1/n)
vb2=float(vpart1/part2)
vb0=vb1+vb2
VB0_hat=sigma_hat2*vb0
print("value of VB0_hat :", VB0_hat)
print("This is the 2nd Assignment(example.1)of Stat701 in python.Thanku for watching :)")
