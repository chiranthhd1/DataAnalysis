i = 0
numbers = []
number = int(raw_input("> "))

def loop():
    #global i
    print "At the top i is ", i
    numbers.append(i)
    
    print "At the bottom i is ", number-i
                
while i<number:
    loop()
    i += 1
    
print "The numbers are:"

for num in numbers:
    print num   
