from os import *
from sys import *
from collections import *
from math import *

def matrixBoundaryTraversal(mat: [[]], m: int, n: int) -> []:
    # Write your code from here.
    result = []

    if n == 0 or m == 0:
        return result
        
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                result.append(mat[i][j])

    return result


def main():
    T = int(input())

    for _ in range(T):
      mRows, nCols = map(int, input().split())

      mat = [list(map(int, input().split())) for _ in range(mRows)]

      res = matrixBoundaryTraversal(mat, mRows, nCols)

    #   print(res)
      print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()

        

# Problem statement
# Given a matrix of integers containing ‘M’ rows and ‘N’ columns. Print the boundary elements of the matrix. The order of printing does not matter.

# Note :

# The output you will see will be in sorted order.
# Your order of output does not matter.
# You can return your result in any order.
# Example :
# Input: ‘M’ = 2, ‘N’ = 2, ‘MAT’ = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# input

# Output: [1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16]
# If we traverse the matrix in clockwise order from the top left then it will be 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5. Which in output will be shown in sorted order which is 1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16.
# output

# Referring to the image above, we are printing only the elements that lie on the boundary.

# Sample Input 1 :
# 2
# 3 2
# 5 3 
# 5 7 
# 5 5 
# 2 2
# 6 8 
# 5 5 
# Sample Output 1 :
# 3 5 5 5 5 7
# 5 5 6 8

