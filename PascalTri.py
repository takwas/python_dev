

# Code to create the Pascal's Triangle

start_line_length = 3
common_diff = 6


def generate_line(line_num):
	line_length = start_line_length + common_diff*line_num



def run():
	curr_list = last_list = [1]
	counter = 0
	
	print last_list
	
	while counter <= 8:
		
		curr_list.__iadd__([1])
###		curr_list[0] = curr_list[-1] = 1			# multiple assignment

		if len(curr_list)==2:
			counter += 1
			last_list = curr_list
			print curr_list
			continue
			
		for i in range(1, len(curr_list)-1):			# loop through the elements of new list; [start:1; stop:len-2 (inclusive)]
			curr_list[i] = last_list[i-1] + last_list[i]
			print curr_list
		
		counter += 1
		last_list = curr_list


if __name__ == '__main__':
	run()
