import matplotlib.pyplot as plt

# Read in the data from the two text files
# https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html
# https://www.pythontutorial.net/python-basics/python-write-text-file/
with open('simulated_data_1.txt', 'r') as file1, open('simulated_data_2.txt', 'r') as file2:
    data_1 = [float(line) for line in file1]
    data_2 = [float(line) for line in file2]

# Plot the data from the two scenarios on the same plot
# https://www.geeksforgeeks.org/how-to-plot-data-from-a-text-file-using-matplotlib/
plt.plot(data_1, label='Hydrogen Gas')
plt.plot(data_2, label='Methane Gas')


# Add labels and title to the plot
plt.xlabel('Time (min)')
plt.ylabel('Change in Flow Rate (sccm)')
plt.title('Flow Rate of Gases Over Time in Chemical Vapor Deposition System')
plt.legend()
plt.show()

