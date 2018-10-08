# MS(CS)  2017-AG-3684 
# ASSIGNMENT NO 2
#Get data from excel file
a <-read.delim(file.choose(),header=T)
a
attach(a)

# Multiple Linear Regression Example 
fit <- lm(CPU ~ RAMS + REG)

#MEAN OF CPU,RANSIZE And REGISTER SIZE
u=mean(CPU)
l=mean(RAMS)
d=mean(REG)
print(u)
print(l)
print(d)

#Value OF Mean Square Error
(summary(fit)$sigma)**2

#STANDARD ERRORS OF COEFFICIENTS
summary(fit)$coef[,2] 

#GET VALUES OF SLOPE AND INTERCEPT
a=intcp <- coef(fit)[1] 
s=slp <-  coef(fit)[2] 
h=slp <-  coef(fit)[3] 
print(s)
print(a)
print(h)

#FITTED VALUES
z=(a+(s*RAMS)+(h*REG))
print(z)

#TOTAL Sum of Square
k=sum((CPU-u)^2)
print(k)

#REGRESSION Sum of Square
p=sum((z-u)^2)
print(p)

#ERROR Sum of Square
g=sum((CPU-z)^2)
print(g)

#Analysis of variance
anova(fit)

#Confidence Interval 
confint(fit)

#Summary of whole result
summary(fit) # show results

#GRaph of the MLR
plot(fit,main="Scatterplot")

#ONE SAMPLE T TEST
t.test(REG, mu = 0, alternative = "two.sided")
#ONE SAMPLE T TEST
t.test(RAMS, mu = 0, alternative = "two.sided")
#WELCH SAMPLE T TEST
t.test(RAMS,REG)
