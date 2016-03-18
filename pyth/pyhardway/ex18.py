def print_two(*a):
	arg1,arg2 = a
	print "arg1: %r, arg2: %r" %(arg1,arg2)

def print_two_again(arg1,arg2):
	print "arg1: %r, \targ2: %r" %(arg1,arg2)

def print_one(arg1):
	print "arg1: %r" %arg1

def print_none():
	print "I got nothin!"

print_two("chiranth","hd")
print_two_again("Chir","Anth")
print_one("chiranth")
print_none()
