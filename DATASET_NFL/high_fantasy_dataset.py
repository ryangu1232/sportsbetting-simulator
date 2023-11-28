#contains list of all the collected data
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is ESPN projecting?: "))


#dataset for high scores
projected_high_scores = np.array([16.17,	18.61,	18.43,	19.03,	15.26,	17.71,	14.21,	16.27,	16.58,	14.02,	14.22,	13.34,	12.02,	10.62,	14.8,	19.07,		18.15,	14.13, 	10.79,	19.66,	12.63, 	12.81,	19.43,	13.32,	16.01,	15.64,	11.82, 	12.18,	12.43,	15.88,	18.94,	22.75,	18.17,	16.16,	19.0,	18.25,	11.95,])
actual_high_scores = np.array([24.88,	19.08,	17,	10.2,	18.7,	21.5,	17.44,	22.70,	29.30,	1.50,	12.70,	19.00,	13.20,	9.50,	9.36,	33.88,		23.20,	11.5,	19.98,	24.30,	14.50,	19.20,	17.80,	13.80,	16.20,	0.3,	15.90,	12.60,	11.40,	20.20,	10.86,	33.86,	5.60,	16.00,	9.50,	35.90,	18.30,])
high_prizepicks_line = np.array([17,	19.5,	15.5,	16.5,	14.5,	18.5,	15,	15,	15.5,	11.5,	12.5,	12.5,	12.0,	11.0,	15.0, 	21, 		15.5,	12,	11, 	20.5, 	10, 	11, 	19, 	13.5, 	14.5, 	14.5, 	12, 	12.5, 	10.5, 	12.5, 	20.0, 	23.5, 	16.0, 	13.5, 	17, 	17, 	10.5, ])

#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_high_scores - projected_high_scores
high_mean_error = sum(high_errors)/len(high_errors)
high_standard_dev = stat.stdev(high_errors)


def compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation):    
    #solves for z value
    high_z_value = (prize_picks_line - espn_projection - mean_error) / std_deviation
    
    # calculates the probability
    probability = 0.5 * (1 + math.erf(-high_z_value / math.sqrt(2)))
    
    # converts to percent
    probability_percentage = probability * 100
    
    return probability_percentage

prob = compute_probability(prize_picks_line, espn_projection, high_mean_error, high_standard_dev)
print(f"The probability of it hitting is {prob}")

