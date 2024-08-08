
## Imp: 

# Prerequisites

# Before diving into this section, it's crucial that you have a solid understanding of Binary Search Trees (BST) and all the associated methods. Only then should you proceed.

# Learning Resources

# I couldn't find a YouTube video as good as the previous ones, but I've compiled some resources and done my best to explain and break down the code clearly for you.

# YT videos: ( https://www.youtube.com/watch?v=DB1HFCEdLxA ) ( https://www.youtube.com/watch?v=JPI-DPizQYk&t=1s )



# Important:


# I anticipate that many people might find the rotation of AVL trees challenging. To help with this, I've included a section titled "Help Regarding Rotation" that thoroughly explains rotations and how they work. This should clear up any doubts you may have! ( See end of this file )










##  Self-Balancing BST: AVL Tree



# An AVL tree is a type of self-balancing binary search tree named after its inventors, Adelson-Velsky and Landis. The AVL tree maintains its height balance by performing rotations during insertions and deletions, ensuring that the difference in height between the left and right subtrees of any node is at most 1.

# Key Properties


# Height Balance: For any node in the tree, the height difference (balance factor) between its left and right subtrees is at most 1.
# Rotations: The tree uses rotations to maintain balance after insertions and deletions.



# Rotations


# Single Rotations:
# Right Rotation (RR): Used to balance a left-heavy subtree.
# Left Rotation (LR): Used to balance a right-heavy subtree.

# Double Rotations:
# Left-Right Rotation (LR): A combination of a left rotation followed by a right rotation, used to balance a left-right-heavy subtree.

# Right-Left Rotation (RL): A combination of a right rotation followed by a left rotation, used to balance a right-left-heavy subtree.





## Explanation of Rotations in the Code:




# Left-Left (LL) Case: This happens when the balance factor is greater than 1 and the new data is less than the left child's data. We perform a right rotation around the root node.

# Right-Right (RR) Case: This happens when the balance factor is less than -1 and the new data is greater than the right child's data. We perform a left rotation around the root node.

# Left-Right (LR) Case: This happens when the balance factor is greater than 1 and the new data is greater than the left child's data. We first perform a left rotation on the left child and then a right rotation on the root node.

# Right-Left (RL) Case: This happens when the balance factor is less than -1 and the new data is less than the right child's data. We first perform a right rotation on the right child and then a left rotation on the root node.






# Real-Life Usage of AVL Trees


# Databases: AVL trees are used in database indexing to ensure efficient data retrieval.
# File Systems: They help in managing file systems, where quick lookup, insertion, and deletion of files are required.
# Network Routers: Used in routing tables for efficiently finding paths in networks.
# Compiler Design: Used in syntax trees to maintain the hierarchical structure of parsed code.
# Gaming: For managing objects that frequently change positions.




# Code Explanation











# Tip:



# In Code A, you'll see the standard way people typically write an AVL tree. In Code B, I've simply changed the variable names to make it easier to understand what each line of code is doing. You can use either one—choose whichever you're more comfortable with!




## Code A: 


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root_node, data):
        # Base case: If the root is None, create a new node and return it
        if root_node is None:
            return Node(data)
        
        # Recursive case: Insert the data in the left or right subtree
        if data < root_node.data:
            root_node.left = self.insert(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self.insert(root_node.right, data)
        else:
            # Duplicate data is not allowed in AVL tree
            return root_node
        
        # Update the height of the ancestor node
        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        # Get the balance factor of the ancestor node to check whether this node became unbalanced
        balance = self.get_balance(root_node)

        # If the node is unbalanced, then there are 4 cases to handle:

        # Left-Left (LL) Case
        if balance > 1 and data < root_node.left.data:
            return self.right_rotation(root_node)
        
        # Right-Right (RR) Case
        if balance < -1 and data > root_node.right.data:
            return self.left_rotation(root_node)
        
        # Left-Right (LR) Case
        if balance > 1 and data > root_node.left.data:
            root_node.left = self.left_rotation(root_node.left)
            return self.right_rotation(root_node)
        
        # Right-Left (RL) Case
        if balance < -1 and data < root_node.right.data:
            root_node.right = self.right_rotation(root_node.right)
            return self.left_rotation(root_node)

        # Return the (unchanged) node pointer
        return root_node
        
    def left_rotation(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotation(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root):
        if root:
            print(f"{root.data} ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)

# Usage
avl = AVLTree()
root_node = None

elements = [30, 20, 10]
for elem in elements:
    root_node = avl.insert(root_node, elem)

print("Pre-order traversal of the constructed AVL tree is:")
avl.pre_order(root_node)  # Output: 20 10 30
print("\n")


# Let's break down the insertion and rotation step-by-step using the AVL tree:

# Step-by-Step Insertion and Rotation

# Insert 30:

# root_node is None.
# Insert 30 as the root node.

#  30
# /  \




# Insert 20:

# root_node is 30.
# 20 is less than 30, so we insert 20 as the left child of 30.

#   30
#  /
# 20



# Insert 10:

# root_node is 30.
# 10 is less than 30, so we move to the left child of 30 (which is 20).
# 10 is less than 20, so we insert 10 as the left child of 20.


#     30
#    /
#   20
#  /
# 10


# ### Detecting Imbalance and Performing Rotation

# At this point, the tree is unbalanced with a left-left (LL) case, and we need to perform a right rotation around `30` to balance the tree. Let's see how this is done:

# #### Right Rotation on 30:

# Before rotation:

#     30
#    /
#   20
#  /
# 10



# **Right Rotation Steps:**

# 1. **Identify nodes**: `z = 30`, `y = 20`, and `T3 = None`.
# 2. **Perform rotation**:
#    - `y.right` becomes `z`.
#    - `z.left` becomes `T3`.

# After rotation:


#  20
# /  \
# 10 30








## Full AVL Tree Implementation with Delete, Floor, and Ceiling Methods








class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root_node, data):
        if root_node is None:
            return Node(data)
        
        if data < root_node.data:
            root_node.left = self.insert(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self.insert(root_node.right, data)
        else:
            return root_node
        
        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        balance = self.get_balance(root_node)

        if balance > 1 and data < root_node.left.data:
            return self.right_rotation(root_node)
        
        if balance < -1 and data > root_node.right.data:
            return self.left_rotation(root_node)
        
        if balance > 1 and data > root_node.left.data:
            root_node.left = self.left_rotation(root_node.left)
            return self.right_rotation(root_node)
        
        if balance < -1 and data < root_node.right.data:
            root_node.right = self.right_rotation(root_node.right)
            return self.left_rotation(root_node)
        
        return root_node

    def delete(self, root_node, data):
        if not root_node:
            return root_node
        
        if data < root_node.data:
            root_node.left = self.delete(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self.delete(root_node.right, data)
        else:
            if root_node.left is None:
                return root_node.right
            elif root_node.right is None:
                return root_node.left

            temp = self.get_min_value_node(root_node.right)
            root_node.data = temp.data
            root_node.right = self.delete(root_node.right, temp.data)

        if root_node is None:
            return root_node

        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        balance = self.get_balance(root_node)

        if balance > 1 and self.get_balance(root_node.left) >= 0:
            return self.right_rotation(root_node)
        
        if balance > 1 and self.get_balance(root_node.left) < 0:
            root_node.left = self.left_rotation(root_node.left)
            return self.right_rotation(root_node)
        
        if balance < -1 and self.get_balance(root_node.right) <= 0:
            return self.left_rotation(root_node)
        
        if balance < -1 and self.get_balance(root_node.right) > 0:
            root_node.right = self.right_rotation(root_node.right)
            return self.left_rotation(root_node)

        return root_node

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)
    
    def floor(self, root_node, data):
        if root_node is None:
            return None
        
        if data == root_node.data:
            return root_node.data
        
        if data < root_node.data:
            return self.floor(root_node.left, data)
        
        floor_value = self.floor(root_node.right, data)
        return floor_value if floor_value is not None else root_node.data
    
    def ceiling(self, root_node, data):
        if root_node is None:
            return None
        
        if data == root_node.data:
            return root_node.data
        
        if data > root_node.data:
            return self.ceiling(root_node.right, data)
        
        ceiling_value = self.ceiling(root_node.left, data)
        return ceiling_value if ceiling_value is not None else root_node.data
    
    def left_rotation(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotation(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root):
        if root:
            print(f"{root.data} ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)

# Usage
avl = AVLTree()
root_node = None

elements = [10, 20, 30, 40, 50, 25, 60]
for elem in elements:
    root_node = avl.insert(root_node, elem)

print("Pre-order traversal of the constructed AVL tree is:")
avl.pre_order(root_node)  # Expected Output: 30 20 10 25 50 40 60
print("\n")


root_node = avl.delete(root_node, 20)
print("Pre-order traversal after deleting 20:")
avl.pre_order(root_node)  # Expected Output: 30 25 10 50 40 60
print("\n")

# floor and ceiling methods
floor_value = avl.floor(root_node, 27)
ceiling_value = avl.ceiling(root_node, 27)
print(f"Floor of 25: {floor_value}")  # Output: 25
print(f"Ceiling of 25: {ceiling_value}")  # Output: 30



# Let's break down the delete method step-by-step to understand how it works and maintains the AVL tree properties.



# Full delete Method




def delete(self, root_node, data):
    # Step 1: Perform standard BST delete
    if not root_node:
        return root_node
    
    if data < root_node.data:
        root_node.left = self.delete(root_node.left, data)
    elif data > root_node.data:
        root_node.right = self.delete(root_node.right, data)
    else:
        # Node with only one child or no child
        if root_node.left is None:
            return root_node.right
        elif root_node.right is None:
            return root_node.left
        
        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = self.get_min_value_node(root_node.right)
        
        # Copy the inorder successor's data to this node
        root_node.data = temp.data
        
        # Delete the inorder successor
        root_node.right = self.delete(root_node.right, temp.data)

    # If the tree had only one node then return
    if root_node is None:
        return root_node

    # Step 2: Update height of the current node
    root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

    # Step 3: Get the balance factor of this node (to check whether this node became unbalanced)
    balance = self.get_balance(root_node)

    # Step 4: If this node becomes unbalanced, then there are 4 cases

    # Left Left Case
    if balance > 1 and self.get_balance(root_node.left) >= 0:
        return self.right_rotation(root_node)

    # Left Right Case
    if balance > 1 and self.get_balance(root_node.left) < 0:
        root_node.left = self.left_rotation(root_node.left)
        return self.right_rotation(root_node)

    # Right Right Case
    if balance < -1 and self.get_balance(root_node.right) <= 0:
        return self.left_rotation(root_node)

    # Right Left Case
    if balance < -1 and self.get_balance(root_node.right) > 0:
        root_node.right = self.right_rotation(root_node.right)
        return self.left_rotation(root_node)

    return root_node



# Detailed Explanation


# Step 1: Standard BST Delete
# Base Case:


# if not root_node:
#     return root_node


# If the node to be deleted is not found, return None.



# Recursive Deletion:


# if data < root_node.data:
#     root_node.left = self.delete(root_node.left, data)
# elif data > root_node.data:
#     root_node.right = self.delete(root_node.right, data)


# If the data to be deleted is smaller than the root's data, go to the left subtree.
# If the data to be deleted is greater than the root's data, go to the right subtree.


# Node to be Deleted Found:


# else:
#     if root_node.left is None:
#         return root_node.right
#     elif root_node.right is None:
#         return root_node.left
    
#     temp = self.get_min_value_node(root_node.right)
#     root_node.data = temp.data
#     root_node.right = self.delete(root_node.right, temp.data)


# If the node has only one child or no children:
# If it has no left child, replace it with its right child.
# If it has no right child, replace it with its left child.


# If the node has two children:

# Find the inorder successor (the smallest node in the right subtree).
# Replace the node's data with the inorder successor's data.
# Delete the inorder successor.


# Step 2: Update the Height

# root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))
# Update the height of the current node.


# Step 3: Get the Balance Factor

# balance = self.get_balance(root_node)
# Get the balance factor to check if the node has become unbalanced.


# Step 4: Balance the Tree (4 Cases)


# Left Left Case:


# if balance > 1 and self.get_balance(root_node.left) >= 0:
#     return self.right_rotation(root_node)

# If the node is left-heavy and the left subtree is balanced or left-heavy, perform a right rotation.



# Left Right Case:


# if balance > 1 and self.get_balance(root_node.left) < 0:
#     root_node.left = self.left_rotation(root_node.left)
#     return self.right_rotation(root_node)

# If the node is left-heavy and the left subtree is right-heavy, perform a left rotation on the left child followed by a right rotation on the node.



# Right Right Case:


# if balance < -1 and self.get_balance(root_node.right) <= 0:
#     return self.left_rotation(root_node)

# If the node is right-heavy and the right subtree is balanced or right-heavy, perform a left rotation.



# Right Left Case:


# if balance < -1 and self.get_balance(root_node.right) > 0:
#     root_node.right = self.right_rotation(root_node.right)
#     return self.left_rotation(root_node)


# If the node is right-heavy and the right subtree is left-heavy, perform a right rotation on the right child followed by a left rotation on the node.


# Helper Methods


# Get Minimum Value Node:


# def get_min_value_node(self, node):
#     if node is None or node.left is None:
#         return node
#     return self.get_min_value_node(node.left)


# Finds the node with the smallest value in a subtree (inorder successor).



# Get Height:


# def get_height(self, node):
#     if not node:
#         return 0
#     return node.height


# Returns the height of a node.



# Get Balance:


# def get_balance(self, node):
#     if not node:
#         return 0
#     return self.get_height(node.left) - self.get_height(node.right)


# Returns the balance factor of a node.



# Left Rotation:


# def left_rotation(self, z):
#     y = z.right
#     T2 = y.left

#     y.left = z
#     z.right = T2

#     z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
#     y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

#     return y


# Performs a left rotation around a node to maintain balance.



# Right Rotation:


# def right_rotation(self, z):
#     y = z.left
#     T3 = y.right

#     y.right = z
#     z.left = T3

#     z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
#     y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

#     return y



# Performs a right rotation around a node to maintain balance.



# Summary



# The delete method works by first performing a standard binary search tree deletion, which involves finding and removing the node with the given data. If the node has two children, it replaces the node's data with the inorder successor's data and deletes the inorder successor.

# After deletion, the method updates the height of the affected nodes and checks their balance factors. If a node is found to be unbalanced, it performs the necessary rotations to restore the AVL tree properties.

# The helper methods (get_min_value_node, get_height, get_balance, left_rotation, and right_rotation) assist in these operations, ensuring the tree remains balanced after deletions.



## Code B:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root_node, data):
        if root_node is None:
            return Node(data)
        
        if data < root_node.data:
            root_node.left = self.insert(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self.insert(root_node.right, data)
        else:
            return root_node
        
        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        balance = self.get_balance(root_node)

        if balance > 1 and data < root_node.left.data:
            return self.right_rotation(root_node)
        
        if balance < -1 and data > root_node.right.data:
            return self.left_rotation(root_node)
        
        if balance > 1 and data > root_node.left.data:
            root_node.left = self.left_rotation(root_node.left)
            return self.right_rotation(root_node)
        
        if balance < -1 and data < root_node.right.data:
            root_node.right = self.right_rotation(root_node.right)
            return self.left_rotation(root_node)
        
        return root_node
    
    def delete(self, root_node, data):
        if root_node is None:
            return None
        
        if data < root_node.data:
            root_node.left = self.delete(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self.delete(root_node.right, data)
        else:
            if root_node.left is None:
                return root_node.right
            elif root_node.right is None:
                return root_node.left
            else:
                temp = self.get_min_right_val(root_node.right)
                root_node.data = temp.data
                root_node.right = self.delete(root_node.right, temp.data)

        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        balance = self.get_balance(root_node)

        if balance > 1 and self.get_balance(root_node.left) <= 0:
            return self.right_rotation(root_node)
        
        if balance < -1 and self.get_balance(root_node.right) >= 0:
            return self.left_rotation(root_node)
        
        if balance > 1 and self.get_balance(root_node.left) > 0:
            root_node.left = self.left_rotation(root_node.left)
            return self.right_rotation(root_node)
        
        if balance < -1 and self.get_balance(root_node.right) < 0:
            root_node.right = self.right_rotation(root_node.right)
            return self.left_rotation(root_node)
        
        return root_node

    def get_min_right_val(self, root_node):
        current = root_node
        while current.left is not None:
            current = current.left
        return current
        
    def left_rotation(self, root_node):
        new_root = root_node.right
        new_root_left = new_root.left

        new_root.left = root_node
        root_node.right = new_root_left

        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root
        
    def right_rotation(self, root_node):
        new_root = root_node.left
        new_root_right = new_root.right

        new_root.right = root_node
        root_node.left = new_root_right

        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def get_height(self, root_node):
        if root_node is None:
            return 0
        return root_node.height
    
    def get_balance(self, root_node):
        if root_node is None:
            return 0
        return self.get_height(root_node.left) - self.get_height(root_node.right)
    
    def floor(self, root_node, data):
        if root_node is None:
            return root_node
        
        if data == root_node.data:
            return root_node.data
        
        if data < root_node.data:
            return self.floor(root_node.left, data)
        
        floor_value = self.floor(root_node.right, data)
        return floor_value if floor_value is not None else root_node.data
    
    def ceiling(self, root_node, data):
        if root_node is None:
            return root_node
        
        if data == root_node.data:
            return root_node.data
        
        if data > root_node.data:
            return self.ceiling(root_node.right, data)
        
        ceiling_val = self.ceiling(root_node.left, data)
        return ceiling_val if ceiling_val is not None else root_node.data
    
    def pre_order(self, root_node):
        if root_node:
            print(root_node.data, end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)


avl = AVLTree()
root = None

elements = [10, 20, 30, 40, 50, 25, 60]
# elements = [10, 20, 30, 40]
for elem in elements:
    root = avl.insert(root, elem)

print("Pre-order traversal of the constructed AVL tree is:")
avl.pre_order(root) # 30 20 10 25 50 40 60
print("\n")

root = avl.delete(root, 20)
print("Pre-order traversal after deleting 20:")
avl.pre_order(root)  # 30 25 10 50 40 60
print("\n")

floor_value = avl.floor(root, 27)
ceiling_value = avl.ceiling(root, 27)
print(f"Floor of 25: {floor_value}")  # Output: 25
print(f"Ceiling of 25: {ceiling_value}")  # Output: 30



# Code Explanation
# Here is a comprehensive implementation of an AVL tree with detailed explanations of each line of code.

# Node Class



# class Node:
#     def __init__(self, data):
#         self.data = data  # The value stored in the node.
#         self.left = None  # Pointer to the left child.
#         self.right = None  # Pointer to the right child.
#         self.height = 1  # Height of the node for balancing purposes.


# Node class: Represents each node in the AVL tree.

# Attributes:
# data: The value stored in the node.
# left: Pointer to the left child node.
# right: Pointer to the right child node.
# height: The height of the node, used to keep the tree balanced.



# AVLTree Class



class AVLTree:
    def insert(self, root_node, data):
        if root_node is None:
            return Node(data)  # Create a new node if the tree is empty.

        if data < root_node.data:
            root_node.left = self.insert(root_node.left, data)  # Insert into the left subtree.
        elif data > root_node.data:
            root_node.right = self.insert(root_node.right, data)  # Insert into the right subtree.
        else:
            return root_node  # Duplicate data are not allowed.

        # Update the height of the current node.
        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))

        # Get the balance factor to check if the node is unbalanced.
        balance = self.get_balance(root_node)

        # Left Left Case
        if balance > 1 and data < root_node.left.data:
            return self.right_rotation(root_node)

        # Right Right Case
        if balance < -1 and data > root_node.right.data:
            return self.left_rotation(root_node)

        # Left Right Case
        if balance > 1 and data > root_node.left.data:
            root_node.left = self.left_rotation(root_node.left)
            return self.right_rotation(root_node)

        # Right Left Case
        if balance < -1 and data < root_node.right.data:
            root_node.right = self.right_rotation(root_node.right)
            return self.left_rotation(root_node)

        return root_node  # Return the (unchanged) node pointer.
    

# insert method:


# Inserts a new node with data into the AVL tree.
# Checks if the current node is None and creates a new node if so.
# Recursively inserts the data into the left or right subtree.
# Updates the height of the current node.
# Checks the balance factor of the current node to determine if it is unbalanced.
# Performs rotations (left, right, left-right, or right-left) to rebalance the tree.


# Rotation Methods



    def left_rotation(self, root_node):
        new_root = root_node.right  # The new root will be the right child.
        new_root_left = new_root.left  # The left subtree of the new root.

        new_root.left = root_node  # The current root becomes the left child of the new root.
        root_node.right = new_root_left  # Update the right subtree of the old root.

        # Update heights.
        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root  # Return the new root.

    def right_rotation(self, root_node):
        new_root = root_node.left  # The new root will be the left child.
        new_root_right = new_root.right  # The right subtree of the new root.

        new_root.right = root_node  # The current root becomes the right child of the new root.
        root_node.left = new_root_right  # Update the left subtree of the old root.

        # Update heights.
        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root  # Return the new root.
    

# left_rotation method:

# Performs a left rotation to rebalance the tree.
# Updates the parent and child pointers to reflect the rotation.
# Updates the heights of the nodes involved in the rotation.
# Returns the new root of the subtree.



# right_rotation method:

# Performs a right rotation to rebalance the tree.
# Updates the parent and child pointers to reflect the rotation.
# Updates the heights of the nodes involved in the rotation.
# Returns the new root of the subtree.



# Utility Methods



    def get_height(self, root_node):
        if root_node is None:
            return 0  # The height of a non-existent node is 0.
        return root_node.height  # Return the height of the node.

    def get_balance(self, root_node):
        if root_node is None:
            return 0  # The balance factor of a non-existent node is 0.
        return self.get_height(root_node.left) - self.get_height(root_node.right)  # Balance factor.
    

# get_height method:

# Returns the height of the node.
# If the node is None, returns 0.
# get_balance method:

# Returns the balance factor of the node.
# The balance factor is the difference between the heights of the left and right subtrees.



# Pre-order Traversal Method



    def pre_order(self, root_node):
        if root_node:
            print(root_node.data, end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)


# pre_order method:


# Performs a pre-order traversal of the AVL tree.
# Visits the current node, then the left subtree, and finally the right subtree.
# Prints the data of the nodes.


# Example Usage



avl = AVLTree()
root = None

elements = [10, 20, 30, 40, 50, 25, 60]
for elem in elements:
    root = avl.insert(root, elem)

print("Pre-order traversal of the constructed AVL tree is:")
avl.pre_order(root)  # Output: 30 -> 20 -> 10 -> 25 -> 50 -> 40 -> 60
print("\n")

root = avl.delete(root, 20)
print("Pre-order traversal after deleting 20:")
avl.pre_order(root)  # Output: 30 -> 25 -> 10 -> 50 -> 40 -> 60
print("\n")


# Insertion and Deletion:



# Inserts the elements [10, 20, 30, 40, 50, 25, 60] into the AVL tree.
# Performs a pre-order traversal to print the tree.
# Deletes the node with value 20 and prints the tree again after deletion.


# Time and Space Complexity


# Time Complexity:
# Insertion, Deletion, Search: O(log n) due to the balanced nature of the AVL tree.
# Rotation Operations: O(1), since they only involve a constant number of node reassignments and height updates.


# Space Complexity:
# O(n) due to the storage of n nodes.















## Help Regarding Rotation



# ( I've provided explanations in both simple and accurate terms. The simple explanation gives you a general idea of how rotations work, which can help with initial understanding. Once you're comfortable with that basic concept, you can refer to the more accurate explanation to grasp the precise details and implementation. This approach will ensure you have both a conceptual and technical understanding of AVL tree rotations. )








# In an AVL tree, to maintain the balance property (the difference in heights between the left and right subtrees is at most 1), rotations are used. There are four types of rotations:

# Right Rotation (LL Rotation)
# Left Rotation (RR Rotation)
# Left-Right Rotation (LR Rotation)
# Right-Left Rotation (RL Rotation)



# 1. Right Rotation (LL Rotation)
# This rotation is performed when there is a left-heavy subtree.

# Example:
# Consider the following tree, where the node 10 is unbalanced due to the left-heavy subtree:


#        10
#       /  
#      5   
#     /    
#    2     



# Right Rotation:

# The left child (5) becomes the new root.
# The original root (10) becomes the right child of the new root.
# The right subtree of the new root (if any) becomes the left subtree of the original root.



# Before Rotation:            After Right Rotation:
#        10                           5
#       /                            / \
#      5                            2   10
#     /     
#    2   





##  Simplified Explanation:




# In simple terms, we're performing a right rotation because the left subtree is unbalanced. Let's walk through the process:

# Identifying the Imbalance:
# We start by checking the balance factor of each node. The node with data 2 is balanced, and so is the node with data 5. However, the root node 10 is not balanced because its balance factor is too high.

# Why Rotate the Root Node (10)?
# We rotate the root node 10 to correct the imbalance.

# The Rotation Process:
# Think of it like this: we take the middle element, which is 5, and promote it to become the new root node. The original root node 10 is then moved down to the right side to fill the empty space.

# General Rule:
# This approach applies to left rotations as well, but in the opposite direction. The key idea is to always make the middle element (in this case, 5) the new root node to keep the tree balanced.

# While this explanation isn't perfectly precise, it should give you a good idea of how rotations work and help you start understanding AVL trees more quickly.






# Accurate terms


# When an AVL tree becomes unbalanced, we use rotations to fix it. Here’s a simple way to understand the right rotation:

# Identifying the Imbalance:

# In an AVL tree, each node has a balance factor, which is the height difference between its left and right subtrees.
# If the balance factor is too high (greater than 1), it means the left subtree is too heavy. If it's too low (less than -1), the right subtree is too heavy.
# Right Rotation Explained:

# Imagine you have a tree where the left side is too tall, like this:


#     10
#    /
#   5
#  /
# 2


# To fix this imbalance, we perform a right rotation. Here's how it works:

# Step 1: Take the left child of the root (which is 5) and make it the new root of the subtree.
# Step 2: Move the original root (10) down to become the right child of the new root (5).
# Step 3: The new root (5) will have 2 as its left child and 10 as its right child.
# After the right rotation, the tree looks like this:


#     5
#    / \
#   2   10


# This rotation helps balance the tree by making the new root (5) the center of the subtree, which corrects the height imbalance.

# Left Rotation:

# The same idea applies in reverse for left rotations, which are used when the right subtree is too tall.
# In essence, rotations in AVL trees help us keep the tree balanced and efficient by adjusting the positions of nodes. The goal is to ensure that no subtree is too tall compared to its sibling.







# Code:


def right_rotation(self, root_node):
    new_root = root_node.left
    root_node.left = new_root.right
    new_root.right = root_node

    # Update heights
    root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))
    new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

    return new_root




# 2. Left Rotation (RR Rotation)
# This rotation is performed when there is a right-heavy subtree.

# Example:
# Consider the following tree, where the node 10 is unbalanced due to the right-heavy subtree:


#     10
#       \
#        15
#          \
#           20



# Left Rotation:

# The right child (15) becomes the new root.
# The original root (10) becomes the left child of the new root.
# The left subtree of the new root (if any) becomes the right subtree of the original root.



# Before Rotation:            After Left Rotation:
#        10                          15
#          \                        /  \
#          15                      10   20
#            \        
#             20  
# 
#    
# Code:


def left_rotation(self, root_node):
    new_root = root_node.right
    root_node.right = new_root.left
    new_root.left = root_node

    # Update heights
    root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))
    new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

    return new_root



# 3. Left-Right Rotation (LR Rotation)
# This rotation is performed when there is a left-heavy subtree with a right-heavy child.

# Example:
# Consider the following tree:


#        10
#       /  
#      5   
#       \    
#        8



# Left-Right Rotation:

# First, perform a left rotation on the left child (5).
# Then, perform a right rotation on the root (10).



# Before Rotation:             After Left Rotation:          After Right Rotation:
#        10                           10                          8
#       /                            /                           / \
#      5                            8                           5  10
#       \                          / 
#        8                        5
# 
#                    
# Code:


def left_right_rotation(self, root_node):
    root_node.left = self.left_rotation(root_node.left)
    return self.right_rotation(root_node)


# 4. Right-Left Rotation (RL Rotation)
# This rotation is performed when there is a right-heavy subtree with a left-heavy child.

# Example:
# Consider the following tree:


#     10
#       \
#        15
#       /  
#      12


# Right-Left Rotation:

# First, perform a right rotation on the right child (15).
# Then, perform a left rotation on the root (10).



# Before Rotation:             After Right Rotation:          After Left Rotation:
#        10                            10                            12
#          \                            \                          /  \
#          15                           12                        10   15
#         /                              \        
#        12                              15

# Code: 

def right_left_rotation(self, root_node):
    root_node.right = self.right_rotation(root_node.right)
    return self.left_rotation(root_node)






# Final Visual Representation







# Insert 10:
#     10



# Insert 20:
#     10
#       \
#       20




# Insert 30 (RR Rotation on 10):
#       20
#      /  \
#     10   30




# Insert 40:
#       20
#      /  \
#     10   30
#             \
#             40




# Insert 50 (RR Rotation on 30):
#       20
#      /  \
#     10   40
#          /  \
#         30   50




# Insert 25 (RL Rotation on 40):
#       20
#      /  \
#     10   30
#             \
#             40
#             /  \
#            25   50





# Insert 60 (RR Rotation on 30):
#       30
#      /  \
#     20   50
#    /  \   /
#   10   25 40
#            \
#            60



## Now you can start Red Black Tree 😊




