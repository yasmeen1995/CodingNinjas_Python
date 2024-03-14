from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameterOfBinaryTree(root) :
    def helper(node):
        if not node:
            return 0, 0  # height, diameter
        
        left_height, left_diameter = helper(node.left)
        right_height, right_diameter = helper(node.right)
        
        current_height = 1 + max(left_height, right_height)
        current_diameter = max(left_height + right_height, left_diameter, right_diameter)

        return current_height, current_diameter
    
    _, diameter = helper(root)
    return 1 + diameter


# Another way:
# def diameterHepler(root):
#     if root is None:
#         pair = Pair(0,0)
#         return pair

#     leftPair = diameterHepler(root.left)
#     rightPair = diameterHepler(root.right)

#     leftDiameter = leftPair.diameter
#     rightDiameter = rightPair.diameter

#     diameterFromRoot = leftPair.height + rightPair.height + 1

#     diameter = max ( leftDiameter, rightDiameter, diameterFromRoot)
#     height = max(leftPair.height + rightPair.height) + 1

#     return Pair(diameter, height)

# def diameterOfBinaryTree(root) :
#     pair = diameterHepler(root)
#     return pair.diameter



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
    if root==None:
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

print(diameterOfBinaryTree(root))



# Problem statement
# For a given Binary of type integer, find and return the ‘Diameter’.

# Diameter of a Tree
# The diameter of a tree can be defined as the maximum distance between two leaf nodes.
# Here, the distance is measured in terms of the total number of nodes present along the path of the two leaf nodes, including both the leaves.

# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 2 4 5 6 -1 -1 7 20 30 80 90 -1 -1 8 -1 -1 9 -1 -1 -1 -1 -1 -1 
# Sample Output 1:
# 9
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
# 5