
# This code demonstrates the technique
# of 'Incremental Development' that involves
# writing chunks of code at a time to
# save a lot of debugging time.

# Exercise:
# Use Incremental Development to create a
# function that computes the length of the
# hypotenuse of a right triangle given the
# lengths of the other two sides.
# 
# Record each stage of the developmental
# process as you go on

#Imports:
import math


# Step 1:
# def get_hypo():
#	return 0.0
	
# Step 2:
#def get_hypo(side_1, side_2):
#	print 'Side 1:', side_1
#	print 'Side 2:', side_2
#	return 0.0

#Step 3:
#def get_hypo(side_1, side_2):
#	sq_1 = side_1*side_1
#	sq_2 = side_2*side_2
#	print 'Square Side 1:', sq_1
#	print 'Square Side 2:', sq_2
#
#	return 0.0


#Step 4:
#def get_hypo(side_1, side_2):
#	sq_1 = side_1*side_1
#	sq_2 = side_2*side_2
#	print 'Square Side 1:', sq_1
#	print 'Square Side 2:', sq_2
#
#	sq_sum = sq_1+sq_2
#	print "Sum of squares of",side_1,"and",side_2,":",sq_sum
#
#	return 0.0


#Step 5: (Final Step)
def get_hypo(side_1, side_2):
	sq_1 = side_1*side_1
	sq_2 = side_2*side_2
	sq_sum = sq_1+sq_2
	
	hypo = math.sqrt(sq_sum)
	print "Required hypotenuse:", hypo
	return 0.0
