def add(a,b):
	print "Adding %f and %f" %(a,b)
	return a+b
def sub(a,b):
	print "Subtracting %d and %d" %(a,b)
	return a-b
def mult(a,b):
	print "Multiplying %r and %r" %(a,b)
	return a*b
def div(a,b):
	print "Dividing %r and %r" %(a,b)
	return a/b

print "Lets do some math using functions"
a=float(raw_input(" enter the first number\n"))
b=float(raw_input("enter the second number \n"))

ad = add(a,b)
su = sub(a,b)
mu = mult(a,b)
di = div(a,b)

print "Sum is %r, sub is %r, mul is %r and div is %r" %(ad,su,mu,di)

# A puzzle

print "Here is a puzzle"

what = add(ad , sub (su , mult(mu , div(di,2))))

print "This becomes ", what ,"can you guess whats done here"

