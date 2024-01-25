# Problem statement
# Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.

# Example:
# If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

# The string is compressed only when the repeated character count is more than 1.
# Note:
# Consecutive count of every character in the input string is less than or equal to 9. You are not required to print anything. It has already been taken care of. Just implement the given function and return the compressed string.


from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(input) :
	# Write your code here.
	ans = ""
	currChar = input[0]
	currLen = 1

	for i in range(1, len(input)):
		if input[i] == currChar:
			currLen +=1
		else:
			ans = ans + currChar
			if currLen != 1:
				ans = ans + str(currLen)
			
			currChar = input[i]
			currLen = 1
	
	#To handle last character
	ans = ans + currChar
	if currLen != 1:
		ans = ans + str(currLen )

	return ans



# Main.
# string = stdin.readline().strip();

string = 'aaabbccdsa'

ans = getCompressedString(string)
print(ans)

# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa
# Explanation for Sample Output 1:
# In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is repeated 2 times and 'd', 's' and 'a' and occuring 1 time hence no compression for last 3 characters.
