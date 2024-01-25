# Problem statement
# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.

# The input string will remain unchanged if the given character(X) doesn't exist in the input string.



from sys import stdin

def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here

	temp_str = ''

	for char in string:
		if char != ch:
			temp_str += char
		
	return temp_str


#main
# string = stdin.readline().strip()
# ch = stdin.readline().strip()[0]
string="aabccbaa"
ch = 'a'

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)


