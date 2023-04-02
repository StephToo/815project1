import numpy as np
import random as random


# Define the probability distribution with a configurable parameter
def generate_prob_dist(param):
    return np.array([param, 1 - param])

# Set up the two different scenarios with different parameter values
monolayer = 0.8
bilayer = 0.2

# Simulate random categorical samples from the probability distribution for scenario 1
num_samples1 = 100
samples1 = np.random.choice(["A", "B"], size=num_samples1, p=generate_prob_dist(monolayer))

# Simulate random categorical samples from the probability distribution for scenario 2
num_samples2 = 100
samples2 = np.random.choice(["A", "B"], size=num_samples2, p=generate_prob_dist(bilayer))

# Print the samples for both scenarios
print("Scenario 1 samples:", samples1)
print("Scenario 2 samples:", samples2)

# Save the generated samples to a text file
with open("samples.txt", "w") as f:
    f.write("Scenario 1 samples: " + " ".join(samples1) + "\n")
    f.write("Scenario 2 samples: " + " ".join(samples2) + "\n")

