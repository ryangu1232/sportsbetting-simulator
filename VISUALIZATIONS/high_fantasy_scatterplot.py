import numpy as np
from matplotlib import pyplot as plt
import statistics as stat

#dataset for high scores
projected_high_scores = np.array([16.17,	18.61,	18.43,	19.03,	15.26,	17.71,	14.21,	16.27,	16.58,	14.02,	14.22,	13.34,	12.02,	10.62,])
actual_high_scores = np.array([24.88,	19.08,	17,	10.2,	18.7,	21.5,	17.44,	22.70,	29.30,	1.50,	12.70,	19.00,	13.20,	9.50,])
high_prizepicks_line = np.array([17,	19.5,	15.5,	16.5,	14.5,	18.5,	15,	15,	15.5,	11.5,	12.5,	12.5,	12.0,	11.0,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_high_scores - projected_high_scores
high_mean_error = sum(high_errors)/len(high_errors)
high_standard_dev = stat.stdev(high_errors)

plt.hist(high_errors, bins = np.arange(-15,16,5))
plt.show()

