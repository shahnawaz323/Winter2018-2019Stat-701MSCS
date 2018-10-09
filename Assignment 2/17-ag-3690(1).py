#Upload excel file
#figure=pd.read_csv("add.csv")
#figure.head()
fig = plt.figure()
axes = fig.add_subplot(111, projection='3d')
CPU = np.array([ 28, 27, 33, 44, 50, 60, 65])
RAMS = np.array([5,5,7,8,4,2,7,])
REG=np.array([40,50,50,70,65,65,80])
#Second Way to Combine data
figure = pd.DataFrame({
        "CPU": CPU
        , "RAM SIZE": RAMS
        , "REGISTER SIZE": REG }
)
print("Data for Multiple Linear Regression")
print(figure)
Reg2 = ols(formula = "CPU ~ RAMS + REG", data = figure)
rt = Reg2.fit()
print("Values of regression coefficients and intercept")
print(rt.params)
gt=np.array(rt.fittedvalues)

#Mean value cpu
num.items = len(CPU)
mean = sum(CPU) / num.items
print("Y bar VAlue is=",mean)

#total sum square
differences = [CPU - mean for CPU in CPU]
sq_differences = [d ** 2 for d in differences]
ghj = np.sum(sq_differences)
print('The  TOTAL sum of square(TSS) is =',ghj)

#Regration sum OF square
d = np.array([gt - 43.85])
jk = np.array([d ** 2 for d in d])
hjk = np.sum(jk)
print('The REGRESSION SUM OF SQUARE (RSS)is =',hjk)

#Error sum OF sqaure
differences = [CPU - gt]
sq_differences = [d ** 2 for d in differences]
ssd = np.sum(sq_differences)
print('The ERROR sum of square is(ESS) =.',ssd)

#R square cofficient OF determination
print("R Square Value")
ik=hjk/ghj
print("R Square is=",ik)

#Sumary of whole data
print(rt.summary())

print ("ANOVA TABLE FOR GIVEN DATA")
mod = ols('CPU ~ RAMS + REG', data=figure).fit()
aov.table = sm.stats.anova_lm(mod, typ=2)
print(aov.table)

#ONe Sample T Test
print("One Sample T Test ")
one=stats.ttest_1samp(RAMS, 0.0)
print(one)
one=stats.ttest_1samp(REG, 0.0)
print(one)
one=stats.ttest_1samp(CPU, 0.0)
print(one)

#Scatter Plot
axes.scatter(RAMS,REG,CPU,c='blue',marker='o')
axes.set_xlabel("RAM SIZE")
axes.set_ylabel("REGISTER SIZE")
axes.set_zlabel("CPU")
plot.show()
#PLOT Histogram
figure.hist(bins=50, figsize=(20,15))
plot.savefig("attribute_histogram_plots")
plot.show()
