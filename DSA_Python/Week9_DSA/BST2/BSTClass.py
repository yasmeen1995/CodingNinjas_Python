class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    

    def printTreeHelper(self, root):
        if root == None:
            return
        
        print(root.data, end = ":")

        if root.left != None:
            # print("L:",end='')
            # print(root.left.data,end=',')
            print("L:" + str(root.left.data), end=",")
        if root.right != None:
            # print("R:",end='')
            # print(root.right.data,end='')
            print("R:" + str(root.right.data), end="")
        print()
        
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)


    def printTree(self):
        ##################################
        # PLEASE IMPLEMENT THIS FUNCTION #
        ##################################
        self.printTreeHelper(self.root)

    
    def searchHelper(self, root, data):
        if root == None:
            return False

        if root.data == data:
            return True
        if root.data > data:
            #Call on left
            return self.searchHelper(root.left, data)
        else:
            #Call on right
            return self.searchHelper(root.right, data)


    def search(self, data):
        ##################################
        # PLEASE IMPLEMENT THIS FUNCTION #
        ##################################
        return self.searchHelper(self.root, data)

    def insertHelper(self, root, data):
        if root is None:
            node = BinaryTreeNode(data)
            return node

        if root.data >= data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root


        
    def insert(self, data):
        ##################################
        # PLEASE IMPLEMENT THIS FUNCTION #
        ##################################
        self.numNodes += 1
        # When there is no root at all then create that root here
        self.root = self.insertHelper(self.root, data) 
    
    
    def min(self, root):
        if root == None:
            return 100000000 #Positive infi

        if root.left == None:
            return root.data
        return self.min(root.left)


    def deleteDataHelper(self, root, data):
        if root == None:
            return False, None

        if root.data < data:
            deleted, newRightNode = self.deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root

        if root.data > data:
            deleted, newLefttNode = self.deleteDataHelper(root.left, data)   
            root.left = newLefttNode
            return deleted, root
        
        #Root is leave::  self.root == data
        if root.left == None and root.right == None:
            return True, None

        # Root has one right child
        if root.left == None:
            return True, root.right

        # Root has one left child
        if root.right == None:
            return True, root.left

        # Root has two children
        minRightVal = self.min(root.right)  # getting min from right subtree
        root.data = minRightVal #coping the min from right subtree to the root
        deleted, newRightNode = self.deleteDataHelper(root.right, minRightVal)
        root.right = newRightNode
        return True, root


    def delete(self, data):
        ##################################
        # PLEASE IMPLEMENT THIS FUNCTION #
        ##################################
        deleted, newRoot = self.deleteDataHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()



# Problem statement
# Implement the BST class which includes following functions -

# 1. insert -
# Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.

# 2. search
# Given an element, find if that is present in BST or not. Return true or false.

# 3. delete -
# Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.

# 4. printTree (recursive) -
# Print the BST in in the following format -

# For printing a node with data N, you need to follow the exact format -

# N:L:x,R:y
# where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.

# There is no space in between.

# You need to print all nodes in the recursive format in different lines.

