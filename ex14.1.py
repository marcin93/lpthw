# -*- coding: utf-8 -*-
from sys import argv

script, user_name = argv
pro = 'pisz_tu: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(pro)

print "Where do you live %s?" % user_name
lives = raw_input(pro)

print "What kind of computer do you have?"
computer = raw_input(pro)

print '''
Allright, so you said %r about liking me.
You live in %r. Not sure where this is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)