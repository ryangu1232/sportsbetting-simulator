#contains list of all the collected data
import numpy as np
import pandas as np
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is ESPN projecting?: "))


#dataset for low scores
projected_high_scores = np.array([16.17,	18.61,	18.43,	19.03,	15.26,	17.71,])
actual_high_scores = np.array([24.88,	19.08,	17,	10.2,	18.7,	21.5,])
high_prizepicks_line = np.array([17,	19.5,	15.5,	16.5,	14.5,	18.5,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_high_scores - projected_high_scores
high_mean_error = sum(high_errors)/len(high_errors)
high_standard_dev = stat.stdev(high_errors)


def compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation):    
    #solves for z value
    high_z_value = (prize_picks_line - espn_projection - mean_error) / std_deviation
    
    # Calculate the probability
    probability = 0.5 * (1 + math.erf(-high_z_value / math.sqrt(2)))
    
    # Convert probability to percentage
    probability_percentage = probability * 100
    
    return high_z_value, probability_percentage

z, prob = compute_probability(prize_picks_line, espn_projection, high_mean_error, high_standard_dev)
print(f"The probability of it hitting is {prob}")