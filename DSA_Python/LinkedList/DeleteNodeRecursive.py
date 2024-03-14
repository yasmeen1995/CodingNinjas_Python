from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNodeRec(head, pos) :
	#Your code goes here
    if head is None:
        return head

    if pos == 0:
        return head.next

    smallHead = deleteNodeRec(head.next, pos-1)
    head.next = smallHead

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
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())    

    newHead = deleteNodeRec(head, pos)
    printLinkedList(newHead)

    t -= 1


# Problem statement
# Given a singly linked list of integers and position 'i', delete the node present at the 'i-th' position in the linked list recursively.

#  Note :
# Assume that the Indexing for the linked list always starts from 0.

# No need to print the list, it has already been taken care. Only return the new head to the list.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.
# 0 <= i < M

# Time Limit:  2 sec
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3
# Sample Output 1 :
# 3 4 5 6 1 9
# Sample Input 2 :
# 2
# 30 -1
# 0
# 10 20 30 50 60 -1
# 4
# Sample Output 2 :
# 10 20 30 50 
