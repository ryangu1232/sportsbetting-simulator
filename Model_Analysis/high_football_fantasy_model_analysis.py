import numpy as np
nope = "nope"
yes = "yes"

right_or_not = np.array([nope,	yes,	yes,	nope,	yes,	nope,	nope,	yes,	yes,	nope,	yes,	yes,	yes,	yes,])
num_right = np.count_nonzero(right_or_not == yes)
hit_percentages = np.array([52.75,	46.094,	53.68,	60.774,	41.36,	45.577,	50.67,	34.137,	40.453,]) 
model_prediction_percentages = np.mean(hit_percentages)

print("The number of correct is:", (num_right/len(right_or_not))*100)
print(model_prediction_percentages)


