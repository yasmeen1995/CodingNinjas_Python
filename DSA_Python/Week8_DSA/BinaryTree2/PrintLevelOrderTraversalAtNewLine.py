from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    #Your code goes here
    if root is None:
        return
    
    q = queue.Queue()

    if root.data != -1:
        q.put(root)

    q1= queue.Queue()
    
    while not q.empty():
        while not q.empty():
            root = q.get()
            print(root.data,end=" ")
            if root.left is not None:
                q1.put(root.left)
            if root.right is not None:
                q1.put(root.right)
        print()

        q, q1=q1, q
        

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


# Main
root = takeInput()
printLevelWise(root)


# Problem statement
# For a given a Binary Tree of type integer, print it in a level order fashion where each level will be printed on a new line. Elements on every level will be printed in a linear fashion and a single space will separate them.

# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1 
# Sample Output 1:
# 10 
# 20 30 
# 40 50 60 
# Sample Input 2:
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
# 8 
# 3 10 
# 1 6 14 
# 4 7 13

