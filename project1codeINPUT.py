import random

# Define the probability distribution with a configurable parameter
# https://www.geeksforgeeks.org/random-normalvariate-function-in-python/
def probability_distribution(parameter):
    return random.normalvariate(0, parameter)

# Set the configurable parameter values
parameter_value_1 = 0.33
parameter_value_2 = 0.15

# Simulate the experiment, store simulated results in a persistent data format
# https://www.pythontutorial.net/python-basics/python-write-text-file/
with open('simulated_data_1.txt', 'w') as file1, open('simulated_data_2.txt', 'w') as file2:
    for i in range(100):
        result_1 = probability_distribution(parameter_value_1)
        result_2 = probability_distribution(parameter_value_2)
        file1.write(str(result_1) + '\n')
        file2.write(str(result_2) + '\n')

