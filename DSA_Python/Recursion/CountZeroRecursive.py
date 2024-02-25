from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


def countZerosRecursive(n):
    if n <10:
        if n == 0:
            return 1
        else:
            return 0
 
    n_1_dig = n // 10
    n_th_dig = n % 10

    smallAns = countZerosRecursive(n_1_dig)

    if n_th_dig == 0:
        smallAns += 1
    
    return smallAns

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(countZerosRecursive(n))


# def countZerosRecursive(n):
#     if n <10:
#         if n == 0:
#             return 1
#         else:
#             return 0
 
#     n_1_dig = n // 10
#     n_th_dig = n % 10
#     count = 0

#     if n_th_dig == 0:
#         count += 1+ countZerosRecursive(n_1_dig)
#     else:
#         return countZerosRecursive(n_1_dig)
    
#     return count

# n = int(input())
# print(countZerosRecursive(n))



# Problem statement
# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.

# Sample Input 1 :
# 0
# Sample Output 1 :
# 1
# Sample Input 2 :
# 00010204
# Sample Output 2 :
# 2

# Explanation for Sample Output 2 :
# Even though "00010204" has 5 zeros, the output would still be 2 because when you convert it to an integer, it becomes 10204.

# Sample Input 3 :
# 708000
# Sample Output 3 :
# 4
