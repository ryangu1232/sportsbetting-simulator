#objective: to create a function that takes in two arrays and iterates them. 
#you want the function to take in the prizepicks line as well as take in the espn projections and return an array with the estimation percent
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math


#dataset for high scores
projected_low_scores = np.array([9.8,	9.16,	9.39,	11.58,	8.2,	8.11,	8.6,	6.97,	7.61,	12.27,	7.98,	7.86,	8.53,	9.7,	6.36,	5.44,	8.43,	7.24,	7.76,	9.74,	6.63,	8.03,	8.75,	8.72,])
actual_low_scores = np.array([2.5,	15.00,	5.40,	10.00,	8.00,	5.00,	7.20,	10,	7.00,	11.20,	8.0,	0,	16.30,	1.60,	15.5,	11.0,	5.00,	14.20,	7.00,	7.70,	12.00,	7.00,	7.00,	21.40,])
low_prizepicks_line = np.array([8.5,	8.5,	8,	9.5,	8,	7.5,	7.5,	7.5,	7.5,	9.5, 	8,	8,	9,	8,	6,	6, 	8.5,	6, 	6.5,	7.5,	7.5,	7.5,	8.5,	6.5,])

array_of_prob_percentages = np.array([])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
low_errors = actual_low_scores - projected_low_scores
low_mean_error = sum(low_errors)/len(low_errors)
low_standard_dev = stat.stdev(low_errors)

array_of_low_prob_percentages = np.array([])

def compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation, prob_percentages):    
    for i in np.arange(0,len(projected_low_scores)):
        standard = prize_picks_line[i] - espn_projection[i]
        
        high_z_value = (standard - mean_error) / std_deviation
    
        # calculates the probability
        probability = 0.5 * (1 + math.erf(-high_z_value / math.sqrt(2)))
    
        # converts to percent
        probability_percentage = probability * 100
    
        prob_percentages = np.append(prob_percentages, probability_percentage )
    return prob_percentages

yes = "yes"
nope = "nope"
results = np.array([nope,	yes,	nope,	yes,	yes,	nope,	nope,	nope,	nope,])
low_prob = compute_probability(low_prizepicks_line, projected_low_scores, low_mean_error, low_standard_dev, array_of_low_prob_percentages)
model_average = np.average(low_prob)
actual_results = (np.count_nonzero(results == "yes")/(len(results)+1))*100
#print(f"The margin of error is {model_average - actual_results}")
print(actual_results)
print(model_average)