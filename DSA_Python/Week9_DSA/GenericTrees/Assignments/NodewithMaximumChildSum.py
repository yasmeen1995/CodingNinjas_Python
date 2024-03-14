from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

def maxSumNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree == None:
        return 

    ans_node = tree
    sum = tree.data

    for child in tree.children:
        sum += child.data
    
    # max_child = 0
    for child in tree.children:
        temp_node, temp_sum = maxSumNode(child)

        if temp_sum > sum:
            sum = temp_sum
            ans_node = temp_node

    return ans_node, sum



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
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)


# Problem statement
# Given a generic tree, find and return the node for which sum of its data and data of all its child nodes is maximum. In the sum, data of the node and data of its immediate child nodes has to be taken.

# Constraints:
# Time Limit: 1 sec
# 0 < Node's val <= 10^5
# Sample Input 1 :
# 5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0

# Sample Output 1 :
# 1
