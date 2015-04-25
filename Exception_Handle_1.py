

def  input_number():
	x = input("Enter a number: ")
	
	if x <= 10:
		raise ValueError, "Please be positive; g0 for something bigger!"
	return x
	

def use_input_number(input_number):
	print "The number you have selected is:", "input_number"
	
	
try:
	use_input_number(input_number())
except ValueError:
	print "Well, I didn't get a number after all... :("
