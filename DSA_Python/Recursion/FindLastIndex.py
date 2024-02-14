from math import *
from collections import *
from sys import *
from os import *

def findLastIndex(a,x):
    l = len(a)
    if l ==0:
        return -1

    smallerList = a[1:]
    smalletListOutput = findLastIndex(smallerList, x)

    if smalletListOutput != -1:
        return smalletListOutput + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1
    
# def findLastIndex(a,x,si):
#     l = len(a)
#     if si == l:
#         return -1
#     smallerListOutput = findLastIndex(a, x, si+1)
#     if smallerListOutput != -1:
#         return smallerListOutput
#     else:
#         if a[si] == x:
#             return si
#         else:
#             return -1


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(findLastIndex(arr, x))
# print(findLastIndex(arr, x, 0))



# Problem statement
# Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.

# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.

# You should start traversing your array from 0, not from (N - 1).

# Do this recursively. Indexing in the array starts from 0.


# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 3
