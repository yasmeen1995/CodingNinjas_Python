import sys

#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
## Print output as specified in the question.

from sys import stdin
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def heightOfTree(root):
    if root is None:
        return 0

    rootHeight = 0
    for child in root.children:
        childHeight = heightOfTree(child)
        rootHeight = max(childHeight, rootHeight)

    return rootHeight + 1

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
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
root = createLevelWiseTree(arr)
print(heightOfTree(root))



# Problem statement
# Given a generic tree, find and return the height of given tree. The height of a tree is defined as the longest distance from root node to any of the leaf node. Assume the height of a tree with a single node is 1.

# Constraints:
# Time Limit: 1 sec
# Sample Input 1:
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1:
# 3