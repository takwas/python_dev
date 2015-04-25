
import math

# This program prints the powers of two
# up to the value '65536'

#the highest value expected, and at which to stop
CAP = 65536

# method that returns the value of
# two raised to the given index
def two_to_pow(power):
	return math.pow(2,power)

# method to run the program
def run():
	count = 0
	while True:
		result = int(two_to_pow(count))
		print '2 ^', count, '\t=\t\b\b\b\b', result
		
		if result >= CAP:
			break
		count+=1

# calling the run method
run()
