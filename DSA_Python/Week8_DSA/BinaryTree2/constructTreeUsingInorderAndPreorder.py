from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preOrder, inOrder, n) :
	#Your code goes here
    if len(preOrder) == 0:
        return None

    rootData = preOrder[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1 

    for i in range(len(inOrder)):
        if inOrder[i] == rootData:
            rootIndexInInorder = i
            break

    if rootIndexInInorder == -1:
        return None

    leftInOrder = inOrder[0:rootIndexInInorder]
    rightInOrder = inOrder[rootIndexInInorder+1:]

    lenLeftSubtree = len(leftInOrder)

    leftPreOrder = preOrder[1:lenLeftSubtree+1]
    rightPreOrder = preOrder[lenLeftSubtree+1:]

    leftChild = buildTree(leftPreOrder, leftInOrder, n)
    rightChild = buildTree(rightPreOrder, rightInOrder, n)

    # Connection
    root.left = leftChild
    root.right = rightChild

    return root


'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)
                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)



# ex:
# preOrder = [1,2,4,5,3,6,7]
# inOrder = [4,2,5,1,6,3,7]
# n = len(inOrder)

# root = buildTree(preOrder, inOrder, n)
# printTreeDetailed(root)

# Problem statement
# For a given preorder and inorder traversal of a Binary Tree of type integer stored in an array/list, create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

# Note:
# Assume that the Binary Tree contains only unique elements. 

# Constraints:
# 1 <= N <= 10^3
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 7
# 1 2 4 5 3 6 7 
# 4 2 5 1 6 3 7 
# Sample Output 1:
# 1 
# 2 3 
# 4 5 6 7 
# Sample Input 2:
# 6
# 5 6 2 3 9 10 
# 2 6 3 9 5 10 
# Sample Output 2:
# 5 
# 6 10 
# 2 3 
# 9 