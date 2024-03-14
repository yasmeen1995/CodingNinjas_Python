from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists(head1, head2):
    # Write your code here
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    
    if head1.data <= head2.data: #h1 smaller
        finalHead = head1
        finalTail = head1
        head1 = head1.next
    else:
        finalHead = head2
        finalTail = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data: #h1 smaller
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next
        else:
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next

    if head1 is not None:
        finalTail.next = head1
    elif head2 is not None:
        finalTail.next = head2

    return finalHead


def midPointofLL(head) :
    # Write your code here
    if head is None:
        return head

    slow = head
    fast = head
    while (fast.next is not None) and (fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next

    return slow

def mergeSort(head) :
	#Your code goes here
    if head is None or head.next is None:
        return head
    
    mid = midPointofLL(head)
    head2 = mid.next
    mid.next = None
    
    LeftHead1 = mergeSort(head)
    RightHead2= mergeSort(head2)
    
    head = mergeTwoSortedLinkedLists(LeftHead1,RightHead2)
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


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1

# Problem statement
#  Given a singly linked list of integers, sort it using 'Merge Sort.'

# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 10 9 8 7 6 5 4 3 -1
# Sample Output 1 :
#  3 4 5 6 7 8 9 10 
#  Sample Input 2 :
# 2
# -1
# 10 -5 9 90 5 67 1 89 -1
# Sample Output 2 :
# -5 1 5 9 10 67 89 90 