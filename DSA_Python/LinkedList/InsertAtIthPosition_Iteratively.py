#Insert at ith position Iteratively:
# 1 2 3 4 5 -1

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

def length(head):
    count = 0 
    current = head
    while current is not None:
        count += 1
        current = current.next 
    return count


def insertAtIthPosition(head, i, data):
    # Can't insert if below condition is true
    if i < 0 or i > length(head):
        return head
    
    # Insert logic:
    count = 0
    prev = None
    curr = head

    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head


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

head = takeInput()
printLL(head)
head = insertAtIthPosition(head, 2, 6)
printLL(head)

head = insertAtIthPosition(head, 0, 9)
printLL(head)

head = insertAtIthPosition(head, 7, 10)
printLL(head)



# I/P: 1 2 3 4 5 -1
# 1->2->3->4->5->None
# 1->2->6->3->4->5->None
# 9->1->2->6->3->4->5->None
# 9->1->2->6->3->4->5->10->None