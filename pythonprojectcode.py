# I want to use a categorical distribution of randomly sampled values to understand the weather
# I will divide the weather "types" into 3 bins, with their values corresponding to limits placed on the random data

import numpy as np

# I will probably change these values depending on what limits I want to set for the random data
probabilities = [0.1, 0.5, 1]


values = np.cumsum(probabilities)

np.random.rand()

dataset = np.random.rand(10)
# this will give me 10 sampled values but I will increase this once I have coded a histogram to plot the data to in a separate python file
print(dataset)
# print commands are here for now so I can see what the output of my code is each time 

condlist = [dataset <= limit for limit in values]
# this limit is set by the values I have assigned from the probabilities
# this is how I will characterize my data 

print(condlist)

# I would like to make this code more complex but for now want to make sure it can do the minimum of what I am asking it to do

