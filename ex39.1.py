# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

# create a mapping of province to abbreviation
provinces = {
	'Mazowieckie': 'MA',
	'Łódzkie': 'LO',
	'Małopolskie': 'MP',
	'Pomorskie': 'PM',
	'Śląskie': 'SL'
	}
	
# create a basic set of province and some cities in them
cities = {
	'MA': 'Warszawa',
	'LO': 'Łódź',
	'SL': 'Katowice'
	}
	
# add some more cities
cities['PM'] = 'Gdańsk'
cities['MP'] = 'Kraków'

# print out more cities
print '-' * 10
print "MA province has: ", cities['MA']
print "SL province has: ", cities['SL']

# print some province
print '-' * 10
print "Mazowieckie's abbreviation is: ", provinces['Mazowieckie']
print "Małopolskie's abbreviation is: ", provinces['Małopolskie']

# do it by using the province then cities dict
print '-' * 10
print "Mazowieckie has: ", cities[provinces['Mazowieckie']]
print "Małopolskie has: ", cities[provinces['Małopolskie']]

# print every province abbreviation
with open(filename, 'w') as f:
	f.write ('-' * 10)
	for province, abbrev in provinces.items():
		f.write ("%s is abbreviated %s " % (province, abbrev))
		
	f.close()
# print every city in province
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
for province, abbrev in provinces.items():
	print "%s province is abbreviated %s and has city %s" % (province, abbrev, cities[abbrev])
	
print '-' * 10
# safely get a abbreviation by state that might not be there
province = provinces.get('Lubelskie', None)

if not province:
	print "Sorry, no Lubelskie."
	
# get a city with a default value
city = cities.get('LU', 'Does Not Exist')
print "The city for province 'LU' is: %s" % city