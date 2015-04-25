

###############################################################
# A modified version of the find() function
# from the book:
# "How to Think Like a Computer Scientist: Learning with Python" (Allen Downey et al)
# Original version is shown further below
def mod_find_ind(str, ch, ind, verbose=None):
	for i in range(ind, len(str)):
		if (str[i]==ch):
			if verbose is not None and verbose:
				print ch,"found within", str, "at index:", i
			return i
	
	if verbose is not None and verbose:
		print ch,"not found within", str
	return -1

### FUNCTION OVERLOAD
# Default non-verbose function
#def mod_find_ind(str, ch, ind):
#	return mod_find_ind(str, ch, ind, False)




###############################################################
# Composed function
# (calling another function and passing in required parameter)
def mod_find(str, ch, verbose = None):
	if verbose is None:
		return mod_find_ind(str, ch, 0)
	else:
		return mod_find_ind(str, ch, 0, verbose)

### FUNCTION OVERLOAD
# Default non-verbose function
#def mod_find(str, ch, ind):
#	return mod_find(str, ch, ind, False)




###############################################################
# Original version of find() function from the book
def find(str, ch):
	index = 0
	while index < len(str):
		if str[index] == ch:
			return index
			
		index = index + 1
	return -1



###############################################################

# Trying to locate substring within string
def find_subStr_ind(str, sub, ind, verbose=None):
	# fi = first-index; li = last-index
	fi = ind
	li = fi + len(sub)
	
	if mod_find(str, sub[0]) != -1:
		while li<=len(str):
			if (sub == str[fi:li]):
				if verbose is not None and verbose:
					print sub,"found within", str, "at index-range:", '[',fi,'-',li,']'
				return (fi, li)
			fi += 1
			li += 1
	
	if verbose is not None and verbose:
		print sub,"not found within", str
	return (-1,)



###############################################################
# Composed function
# (calling another function and passing in required parameter)
def find_subStr(str,sub,verbose=None):
	if verbose is None:
		return find_subStr_ind(str,sub,0)
	else:
		return find_subStr_ind(str,sub,0,verbose)



###############################################################


###############################################################
# Testing out the functions...
###############################################################

verbose = True

mod_find_ind("banana",  "a", 4, verbose)
mod_find_ind("banana",  "a", 1, verbose)
mod_find_ind("banana",  "a", 2, verbose)

mod_find("banana",  "a", verbose)

print find_subStr_ind("banana",  "an", 2, verbose)
