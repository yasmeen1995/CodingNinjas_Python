from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getSum(root):
	#Your code goes here
    if root == None:
        return 0

    leftSum = getSum(root.left)
    rightSum = getSum(root.right)

    return root.data + leftSum + rightSum


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

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
print(getSum(root))


# Problem statement
# For a given Binary Tree of integers, find and return the sum of all the nodes data.

# Constraints:
# 1 <= N <= 10^6
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 2 3 4 6 -1 -1 -1 -1 -1
# Sample Output 1:
#  15
# Explanation :
# The binary tree formed using the input values: 2, 3, 4, 6, -1, -1, -1, -1, -1. Hence the sum is 15. 

# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
#  28
