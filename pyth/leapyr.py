inp = int (raw_input("Please neter the year"))

if (inp % 4 )  == 0:
	if (inp % 100) == 0:
		if (inp % 400) == 0:
			print ("entered year is a leap year")
		else:
			print ("2 Entered year is not a leap year")
	else:
		print ("2 Entered year is not a leap year")
else:
	print (" 3 Entered year is not a leap year")
