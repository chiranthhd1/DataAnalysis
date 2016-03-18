num1 = float(raw_input("enter the first number: "),)
num2 = float(raw_input("enter the second number: "),)
num3 = float(raw_input("enter the third number: "),)


if (num1 == num2 == num3):
	print ("All numbers are equa")


elif (num1 > num2):
	if (num1 > num3):
		print (" %f is greater ") %(num1)
	elif ( num3 > num2):
		print ("%f is greater" ) %(num3)
	else:
		print ("Numbers are equal")
else:
	if (num2 > num3):	
		print (" %f is greater ")%(num2)
	elif ( num3 > num1):
		print ("%f is greater" ) %(num3)
	else:
		print ("Numbers are equal")
 


