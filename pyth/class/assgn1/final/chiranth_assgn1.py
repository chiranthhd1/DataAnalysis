import matplotlib.pyplot as plt
import numpy as np

# Below file contains my traceroute data
f = open ("chiranth_assgn1.txt")
# Fetching the last traceroute value by the last server name
str1 = "dedicated.codero.net"
# initiating empty lists

x=[]
y=[]
values = []

# Initiating the counter
i=1

# Fetching the last traceroute and adding it to Values List
for lines in f:
	if ( str1 ) in lines:
		values.append(lines)

# striping the traceroute and getting the first delay and adding it to X list
for line in values:
	y.append(str(i))	# counter
	i+=1
	value2 = line.strip().split(" ")
	x.append(float(value2[5]))

# This is just a plot of traceroute delay with no of traceroutes	
plt.plot(y,x)
plt.title(' Traceroute vs Time')
plt.xlabel('Time intervals')
plt.ylabel('Traceroute time')
plt.show()

# Choose how many bins you want here
num_bins = 50

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(x, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf

plt.title('Cdf')
plt.ylabel('Probability')
plt.xlabel('Traceroute Time')
plt.plot(bin_edges[1:], cdf)

plt.show()



