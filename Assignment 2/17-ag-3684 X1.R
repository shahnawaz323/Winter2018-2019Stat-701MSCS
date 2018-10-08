# MS(CS)  2017-AG-3684 
# ASSIGNMENT NO 2
#Get data from excel file
a <-read.delim(file.choose(),header=T)
a
attach(a)
# Multiple Linear Regression Example 
it <- lm(Y ~ X1 + X2)

#Mean of Y,X1,X2
u=mean(Y)
l=mean(X1)
d=mean(X2)
print(u)
print(l)
print(d)

#Value of Mean Square Error
(summary(it)$sigma)**2

#STANDARD ERRORS OF COEFFICIENTS
summary(it)$coef[,2] 

#GET VALUES OF SLOPE AND INTERCEPT
a=intcp <- coef(it)[1] 
s=slp <-  coef(it)[2] 
h=slp <-  coef(it)[3] 
print(s)
print(a)
print(h)
#FITTED Y,
z=(a+(s*X1)+(h*X2))
print(z)

#TOTAL Sum of Square
k=sum((Y-u)^2)
print(k)

#REGRESSION Sum of Square
p=sum((z-u)^2)
print(p)

#ERROR Sum of Square
g=sum((Y-z)^2)
print(g)

#R SQUARE COfficient of DETERMINATION
yt=p/k
print(yt)

#Confidence Interval 
confint(it)

#Summary of Whole Data
summary(it) 

#Graph of MLR
plot(it,main="Scatterplot")

#ANOVA TABLE
anova(it)

#ONE SAMPLE T TEST
t.test(X1, mu = 0, alternative = "two.sided")
#ONE SAMPLE T TEST
t.test(X2, mu = 0, alternative = "two.sided")
#WELCH SAMPLE T TEST
t.test(X1,X2)
