from sys import stdin

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

    if head1.data >= head2.data: #h2 smaller
        finalHead = head2
        finalTail = head2
        head2 = head2.next
    else:
        finalHead = head1
        finalTail = head1
        head1 = head1.next

    while head1 is not None and head2 is not None:
        if head1.data >= head2.data: #h2 smaller
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next
        else:
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next

    if head1 is not None:
        finalTail.next = head1
    elif head2 is not None:
        finalTail.next = head2

    return finalHead


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


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1


# Problem statement
# You have been given two sorted(in ascending order) singly linked lists of integers.

# Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order) and return the new head to the list.

# Note :
# Try solving this in O(1) auxiliary space.

# No need to print the list, it has already been taken care.

# Constraints :
# 1 <= t = 10^2
# 0 <= N <= 10 ^ 4
# 0 <= M <= 10 ^ 4
# Where N and M denote the sizes of the singly linked lists. 

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 2 5 8 12 -1
# 3 6 9 -1
# Sample Output 1 :
# 2 3 5 6 8 9 12 
# Sample Input 2 :
# 2
# 2 5 8 12 -1
# 3 6 9 -1
# 10 40 60 60 80 -1
# 10 20 30 40 50 60 90 100 -1
# Sample Output 2 :
# 2 3 5 6 8 9 12 
# 10 10 20 30 40 40 50 60 60 60 80 90 100