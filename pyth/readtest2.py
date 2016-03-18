#f = open("TestData.csv","r")
f = open("uptest.csv","r")

data = f.read()
#rows = data.split(",")
rows = data.split("\n")
#print(rows)
print(rows[0:10])




