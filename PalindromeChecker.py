
import sys
from math import ceil

# Checks if a given word is palindromic or not

# accepts a word from the user, to process
def get_word():
	word = raw_input("Please type in a word for me to process (and hit ENTER)");
	return word
	

# checks if two given letters are the same
# returns True if so; False otherwise
def lettersMatch(letter_1, letter_2):
	if letter_1 == letter_2:
		return True
		
		
		

def palindro_check(word):
	start_index = 0
	end_index = -1
	
	if len(word)==1:
		return True
	
	while (start_index<=int(ceil(len(word)/2.0))):
		if word[start_index]!=word[end_index]:
			return False
		
		start_index += 1
		end_index -= 1

	return True


# runs the program	
def run():
	print "\nWelcome :)\n"
	
	
	if len(sys.argv)<2:
		word = 'default'
	else:
		word = sys.argv[1]
	
	
	if palindro_check(word):
		print "\t\"%s\" is a palindrome.\t;)" %(word)
	else:
		print "\t\"%s\" is not a palindrome.\t:(" %(word)


# run the program
if __name__ == '__main__':
	run()
	print ""
