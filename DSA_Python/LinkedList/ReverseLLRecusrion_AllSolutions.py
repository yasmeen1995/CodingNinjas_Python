#Insert at ith position Iteratively:
# 1 2 3 4 5 -1

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end="")
        head = head.next
    print("None")
    return

# O(N^2)
def reverseLLRec1(head) :
	#Your code goes here
    # Base Case:
    if head is None or head.next is None:
        return head
    
    # I.H
    smallHead = reverseLLRec1(head.next)

    curr = smallHead
    while curr.next is not None:
        curr = curr.next

    curr.next = head
    head.next = None

    return smallHead

# O(N)
def reverseLLRec2(head) :
    # Base Case:
    if head is None or head.next is None:
        return head, head  
    # I.H

    smallHead, smallTail = reverseLLRec2(head.next)

    smallTail.next = head
    head.next = None

    return smallHead, head

# O(N)
def reverseLLRec3(head) :
	#Your code goes here
    # Base Case:
    if head is None or head.next is None:
        return head 
         
    # I.H
    smallHead = reverseLLRec3(head.next)
    # head.next.next = head
    tail = head.next
    tail.next = head

    head.next = None

    return smallHead
    
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
            
        newNode = Node(currData)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode # tail points to newNode
            tail = newNode

    return head

# 1 2 3 4 5 -1

head = takeInput()
printLL(head)

head = reverseLLRec1(head)
printLL(head)

head, tail = reverseLLRec2(head)
printLL(head)


head = reverseLLRec3(head)
printLL(head)
