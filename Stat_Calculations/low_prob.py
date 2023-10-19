import math


def compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation):
    # Calculate the required error for the actual points to exceed the prize picks line
    required_error = prize_picks_line - espn_projection
    
    # Calculate the Z-value
    z_value = (required_error - mean_error) / std_deviation
    
    # Calculate the probability using the Z-table (cumulative distribution function of the normal distribution)
    probability = 0.5 * (1 + math.erf(-z_value / math.sqrt(2)))
    
    # Convert probability to percentage
    probability_percentage = probability * 100
    
    return z_value, probability_percentage

# Example usage:
prize_picks_line = 22
espn_projection = 20
mean_error = 0
std_deviation = 3

z, prob = compute_probability(prize_picks_line, espn_projection, mean_error, std_deviation)
print(f"Z-value: {z:.2f}")
print(f"Probability of scoring more than {prize_picks_line} points: {prob:.2f}%")
