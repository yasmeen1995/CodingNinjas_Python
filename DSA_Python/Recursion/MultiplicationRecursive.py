from math import *
from collections import *
from sys import *
from os import *
import sys

# Key Takeway:
# Add below lines to pass the 6th testcase, seems the error was due to maximum recursion limit error
# import sys
# sys.setrecursionlimit(10**6)

## Read input as specified in the question.
## Print output as specified in the question.
def multiplicationRecursive(m, n):
    # 3+3+3+3+3 (M=3, N = 5)
    if n == 0:
        return 0

    if n == 1:
        return m

    smallOut = multiplicationRecursive(m, n-1)
    return m + smallOut


sys.setrecursionlimit(10**6)
M = int(input())
N = int(input())
result = multiplicationRecursive(M, N)

print(result)


# Problem statement
# Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.

# Sample Input 1 :
# 3 
# 5
# Sample Output 1 :
# 15
