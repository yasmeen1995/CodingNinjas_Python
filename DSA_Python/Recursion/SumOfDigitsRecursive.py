from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def sumOfDigitsRecursive(n):
    if n == 0:
        return 0

    n_1_dig = n//10
    n_th_dig = n%10

    # inductive hypothesis assume sumOfDigitsRecursive(n/10) will bring the sum of remaining digits
    smallOut = sumOfDigitsRecursive(n_1_dig)
    return  smallOut + n_th_dig
    

n = int(input())
res = sumOfDigitsRecursive(n)
print(res)


# Problem statement
# Write a recursive function that returns the sum of the digits of a given integer.

# Sample Input 1 :
# 12345
# Sample Output 1 :
# 15
