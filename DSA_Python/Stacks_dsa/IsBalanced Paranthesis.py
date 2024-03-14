from sys import stdin

def isBalanced(expression) :
	#Your code goes here
	s = []
	for bracket in expression:
		if bracket in '({[':
			s.append(bracket)
		elif bracket is ')':
			if ( not s or s[-1] != '(' ): #Stack is empty or last elem is != '('
				return False
			# print('yas ',s)
			s.pop()

		elif bracket is '}':
			if ( not s or s[-1] != '{' ): #Stack is empty or last elem is != '{'
				return False
			s.pop()
		elif bracket is ']':
			if ( not s or s[-1] != '[' ): #Stack is empty or last elem is != '['
				return False
			s.pop()

	if (not s):
		return True
	else:
		return False


#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")


# Problem statement
# For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. Brackets are said to be balanced if the bracket which opens last, closes first.

# Example:
# Expression: (()())
# Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
# You need to return a boolean value indicating whether the expression is balanced or not.

# Note:
# The input expression will not contain spaces in between.

# Constraints:
# 1 <= N <= 10^7
#  Where N is the length of the expression.

# Time Limit: 1sec
# Sample Input 1 :
# (()()())
# Sample Output 1 :
# true
# Sample Input 2 :
# ()()(()
# Sample Output 2 :
# false
# Explanation to Sample Input 2:
# The initial two pairs of brackets are balanced. But when you see, the opening bracket at the fourth index doesn't have its corresponding closing bracket which makes it imbalanced and in turn, making the whole expression imbalanced. Hence the output prints 'false'.
