from sys import stdin , setrecursionlimit
setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Taking Input Using Fast I/O
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


# To print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


def reverse(head):
    # Write your code here
    current = head
    prev=None
    
    while current is not None:
        next_ = current.next 
        current.next = prev
        prev = current
        current = next_
    head = prev
    
    return head


# Main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    
    ans=reverse(head)
    printLinkedList(ans)

    t -= 1 


# Problem statement
# Given a singly linked list of integers, reverse it iteratively and return the head to the modified list.

#  Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.

# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 -1
# Sample Output 1 :
# 8 7 6 5 4 3 2 1
# Sample Input 2 :
# 2
# 10 -1
# 10 20 30 40 50 -1
# Sample Output 2 :
# 10 
# 50 40 30 20 10 