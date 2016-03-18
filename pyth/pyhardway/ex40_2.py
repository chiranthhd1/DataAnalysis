states = {
	'Oregon': 'OR',
	'New Jersey': 'NJ',
	'New york': 'NY',
	'Florida': 'FL'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Michigan',
	'FL': 'Florida',
}

cities['NY'] = 'New York'
cities['JC'] = 'Jersey city'

print '-' * 20

print "NY state has: ", cities['NY']
print "NJ state has: ", cities['JC']

print '-'*20

#using the state and then the cities dict
print '-'*20
print 'New York has ', cities[states['New york']]
print 'florida has ', cities[states['Florida']]
print '-'*20
