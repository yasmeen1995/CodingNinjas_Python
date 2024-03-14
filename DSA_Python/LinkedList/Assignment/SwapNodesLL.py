from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def swapNodes(head, i, j) :
	#Your code goes here
    if head is None:
        return None
   
    current = head
    curr_ptr1 = head
    curr_ptr2 = head
    prev_ptr1 = None
    prev_ptr2 = None

    i_count = 0
    j_count = 0

    while curr_ptr1:
        if i_count == i:
            next_ptr1 = curr_ptr1.next
            break
        else:
            prev_ptr1 = curr_ptr1
            curr_ptr1 = curr_ptr1.next
            i_count += 1

    while curr_ptr2:
        if j_count == j:
            next_ptr2 = curr_ptr2.next
            break
        else:
            prev_ptr2 = curr_ptr2
            curr_ptr2 = curr_ptr2.next
            j_count += 1

    temp = curr_ptr2

    if i == 0:
        prev_ptr2.next = curr_ptr1
        curr_ptr1.next = next_ptr2
        head = temp
        temp.next = next_ptr1

    # when i and j are consecutive to each other
    elif curr_ptr1.next == curr_ptr2:
        curr_ptr1.next = next_ptr2
        prev_ptr1.next = temp
        temp.next = curr_ptr1

    else:
        prev_ptr2.next = curr_ptr1
        curr_ptr1.next = next_ptr2
        prev_ptr1.next = temp
        temp.next = next_ptr1

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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1


# Problem statement
# You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions and return the new head to the list.

# Note :
# 1. Remember, You need to swap the nodes, not only the data.
# 2. Indexing starts from 0.
# 3. No need to print the list, it has already been taken care.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.
# 0 <= i < M
# 0 <= j < M

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3 4
# Sample Output 1 :
# 3 4 5 6 2 1 9 
#  Sample Input 2 :
# 2
# 10 20 30 40 -1
# 1 2
# 70 80 90 25 65 85 90 -1
# 0 6
#  Sample Output 2 :
# 10 30 20 40 
# 90 80 90 25 65 85 70 