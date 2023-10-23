#objective: to create a function that takes in two arrays and iterates them. 
#you want the function to take in the prizepicks line as well as take in the espn projections and return an array with the estimation percent
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math


#dataset for high scores
projected_high_scores = np.array([16.17,	18.61,	18.43,	19.03,	15.26,	17.71,	14.21,	16.27,	16.58,	14.02,	14.22,	13.34,	12.02,	10.62,	14.8,	19.07,		18.15,	14.13, 	10.79,	19.66,	12.63, 	12.81,	19.43,	13.32,	16.01,	15.64,	11.82, 	12.18,	12.43,	15.88,	18.94,	22.75,	18.17,	16.16,	19.0,	18.25,	11.95,])
actual_high_scores = np.array([24.88,	19.08,	17,	10.2,	18.7,	21.5,	17.44,	22.70,	29.30,	1.50,	12.70,	19.00,	13.20,	9.50,	9.36,	33.88,		23.20,	11.5,	19.98,	24.30,	14.50,	19.20,	17.80,	13.80,	16.20,	0.3,	15.90,	12.60,	11.40,	20.20,	10.86,	33.86,	5.60,	16.00,	9.50,	35.90,	18.30,])
high_prizepicks_line = np.array([17,	19.5,	15.5,	16.5,	14.5,	18.5,	15,	15,	15.5,	11.5,	12.5,	12.5,	12.0,	11.0,	15.0, 	21, 		15.5,	12,	11, 	20.5, 	10, 	11, 	19, 	13.5, 	14.5, 	14.5, 	12, 	12.5, 	10.5, 	12.5, 	20.0, 	23.5, 	16.0, 	13.5, 	17, 	17, 	10.5, ])

array_of_prob_percentages = np.array([])


#calculates the errors, average of errors, and standard deviation of low errors to determine variation of errors. 
high_errors = actual_high_scores - projected_high_scores
high_mean_error = sum(high_errors)/len(high_errors)
high_standard_dev = stat.stdev(high_errors)


def compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation, prob_percentages):    
    for i in np.arange(0,len(projected_high_scores)):
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
results = np.array([yes,	nope,	yes,	nope,	yes,	yes,	yes,	yes,	yes,	nope,	yes,	yes,	yes,	nope,	nope,	yes,		yes,	nope,	yes,	yes,	yes,	yes,	nope,	yes,	yes,	nope,	yes,	yes,	yes,	yes,	nope,	yes,	nope,	yes,	nope,	yes,	yes,])
high_prob = compute_probability(high_prizepicks_line, projected_high_scores, high_mean_error, high_standard_dev, array_of_prob_percentages)
model_average = np.average(high_prob)
actual_results = (np.count_nonzero(results == "yes")/(len(results)+1))*100
print(model_average)
