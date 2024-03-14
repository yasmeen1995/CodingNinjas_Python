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
    # Your code goes here
    if root == None:
        return 

    q = queue.Queue()

    if root.data != -1:
        q.put(root)
    
    while (not(q.empty())):
        current_root = q.get()
        print(current_root.data, end= ":")

        if current_root.left != None:
            print("L:"+str(current_root.left.data), end = ",")
            q.put(current_root.left)
        
        if current_root.left == None:
            print("L:" +str(-1), end = ",")

        if current_root.right != None:
            print("R:"+str(current_root.right.data))
            q.put(current_root.right)
        if current_root.right == None:
            print("R:" + str(-1))



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
# For a given a Binary Tree of type integer, print the complete information of every node, when traversed in a level-order fashion.

# To print the information of a node with data D, you need to follow the exact format :

#            D:L:X,R:Y

# Where D is the data of a node present in the binary tree. 
# X and Y are the values of the left(L) and right(R) child of the node.
# Print -1 if the child doesn't exist.

# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
#  Sample Output 1:
# 8:L:3,R:10
# 3:L:1,R:6
# 10:L:-1,R:14
# 1:L:-1,R:-1
# 6:L:4,R:7
# 14:L:13,R:-1
# 4:L:-1,R:-1
# 7:L:-1,R:-1
# 13:L:-1,R:-1
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
#  Sample Output 2:
# 1:L:2,R:3
# 2:L:4,R:5
# 3:L:6,R:7
# 4:L:-1,R:-1
# 5:L:-1,R:-1
# 6:L:-1,R:-1
# 7:L:-1,R:-1