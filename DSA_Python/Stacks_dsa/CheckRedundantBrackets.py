
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
	stack = []
	for bracket in expression:
		count = 0
		if bracket != ")":
			stack.append(bracket)

		elif bracket == ")" :
			while stack[-1] != '(' : 
				stack.pop()
				count += 1
			stack.pop()
			
			# If count > 2 then two chars inbetween (__) brackets
			if count <= 1:
				return True

	return False


#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")

# Problem statement
# For a given expression in the form of a string, find if there exist any redundant brackets or not. It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.

# A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.

# Example:
# Expression: (a+b)+c
# Since there are no needless brackets, hence, the output must be 'false'.

# Expression: ((a+b))
# The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.
# Note:
# You will not get a partial score for this problem. You will get marks only if all the test cases are passed.
# Return "false" if no brackets are present in the input.

# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the expression.

# Time Limit: 1 second
# Sample Input 1:
# a+(b)+c 
# Sample Output 1:
# true
# Explanation:
# The expression can be reduced to a+b+c. Hence, the brackets are redundant.
# Sample Input 2:
# (a+b)
# Sample Output 2:
# false