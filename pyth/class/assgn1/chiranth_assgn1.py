f = open ("chiranth_assgn1.txt")
w = open("chd4.txt", 'w')
data = []
str1 = "dedicated.codero.net"
str2 = "Feb"

for lines in f:
	if ( str1 or  str2 ) in lines:
		w.write(lines)
w.close()
i=1
z=open("chd4.txt")
x=open("chd_final2.txt",'w')
y=open("chd_time.txt",'w')
for line in z:
        da = line.strip().split(" ")
        print da[5]
	x.write(da[5])
	x.write(" ")
	y.write(str(i))
	y.write(" ")
	i+=1
x.close()
y.close()
