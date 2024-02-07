from os import *
from sys import *
from collections import *
from math import *

from typing import List

def transpose(m: int, n: int, mat: List[List[int]]) -> List[List[int]]:
    # Write your code here.
    res = []
    for col in range(n):
        res.append([mat[row][col] for row in range(m)])
        # print('yash ' , [mat[row][col] for row in range(m)])
        
    return res


def main():
        T = int(input())

        for _ in range(T):
            m, n = map(int, input().strip().split())
            
            matrix = []
            for _ in range(m):
                row = list(map(int, input().strip().split()))
                matrix.append(row)
            
            result = transpose(m, n, matrix)
            print(result)


if __name__ == "__main__":
    main()


# Problem statement
# You are given a matrix ‘MAT’. Print and return the transpose of the matrix. The transpose of a matrix is obtained by changing rows to columns and columns to rows. In other words, transpose of a matrix A[][] is obtained by changing A[i][j] to A[j][i].

# For example:
# Let matrix be : 
# 1 2
# 3 4

# Then transpose of the matrix will be: 
# 1 3
# 2 4

# Sample Input 1 :
# 2
# 2 2
# 1 2
# 3 4
# 3 2
# 1 2 
# 2 3
# 3 4
# Sample Output 1 :
# 1 3
# 2 4
# 1 2 3
# 2 3 4

# Sample Input 2 :
# 2
# 2 3
# 1 2 3 
# 3 4 5
# 2 1
# 1
# 2
# Sample Output 2 :
# 1 3
# 2 4 
# 3 5
# 1 2