#!/usr/bin/python


# My module to test Python's
# module: doctest




# Doctest module will execute the
# doc strings found here
def square(num):
	"""
	Squares num.

	>>> square(2)
	4 
	>>> 
	>>> square(-2) 
	4
	>>> 
	"""
	from math import pow
	return int(pow(num, 2))


if __name__ == '__main__':
	import doctest
	doctest.testmod()