import sys
import queue

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root
        
def sumOfAllNodes(root) :
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root == None:
        return 0

    sum = root.data
    for child in root.children:
        sum += sumOfAllNodes(child)

    return sum
    
#main
sys.setrecursionlimit(10**6)
li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(sumOfAllNodes(root))



# Problem statement
# Given a generic tree, find and return the sum of all nodes present in the given tree.

# Constraints:
# Time Limit: 1 sec
# Sample Input 1:
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1:
# 190