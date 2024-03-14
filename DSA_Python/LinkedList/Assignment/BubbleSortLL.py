from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(11000)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# def length(head):
#     count = 0
#     current = head
#     while current is not None:
#         count += 1
#         current = current.next
#     return count

# Recursive
def length(head):
    if head is None:
        return 0
    temp = head
    size = 1 + length(temp.next)
    return size

def bubbleSort(head) :
	#Your code goes here
    for i in range(length(head)):
        prev = None
        curr = head
        
        while curr.next is not None:
            if curr.data > curr.next.data:
                if prev is not None:
                    temp = curr.next.next #store the next node after the next noe
                    curr.next.next = curr #Update the next of the next node to point to the curr node
                    prev.next = curr.next #Update the previous node to point to the next node
                    curr.next = temp # Update the current node to point to the node after the next node
                    prev = prev.next #Move the previous pointer to the next node

                else:
                    head = curr.next # Update the head to point to the next node
                    curr.next = head.next # Update the current node to point to the node after the new head
                    head.next = curr #Update the new head to point to the current node
                    prev = head #Set the previous pointer to the new head
            else:
                prev = curr
                curr = curr.next
            
    return head


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



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)


# Problem statement
# Given a singly linked list of integers, sort it using 'Bubble Sort.'

# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.

# Constraints :
# 0 <= M <= 10^3
# Where M is the size of the singly linked list.

# Time Limit: 1sec
# Sample Input 1 :
# 10 9 8 7 6 5 4 3 -1
# Sample Output 1 :
#  3 4 5 6 7 8 9 10 
#  Sample Input 2 :
# 10 -5 9 90 5 67 1 89 -1
# Sample Output 2 :
# -5 1 5 9 10 67 89 90 