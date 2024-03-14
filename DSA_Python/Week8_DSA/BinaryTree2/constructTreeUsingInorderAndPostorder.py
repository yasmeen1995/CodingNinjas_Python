from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(postOrder, inOrder, n) :
	#Your code goes here
    if len(postOrder) == 0:
        return None

    rootData = postOrder[-1]
    root = BinaryTreeNode(rootData)
    rootIndexInorder = -1 

    for i in range(len(inOrder)):
        if inOrder[i] == rootData:
            rootIndexInorder = i
            break

    if rootIndexInorder == -1:
        return None
    
    leftInOrder = inOrder[0:rootIndexInorder]
    rightInOrder = inOrder[rootIndexInorder+1:]

    # Now we need to know the len of leftsubTree and rightSubtree
    lenOfLeftSubtree = len(leftInOrder)

    leftPostOrder = postOrder[0:lenOfLeftSubtree]
    rightPostOder = postOrder[lenOfLeftSubtree:-1]

    # print('yss, ', rightPostOder)

    leftChild = buildTree(leftPostOrder, leftInOrder, n)
    rightChild = buildTree(rightPostOder, rightInOrder, n)

    
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

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)



# Problem statement
# For a given postorder and inorder traversal of a Binary Tree of type integer stored in an array/list, create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

# Note:
# Assume that the Binary Tree contains only unique elements. 

# Constraints:
# 1 <= N <= 10^4
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 7
# 4 5 2 6 7 3 1 
# 4 2 5 1 6 3 7 
# Sample Output 1:
# 1 
# 2 3 
# 4 5 6 7 
# Sample Input 2:
# 6
# 2 9 3 6 10 5 
# 2 6 3 9 5 10 
# Sample Output 2:
# 5 
# 6 10 
# 2 3 
# 9