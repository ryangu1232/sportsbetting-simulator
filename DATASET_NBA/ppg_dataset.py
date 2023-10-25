#contains list of all the collected data
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is NBA Stats projecting?: "))


#dataset for high scores
projected_ppg = np.array([27,	25,	17,	13,	12,	25,	21,	16,	15,	10,	30,	25,	15,		11,	32,	23,	17.0,	16,])
actual_ppg = np.array([21,	17,	14,	11,	6,	21,	29,	12,	15,	20,	32,	18,	14,		17,	27,	15,	14,	10.0,])
pra_prizepicks_line = np.array([23.5,	23.5,	15.5,	13.5,	9.5,	22.5,	26,	14.5,	14,	10.5,	27.5,	28.5,	12.0,		5.5,	29.5,	19.5,	12.0,	16.5,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_ppg - projected_ppg
high_mean_error = sum(high_errors)/len(high_errors)
high_standard_dev = stat.stdev(high_errors)
absolute_pra_error = abs(high_errors)
absolute_pra_error_mean = sum(absolute_pra_error)/len(absolute_pra_error)

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



