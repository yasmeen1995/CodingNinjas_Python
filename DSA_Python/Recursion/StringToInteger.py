# Write your code here...
from math import *
from collections import *
from sys import *
from os import *

def stringToInt(s):
    l = len(s)
    
    if len(s) == 1:
        # print('yash ', ord(s))
        return ord(s)-ord('0')
        
    first =  ord(s[0]) - ord('0')
    # first stores the ascii value of character at s[0] location
    smallList = stringToInt(s[1:])
    return (first * (10 ** (l-1))) + smallList

s = input()
print(stringToInt(s))


# Problem statement
# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.

# Sample Input 1 :
# 00001231
# Sample Output 1 :
# 1231
# Sample Input 2 :
# 12567
# Sample Output 2 :
# 12567
# #