


# 15. Trees



# 15.1 Tree Data Structure
# A tree is a hierarchical data structure that consists of nodes, with a single node called the root. Each node can have zero or more child nodes, and each node has exactly one parent node, except for the root node, which has no parent. Trees are widely used in computer science for various purposes.

# Terminology:

# Root: The top node in a tree.
# Node: Each element in a tree.
# Edge: The connection between two nodes.
# Parent: The node above another node.
# Child: The node below another node.
# Leaf: A node with no children.
# Subtree: A tree consisting of a node and its descendants.
# Height: The length of the longest path from the root to a leaf.
# Depth: The length of the path from the root to a node.
# Tree Example:


#          A
#         / \
#        B   C
#       / \   \
#      D   E   F



# 15.2 Application of Tree
# Applications:

# Hierarchical Data: Representing hierarchical structures like file systems, organizational structures, etc.
# Searching Algorithms: Implementing search trees like Binary Search Trees (BST), AVL trees, etc.
# Routing Algorithms: Used in networking to determine the most efficient routing paths.
# Database Indexing: B-trees and their variants are used in database indexing.
# Expression Parsing: Abstract syntax trees in compilers for parsing expressions.


# 15.3 Binary Tree in Python
# A binary tree is a tree data structure where each node has at most two children, referred to as the left child and the right child.

# Binary Tree Implementation in Python:


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# # Example usage:
# # Creating a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)



# 15.4 Tree Traversal
# Tree traversal refers to the process of visiting all the nodes of a tree in a specific order. There are three common types of tree traversal:

# Inorder Traversal (Left, Root, Right)
# Inorder traversal visits the nodes of a binary tree in the following order: left subtree, root node, right subtree.

# Inorder Traversal Implementation:


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# # Example usage:
inorder_traversal(root)  # Output: 4 2 5 1 3
# Preorder Traversal (Root, Left, Right)
# Preorder traversal visits the nodes of a binary tree in the following order: root node, left subtree, right subtree.

# Preorder Traversal Implementation:


def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# # Example usage:
preorder_traversal(root)  # Output: 1 2 4 5 3
# Postorder Traversal (Left, Right, Root)
# Postorder traversal visits the nodes of a binary tree in the following order: left subtree, right subtree, root node.

# Postorder Traversal Implementation:


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

# # Example usage:
postorder_traversal(root)  # Output: 4 5 2 3 1



# Detailed Breakdown
# Node Class:


# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
# self.left: Points to the left child of the node.
# self.right: Points to the right child of the node.
# self.val: Stores the value of the node.


# Creating a Binary Tree:


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root = Node(1): Creates the root node with value 1.
# root.left = Node(2): Creates the left child of the root node with value 2.
# root.right = Node(3): Creates the right child of the root node with value 3.
# root.left.left = Node(4): Creates the left child of the node with value 2.
# root.left.right = Node(5): Creates the right child of the node with value 2.
# Inorder Traversal:


# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.val, end=" ")
#         inorder_traversal(root.right)
# if root:: Checks if the current node is not None.
# inorder_traversal(root.left): Recursively visits the left subtree.
# print(root.val, end=" "): Prints the value of the current node.
# inorder_traversal(root.right): Recursively visits the right subtree.
# Preorder Traversal:


# def preorder_traversal(root):
#     if root:
#         print(root.val, end=" ")
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)
# print(root.val, end=" "): Prints the value of the current node.
# preorder_traversal(root.left): Recursively visits the left subtree.
# preorder_traversal(root.right): Recursively visits the right subtree.
# Postorder Traversal:


# def postorder_traversal(root):
#     if root:
#         postorder_traversal(root.left)
#         postorder_traversal(root.right)
#         print(root.val, end=" ")
# postorder_traversal(root.left): Recursively visits the left subtree.
# postorder_traversal(root.right): Recursively visits the right subtree.
# print(root.val, end=" "): Prints the value of the current node.