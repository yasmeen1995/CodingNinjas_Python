'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head) :
    #Your code goes here
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


    
# Problem statement
# Given the head of a singly linked list of integers, find and return its length.

# Sample Input 1 :
# 3 4 5 2 6 1 9 -1


# Sample Output 1 :
# 7


# Explanation of sample input 1 :
# The number of nodes in the given linked list is 7.
# Hence we return 7.


# Sample Input 2 :
# 10 76 39 -3 2 9 -23 9 -1

# Sample Output 2 :
# 8


# Expected Time Complexity:
# Try to do this in O(n).


#  Constraints :
# 0 <= N <= 10^5
# Time Limit: 1 sec

