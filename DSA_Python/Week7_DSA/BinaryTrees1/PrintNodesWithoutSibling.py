from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printNodesWithoutSibling(root) :
	# Your code goes here
    if root == None:
        return None

    if root.left == None and root.right != None:
        print(root.right.data, end = " ")
    
    if root.right == None and root.left != None:
        print(root.left.data, end = " ")
    
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)



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
printNodesWithoutSibling(root)




# Problem statement
# For a given Binary Tree of type integer, print all the nodes without any siblings.

# Example Input :
# 1 4 5 6 -1 -1 7 20 30 80 90 -1 -1 -1 -1 -1 -1 -1 -1
# Explanation:
# The input tree when represented in a two-dimensional plane, it would look like this:     

# In respect to the root, node data in the left subtree that satisfy the condition of not having a sibling would be 6, taken in a top-down sequence. Similarly, for the right subtree, 7 is the node data without any sibling.

# Since we print the siblings in the left-subtree first and then the siblings from the right subtree, taken in a top-down fashion, we print 6 7.
# Example Output:
# 6 7  

#  Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 second
# Sample Input 1:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output 1:
# 9 