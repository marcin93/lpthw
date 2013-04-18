# -*- coding: utf-8 -*-
from sys import argv # from module 'sys' import 'argv' element

script, filename = argv # by argv i will use

txt = open(filename) # variable txt opens the file which was given

print "Here's your file %r:" % filename # display name of file which was given
print txt.read() # print what is in file
txt.close()

print "Type the filename again:" 
file_again = raw_input("> ") # script get the new file name which will be open

txt_again = open(file_again) # new variable declaration and their duties > open given file

print txt_again.read() # print what is in given second file
txt_again.close()