import numpy as num
import math

def coefficient(x1 ,x2 , y):
    # number of observations/points
    n = num.size(x1)
    # mean of x and y vector
    meanx1 ,meanx2 , meany = num.mean(x1) ,num.mean(x2) , num.mean(y)
    print("Mean of X1 = {} \nMean of X2 = {}\nMean of Y = {}".format(num.mean(x1), num.mean(x2), num.mean(y)))
    # calculating cross-deviation and deviation about x
    Sxx2 = (num.sum(x2 ** 2)- n * (meanx2) ** 2)
    print("Sum of Square of X2 = {}".format(Sxx2))
    Sx1x2 = (num.sum(x1 * x2) - n * (meanx1 * meanx2))
    print("Sum of Square of X1X2 = {}".format(Sx1x2))
    Sx1y = (num.sum(x1 * y) - n * (meanx1 * meany))
    print("Sum of Square of X1Y = {}".format(Sx1y))
    Sx2 = (num.sum(x1 ** 2)- n * (meanx1) ** 2)
    print("Sum of Square of X1 = {}".format(Sx2))
    Sx2y = (num.sum(x2 * y) - n * (meanx2 * meany))
    print("Sum of Square of X1Y = {}".format(Sx2y))
    # calculating regression coefficients
    b1 = float((Sxx2 * Sx1y) - (Sx1x2 * Sx2y))/float((Sx2 * Sxx2) - (Sx1x2 * Sx1x2))
    b2 = float((Sx2 * Sx2y) - (Sx1x2 * Sx1y))/float((Sx2 * Sxx2) - (Sx1x2 * Sx1x2))
    b0 = float(meany - b1 * meanx1 - b2 * meanx2)
    print("\nEstimated coefficients:\nb0 = {}  \nb1 = {} \nb2 = {}".format(b0, b1, b2))
    # Total Sum of Squares
    tss = num.sum((y - meany) ** 2)
    y_pred = (b0 + (b1 * x1) + (b2 * x2))
    mss = (num.sum((y_pred - meany) ** 2))
    rss = (num.sum((y - y_pred) ** 2))
    r2 = float(mss / tss)
    sum_y_hat = num.sum(y_pred)
    print("Sum of Y^ = {}".format(sum_y_hat))
    return tss, mss, rss, r2

def main():
    # observations
    x1 = num.array([0, 0, 10, 10, 20, 20])
    x2 = num.array([0, 0, 100, 100, 400, 400])
    y = num.array([5, 7, 15, 17, 9, 11])
    # coefficients
    b = coefficient(x1 ,x2 ,y)
    print("\nTotal Sum of Squares (TSS) = {} ".format(b[0]))
    print("Model/Regression Sum of Squares (MSS/SSR) = {}".format(b[1]))
    print("Residual/Error Sum of Square (RSS/SSE) = {}".format(b[2]))
    print("Co-efficient of Determination (R^2) = {}".format(b[3]))
main()
