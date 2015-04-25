
"""
This is essentially a test module.
So no functions are defined here
"""

from PalindromeChecker import palindro_check

start = 1
stop = 1000000
count = 0

output = '{\n\n'

"""
For every palindromic number found in the
range, print it out to standard output
"""
for i in range(start, stop):
	
	if palindro_check(str(i)):
		count+=1
###		print '\t%d is a paliondrome' %i
		output += '%d\t' %i

output += '\n\n}'
print 'Palindromes found:\n%s'%output
print	# print a blank line

# tell us how many palindromes were found in all
if count >1:
	print "Found %d palindromes between %d and %d" %(count, start, stop)
elif count == 1:
	print "Found 1 palindrome between %d and %d" %(start, stop)
else:
	print "Found no palindromes between %d and %d" %(start, stop)
