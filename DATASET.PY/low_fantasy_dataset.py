#contains list of all the collected data
import numpy as np
import pandas as np
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is ESPN projecting?: "))


#dataset for low scores
projected_low_scores = np.array([9.8,	9.16,	9.39,	11.58,	8.2,	8.11,])
actual_low_scores = np.array([2.5,   15.00,	5.40,	10.00,	8.00,	5.00,])
low_prizepicks_line = np.array([8.5,	8.5,	8,	9.5,	8,	7.5,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
low_errors = actual_low_scores - projected_low_scores
low_mean_error = sum(low_errors)/len(low_errors)
low_standard_dev = stat.stdev(low_errors)
coef_of_variation = low_standard_dev/low_errors


def compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation):
    # Calculate the required error for the actual points to exceed the prize picks line
    required_error = prize_picks_line - espn_projection
    
    # Calculate the Z-value
    z_value = (required_error - mean_error) / std_deviation
    
    # Calculate the probability using the Z-table (cumulative distribution function of the normal distribution)
    probability = 0.5 * (1 + math.erf(-z_value / math.sqrt(2)))
    
    # Convert probability to percentage
    probability_percentage = probability * 100
    
    return z_value, probability_percentage

z, prob = compute_probability(prize_picks_line, espn_projection, low_mean_error, low_standard_dev)
print(f"Z-value: {z:.2f}")
print(f"Probability of scoring more than {prize_picks_line} points: {prob:.2f}%")


