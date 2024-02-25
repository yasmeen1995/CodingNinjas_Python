from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def checkABRecursion(s):

    if len(s) == 0:
        return "true"

    if len(s) == 1:
        if s[0] == 'a':
            return "true"
        else:
            return "false"
        
    if len(s) == 2:
        if s[0] == 'a' and s[1]=='a':
            return "true"
        else:
            return "false"

    if s[0] == 'a' and s[1]== 'b' and s[2] == 'b':
        smallAns =  checkABRecursion(s[3:])
    elif s[0] == 'a' and s[1]== 'a':
        smallAns =  checkABRecursion(s[1:])
    else:
        return "false"

    return smallAns
    
   

s = input()
print(checkABRecursion(s))




# Problem statement
# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:

# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
# Sample Input 1 :
# abb
# Sample Output 1 :
# true
# Sample Input 2 :
# abababa
# Sample Output 2 :
# false
# Explanation for Sample Input 2
# In the above example, a is not followed by either "a" or "bb", instead it's followed by "b" which results in false to be returned.

