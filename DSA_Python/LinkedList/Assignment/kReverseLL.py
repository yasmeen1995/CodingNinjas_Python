from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def kReverse(head, k) :
	#Your code goes here
    if head is None or head.next is None or k<= 1:
        return head 

    curr = head
    prev = None
    next_ = None
    count, nodeCount = 0, 0

    temp = head
    while temp is not None:
        temp = temp.next
        nodeCount += 1 #Count the no.of nodes in LL

    # Reverse K nodes
    while count < k and curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
        count+=1
    
    #Recursive call on the next group of nodes
    head.next = kReverse(next_, k)

    return prev


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


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1

# Problem statement
# Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.

#  'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.

# Example :
# Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

# For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

# For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4
#  Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.
# 0 <= k <= M

# Time Limit:  1sec
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 9 10 -1
# 4


# Sample Output 1 :
# 4 3 2 1 8 7 6 5 10 9
# Sample Input 2 :
# 2
# 1 2 3 4 5 -1
# 0
# 10 20 30 40 -1
# 4
# Sample Output 2 :
# 1 2 3 4 5 
# 40 30 20 10 