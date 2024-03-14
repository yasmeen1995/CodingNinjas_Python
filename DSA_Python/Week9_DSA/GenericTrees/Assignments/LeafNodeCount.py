import sys
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree == None: # If there is no tree at all
        return 0

    if len(tree.children) == None: #If root has no children
        return 1

    count = 0
    for child in tree.children:
        count += leafNodeCount(child)

    return count

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
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))



# Problem statement
# Given a generic tree, count and return the number of leaf nodes present in the given tree.

# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1 :
# 4