from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def countWaysToClimbStairs(n):
    if n == 0:
        # Base case: if there are no steps, tehre is no way to climb.
        return 1
    if n < 0: 
        # Base case: If there are Negative steps, it's not possible to climb.
        return 0

    # Recusrion calculation of ways to clim n steps using 1,2, or 3steps at a time.
    smallAns = countWaysToClimbStairs(n-1)  + countWaysToClimbStairs(n-2)  + countWaysToClimbStairs(n-3)

    return smallAns

n = int(input())
print(countWaysToClimbStairs(n))



# Problem statement
# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

# Sample Input 1 :
# 4
# Sample Output 1 :
# 7
# Sample Input 2 :
# 5
# Sample Output 2 :
# 13