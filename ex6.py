# -- coding: utf-8 --
#variables section
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# show value under the 'x'
print x
# show value under the 'y'
print y

# show what was under the %r param"
print "I said: %r." % x
# show what was under the %s param"
print "I also said: '%s'." % y
# another variable
hilarious = False
# try to evoke %r param in another string
joke_evaluation = "Isn't that joke so funny?! %r"
#show 
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e