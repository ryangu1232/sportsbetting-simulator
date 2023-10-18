import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt

x = int(input("Enter the line for fantasy points as a player: "))

projected_high_scores = np.array([16.17,	18.61,	18.43,	19.03,	15.26,	17.71,])
actual_high_scores = np.array([24.88,	19.08,	17,	10.2,	18.7,	21.5,])
high_prizepicks_line = np.array([17,	19.5,	15.5,	16.5,	14.5,	18.5,])

high_error = actual_high_scores - projected_high_scores
high_error_mean = sum(high_error)/len(high_error)
high_standard_dev = stat.stdev(high_error)

plt.hist(high_error, np.arange(-10,11,5))
plt.show()


