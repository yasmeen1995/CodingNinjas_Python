
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def getMidList(currNode):
    slow = currNode
    fast = currNode

    while (fast.next is not None) and (fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

def reverseList(currNode):
    prev = None
    next = None

    while currNode is not None:
        next = currNode.next
        currNode.next = prev
        prev = currNode
        currNode = next
    return prev


def isPalindrome(head) :
    #Your code goes here
    if head is None or (head.next is None):
        return True
    
    mid = getMidList(head)
    revHead = reverseList(mid)

    while revHead is not None and head is not None:
        if revHead.data != head.data:
            return False
        revHead = revHead.next
        head = head.next
    
    return True

    

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1

# Problem statement
# You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Time Limit: 1sec

# Where 'M' is the size of the singly linked list.
# Sample Input 1 :
# 1
# 9 2 3 3 2 9 -1
# Sample Output 1 :
# true
# Sample Input 2 :
# 2
# 0 2 3 2 5 -1
# -1
# Sample Output 2 :
# false
# true
# Explanation for the Sample Input 2 :
# For the first query, it is pretty intuitive that the the given list is not a palindrome, hence the output is 'false'.

# For the second query, the list is empty. An empty list is always a palindrome , hence the output is 'true'.