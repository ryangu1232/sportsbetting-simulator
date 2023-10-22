import numpy as np
from matplotlib import pyplot as plt
import statistics as stat

projected_low_scores = np.array([9.8,	9.16,	9.39,	11.58,	8.2,	8.11,	8.6,	6.97,	7.61,])
actual_low_scores = np.array([2.5,	15.00,	5.40,	10.00,	8.00,	5.00,	7.20,	10,	7.00,])
low_prizepicks_line = np.array([8.5,	8.5,	8,	9.5,	8,	7.5,	7.5,	7.5,	7.5,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
low_errors = actual_low_scores - projected_low_scores
low_mean_error = sum(low_errors)/len(low_errors)
low_standard_dev = stat.stdev(low_errors)
coef_of_variation = low_standard_dev/low_errors

plt.hist(low_errors, bins = [-10, -5, 0, 5, 11])
plt.show()


print(low_errors)