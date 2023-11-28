#objective: to create a function that takes in two arrays and iterates them. 
#you want the function to take in the prizepicks line as well as take in the espn projections and return an array with the estimation percent
import numpy as np
import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import math


#dataset for high scores
projected_high_scores = np.array([42,	38.0,	25,	20,	36,	46,	23,	23,	15,	41,	36,	28,	43,	29,	29,	23,	32,	30,	26,	20,	27,	26,	40,	31,	24,	22,	39,	29,	25,	43,	33,	30,	30,	23,	32,	32,	23,	33,	33,	23,	22,	37,	27,	18,	18,	31,	16,	39,	31,	30,	30,	19,	23,	36,	32,	23,	18,	30,	29,	20,	25,	44,	36,	21,	37,	34,	32,	21,	41,	35,	35,	32,	34,	34,	23,	50,	40,	21,	26,	46,	27,	20,	38,	27,	19,	33,	32,	24,	30,	49,	33,	25,	22,	34,	32,	24,	16,	33,	35,	28,	39,	33,	32,	26,	20,	36,	34,	32,	21,	33,	20,	23,	20,	39,	28,	23,	33,	28,	19,	41,	31,	22,			46,	34,	26,	22,		58,	48,		22,	21,	42,	31,	21,	25,	21,	44,	30,	23,			34,	27,	34,	17,		51,		34,	26,	40,	37,	18,	38,	37,	29,	25,	36,	36,	32,	20,	27,	27,	27,	42,	37,	33,	34,	25,	28,	27,		21,	20,	35,	35,	32,	19,		34,	24,	20,	21,	50,					34,	32,	22,	22,			35,	29,		20,		52,	43,	22,	36,	21,	24,	21,		45,	32,	23,				38,	28,	21,	19,	23,	48,	35,	23,	23,		24,		25,	21,		43,	39,		26, ])
actual_high_scores = np.array([34,	29.0,	26,	22,	29,	53,	26,	27,	23,	47,	31,	31,	33,	25,	29,	11,	11,	20,	28,	20,	24,	17,	33,	19,	14,	20,	31,	35,	32,	49,	22,	38,	15,	20,	23,	31,	29.0,	25,	27,	11,	25,	34,	20,	16,	28,	42,	30,	36,	21,	33,	30,	9,	18,	41,	32,	29,	18,	28,	19,	27,	30,	46,	28,	17,	23,	27,	24,	23,	33,	34,	32,	25,	16,	41,	20,	38,	51,	15,	13,	37,	43,	29,	52,	16,	17,	38,	44,	13,	23,	41,	27,	15,	25,	21,	32,	23,	23,	23,	26,	23,	36,	31,	22,	12,	13,	55,	26,	17,	3,	39,	20,	23,	11,	51,	47,	19,	22,	37,	29,	18,	14,	11,			47,	29,	14,	31,		40,	15,		17,	23,	34,	21,	19,	25,	25,	37,	23,	13,			12,	31,	31,	18,		57,		40,	31,	49,	32,	12,	48,	50,	29,	9,	28,	28,	30,	24,	11,	15,	19,	42,	24,	44,	19,	14,	16,	30,		21,	19,	29,	26,	44,	12,		37,	34,	20,	23,	59,					39,	43,	37,	14,			21,	44,		16,		42,	34,	21,	24,	20,	20,	21,		45,	31,	9,				46,	13,	25,	12,	27,	48,	35,	11,	30,		28,		19,	26,		26,	50,		17,																																																	])
high_prizepicks_line = np.array([38.5,	38.5,	23.0,	21.5,	33,	48,	21.5,	22.5,	15.0,	39.5,	41.0,	24,	42,	26.5,	24.0,	23.5,	30.5,	31.5,	27.5,	17.5,	26.5,	25.5,	39.5,	31.5,	20.5,	18.5,	39.5,	28,	22.5,	40,	31,	29.5,	28.0,	17.5,	34,	35,	25.5,	33.5,	27,	17.5,	24.5,	35.0,	24.5,	15.5,	19.5,	29.5,	16.5,	34.0,	28.5,	31.5,	33.5,	28.5,	23.5,	34.5,	32.5,	26.5,	19.5,	36.5,	22.5,	22.5,	26.5,	40.5,	31.5,	18,	34.5,	34.5,	32.0,	20.5,	35,	27,	37,	24.5,	28,	36,	25.5,	44,	38.5,	20,	20.5,	43.5,	29.5,	23,	43.5,	25.5,	19.5,	33,	38.5,	23.5,	23.5,	50.5,	32.5,	23.5,	24.5,	35.5,	28.5,	22.5,	16.5,	31.5,	33.5,	26.5,	36.5,	36.5,	27.5,	24.5,	17.5,	29.5,	30.5,	28.5,	23.5,	32,	17.5,	20.5,	17.5,	44.5,	33.5,	22.5,	35,	28.5,	21.5,	39.5,	28.5,	19.5,			48.5,	32.5,	22.5,	23.5,		45.5,	43.5,		20.5,	16.5,	38.5,	28.5,	19.5,	21.5,	16.5,	40.5,	25.5,	21.5,			29.5,	29,	31.5,	17.5,		44.5,		39,	25.5,	36.5,	38.5,	17.5,	38.5,	36.5,	23.5,	22.5,	35.5,	32.5,	26.5,	18.5,	25.5,	25.5,	23.5,	39.5,	30.5,	31,	25.5,	20.5,	30.35,	31.5,		22,	21.5,	34,	31,	28.5,	21.5,		34.5,	22.5,	16.5,	19.5,	53.5,					35.5,	27.5,	23.5,	23.5,			34.5,	32,		18.5,		44.5,	39.5,	20.5,	34.5,	18.5,	23.5,	16.5,		40.5,	28.5,	17.5,				31.5,	24.5,	20.5,	13.5,	19,	47.5,	32.5,	24,	21.5,		26.5,		21.5,	20.5,		33.5,	41.5,		20.5,																																																	])

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
results = np.array([nope,	nope,	yes,	yes,	nope,	yes,	yes,	yes,	yes,	yes,	nope,	yes,	nope,	nope,	yes,	nope,	nope,	nope,	yes,	yes,	nope,	nope,	nope,	nope,	nope,	yes,	nope,	yes,	yes,	yes,	nope,	yes,	nope,	yes,	nope,	nope,	yes,	nope,	yes,	nope,	yes,	nope,	nope,	yes,	yes,	yes,	yes,	yes,	nope,	yes,	nope,	nope,	nope,	yes,	nope,	yes,	nope,	nope,	nope,	yes,	yes,	yes,	nope,	nope,	nope,	nope,	nope,	yes,	nope,	yes,	nope,	yes,	nope,	yes,	nope,	nope,	yes,	nope,	nope,	nope,	yes,	yes,	yes,	nope,	nope,	yes,	yes,	nope,	nope,	nope,	nope,	nope,	yes,	nope,	yes,	yes,	yes,	nope,	nope,	nope,	nope,	nope,	nope,	nope,	nope,	yes,	nope,	nope,	nope,	yes,	yes,	yes,	nope,	yes,	yes,	nope,	nope,	yes,	yes,])
high_prob = compute_probability(high_prizepicks_line, projected_high_scores, high_mean_error, high_standard_dev, array_of_prob_percentages)


#finds the total accuracy of the model
model_average = np.average(high_prob)
actual_results = (np.count_nonzero(results == "yes")/(len(results)+1))*100

#array of %averages is stored in the high_prob variable. 
print(f"the model predicts {model_average} of the bets will hit and {actual_results} of the bets hit, meaning that the model is {model_average - actual_results} over")