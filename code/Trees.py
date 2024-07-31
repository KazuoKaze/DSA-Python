




## Tips: 
# 
# 
# 
# 
# If you wanna understand Trees effectively please first complete Queue, Stack and Linked List. Mastering these topics will make learning Trees a breeze 
# Good luck with learning Trees






## Imp watch this YT playlist to understand Binary Tree 





## https://www.youtube.com/watch?v=6oL-0TdVy28&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&pp=iAQB






## Also you can find a nutshell code of whole topics and other binary methods in a single one ( check out last code )







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






## 15.2 Application of Tree







# Applications:

# Hierarchical Data: Representing hierarchical structures like file systems, organizational structures, etc.
# Searching Algorithms: Implementing search trees like Binary Search Trees (BST), AVL trees, etc.
# Routing Algorithms: Used in networking to determine the most efficient routing paths.
# Database Indexing: B-trees and their variants are used in database indexing.
# Expression Parsing: Abstract syntax trees in compilers for parsing expressions.







## 15.3 Binary Tree in Python








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







## 15.4 Tree Traversal








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


# Traversal of a binary tree is a fundamental operation that allows us to visit each node in a specific order. The three common traversal methods—Inorder, Preorder, and Postorder—are used for various purposes depending on the specific requirements of an application or problem. Here’s a breakdown of each traversal method, its implementation, and its use cases:

# 1. Inorder Traversal (Left, Root, Right)
# Code:


# def inorder(self, node):
#     if node:
#         self.inorder(node.left)
#         print(node.data, end=' -> ')
#         self.inorder(node.right)


# Use Case:

# Binary Search Trees (BSTs): Inorder traversal of a BST retrieves the nodes in non-decreasing order. This is particularly useful for sorting and checking the properties of BSTs.
# Syntax Trees: It helps in converting the syntax tree into infix expressions, making it useful in compiler design.


# 2. Preorder Traversal (Root, Left, Right)
# Code:


# def preorder(self, node):
#     if node:
#         print(node.data, end=' -> ')
#         self.preorder(node.left)
#         self.preorder(node.right)
# Use Case:

# Tree Copying: Preorder traversal is used to create a copy of the tree.
# Prefix Expressions: It helps in converting the syntax tree into prefix expressions, useful in certain types of computations and evaluations.
# File Systems: Preorder traversal is used to list directories and files (like in a file explorer).


# 3. Postorder Traversal (Left, Right, Root)
# Code:


# def postorder(self, node):
#     if node:
#         self.postorder(node.left)
#         self.postorder(node.right)
#         print(node.data, end=' -> ')
# Use Case:

# Tree Deletion: Postorder traversal is used to delete a tree. This ensures that the children nodes are deleted before their parent node.
# Expression Evaluation: It helps in converting the syntax tree into postfix expressions, useful for evaluating expressions using a stack.
# Why Specific Orders?
# The traversal orders are not arbitrary; they are designed to serve specific purposes:

# Inorder Traversal: This visits nodes in non-decreasing order for BSTs, making it ideal for operations that require sorted data.
# Preorder Traversal: This is useful for creating a replica of the tree or producing prefix expressions (polish notation).
# Postorder Traversal: This is useful for deleting a tree or evaluating postfix expressions (reverse polish notation).


# Why Not Other Orders?
# The given traversal orders (Inorder, Preorder, Postorder) are the most commonly used because they address the most frequent needs in computer science and data structures. Traversing the right subtree before the left subtree is less common because the natural hierarchical representation of trees and binary search properties often make left-first traversals more useful. However, there are no strict rules against defining custom traversal orders if a particular application requires it.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def inorder(self, root_node):
        if root_node:
            self.inorder(root_node.left)
            print(root_node.data, end=' -> ')
            self.inorder(root_node.right)

    def preorder(self, root_node):
        if root_node:
            print(root_node.data, end=' -> ')
            self.preorder(root_node.left)
            self.preorder(root_node.right)

    def postorder(self, root_node):
        if root_node:
            self.postorder(root_node.left)
            self.postorder(root_node.right)
            print(root_node.data, end=' -> ')


bi = BinaryTree(1)
bi.root.left = Node(2) 
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)

bi.inorder(bi.root)
print('')
bi.preorder(bi.root)
print('')
bi.postorder(bi.root)








## Level order traversal










# Level order traversal is a method of traversing a binary tree level by level, starting from the root. This traversal visits all nodes at the current level before moving on to nodes at the next level. It is also known as breadth-first traversal.

# Why Use a Queue?
# A queue is ideal for level order traversal because it operates on a first-in, first-out (FIFO) basis. This ensures that nodes are processed in the order they are encountered, maintaining the correct sequence for level-by-level traversal.

# Code Example and Explanation
# Here’s how you can implement level order traversal using a queue:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)  # Add data to the end of the queue

    def get(self):
        return self.queue.pop(0)  # Remove and return data from the front of the queue
    
    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty

    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # Return the front data without removing it
        else:
            return None

    def get_size(self):
        return len(self.queue)  # Return the current size of the queue

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)  # Initialize the binary tree with the root node

    def level_order(self, root_node):
        if not root_node:
            return None  # If the root node is None, return None
        
        queue = Queue()
        queue.put(root_node)
        level_order_list = []

        while not queue.is_empty():
            out_node = queue.get()  # Dequeue a node
            level_order_list.append(out_node)  # Append the node to the result list

            if out_node.left:
                queue.put(out_node.left)  # Enqueue the left child
            if out_node.right:
                queue.put(out_node.right)  # Enqueue the right child

        return [node.data for node in level_order_list]  # Extract data values from nodes

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2) 
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)

print(bi.level_order(bi.root))  # Output: [1, 2, 3, 4, 5]








## reverse level traversal









# Reverse level order traversal is the process of traversing a binary tree level by level but starting from the bottom-most level and moving upwards to the root. This is essentially the opposite of the standard level order traversal.

# Approach
# To achieve reverse level order traversal, you can use the following approach:

# Use a Queue for Standard Level Order Traversal:

# Traverse the tree level by level, and use a queue to keep track of nodes.
# Use a Stack to Reverse the Order:

# Push each node's value onto a stack as you dequeue it from the queue. The stack will help reverse the order because it follows Last-In-First-Out (LIFO) principle.
# Output from the Stack:

# Pop nodes from the stack to get the reverse level order traversal.


# Code Example
# Here's how you can implement reverse level order traversal in Python:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1]
    
    def get_size(self):
        return len(self.stack)
    
    def get_stack(self):
        return self.stack

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
        
    def get_size(self):
        return len(self.queue)

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def reverse_order_trav(self, root_node):
        if root_node is None:
            return []
        
        stack = Stack()
        queue = Queue()

        queue.put(root_node)

        while not queue.is_empty():
            out_node = queue.get()

            # Enqueue the right child first to ensure correct order in the stack
            if out_node.right:
                queue.put(out_node.right)
            if out_node.left:
                queue.put(out_node.left)

            # Push the node onto the stack
            stack.append(out_node)
        
        reverse_level = []
        
        # Pop nodes from the stack to get them in reverse level order
        while not stack.is_empty():
            reverse_level.append(stack.pop().data)

        return reverse_level

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2) 
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)

print(bi.reverse_order_trav(bi.root))  # Output: [4, 5, 3, 2, 1]


# When it comes to reverse level order traversal, the best method depends on factors like code simplicity, memory usage, and execution time. Here’s a comparison of common approaches:

# 1. Queue and Stack Method
# Description: Use a queue for level-order traversal and a stack to reverse the order.

# Pros:

# Straightforward and intuitive.
# Clear separation of concerns: queue handles level-order traversal, and stack handles reversal.
# Cons:

# Requires two additional data structures: a queue and a stack.
# Slightly more complex due to managing multiple structures.
# Code Example:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def reverse_level_order_trav(self, root_node):
        if not root_node:
            return []

        queue = Queue()
        stack = Stack()
        queue.put(root_node)

        while not queue.is_empty():
            node = queue.get()
            stack.append(node)

            if node.right:
                queue.put(node.right)
            if node.left:
                queue.put(node.left)

        result = []
        while not stack.is_empty():
            result.append(stack.pop().data)

        return result
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# 2. Two Queues Method
# Description: Use one queue for level-order traversal and a second queue to reverse the order.

# Pros:

# Avoids the explicit use of a stack.
# Simple approach with clear logic.
# Cons:

# Requires an extra queue, which adds to the space complexity.
# Code Example:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def reverse_level_order_trav(self, root_node):
        if not root_node:
            return []

        level_queue = Queue()
        reverse_queue = Queue()
        level_queue.put(root_node)

        while not level_queue.is_empty():
            node = level_queue.get()
            reverse_queue.put(node.data)

            if node.right:
                level_queue.put(node.right)
            if node.left:
                level_queue.put(node.left)

        result = []
        while not reverse_queue.is_empty():
            result.append(reverse_queue.get())

        return result
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# 3. Single Queue with List Reversal Method
# Description: Perform level-order traversal using a single queue and reverse the collected nodes' values at the end.

# Pros:

# Simpler and uses only one additional data structure.
# Easy to understand and implement.
# Cons:

# Requires reversing the list of collected values, which adds an extra step.
# Code Example:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def reverse_level_order_trav(self, root_node):
        if not root_node:
            return []

        queue = Queue()
        queue.put(root_node)
        level_order_list = []

        while not queue.is_empty():
            node = queue.get()
            level_order_list.append(node.data)

            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        return level_order_list[::-1]  # Reverse the list

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)

print(bi.reverse_level_order_trav(bi.root))  # Output: [4, 5, 3, 2, 1]
# Time Complexity: O(n) 
# Space Complexity: O(n)

# Summary
# Queue and Stack Method: Offers clear separation of concerns but uses two additional data structures.
# Two Queues Method: Straightforward and avoids a stack but uses an extra queue.
# Single Queue with List Reversal Method: Simplest and efficient with minimal data structures, but involves an extra reversal step.







## Calculating Height of Tree








# Calculating the height of a binary tree is a common problem in tree data structure algorithms. The height of a binary tree is defined as the number of edges on the longest path from the root node to a leaf node. It can also be defined as the number of nodes along the longest path from the root node to the deepest leaf node, minus one.

# How to Calculate Tree Height

# 1. Definition
# Height of a Node: The height of a node is the number of edges on the longest path from the node to a leaf node.
# Height of a Tree: The height of the root node of a tree.
# Approach
# Recursive Approach
# The recursive approach is straightforward and intuitive. You compute the height of the left and right subtrees of a node and then use the larger of the two heights to compute the height of the node.

# Steps:

# Base Case: If the node is None, return -1 (for height definition) or 0 (for height definition including the node itself).
# Recursive Case: Compute the height of the left subtree and the height of the right subtree.
# Combine Results: The height of the current node is 1 + max(height_of_left_subtree, height_of_right_subtree).


# Code Example
# Here's how you can calculate the height of a binary tree using a recursive approach in Python:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    
    def height(self, node):
        if node is None:
            return -1  # For height definition (0-based) or return 0 for height definition including node itself
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)

# Example usage
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.root.right.right = Node(7)

print("Height of the tree:", bi.height(bi.root))  # Output will be 2 (0-based height)


# Explanation:

# if node is None:: This is the base case. When you reach a leaf node's child (which is None), the height is -1 (or 0 if you include the node itself in the height).
# height(node.left) and height(node.right): Recursively calculate the height of the left and right subtrees.
# 1 + max(left_height, right_height): The height of the current node is 1 plus the maximum height of its two subtrees.


# Alternative Iterative Approach
# While the recursive approach is the most common, you can also compute the height of a binary tree iteratively using a level-order traversal (BFS) approach. Here's how you might do that:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def height(self):
        if not self.root:
            return -1
        
        queue = Queue()
        queue.put(self.root)
        height = -1

        while not queue.is_empty():
            level_size = len(queue.queue)
            height += 1

            for _ in range(level_size):
                node = queue.get()
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
        
        return height

# Example usage
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.root.right.right = Node(7)

print("Height of the tree:", bi.height())  # Output will be 2


# Explanation:

# Level-order Traversal: Traverse the tree level by level.
# height Calculation: Increase the height count at the end of each level.


# Summary
# Recursive Approach: Simple and intuitive; uses the call stack to manage function calls.
# Iterative Approach: Uses a queue for level-order traversal; avoids recursion and can be more space-efficient for very deep trees.








## Size of a binary tree









# Calculating the size of a binary tree, which is the total number of nodes in the tree, can be done in various ways. Below are explanations and implementations for calculating the size of a binary tree using both recursive and iterative methods.

# Recursive Approach
# In the recursive approach, you traverse the tree and count nodes by summing the sizes of the left and right subtrees and adding one for the current node.

# Implementation
# Here's how you can implement the size calculation recursively:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def size_of_tree(self, node):
        """ Calculate the size of the tree recursively. """
        if node is None:
            return 0
        else:
            left_size = self.size_of_tree(node.left)
            right_size = self.size_of_tree(node.right)
            return left_size + right_size + 1

bi = BinaryTree(1)
bi.root.left = Node(2) 
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)

print(bi.size_of_tree(bi.root))  # Output: 5


# Explanation
# Base Case:

# If the node is None, return 0 because there are no nodes.
# Recursive Case:

# Calculate the size of the left subtree.
# Calculate the size of the right subtree.
# Add 1 for the current node and return the total.


# Iterative Approach
# The iterative approach can be implemented using a breadth-first traversal (level-order traversal) or a depth-first traversal. Here’s how you can do it using a queue.

# Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def get(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def size_of_tree(self, root_node):
        if root_node is None:
            return 0
        
        queue = Queue()
        queue.put(root_node)
        size = 0

        while not queue.is_empty():
            node = queue.get()
            size += 1

            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        return size

bi = BinaryTree(1)
bi.root.left = Node(2) 
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)

print(bi.size_of_tree(bi.root))  # Output: 5


# Explanation
# Initialization:

# Use a queue to perform level-order traversal.
# Processing Nodes:

# Enqueue the root node and initialize size to 0.
# While the queue is not empty:
# Dequeue a node and increment the size.
# Enqueue the left and right children of the node if they exist.
# Return Size:

# The size variable will hold the total number of nodes in the tree.
# Summary
# Recursive Approach: Simple and elegant but can lead to deep recursion for large trees, which might cause stack overflow in some programming languages or environments.

# Iterative Approach: Uses extra space for the queue but avoids deep recursion, which can be beneficial for large trees.

# Both methods have a time complexity of O(n) 








## Printing Nodes at Distance K from the Root in a Binary Tree









# To understand how to print nodes at distance 
# 𝐾
# K from the root in a binary tree, let's delve into the recursive approach, its implementation, and the underlying concepts in detail.

# Concepts and Approach
# Binary Tree Structure:

# A binary tree is a tree data structure where each node has at most two children, referred to as the left child and the right child.
# The root node is the topmost node of the tree.
# Distance K:

# The distance 
# K from the root refers to the number of edges between the root and the target nodes.
# If 
# K is 0, the node at distance 
# K from the root is the root itself.
# For K>0, you need to find nodes that are exactly 
# K edges away from the root.


# Recursive Traversal:

# The recursion will help in traversing the tree level by level until the desired level 
# K is reached.
# At each level, 
# K is decremented by 1 as we move to the next level.


# Base Case and Recursive Case:

# The base case checks if the node is None or if 
# K is 0.
# The recursive case decrements 
# K and continues to traverse the left and right subtrees.
# Implementation
# Here's the step-by-step implementation in Python:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def print_nodes_at_k_distance(self, node, k):
        """ Print nodes at distance K from the root. """
        if node is None:
            return

        if k == 0:
            print(node.data, end=' ')
            return

        # Recur for left and right subtrees
        self.print_nodes_at_k_distance(node.left, k-1)
        self.print_nodes_at_k_distance(node.right, k-1)

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.root.right.left = Node(6)
bi.root.right.right = Node(7)

k = 2
bi.print_nodes_at_k_distance(bi.root, k)  # Output: 4 5 6 7








## 15.10 Iterative Inorder Traversal









# Inorder traversal visits nodes in the order: left subtree, root, right subtree. To perform this iteratively, we use a stack to simulate the recursion.

# Algorithm:
# Initialize an empty stack.
# Start from the root and push all the left children to the stack.
# Pop an item from the stack, print it, and push its right child and all its left descendants to the stack.
# Repeat until the stack is empty.
# Here's the code for iterative inorder traversal:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def iterative_inorder(self, root_node):
        if root_node is None:
            return None

        stack = Stack()
        current = root_node
        final_list = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif not stack.is_empty():
                current = stack.pop()
                final_list.append(current.data)
                current = current.right
            else:
                break

        return final_list

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.root.right.left = Node(6)
bi.root.right.right = Node(7)

print(bi.iterative_inorder(bi.root))  # Output: [4, 2, 5, 1, 6, 3, 7]








## 15.11 Iterative Preorder Traversal









# Preorder traversal visits nodes in the order: root, left subtree, right subtree. To perform this iteratively, we use a stack.

# Algorithm:
# Initialize an empty stack and push the root node.
# Pop the top item from the stack and print it.
# Push the right child of the popped item to the stack (if it exists).
# Push the left child of the popped item to the stack (if it exists).
# Repeat until the stack is empty.
# Here's the code for iterative preorder traversal:



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def iterative_preorder(self, root_node):
        if root_node is None:
            return None
        
        stack = Stack()
        stack.append(root_node)
        result = []

        while not stack.is_empty():
            out_node = stack.pop()
            result.append(out_node.data)

            if out_node.right:
                stack.append(out_node.right)

            if out_node.left:
                stack.append(out_node.left)

        return result

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.root.right.left = Node(6)
bi.root.right.right = Node(7)

print(bi.iterative_preorder(bi.root))  # Output: [1, 2, 4, 5, 3, 6, 7]







## Iterative Preorder Traversal (Space Optimized)








# An iterative preorder traversal can be further optimized to use less space by using a single stack. The key idea is to handle the nodes in such a way that you don't push the left child onto the stack if it can be handled immediately. Here’s how you can achieve this:

# Iterative Preorder Traversal (Space Optimized)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def iterative_preorder_space_optimized(self, root_node):
        if root_node is None:
            return None
        
        stack = Stack()
        stack.append(root_node)
        result = []

        while not stack.is_empty():
            while root_node:
                result.append(root_node.data)
                if root_node.right:
                    stack.append(root_node.right)
                root_node = root_node.left

            if not stack.is_empty():
                root_node = stack.pop()

        return result

# Example usage:
bi = BinaryTree(1)
bi.root.left = Node(2)
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.root.right.left = Node(6)
bi.root.right.right = Node(7)

print(bi.iterative_preorder_space_optimized(bi.root))  # Output: [1, 2, 4, 5, 3, 6, 7]


# Explanation:
# Node Class: Defines a binary tree node with left and right children.

# Stack Class: Manages stack operations.

# BinaryTree Class:

# Initialization: Initializes the tree with a root node.

# iterative_preorder_space_optimized Method: Performs iterative preorder traversal with optimized space usage.

# Traversal:

# If root_node is not None, initialize the stack with the root node.
# While the stack is not empty:
# Traverse the left children of the nodes directly, appending their data to the result list and pushing their right children (if any) onto the stack.
# Once a left child is None, pop the next node from the stack and continue the process.
# Return the result list containing the preorder traversal of the tree.
# Example Usage: Demonstrates creating a binary tree and calling the iterative_preorder_space_optimized method, which prints the nodes in preorder sequence.

# This space-optimized implementation minimizes the number of nodes held in the stack at any time, thereby reducing the overall space complexity.











## Whole Binary Tree and above code and topics in a nutshell 










class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def is_empty(self):
        return len(self.queue) == 0

    def get(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def inorder(self, root_node):
        if root_node:
            self.inorder(root_node.left)
            print(root_node.data, end=' -> ')
            self.inorder(root_node.right)

    def preorder(self, root_node):
        if root_node:
            print(root_node.data, end=' -> ')
            self.preorder(root_node.left)
            self.preorder(root_node.right)

    def postorder(self, root_node):
        if root_node:
            self.postorder(root_node.left)
            self.postorder(root_node.right)
            print(root_node.data, end=' -> ')

    def level_order(self, root_node):
        if root_node is None:
            return None
        
        queue = Queue()
        queue.put(root_node)
        final_list = []

        while not queue.is_empty():
            out_node = queue.get()
            final_list.append(out_node.data)

            if out_node.left:
                queue.put(out_node.left)
            if out_node.right:
                queue.put(out_node.right)
            
        return final_list
    
    def reverse_level_order(self, root_node):
        if root_node is None:
            return None
        
        queue = Queue()
        stack = Stack()

        final_list = []

        queue.put(root_node)

        while not queue.is_empty():
            out_node = queue.get()

            if out_node.right:
                queue.put(out_node.right)

            if out_node.left:
                queue.put(out_node.left)

            stack.append(out_node)

        while not stack.is_empty():
            final_list.append(stack.pop().data)

        
        return final_list
    
    def recursive_height_of_tree(self, root_node):
        if root_node is None:
            return -1
        
        left_tree = self.recursive_height_of_tree(root_node.left)
        right_tree = self.recursive_height_of_tree(root_node.right)

        return 1 + max(left_tree, right_tree)
    
    def recursive_size_of_tree(self, root_node):
        if root_node is None:
            return 0
        
        left_tree = self.recursive_size_of_tree(root_node.left)
        right_tree = self.recursive_size_of_tree(root_node.right)

        return 1 + (left_tree + right_tree)

    def print_nodes_at_k_distance(self, root_node, k):
        if root_node is None:
            return None
        
        if k == 0:
            print(root_node.data, end='')
            return 
        
        self.print_nodes_at_k_distance(root_node.left, k-1)
        self.print_nodes_at_k_distance(root_node.right, k-1)

    def iterative_inorder(self, root_node):
        stack = Stack()
        result = []

        while True:
            if root_node is not None:
                stack.append(root_node)
                root_node = root_node.left
            elif not stack.is_empty():
                root_node = stack.pop()
                result.append(root_node.data)
                root_node = root_node.right
            else:
                break

        return result
    
    def iterative_preorder(self, root_node):
        if root_node is None:
            return None
        
        stack = Stack()
        stack.append(root_node)
        result = []

        while not stack.is_empty():
            out_node = stack.pop()
            result.append(out_node.data)

            if out_node.right:
                stack.append(out_node.right)

            if out_node.left:
                stack.append(out_node.left)

        return result
    
    def iterative_preorder_space_optimized(self, root_node):
        if root_node is None:
            return None
        
        stack = Stack()
        stack.append(root_node)
        result = []

        while not stack.is_empty():
            while root_node:
                result.append(root_node.data)
                if root_node.right:
                    stack.append(root_node.right)
                root_node = root_node.left

            if not stack.is_empty():
                root_node = stack.pop()

        return result

            

bi = BinaryTree(1)
bi.root.left = Node(2) 
bi.root.right = Node(3)
bi.root.left.left = Node(4)
bi.root.left.right = Node(5)
bi.inorder(bi.root)
print('')
bi.preorder(bi.root)
print('')
bi.postorder(bi.root)
print('')
print(bi.level_order(bi.root))
print(bi.reverse_level_order(bi.root))
print(bi.recursive_height_of_tree(bi.root))
print(bi.recursive_size_of_tree(bi.root))
k = 2
bi.print_nodes_at_k_distance(bi.root, k)
print(bi.iterative_inorder(bi.root))
print(bi.iterative_preorder(bi.root))
print(bi.iterative_preorder_space_optimized(bi.root)) 
