import sys
import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree == None:  # edge case not base case
        return 
    
    q = queue.Queue()
    q.put(tree)

    while not q.empty():
        current_node = q.get()
        print(str(current_node.data) + ":", end="")

        for index, child in enumerate(current_node.children):
            print(str(child.data), end="")
            if index < len(current_node.children) - 1:
                print(",", end="")
            q.put(child)

        print()

# CodingNinja Solution
# def printLevelWiseTree(tree):
#     q = [tree]
#     while q:
#         parent = q.pop(0)
#         print(parent.data, ":", ",".join(str(num) for num in parent.children), sep='')
#         for child in parent.children:
#             q.append(child)


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
printLevelWiseTree(tree)



# Problem statement
# Given a generic tree, print the input tree in level wise order.

# For printing a node with data N, you need to follow the exact format -

# N:x1,x2,x3,...,xn
# where, N is data of any node present in the generic tree. x1, x2, x3, ...., xn are the children of node N. Note that there is no space in between.
# You need to print all nodes in the level order form in different lines.

# Constraints:
# Time Limit: 1 sec
# 0 <= Data of a node <= 10^5
# Sample Input 1:
# 10 3 20 30 40 2 40 50 0 0 0 0 

# Sample Output 1:
# 10:20,30,40
# 20:40,50
# 30:
# 40:
# 40:
# 50:
