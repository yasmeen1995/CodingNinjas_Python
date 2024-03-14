x=int(input())
y=int(input())
def divide(x, y): 
	# write your code logic !!
	try:
		print(x//y)
	except ZeroDivisionError as e:
		print("Sorry ! You are dividing by zero")
	finally:
		print("This is always executed")


divide(x, y)


# Problem statement
# Your task is to implement the divide function and demonstrate its functionality by creating a Python program.

# Description
# 1. If y is zero, the function should raise a ZeroDivisionError and print the message "Sorry! You are dividing by zero.". If y is not zero, the function should return the result of dividing x by `y.
# 2. Implement a try-except block to handle the ZeroDivisionError exception within the divide function.
# 3. Call the divide function with the provided values and print the result if successful, or the error message if a ZeroDivisionError occurs.
# 4. Ensure that the finally block in the divide function is used to print the message "This is always executed" regardless of whether an exception is raised or not.

# Sample Input :
# 3
# 4 
# Sample Output :
# 0
# This is always executed
# Sample Input :
# 3
# 0
# Sample Output:
# Sorry ! You are dividing by zero
# This is always executed



