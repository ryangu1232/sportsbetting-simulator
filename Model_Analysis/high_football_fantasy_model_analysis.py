import numpy as np
nope = "nope"
yes = "yes"

right_or_not = np.array([yes,	nope,	yes,	nope,	yes,	yes,	yes,	yes,	yes,	nope,	yes,	yes,	yes,	nope,])
num_right = np.count_nonzero(right_or_not == yes)
hit_percentages = np.array([51.31,	53.36,	74.73,	72.74,	63.14,	53.96,	53.96,	66.03,	64.96,	72.70,	68.50,	63.60,	58.82,	56.43,]) 
model_prediction_percentages = np.mean(hit_percentages)
percent_right = (num_right/len(right_or_not))*100
degree_of_error = abs(percent_right-model_prediction_percentages)

print("The percentage that hit is:", percent_right)
print(f"The model predicts that {model_prediction_percentages} of the bets will be correct.")
print("The degree of error is:", degree_of_error)


