#contains list of all the collected data
import numpy as np
import pandas as np
import statistics as stat
from matplotlib import pyplot as plt

projected_low_scores = np.array([9.8,	9.16,	9.39,	11.58,	8.2,	8.11,])
actual_low_scores = np.array([2.5,   15.00,	5.40,	10.00,	8.00,	5.00,])
low_prizepicks_line = np.array([8.5,	8.5,	8,	9.5,	8,	7.5,])

projected_high_scores = np.array([16.17,	18.61,	18.43,	19.03,	15.26,	17.71,])
actual_high_scores = np.array([24.88,	19.08,	17,	10.2,	18.7,	21.5,])
high_prizepicks_line = np.array([17,	19.5,	15.5,	16.5,	14.5,	18.5,])

#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
low_errors = actual_low_scores - projected_low_scores
low_mean_error = sum(low_errors)/len(low_errors)
low_standard_dev = stat.stdev(low_errors)
coef_of_variation = low_standard_dev/low_errors


 
print("Standard Deviation of sample is % s "
    % low_standard_dev)
print(coef_of_variation)