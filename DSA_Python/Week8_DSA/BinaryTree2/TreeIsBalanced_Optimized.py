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


def getHeightAndCheckBalanced(root):
    if root is None:
        return 0, True

    left_height, isLeftBalanaced = getHeightAndCheckBalanced(root.left)
    right_height, isRightBalanaced = getHeightAndCheckBalanced(root.right)

    h = 1 + max(left_height, right_height)

    if left_height - right_height > 1 or right_height - left_height > 1:
        return h, False

    if isLeftBalanaced and isRightBalanaced:
        return h, True
    else:
        return h, False


root = treeInput()
printTreeDetailed(root)
print(getHeightAndCheckBalanced(root))


# def isBalanced(root):
#     h, isRootBanalanced = getHeightAndCheckBalanced(root)
#     return isRootBanalanced

# root = treeInput()
# printTreeDetailed(root)
# print(isBalanced(root))