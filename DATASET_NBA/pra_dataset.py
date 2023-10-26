#contains list of all the collected data
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is NBA Stats projecting?: "))


#dataset for high scores
projected_pra = np.array([42,	38.0,	25,	20,	36,	46,	23,	23,	15,	41,	36,	28,	43,	29,	29,	23,	32,	30,	26,	20,	27,	26,	40,	31,	24,	22,	39,	29,	25,	43,	33,	30,	30,	23,	32,	32,	23,	33,	33,	23,	22,	37,	27,	18,	18,	31,	16,	39,	31,	30,	30,	19,	23,	36,	32,	23,	18,	30,	29,	20,	25,	44,	36,	21,	37,	34,	32,	21,	41,	35,	35,	32,	34,	34,	23,])
actual_pra = np.array([34,	29.0,	26,	22,	29,	53,	26,	27,	23,	47,	31,	31,	33,	25,	29,	11,	11,	20,	28,	20,	24,	17,	33,	19,	14,	20,	31,	35,	32,	49,	22,	38,	15,	20,	23,	31,	29.0,	25,	27,	11,	25,	34,	20,	16,	28,	42,	30,	36,	21,	33,	30,	9,	18,	41,	32,	29,	18,	28,	19,	27,	30,	46,	28,	17,	23,	27,	24,	23,	33,	34,	32,	25,	16,	41,	20,																																																																	])
pra_prizepicks_line = np.array([38.5,	38.5,	23.0,	21.5,	33,	48,	21.5,	22.5,	15.0,	39.5,	41.0,	24,	42,	26.5,	24.0,	23.5,	30.5,	31.5,	27.5,	17.5,	26.5,	25.5,	39.5,	31.5,	20.5,	18.5,	39.5,	28,	22.5,	40,	31,	29.5,	28.0,	17.5,	34,	35,	25.5,	33.5,	27,	17.5,	24.5,	35.0,	24.5,	15.5,	19.5,	29.5,	16.5,	34.0,	28.5,	31.5,	33.5,	28.5,	23.5,	34.5,	32.5,	26.5,	19.5,	36.5,	22.5,	22.5,	26.5,	40.5,	31.5,	18,	34.5,	34.5,	32.0,	20.5,	35,	27,	37,	24.5,	28,	36,	25.5,																																																																	])


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


