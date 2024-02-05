from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(mat, m, n, target):
	# Write your code here.
	for i in range(m):
		for j in range(n):
			if mat[i][j] == target:
				return True
		
	return False


def main():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        # Read matrix size and target value
        m, n, target = map(int, input().strip().split())

        # Read the matrix values
        matrix = []
        for _ in range(m):
            row = list(map(int, input().strip().split()))
            matrix.append(row)


        result = findTargetInMatrix(matrix, m, n, target)

        print(result)


if __name__ == "__main__":
    main()

	

# Problem statement
# You have been given a 2-D array 'MAT' of size M x N where 'M' and 'N' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order.

# Moreover, the first element of a row is greater than the last element of the previous row (if exists).

# You are given an integer 'TARGET' and your task is to find if it exists in the given 'MAT' or not.

# Example :

# Given Matrix : 1 1 and Target : 8
#                4 8 

# The output should be "TRUE" as 8 is present in the Matrix.

# Sample Input 1 :
# 1
# 3 4 8
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# Sample Output 1 :
# TRUE

# Sample Input 2 :
# 2
# 3 3 78
# 1 2 4 
# 6 7 8
# 9 10 34
# 2 2 8
# 1 1
# 4 8
# Sample Output 2 :
# FALSE
# TRUE

