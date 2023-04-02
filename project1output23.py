import numpy as np
import matplotlib.pyplot as plt

# Read the samples from the text file
with open("samples.txt", "r") as f:
    lines = f.readlines()

samples1 = lines[0].strip().split(": ")[1].split()
samples2 = lines[1].strip().split(": ")[1].split()

# Categorize the data
data = {"Scenario 1": {"A": samples1.count("A"), "B": samples1.count("B")},
        "Scenario 2": {"A": samples2.count("A"), "B": samples2.count("B")}}

# Plot the data
fig, ax = plt.subplots()
ax.bar(data.keys(), [data[k]["A"] for k in data.keys()], label="A")
ax.bar(data.keys(), [data[k]["B"] for k in data.keys()], bottom=[data[k]["A"] for k in data.keys()], label="B")
ax.legend()
plt.show()
