# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    current = head
    index = 0

    while current is not None:
        if current.data == n:
            return index
        else:
            index += 1
            current = current.next

    return -1
        
# IMPORTANT
# Problem statement
# You have been given a singly linked list of integers. Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.

# Note :
# Assume that the Indexing for the singly linked list always starts from 0.
#  Constraints :
# 1 <= T <= 10^2
# 0 <= M <= 10^5

# Where 'M' is the size of the singly linked list.

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 3 4 5 2 6 1 9 -1
# 5
# 10 20 30 40 50 60 70 -1
# 6
# Sample Output 1 :
# 2
# -1
#  Explanation for Sample Output 1:
# In test case 1, 'N' = 5 appears at position 2 (0-based indexing) in the given linked list.

# In test case 2, we can see that 'N' = 6 is not present in the given linked list.
# Sample Input 2 :
# 2
# 1 -1
# 2
# 3 4 5 2 6 1 9 -1
# 6
# Sample Output 2 :
# -1
# 4
#  Explanation for Sample Output 2:
# In test case 1, we can see that 'N' = 2 is not present in the given linked list.

# In test case 2, 'N' = 6 appears at position 4 (0-based indexing) in the given linked list.

