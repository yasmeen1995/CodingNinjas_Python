
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def removeDuplicates(head) :
    #Your code goes here
    if head is None:
        return head

    currentNode = head

    while currentNode.next is not None:
        if currentNode.data == currentNode.next.data:
            currentNode.next = currentNode.next.next

        else:
            currentNode = currentNode.next

    # currNode = head
    # nextNode = currNode.next

    # while nextNode is not None:
    #     if currNode.data == nextNode.data:
    #         currNode.next = nextNode.next

    #     else:
    #         currNode = currNode.next
    #         nextNode = nextNode.next

    return head


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
t = int(stdin.readline().strip())

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1


# Problem statement
# You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Time Limit: 1sec

# Where 'M' is the size of the singly linked list.
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
# Sample Input 1 :
# 1
# 1 2 3 3 3 3 4 4 4 5 5 7 -1
# Sample Output 1 :
# 1 2 3 4 5 7 
# Sample Input 2 :
# 2
# 10 20 30 40 50 -1
# 10 10 10 10 -1
# Sample Output 2 :
# 10 20 30 40 50
# 10