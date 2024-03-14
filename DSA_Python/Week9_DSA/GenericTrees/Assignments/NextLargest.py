from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree == None:
        return None

    next_large = None

    if tree.data > n:
        next_large = tree

    for child in tree.children:
        tempNode = nextLargest(child, n)

        if tempNode != None:
            if next_large == None or tempNode.data < next_large.data:
                next_large = tempNode

    return next_large



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)


# Problem statement
# Given a generic tree and an integer n. Find and return the node with next larger element in the tree i.e. find a node with value just greater than n.

# Note: Return NULL if no node is present with the value greater than n.

# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 18
# Sample Output 1 :
# 20
# Sample Input 2 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 21
# Sample Output 2:
# 30
