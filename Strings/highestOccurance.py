# Problem statement
# For a given a string(str), find and return the highest occurring character.

# Example:
# Input String: "abcdeapapqarr"
# Expected Output: 'a'
# Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would be 'a'.
# If there are two characters in the input string with the same frequency, return the character which comes first.

# Consider:
# Assume all the characters in the given string to be in lowercase always.


from sys import stdin

def highestOccuringChar(string) :
	#Your code goes here
	arr = [0]*256 ## No.of ASCII Characters
	maxFreq = 0
	highest_char = ''

	for i in string:
		arr[ord(i)] += 1
		# print(chr(ord(i)))
	
	for i in range(len(arr)):
		if arr[i] >maxFreq:
			maxFreq = arr[i]
			highest_char = chr(i)

	return highest_char

#main
# string = stdin.readline().strip();

string = "abdefgbabfbagggggg"

ans = highestOccuringChar(string)

print(ans)


