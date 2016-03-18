def somefun():
	print "this is a random function"

def anothrfun():
	x = somefun
	return x

a = anothrfun
 
a()
