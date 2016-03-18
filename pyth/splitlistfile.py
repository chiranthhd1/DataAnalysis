f = open("uptest.csv",'r')
data = f.read()
row = data.split("\n")
data = []

for f in row:
	test = f.split(",")
	data.append(test)
print (data[0:3])
print (data[3])
print (data[0][1])






