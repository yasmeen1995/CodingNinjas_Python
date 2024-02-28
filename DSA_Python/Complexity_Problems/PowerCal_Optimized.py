def power(x, n):
    # Please add your code here
    if n == 0:
        return 1
    
    smallPower = power(x, n//2)
    
    if n % 2 == 0:
        return smallPower * smallPower
    else:
        return x*smallPower*smallPower

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))


# Problem statement
# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.

# Do this recursively.

# Sample Input 1 :
#  3 4
# Sample Output 1 :
# 81
# Sample Input 2 :
#  2 5
# Sample Output 2 :
# 32