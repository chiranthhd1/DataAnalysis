from sys import argv

script, filename = argv
n = "\n"

print "We're going to erase this file %r" %filename
print "If you dont want to continue press ctrl+c"
print "to continue press enter"

raw_input("?")

print "opening file now"
target = open(filename,'w')


target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line1 : ")
line2 = raw_input("line1 : ")
line3 = raw_input("line1 : ")

print "Writing to the file now"
#target.write(line1, n , line2, n, line3,n )

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Done! saving now"
target.close()

