#contains list of all the collected data
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math

prize_picks_line = float(input("Input the Prizepicks Line: "))
espn_projection = float(input("How many fantasy points is NBA Stats projecting?: "))


#dataset for high scores
projected_ppg = np.array([27,	25,	17,	13,	12,	25,	21,	16,	15,	10,	30,	25,	15,	11,	32,	23,	17,	16,	24,	18,	14,	14,	20,	15,	26,	20,	18,	15,	24,	21,	17,	29,	24,	20,	19,	16,	24,	20,	17,	24,	23,	14,	12,	23,	18,	12,	12,	19,	9,	26,	23,	18,	23,	12,	11,	26,	20,	12,	10,	20,	15,	14,	14,	33,	20,	14,	28,	24,	17,	13,	28,	24,	24,	17,	24,	23,	15,	32,	30,	14,	16,	32,	21,	13,	26,	12,	12,	14,	11,	21,	20,	17,	21,	11,	25,	22,	15,	15,	12,	24,	23,	13,	11,	21,	15,	21,	16,	15,	25,	23,	20,		9,	27,	23,	23,	14,	12,	28,	25,	13,	10,	27,	21,	14,	10,	21,	17,	13,])
actual_ppg = np.array([21,	17,	14,	11,	6,	21,	29,	12,	15,	20,	32,	18,	14,	17,	27,	15,	14,	10,	10,	14,	14,	14,	19,	8,	23,	11,	9,	15,	15,	24,	25,	34,	11,	30,	9,	12,	15,	14,	24,	18,	25,	6,	16,	20,	11,	11,	24,	30,	14,	19,	16,	22,	20,	5,	7,	26,	19,	15,	11,	15,	7,	20,	17,	31,	16,	8,	16,	20,	11,	15,	23,	24,	19,	12,	8,	31,	17,	23,	39,	13,	6,	24,	31,	20,	39,	4,	10,	15,	6,	21,	30,	10,	14,	0,	22,	22,	10,	9,	8,	15,	21,	13,	11,	12,	15,	20,	19,	13,	14,	10,	18,		5,	26,	24,	12,	8,	10,	51,	20,	14,	6,	34,	34,	15,	2,	11,	24,	15,])
pra_prizepicks_line = np.array([23.5,	23.5,	15.5,	13.5,	9.5,	22.5,	26,	14.5,	14,	10.5,	27.5,	28.5,	12.0,	5.5,	29.5,	19.5,	12.0,	16.5,	22.5,	19.5,	14.5,	11.5,	17.5,	12.5,	26.5,	20.5,	14.5,	12.5,	23.5,	19.5,	15.5,	26,	22,	18.5,	15.5,	11.5,	23.5,	22.5,	18,	24.5,	18,	10.5,	12.5,	20.5,	15.5,	10.5,	12.5,	19.5,	8.5,	22.5,	20.5,	18.5,	26.5,	17.5,	11.5,	24.5,	21.5,	13.5,	11.5,	23.5,	10.5,	16.5,	15.5,	29.5,	16.5,	11.5,	25.5,	23.5,	16.5,	12.5,	24.5,	18.5,	24.5,	13,	19.5,	25.5,	14.5,	27.5,	26,	13.5,	12.5,	28.5,	22.5,	14.5,	31,	13.5,	9,	14.5,	10.5,	20.5,	24,	14.5,	14.5,	10,	27.5,	21.5,	14,	15.5,	9.5,	24.5,	18.5,	10.5,	11,	22.5,	11.5,	21.5,	13.5,	16.5,	23.5,	24.5,	19.5,		7.5,	24.5,	25.5,	18.5,	11.5,	10.5,	22.5,	21.5,	11.5,	10.5,	29.5,	24.5,	14.5,	9.5,	22.5,	16.5,	12.5,])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_ppg - projected_ppg
high_errors = high_errors.astype(float)
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



