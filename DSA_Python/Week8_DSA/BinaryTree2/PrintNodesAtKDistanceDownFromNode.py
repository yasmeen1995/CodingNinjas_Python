from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def nodesAtDistanceKSubtreeHelper(root, distance, k):
#     if root is None:
#         return
#     if distance == k:
#         print(root.data)

#     nodesAtDistanceKSubtreeHelper(root.left, distance+1, k)
#     nodesAtDistanceKSubtreeHelper(root.right, distance+1, k)


# def nodesAtDistanceK(root, node, k) :
# 	#Your code goes here
#     # Target== node
#     if root is None:
#         return -1

#     if root.data == node:
#         nodesAtDistanceKSubtreeHelper(root, 0,  k)
#         return 0

#     leftDistance = nodesAtDistanceK(root.left, node, k)
#     if leftDistance != -1:
#         if leftDistance + 1 == k:
#             print(root.data)
#         else:
#             nodesAtDistanceKSubtreeHelper(root.right, leftDistance-2, k)
#         return leftDistance+1

#     rightDistance = nodesAtDistanceK(root.right, node, k)
#     if rightDistance != -1:
#         if rightDistance + 1 == k:
#             print(root.data)
#         else:
#             nodesAtDistanceKSubtreeHelper(root.left, rightDistance+2, k)
#         return rightDistance+1

#     return -1


def printNodesAtKDistanceDown(root, k):
    if root is None or k < 0:
        return
    
    if k == 0:
        print(root.data)
        return
    
    printNodesAtKDistanceDown(root.left, k - 1)
    printNodesAtKDistanceDown(root.right, k - 1)

def nodesAtDistanceKSubtreeHelper(root, target, k):
    if root is None:
        return -1
    
    if root.data == target:
        printNodesAtKDistanceDown(root, k)
        return 0
    
    leftDistance = nodesAtDistanceKSubtreeHelper(root.left, target, k)
    if leftDistance != -1:
        if leftDistance + 1 == k:
            print(root.data)
        else:
            printNodesAtKDistanceDown(root.right, k - leftDistance - 2)
        return leftDistance + 1

    rightDistance = nodesAtDistanceKSubtreeHelper(root.right, target, k)
    if rightDistance != -1:
        if rightDistance + 1 == k:
            print(root.data)
        else:
            printNodesAtKDistanceDown(root.left, k - rightDistance - 2)
        return rightDistance + 1

    return -1

def nodesAtDistanceK(root, node, k):
    if root is None:
        return
    
    nodesAtDistanceKSubtreeHelper(root, node, k)



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)


# Problem statement
# You are given a Binary Tree of type integer, a integer value of target node's data, and an integer value K.

# Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.

# Example:
# For a given input tree(refer to the image below):
# 1. Target Node: 5
# 2. K = 2
# Starting from the target node 5, the nodes at distance K are 7 4 and 1.


# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.
# 1 ≤ data of node ≤ 10^9
# 1 ≤ target ≤ 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 3 1
# Sample Output 1:
# 9
# 6
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# 3 3
# Sample Output 2:
# 4
# 5
