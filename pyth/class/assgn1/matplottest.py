import numpy as np
import matplotlib.pyplot as plt
import pylab
data = np.loadtxt('chd_final.txt')

# Choose how many bins you want here
num_bins = 1000

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf

pylab.ylabel('cdf')
pylab.xlabel('traceroute time')
plt.plot(bin_edges[1:], cdf)

plt.show()

