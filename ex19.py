from sys import argv

script = argv
prompt = '> '

# function matrix which we use later
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# future use of defined function
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) # directly function invocation

print "OR, we can use variables from our script:" # re-Creation of function
amount_of_cheese = 10 # new values for function
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # new function args

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # math inside function

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # get the earlier define value and combine them and print

print "How many cheese we have?"
cheese_count = raw_input(prompt)
print "How many boxes of crackers we have?"
boxes_of_crackers = raw_input(prompt)
cheese_and_crackers(int(cheese_count), int(boxes_of_crackers))