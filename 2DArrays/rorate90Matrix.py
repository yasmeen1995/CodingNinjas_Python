
from os import *
from sys import *
from collections import *
from math import *
from sys import stdin


def rotateMatrix(matrix):
    # Write your code here.
    n = len(matrix)
    #Step1: Transpose of Matrix
    for row in range(n):
        for col in range(row+1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    
    #Step2: Reverse of the column (Anti-Clock)
    for col in range(n):
        # Rows pointers
        ptrA, ptrB = 0, n-1
        while ptrA <ptrB:
            matrix[ptrA][col], matrix[ptrB][col] = matrix[ptrB][col], matrix[ptrA][col]
            ptrA += 1
            ptrB -= 1

    return (matrix)
            

def main():
    num_testcases = int(input())

    for _ in range(num_testcases):
        n = int(input())

        matrix = []
        # for _ in range(m):
        #     row = list(map(int, input().strip().split()))
        #     matrix.append(row)
        matrix =[ list(map(int, input().split())) for _ in range(n)] 

        result = rotateMatrix(matrix)
        print(result)


if __name__ == "__main__":
    main()



# Problem statement
# You are given a square matrix of non-negative integers 'MATRIX'. Your task is to rotate that array by 90 degrees in an anti-clockwise direction using constant extra space.

# For example:
# For given 2D array :

#     [    [ 1,  2,  3 ],
#          [ 4,  5,  6 ],
#          [ 7,  8,  9 ]  ]

# After 90 degree rotation in anti clockwise direction, it will become:

#     [   [ 3,  6,  9 ],
#         [ 2,  5,  8 ],
#         [ 1,  4,  7 ]   ]


# Sample Input 1:
# 2
# 3
# 1  2  3
# 4  5  6
# 7  8  9
# 4
# 1  2  3  4 
# 5  6  7  8 
# 9 10 11 12 
# 13 14 15 16
# Sample Output 1:
# 3  6  9 
# 2  5  8 
# 1  4  7
# 4  8 12 16 
# 3  7 11 15 
# 2  6 10 14 
# 1  5  9 13
# Explanation of Input 1:
# For, first test case, the given matrix has been rotated by 90 degrees in an anticlockwise direction as the first row is now the first column inverted and so on for second and third rows.

# For, second test case, the given matrix has been rotated by 90 degrees in an anticlockwise direction as the first row is now first column inverted and so on for second, third and fourth rows.


