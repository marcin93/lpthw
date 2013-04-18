from sys import argv # script will be use some params

script, input_file = argv # to run will be use script name and 2nd param

def print_all(f):
	print f.read() # read and print while file

def rewind(f):
	f.seek(0) # set the pointer to the '0' byte in open file
	
def print_a_line(line_count, f):
	print line_count, f.readline() # print number of line and the line
	
current_file = open(input_file) # variable 'current_file' is the whole file

print "First let's print the whole file:\n"

print_all(current_file) # 'print_all' invocation on 'current_file' variable

print "Now let's rewind, kind of like a tape."

rewind(current_file) # 'rewind' invocation on 'current_file' variable

print "Let's print three lines:"

current_line = 1 # setting variable to "1"
print_a_line(current_line, current_file) # 'print_a_line' invocation on 'current_line' and 'current_file' params
current_line +=1 # incrementation on 1
print_a_line(current_line, current_file)
current_line +=1
print_a_line(current_line, current_file)