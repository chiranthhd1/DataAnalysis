len_things = "Apples oranges crows telephones light sugar"

print "Wait there's ot 10 things in that list, let fix that."

stuff = len_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","girl","boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." %len(stuff)

print "There we go: ", stuff

print "Lets do some things with stuff"

print stuff[1]
print stuff[-1] #fancy!!
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

