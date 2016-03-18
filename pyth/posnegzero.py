check = 1
while check ==1:
	num = float(raw_input("Please enter a number"))

	if num > 0:
		print ("entered number is positive")
	elif num < 0:
		print ("Entered number is negaive")
	elif num == 0:
		print("Entered number is zero")
	else :
		print ("Bye")
		break
