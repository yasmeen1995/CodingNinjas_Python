from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
is_heap = True

def is_leaf(node) -> bool:
  if not node.left and not node.right:
    return True
  return False

# Returns the max in the subtree of node
def check(node) -> int:
  global is_heap

  if is_leaf(node):
    return node.data

  if not node.left:
    is_heap = False
    return node.data
  
  if node.left and not node.right and not is_leaf(node.left):
    is_heap = False
    return node.data

  max_left =  check(node.left)
  max_right = node.data

  if node.right:
    max_right = check(node.right)

  maxim = max(max_left, max_right, node.data)

  if maxim == node.data:
    return node.data
  else:
    is_heap = False
    return maxim


def isBinaryHeapTree(root):
  # Write your code here.
  global is_heap
  is_heap = True

  check(root)

  return is_heap


# Problem statement
# You have been given a binary tree of integers.

# Your task is to check if it is a binary heap tree or not.

# Note:

# A binary tree is a tree in which each parent node has at most two children. 

# A binary heap tree has the following properties. 
# 1. It must be a complete binary tree. In the complete binary tree every level, except the last level, is completely filled and the last level is as far left as possible.

# 2. Every parent must be greater than its all children nodes.
# For example:
# Consider this binary tree:
# Figure 1 is a complete binary tree because every level, except the last level, is completely filled and the last nodes are as far left as possible, and the level has 2 nodes both on the left side.

# Figure 2 is not a complete binary tree because level 2 (level is 0 based) is not completely filled means the right child of the node (36) is missing.
# There is another reason, in the last level, there can be one another node in between node (1) and node (14) to make the binary tree as far left as possible.
# Note:
# 1. In the world of programming two types of binary heap tree possible:
#    a. Min-heap - if all parents nodes are lesser than its children nodes.
#    b. Max-heap - if all parents nodes greater than its children nodes, explained in the above figure-1.

# 2. In this problem binary heap tree is a binary max-heap tree.

# Sample Input 1:
# 2
# 10 8 9 5 5 4 5 1 2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 15 14 10 4 5 11 5 1 2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# Sample output 1:
# True
# False
# Explanation of sample input 1:
# Test case 1:
# It is clearly a complete binary tree because every level, except the last level, is completely filled, and every node of the last level is as far left as possible.
# Given binary tree is a binary heap tree because every parent node is greater than all the children nodes.
# Node (10) is greater than :  8, 9, 5, 5, 4, 5, 1,2
# Node (8) is greater than : 5, 5, 1, 2
# Node (9) is greater than : 4, 5
# Node (5) is greater than : 1, 2 (the node (5) at level 2 and the left most)
# All the other nodes have no children.
# Hence all the parent nodes are greater than all the children nodes of a particular node.

# Test case 2:
# It is clearly a complete binary tree because every level, except the last level, is completely filled, and every node of the last level is as far left as possible.
# Given a binary tree is not a binary heap tree, because node (10) has a child node (11) which is greater than the parent node (10)  so it is not a binary heap tree.
# Sample Input 2:
# 2
# 10 1 2 -1 -1 3 -1 -1 -1
# 3 1 2 -1 -1 -1 -1
# Sample output 2:
# False
# True

  

