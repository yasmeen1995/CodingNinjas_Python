
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def geometricSum(k):
    if k == 0:
        return 1
    if k == 1:
        return 1+1/2
    
    if k > 0:
        smallAns = geometricSum(k-1)
        ans =  (1/(2**k)) + (smallAns)
        return ans
        

n = int(input())
result = geometricSum(n)
print("{:.5f}".format(result))



# Problem statement
# Given k, find the geometric sum i.e.

# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
# Note :
# using recursion.

# Sample Input 1 :
# 3
# Sample Output 1 :
# 1.87500
# Sample Input 2 :
# 4
# Sample Output 2 :
# 1.93750
# Explanation for Sample Input 1:
# 1+ 1/(2^1) + 1/(2^2) + 1/(2^3) = 1.87500
