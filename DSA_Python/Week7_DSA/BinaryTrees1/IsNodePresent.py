# Binary TreeNode class
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


import queue

def isNodePresent(root, x):
    # write your code 
    if root == None:
        return False
    
    if root.data == x:
        return True

    if root.left != None:
        return isNodePresent(root.left, x)
    
    if root.right != None:
        return isNodePresent(root.right, x)


# To build the tree
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)

    if length<=0 or levelorder[0]==-1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:

            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:

            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

x = int(input())

present = isNodePresent(root, x)

if present:
    print('true')
else:
    print('false')


# Problem statement
# For a given Binary Tree of type integer and a number X, find whether a node exists in the tree with data X or not.

# Constraints:
# 1 <= N <= 10^5

# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec.
# Sample Input 1:
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# 7
# Sample Output 1:
# true
# Explanation For Output 1:
# Clearly, we can see that 7 is present in the tree. So, the output will be true.
# Sample Input 2:
# 2 3 4 -1 -1 -1 -1
# 10
# Sample Output 2:
# false