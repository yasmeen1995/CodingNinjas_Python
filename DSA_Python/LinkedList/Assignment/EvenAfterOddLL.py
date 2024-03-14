from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def evenAfterOdd(head) :
    #Your code goes here
    if head is None:
        return head

    odd_head = None
    odd_tail = None
    even_head = None
    even_tail = None

    current = head
    while current is not None:
        if current.data % 2 != 0: #Odd Case

            if odd_head is None: 
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next

        else: # Even Case
            if even_head is None:
                even_head = current
                even_tail = current
            
            else:
                even_tail.next = current
                even_tail = even_tail.next
            
        current = current.next

    if odd_tail:
        odd_tail.next = even_head
    
    if even_tail:
        even_tail.next = None
    
    if odd_head is None:
        return even_head
    else:
        return odd_head


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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1


# Problem statement
# For a given singly linked list of integers, arrange the nodes such that all the even number nodes are placed after the all odd number nodes. The relative order of the odd and even terms should remain unchanged.

# Note :
# 1. No need to print the linked list, it has already been taken care. Only return the new head to the list.
# 2. Don't create a new linked list.
# 3.  Just change the data, instead rearrange the provided list.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 1 4 5 2 -1
# Sample Output 1 :
# 1 5 4 2 
# Sample Input 2 :
# 2
# 1 11 3 6 8 0 9 -1
# 10 20 30 40 -1
# Sample Output 2 :
# 1 11 3 9 6 8 0
# 10 20 30 40