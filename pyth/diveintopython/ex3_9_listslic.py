#example 2.9 and example 3.10 , page 23
li = ['a','b','mpiligtim','z','example']
print "List is :", li
print " li[:3] : ", li[:3]
print " li[3:] :", li[3:]
print ' li[:]  :' , li[:]

li.append("new")
print "new list is: " , li
li.insert(2,"another")
print "new list after .insert(2,'another') : " , li

li.extend(["two","elements"])

print "new list after .extend(['two','elements']) is: " , li

