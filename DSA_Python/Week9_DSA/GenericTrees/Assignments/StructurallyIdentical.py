from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree1 == None or tree2 == None:
        return False

    if tree1 == None and tree2 == None:
        return True

    if tree1.data != tree2.data or len(tree1.children) != len(tree2.children):
        return False

    for child1, child2 in zip(tree1.children, tree2.children):
        if not isIdentical(child1, child2):
            return False

    return True
    

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
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')


# Problem statement
# Given two generic trees, return true if they are structurally identical. Otherwise return false.

# Structural Identical
# If the two given trees are made of nodes with the same values and the nodes are arranged in the same way, then the trees are called identical.  
# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output 1 :
# true
# Sample Input 2 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 2 30 40 2 40 50 0 0 0 0
# Sample Output 2:
# false