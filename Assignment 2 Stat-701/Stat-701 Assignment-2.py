import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def estimate_coefficient(x1 ,x2 , y):
    # number of observations/points
    n = np.size(x1)
    print("No of Observation = {}".format(n))
    k = 2
    print("K-value = {}".format(k))
    # mean of x and y vector
    mean_x1 ,mean_x2 , mean_y = np.mean(x1) ,np.mean(x2) , np.mean(y)
    print("Mean of X1 = {} \nMean of X2 = {}\nMean of Y = {}".format(np.mean(x1), np.mean(x2), np.mean(y)))
    # calculating cross-deviation and deviation about x
    Sxx2 = (np.sum((x2 - mean_x2) ** 2))
    print("Sum of Square of X2 = {}".format(Sxx2))
    Sx1x2 = (np.sum((x1 - mean_x1) * (x2 - mean_x2)))
    print("Sum of Square of X1X2 = {}".format(Sx1x2))
    Sx1y = (np.sum((x1 - mean_x1) * (y - mean_y)))
    print("Sum of Square of X1Y = {}".format(Sx1y))
    Sx2 = (np.sum((x1 - mean_x1) ** 2))
    print("Sum of Square of X1 = {}".format(Sx2))
    Sx2y = (np.sum((x2 - mean_x2) * (y - mean_y)))
    print("Sum of Square of X1Y = {}".format(Sx2y))
    value1 = (Sxx2 * Sx1y)
    value2 = (Sx1x2 * Sx2y)
    value3 = (Sx2 * Sxx2)
    value4 = (Sx1x2 * Sx1x2)
    value5 = (Sx2 * Sx2y)
    value6 = (Sx1x2 * Sx1y)
    # calculating regression coefficients
    b1 = float(value1 - value2)/float(value3 - value4)
    b2 = float((value5 - value6)/float(value3 - value4))
    b0 = float(mean_y - b1 * mean_x1 - b2 * mean_x2)
    print("\nEstimated coefficients:\nb0 = {}  \nb1 = {} \nb2 = {}".format(b0, b1, b2))
    # Total Sum of Squares
    tss = np.sum((y - mean_y) ** 2)
    print("\nTotal Sum of Squares (TSS) = {} ".format(tss))
    y_hat = (b0 + (b1 * x1) + (b2 * x2))
    print("y^ = {}".format(y_hat))
    mss = (np.sum((y_hat - mean_y) ** 2))
    print("Model/Regression Sum of Squares (MSS/SSR) = {}".format(mss))
    rss = (np.sum((y - y_hat) ** 2))
    print("Residual/Error Sum of Square (RSS/SSE) = {}".format(rss))
    r2 = float(mss / tss)
    print("Co-efficient of Determination (R^2) = {}".format(r2))
    sum_of_y_hat = np.sum(y_hat)
    print("Sum of Y^ = {}".format(sum_of_y_hat))
    r1 = float(rss/(n-1-k))
    print("r2 = {}".format(r1))
    vb1 = r1 * float(Sxx2/float(value3 - value4))
    print("Varience of b1 = {}".format(vb1))
    vb2 = r1 * float(Sx2/float(value3 - value4))
    print("Varience of b2 = {}".format(vb2))
    vb0 = r1 * float((1/n) + float((mean_x1 * Sxx2) + (mean_x2 * Sx2) + (2 * mean_x1 * mean_x2 * Sx1x2))/float(value3 - value4))
    print("Varience of b0 = {}".format(vb0))

def main():
    # observations
    x1 = np.array([100, 200, 300, 400, 500, 600, 700])
    x2 = np.array ([10, 20, 10, 30, 20, 20,30])
    y = np.array([40, 50, 50, 70, 65, 65, 80])
    # estimating coefficients
    estimate_coefficient(x1 ,x2 ,y)
main()
