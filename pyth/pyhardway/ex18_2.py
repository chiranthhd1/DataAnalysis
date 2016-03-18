def print_two(*a):
	arg1,arg2 = a
	print "These are the values of 'a' and two arguments for the function %r and %r " %(arg1,arg2)

def print_two_again(arg1,arg2):
	print " These are the values fed directly to the fucntion during def %r and %r " %(arg1,arg2)

print_two("chi","hd")
print_two_again("chiranth","hd")
