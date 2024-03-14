from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rootToLeafPathsSumToKHelper(root, path, k):
    if root is None:
        return
    
    newData = k - root.data
    path.append(root.data)

    if root.left is None and root.right is None:
        if newData == 0:
            for i in path:
                print(i, end=" ")
            print()

        path.pop()
        return

    rootToLeafPathsSumToKHelper(root.left, path, newData)
    rootToLeafPathsSumToKHelper(root.right, path, newData)

    path.pop()


def rootToLeafPathsSumToK(root, k):
	#Your code goes here
    path = []
    rootToLeafPathsSumToKHelper(root, path, k)



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
k = int(stdin.readline().strip())
rootToLeafPathsSumToK(root, k)


# Problem statement
# For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all the node data along the path is equal to K.

# If you see in the above-depicted picture of Binary Tree, we see that there are a total of two paths, starting from the root and ending at the leaves which sum up to a value of K = 13.

# The paths are:
# a. 2 3 4 4
# b. 2 3 8

# One thing to note here is, there is another path in the right sub-tree in reference to the root, which sums up to 13 but since it doesn't end at the leaf, we discard it.
# The path is: 2 9 2(not a leaf)

# Sample Input 1:
# 2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
# 13
#  Sample Output 1:
# 2 3 4 4 
# 2 3 8
# Sample Input 2:
# 5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
# 13
#  Sample Output 2:
# 5 6 2
# 5 7 1