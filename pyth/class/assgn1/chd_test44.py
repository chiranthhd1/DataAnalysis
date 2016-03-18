import matplotlib.pyplot as plt
import pylab
import numpy as np

f = open ("chiranth_assgn1.txt")
w = open("chd44.txt", 'w')
data = []
str1 = "dedicated.codero.net"
x=[]
y=[]
for lines in f:
	if ( str1 ) in lines:
		w.write(lines)
w.close()
i=1
z=open("chd44.txt")
x1=open("chd_final44.txt",'w')
y1=open("chd_time44.txt",'w')
for line in z:
        da = line.strip().split(" ")
	x1.write(da[5])
	x1.write(" ")
	x.append(da[5])
	y1.write(str(i))
	y1.write(" ")
	y.append(str(i))
	i+=1
x1.close()
y1.close()

plt.scatter(y,x)
pylab.xlabel('time intervals')
pylab.ylabel('traceroute time')
plt.show()

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
plt.scatter(bin_edges[1:], cdf)

plt.show()

