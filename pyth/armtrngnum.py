num = int(raw_input("Enter a Number : "),)

sum1 = 0

temp = num

while temp > 0:
	digit = temp % 10
	sum1 += digit ** 3
	temp //=10

if num == sum1:
	print(num,"is an Armstrong umber")
else:
	print(num,"is not an armstrong number")
