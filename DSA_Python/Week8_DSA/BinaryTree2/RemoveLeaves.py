class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end =":")
    if root.left != None:
        print("L", root.left.data, end = ", ")
    if root.right != None:
        print("R", root.right.data, end = "")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


def removeLeaves(root):
    if root == None:
        return None
    # checking if root itself a leave
    if root.left == None and root.right == None:
        return None

    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    return root


root = treeInput()
# printTreeDetailed(root)
root1 = removeLeaves(root)
printTreeDetailed(root1)
# 1
# 2
# 4
# -1
# -1
# 5
# 8
# -1
# -1
# 9
# -1
# -1
# 3
# 6
# -1
# -1
# 7
# -1
# -1