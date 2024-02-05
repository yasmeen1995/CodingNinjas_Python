"""
Time Complexity: O(NxM)
Space Complexity: O(1)
"""

from typing import *

def printColWise(a : List[List[int]]) -> List[int]:
    # print('yash a: ', a)
    # print('yash a[0]: ', a[0])
    n, m = len(a), len(a[0])
    # print("yas n", n)
    # print("yas m", m)

    answer = []
    #Col-wise extractions
    for j in range(m):
        for i in range(n):
            answer.append(a[i][j])
    
    # #Row-wise extractions
    # for i in range(n):
    #     for j in range(m):
    #         answer.append(a[i][j])

    return answer



def main():
    T = int(input())  # Read the number of test cases from user input
    test_cases = []   # Initialize an empty list to store the test cases

    # Loop through each test case
    for i in range(T):
        size = list(map(int, input().split()))  # (NxM) Read the size of the matrix for the current test case
        # print('yash size', i, size)
        matrix = [list(map(int, input().split())) for _ in range(size[0])]  #  Read the matrix for the current test case
        test_cases.append(matrix)  # Append the matrix to the list of test cases
    # print('yash testcases: ', test_cases)
    # testcases= [[[4]], [[1, 2, 3, 4, 5]]]

    # Loop through each test case and print the row-wise traversal
    for test_case in test_cases:
        output = printColWise(test_case)  # Call the printRowWise function for the current test case
        print(*output)  # Print the elements of the row-wise traversal separated by space


if __name__ == "__main__":
    main()


# Problem:
# Problem statement
# Given a matrix, ‘A’ of size ‘N’ * ‘M’, you must traverse the matrix column-wise.

# You must return an integer array of size ‘N’ * ‘M’ denoting the column-wise traversal of the matrix.

# For example:

# Input :
# A = [ [1, 2, 3], [4, 5, 6] ]

# Output :
# 1 4 2 5 3 6

# Explanation: 
# For the given matrix, the first column is [1, 4], the second is [2, 5] and the third is [3, 6].
# For column-wise traversal, you must traverse the first column, the second column, and then the third.


# Sample Input 1 :
# 2
# 2 2 
# 4 3
# 2 1
# 5 1
# 1 
# 2 
# 3 
# 4 
# 5
# Sample Output 1 :
# 4 2 3 1
# 1 2 3 4 5 

# sample Input2:
# 2
# 1 1 (NxM)
# 4

# 1 5 (NxM)
# 1 2 3 4 5
# Sample Output 2 :
# 4
# 1 2 3 4 5 


# Input1 ouput flow:
# 2
# 2 2
# yash size 0 [2, 2]
# 4 3
# 2 1
# 5 1
# yash size 1 [5, 1]
# 1
# 2
# 3
# 4
# 5
# yash testcases:  [[[4, 3], [2, 1]], [[1], [2], [3], [4], [5]]]
# yash a:  [[4, 3], [2, 1]]
# yash a[0]:  [4, 3]
# yas n 2
# yas m 2
# 4 2 3 1
# yash a:  [[1], [2], [3], [4], [5]]
# yash a[0]:  [1]
# yas n 5
# yas m 1
# 1 2 3 4 5