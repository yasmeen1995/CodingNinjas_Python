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



def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if left_height - right_height > 1 or right_height - left_height > 1:
        return False

    isLeftBalanaced = isBalanced(root.left)
    isRightBalanaced = isBalanced(root.right)
    if isLeftBalanaced and isRightBalanaced:
        return True
    else:
        return False


root = treeInput()
printTreeDetailed(root)
print(isBalanced(root))

# 1
# 2
# 4
# 6
# -1
# -1
# -1
# -1
# 3
# -1
# 5
# -1
# -1
#False