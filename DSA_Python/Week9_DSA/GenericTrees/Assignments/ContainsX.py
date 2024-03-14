from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def containsX(tree, x):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree == None: # not a base case but edge case
        return

    if tree.data == x:
        return True
    
    for child in tree.children:
        result = containsX(child, x)
        if result == True:
            return True
        
    return False
        

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
x=int(stdin.readline().strip())
tree = createLevelWiseTree(arr)
if containsX(tree,x):
    print('true')
else:
    print('false')


# Problem statement
# Given a generic tree and an integer x, check if x is present in the given tree or not. Return true if x is present, return false otherwise.

# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0
# 40 
# Sample Output 1 :
# true
# Sample Input 2 :
# 10 3 20 30 40 2 40 50 0 0 0 0
# 4 
# Sample Output 2:
# false