def checkNumber(arr, x):
    # Please add your code here
    n = len(arr)
    # Base Case
    if n == 0:
        return False

    # Check if the element is available at last index
    # if arr[-1] == x:
    #     return True
    if arr[n-1] == x:
        return True

    # Recusion
    return checkNumber(arr[:n-1], x)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')


# Problem statement
# Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.

# Do this recursively.

# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 :
# true
