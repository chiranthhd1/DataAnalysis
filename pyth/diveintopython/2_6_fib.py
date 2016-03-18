def fib(n):
	print "n = ", n
	if n > 1:
		return n*fib(n-1)
	else:
		print "End of the line"
		return 1

n = int(raw_input("Enter the number"))
print "Fib series is : ",  fib(n)
