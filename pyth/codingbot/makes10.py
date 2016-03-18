def makes10(a, b):
	if (a or b) == 10:
  		return True
 	elif (a+b)==10:
  		return True
 	else:
  		return False

a=raw_input("a")
b=raw_input("b")

c=makes10(a,b)
print c
