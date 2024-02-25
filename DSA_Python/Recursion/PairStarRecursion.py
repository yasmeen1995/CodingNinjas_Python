from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def pairStarRecursive(s):
    if len(s) <= 1:
        return s

    smallAns = pairStarRecursive(s[1:]) 

    if s[0] == s[1]:
        return s[0] + '*' + smallAns

    return s[0] + smallAns 



from sys import setrecursionlimit
setrecursionlimit(110000)
s = input()
print(pairStarRecursive(s))


# Problem statement
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a
