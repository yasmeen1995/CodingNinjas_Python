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


def insertAtIthPositionRecursive(head, i, data):
    if i < 0:
        return head
    
    # Step1
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    # Step2 ---> Note: Step1 should write first and then step2. Order is important here
    if head is None: #Out of range i > length(head)
        return None
    

    smallHead = insertAtIthPositionRecursive(head.next, i-1, data)
    head.next = smallHead

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
head = insertAtIthPositionRecursive(head, 2, 6)
printLL(head)

head = insertAtIthPositionRecursive(head, 0, 9)
printLL(head)

head = insertAtIthPositionRecursive(head, 7, 10)
printLL(head)