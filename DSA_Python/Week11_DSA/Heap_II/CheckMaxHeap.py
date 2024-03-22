def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    n = len(lst)
    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and lst[left_child] > lst[i]:
            return False
        
        if right_child < n and lst[right_child] > lst[i]:
            return False

    return True


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')


# Problem statement
# Given an array of integers, check whether it represents max-heap or not. Return true if the given array represents max-heap, else return false.

# Constraints:
# 1 <= N <= 10^5
# 1 <= Ai <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 8
# 42 20 18 6 14 11 9 4
# Sample Output 1:
# true