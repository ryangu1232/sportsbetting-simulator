#Linear Regression model to predict a score given the projection from another website. 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#dataset that I collected sportsgamblin
projected_nba_scores = np.array([27,25,	17,	13,	12,	25,	21,	16,	15,	10,	30,	25,	15,	11,	32,	23,	17,	16,	24,	18,	14,	14,	20,	15,	26,	20,	18,	15,	24,	21,	17,	29,	24,	20,	19,	16,	24,	20,	17,	24,	23,	14,	12,	23,	18,	12,	12,	19,	9,	26,	23,	18,	23,	12,	11,	26,	20,	12,	10,	20,	15,	14,	14,	33,	20,	14,	28,	24,	17,	13,	28,	24,	24,	17,	24,	23,	15,	32,	30,	14,	16,	32,	21,	13,	26,	12,	12,	14,	11,	21,	20,	17,	21,	11,	25,	22,	15,	15,	12,	24,	23,	13,	11,	21,	15,	21,	16,	15,	25,	23,	20,		9,	27,	23,	23,	14,	12,	28,	25,	13,	10,	27,	21,	14,	10,	21,	17,	13,	31,	17,	15,			23,	23,	17,	15,	12,	38,	35,		15,	15,	28,	20,	15,	14,	14,							21,	17,	12,												30,	19,	13,	25,	24,	20,	16,	26,	25,	19,	20,	19,	16,	28,	26,	24,	22,	16,	20,	18,		12,	10,	27,	25,	18,	13,		19,	17,	13,	13,	33,	10,	23,	23,	13,	12,	11,	24,	20,		11,		31,	31,	15,	23,	15,	12,	11,	9,	36,	20,	17,	11,	28,	21,	15,	14,	14,	24,	24,	16,	15,	13,	17,	13,	12,	28,	24,	17,	])
actual_nba_scores = np.array([21,	17,	14,	11,	6,	21,	29,	12,	15,	20,	32,	18,	14,	17,	27,	15,	14,	10,	10,	14,	14,	14,	19,	8,	23,	11,	9,	15,	15,	24,	25,	34,	11,	30,	9,	12,	15,	14,	24,	18,	25,	6,	16,	20,	11,	11,	24,	30,	14,	19,	16,	22,	20,	5,	7,	26,	19,	15,	11,	15,	7,	20,	17,	31,	16,	8,	16,	20,	11,	15,	23,	24,	19,	12,	8,	31,	17,	23,	39,	13,	6,	24,	31,	20,	39,	4,	10,	15,	6,	21,	30,	10,	14,	0,	22,	22,	10,	9,	8,	15,	21,	13,	11,	12,	15,	20,	19,	13,	14,	10,	18,		5,	26,	24,	12,	8,	10,	51,	20,	14,	6,	34,	34,	15,	2,	11,	24,	15,	7,	19,	10,			28,	19,	9,	20,	7,	26,	6,		13,	18,	20,	15,	15,	12,	13,							21,	19,	12,												37,	12,	8,	30,	27,	17,	9,	21,	19,	19,	5,	14,	9,	33,	15,	36,	11,	5,	11,	21,		11,	11,	23,	20,	24,	7,		19,	20,	11,	15,	35,	15,	30,	30,	23,	6,	8,	13,	35,		8,		33,	25,	11,	17,	11,	12,	10,	13,	32,	21,	7,	9,	27,	4,	15,	12,	16,	27,	18,	8,	21,	8,	16,	10,	14,	19,	26,	11,																																											])

#statistical functions used to find elements of lin reg model

#takes the sum of the product of corresponding values
def dot(x,y):
    return sum(x*y for x,y, in zip(x,y))

#takes the value of array and subtracts from the mean
def de_mean(x):
    x_avg = np.mean(x)
    return [x-x_avg for x in x]

#finds the covariance. length is len(x)-1 since generally dot provides an underestimation in large sample sizes. 
def covariance(x,y):
    length = len(x)-1
    return dot(de_mean(x),de_mean(y))/length

#finds the correlation coefficient r. 
def correlation(x,y):
    stdev_x = np.std(x)
    stdev_y = np.std(y)
    return covariance(x,y)/(stdev_x*stdev_y)

#Using Least Squares to make sun of squared errors
def least_squares_fit(x,y):
    slope = correlation(x,y)*np.std(y)/np.std(x)
    intercept = np.mean(y) - slope*np.mean(x)
    return slope, intercept

#next finds the predicted values minus the actual
def prediction(intercept, slope, input):
    return slope * input + intercept

#finding errors between predicted and actual
def errors(intercept, slope, input, output):
    return output - prediction(intercept, slope, input)

#finding the sum of errors squared
def sum_of_errors_squared(intercept, slope, input, output):
    return sum(errors(intercept, slope, input, output)**2 for input, output, in zip(input, output))


#finds the slope and intercept, now we need to make the scatterplot and put the line of best fit on it
slope, intercept = least_squares_fit(projected_nba_scores, actual_nba_scores)
plt.scatter(projected_nba_scores, actual_nba_scores)
plt.plot(projected_nba_scores, slope * projected_nba_scores + intercept, color = 'red')
plt.xlabel("Stat Insider Predictions")
plt.ylabel("NBA Actual Points Scored")
plt.show()