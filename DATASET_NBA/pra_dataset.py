#contains list of all the collected data
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is NBA Stats projecting?: "))


#dataset for high scores
projected_pra = np.array([42,38.0,25,	20,	36,	46,	23,	23,	15,	41,	36,	28,	43,	29,	29,	23,	])
actual_pra = np.array([34.0,	29,	26,	22,	29,	53,	26,	27,	23,	47,	31,	31,	33,	25,	29,	11,	])
pra_prizepicks_line = np.array([38.5,38.5,23.0,	21.5,33,48,	21.5,22.5,15.0,	39.5,41.0,24, 42,	26.5,	24.0,	23.5,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_pra - projected_pra
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
print(high_mean_error)
print(absolute_pra_error_mean)


