from sys import argv

script , user_name = argv
prompt = '>'

print "Hi, %s , I'm the %s script," % (user_name, script)

print "Do you like me %r" %user_name
like = raw_input(prompt)
print "Thank you for being frank that you %r like me" %like

print "where do you live %r" %user_name
place = raw_input(prompt)

print "%r is a nice place to live" %place
print "Now fuck off"

 
