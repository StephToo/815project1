# I want to use a categorical distribution of randomly sampled values to understand the weather
# I will divide the weather "types" into 3 bins, with their values corresponding to limits placed on the random data

import numpy as np

# Probababilities attached to the null hypothesis that warm temps are more likely
nullprobabilities = [0.1, 0.3, 0.6]

nullvalues = np.cumsum(nullprobabilities)

np.random.rand()

nulldataset = np.random.rand(100)
# this will give me 10 sampled values but I will increase this once I have coded a histogram to plot the data to in a separate python file
print(nulldataset)
# print commands are here for now so I can see what the output of my code is each time 

nullcondlist = [nulldataset <= limit for limit in nullvalues]
# this limit is set by the values I have assigned from the probabilities
# this is how I will characterize my data 

print(nullcondlist)

# I would like to make this code more complex but for now want to make sure it can do the minimum of what I am asking it to do


probabilities = [0.5, 0.4, 0.1]

values = np.cumsum(probabilities)

np.random.rand()

dataset = np.random.rand(100)
# this will give me 10 sampled values but I will increase this once I have coded a histogram to plot the data to in a separate python file
print(dataset)
# print commands are here for now so I can see what the output of my code is each time 

condlist = [dataset <= limit for limit in values]
# this limit is set by the values I have assigned from the probabilities
# this is how I will characterize my data 

print(condlist)



# null hypothsis 0: probability low temperatures is X probability of medium temps is Y and probability of cold temps is Z
# so proabavilities for hyp 0 is = [0.1,0.3,0.6]
# hypothesis 1: probability of low temp is X' prob of medium temp is Y' and prob of cold temps is Z'
# probabitlies for hyp 1 is = [0.4,0.5,0.1]

# let us now look at null hypotheis
# we will set p = 0.4 