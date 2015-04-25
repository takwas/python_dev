
#author: ac3Takwas
#inspiration: God

# This program prints a multiplication table to
# standard output.

'''
To change the output of this program, edit the
argument passed to the show_table() function
called from the run() function which runs the
program
'''


# global variables
width = 8

# prints a new blank line to standard output
def newline():
	print

def multiply(num_1, num_2):
	return num_1*num_2;

# returns a string containing the list
# of multiples for the first parameter 'num'
# up till the second parameter 'up_to'
def get_multiples(num, up_to):
	line = ''
	product = 0
	text_format = "%"+str(width)+"d"
	
	for i in range (1, up_to+1):
		product = num*i
		line += str(text_format %product)
		
	return line
	
# computes and displays the multiplication table for
# numbers within range start_num and stop_num (inclusive)	
def show_table(stop_num):
	
	for j in range (1, stop_num+1):
		print get_multiples(j, stop_num)
		print
	

# runs the program
def run():

	newline()
	print 'Done!'
	newline()
	newline()

	show_table(6)
	
	print "Exiting the system...\n\n\tPress ENTER to exit"
	newline()

	# simulate "waiting for user-input" before exiting
	raw_input()



# calling the run() function to run the program code
run()

