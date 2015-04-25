
###############################################################
# Composed function
# (calling another function and passing in required parameter)
# Recursively checks the length of each element encountered in
# its traversal
def list_rec_len(some_value):
	if (type(some_value) == list) or (type(some_value) == str):
		print some_value, '=\t', len(some_value)
	
		if type(some_value)==list:
			for i in some_value:
				list_rec_len(i)
	else:
		print some_value, '=\tNOLEN'
	



big_list = [['a','abc', 'aeiou', [['str', 'word'], 3,4,5],['def', 'lawn'],[],['444', 007, '007']],[2],[[0],['rerd', 'nerd', 'ferd'],9],0]


list_rec_len(big_list)
