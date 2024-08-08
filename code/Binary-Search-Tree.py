
## Imp: 

# To better understand Binary Search Trees (BST), I recommend watching this YouTube video: ( https://www.youtube.com/watch?v=yC83Kp2xig8&list=PL5tcWHG-UPH1ZOv2_rWkFVc7CCoGaa8je ). While the video doesn't cover every topic, it provides a solid foundation to help you grasp the key concepts.

# Note on Self-Balancing BSTs
# BSTs also include the topic of Self-Balancing Trees, such as AVL Trees and Red-Black Trees. These are more complex topics, so I've separated them into another file for you to study at your own pace. Don’t skip them—they’re both important! 😭


# As always you can find all methods in a nutshell code ( Visit last code which is Code B )




# 16.1 Introduction to Binary Search Tree (BST)






# A Binary Search Tree (BST) is a data structure that facilitates fast lookup, addition, and removal of items. Each node in a BST has at most two children. The key properties of a BST are:

# The left subtree of a node contains only nodes with values less than the node's value.
# The right subtree of a node contains only nodes with values greater than the node's value.
# Both the left and right subtrees must also be binary search trees.
# Real-life Usage:
# Databases: To maintain and quickly access a sorted set of records.
# File systems: For managing file hierarchy.
# Autocompletion: To quickly find suggestions for typed text.







## 16.3 BST Insert in Python






# Inserting a value into a BST involves traversing the tree to find the correct spot for the new value. The value is added as a leaf node in the appropriate position to maintain the BST property.

# Code Example:



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root_node, data):
        if data < root_node.data:
            if root_node.left:
                self._insert(root_node.left, data)
            else:
                root_node.left = Node(data)
        elif data > root_node.data:
            if root_node.right:
                self._insert(root_node.right, data)
            else:
                root_node.right = Node(data)
        else:
            print('Data already exists in the BST')

# Usage
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)





## 16.2 Search in BST in Python





# To search for a value in a BST, you start from the root and compare the target value with the current node’s value. Based on the comparison, you either move to the left or right subtree, continuing until you find the target value or reach a leaf node.



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root_node, data):
        if data < root_node.data:
            if root_node.left:
                self._insert(root_node.left, data)
            else:
                root_node.left = Node(data)
        elif data > root_node.data:
            if root_node.right:
                self._insert(root_node.right, data)
            else:
                root_node.right = Node(data)
        else:
            print('Data already exists in the BST')

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root_node, data):
        # Base case: root_node is None or the data is present at the root
        if root_node is None or root_node.data == data:
            return root_node

        # Data is greater than root_node's data
        if data > root_node.data:
            return self._search(root_node.right, data)

        # Data is smaller than root_node's data
        return self._search(root_node.left, data)

# Usage
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

result = bst.search(6)
if result:
    print(f"Found: {result.data}")
else:
    print("Not Found")






## 16.4 BST Delete in Python







# Deleting a node in a BST is more complex than searching or inserting because it requires maintaining the BST properties. There are three cases to consider when deleting a node:


##  Imp: Watch this YT video to understand deletion of a node in BST ( https://www.youtube.com/watch?v=LFzAoJJt92M )





class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root_node, data):
        if data < root_node.data:
            if root_node.left:
                self._insert(root_node.left, data)
            else:
                root_node.left = Node(data)
        elif data > root_node.data:
            if root_node.right:
                self._insert(root_node.right, data)
            else:
                root_node.right = Node(data)
        else:
            print('Data already exists in the BST')

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root_node, data):
        if root_node is None:
            return root_node

        if data < root_node.data:
            root_node.left = self._delete(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self._delete(root_node.right, data)
        else:
            # Node with only one child or no child
            if root_node.left is None:
                return root_node.right
            elif root_node.right is None:
                return root_node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(root_node.right)
            root_node.data = temp.data
            root_node.right = self._delete(root_node.right, temp.data)

        return root_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Usage
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

bst.delete(10)





# Delete Function Breakdown
# The delete function in the BinarySearchTree class is responsible for removing a node with a specified value from the BST. This function handles three main scenarios:

# The node to be deleted is a leaf (no children).
# The node to be deleted has one child.
# The node to be deleted has two children.
# Let's go through the delete method and its helper functions step-by-step:

# Main delete Method


# def delete(self, data):
#     self.root = self._delete(self.root, data)


# Purpose: Initiates the deletion process.
# Logic:
# Calls the helper method _delete, starting from the root of the tree.
# Updates the root node in case the root itself is deleted or changed.
# Helper _delete Method



# def _delete(self, root_node, data):
#     if root_node is None:
#         return root_node
    

# Purpose: Handles the recursive deletion of the node.

# Logic:
# If the root_node is None, the tree is empty or the node wasn't found, so return None.


# if data < root_node.data:
#     root_node.left = self._delete(root_node.left, data)


# Purpose: Navigate to the left subtree if the data to be deleted is smaller than the current node's data.
# Logic:
# Recursively call _delete on the left child.


# Update the left child pointer of the current node with the result of the recursive call.

# elif data > root_node.data:
#     root_node.right = self._delete(root_node.right, data)


# Purpose: Navigate to the right subtree if the data to be deleted is larger than the current node's data.
# Logic:


# Recursively call _delete on the right child.
# Update the right child pointer of the current node with the result of the recursive call.

# else:
#     # Node with only one child or no child
#     if root_node.left is None:
#         return root_node.right
#     elif root_node.right is None:
#         return root_node.left


# Purpose: Handle the case where the node to be deleted is found and it has zero or one child.
# Logic:
# If the node has no left child, return the right child (which may be None if there's no right child).
# If the node has no right child, return the left child (which may be None if there's no left child).

#     # Node with two children: Get the inorder successor
#     temp = self._min_value_node(root_node.right)
#     root_node.data = temp.data
#     root_node.right = self._delete(root_node.right, temp.data)


# Purpose: Handle the case where the node to be deleted has two children.
# Logic:
# Find the inorder successor (smallest node in the right subtree) using the _min_value_node method.
# Replace the data of the current node with the data of the inorder successor.
# Recursively delete the inorder successor in the right subtree (since its data has been copied).

# return root_node


# Purpose: Return the modified subtree root after deletion.
# Logic:
# After handling all the cases and necessary modifications, return the updated root node of the current subtree.


# Helper _min_value_node Method

# def _min_value_node(self, node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current


# Purpose: Find the node with the minimum value in a given subtree.
# Logic:
# Initialize current to the given node.
# Traverse to the leftmost node (since the leftmost node in a BST has the smallest value).
# Return the leftmost node.


# Usage Example

# bst = BinarySearchTree()
# bst.insert(8)
# bst.insert(3)
# bst.insert(10)
# bst.insert(1)
# bst.insert(6)
# bst.insert(9)
# bst.insert(11)

# bst.delete(10)
# Explanation:
# Create a BST and insert multiple values to form the tree.
# Call delete(10) to remove the node with the value 10.
# Visual Example of Deletion
# Consider the BST before deletion:


#       8
#      / \
#     3  10
#    / \   \
#   1   6   11
#          /
#         9
# After calling bst.delete(10), the node with value 10 is deleted, and its inorder successor (node with value 11) replaces it. The tree becomes:


#       8
#      / \
#     3  11
#    / \  /
#   1   6 9
# The code ensures the BST properties are maintained after deletion by properly handling nodes with different child configurations and finding the appropriate replacement node when necessary.









## Read here if you din't understand delete function 










# let's break down the delete function and its logic into simpler terms and use visuals to explain the process better.

# Why Update self.root in delete Method

# When we delete a node in a BST, the structure of the tree can change. In some cases, the root of the tree itself might change. For example, if the root node is deleted and it has two children, the root will be replaced by its inorder successor. To handle such changes, we update self.root to ensure it points to the new root of the tree.

# Understanding Inorder Successor and _min_value_node Function
# When deleting a node with two children, we need to find a replacement for the node to maintain the BST properties. We use the inorder successor for this purpose. The inorder successor of a node is the smallest node in its right subtree.

# Here's a step-by-step breakdown:

# Finding the Inorder Successor:

# Start from the right child of the node to be deleted.
# Move to the leftmost node in this right subtree.
# This leftmost node is the inorder successor because it is the smallest node greater than the node to be deleted.
# Replacing the Node to be Deleted:

# Copy the data of the inorder successor to the node to be deleted.
# Delete the inorder successor node from the right subtree (which is now a duplicate).
# Simplified Explanation with Visuals
# Consider the following BST:


#       8
#      / \
#     3  10
#    / \   \
#   1   6   11
#          /
#         9
# We want to delete the node with value 10.

# Step 1: Find the Inorder Successor

# The right child of 10 is 11.
# The leftmost node in the right subtree of 10 is 11 itself (since 11 has no left child).
# Step 2: Replace the Node to be Deleted

# Replace 10 with 11.
# The tree now temporarily looks like this (with 11 duplicated):

#       8
#      / \
#     3  11
#    / \   \
#   1   6   11
#          /
#         9
# Step 3: Delete the Inorder Successor Node

# Delete the original 11 node from the right subtree.
# The tree now looks like this:

#       8
#      / \
#     3  11
#    / \  /
#   1   6 9
# Detailed Code Explanation
# Here is the detailed explanation of the code with comments:




# def delete(self, data):
#     self.root = self._delete(self.root, data)


# Purpose: Initiate the deletion process and ensure the root is updated if it changes.
# Logic: Start deletion from the root and update the root if necessary.



# def _delete(self, root_node, data):
#     if root_node is None:
#         return root_node


# Purpose: Handle the base case where the node is not found.
# Logic: If the current node is None, return None.



#     if data < root_node.data:
#         root_node.left = self._delete(root_node.left, data)


# Purpose: Navigate to the left subtree if the data is smaller.
# Logic: Recursively call _delete on the left child and update the left child pointer.



#     elif data > root_node.data:
#         root_node.right = self._delete(root_node.right, data)


# Purpose: Navigate to the right subtree if the data is larger.
# Logic: Recursively call _delete on the right child and update the right child pointer.



#     else:
#         # Node with only one child or no child
#         if root_node.left is None:
#             return root_node.right
#         elif root_node.right is None:
#             return root_node.left


# Purpose: Handle cases where the node to be deleted has zero or one child.
# Logic: If the node has no left child, return the right child. If no right child, return the left child.



#         # Node with two children: Get the inorder successor
#         temp = self._min_value_node(root_node.right)
#         root_node.data = temp.data
#         root_node.right = self._delete(root_node.right, temp.data)


# Purpose: Handle the case where the node to be deleted has two children.
# Logic:
# Find the inorder successor (smallest node in the right subtree).
# Replace the data of the current node with the data of the inorder successor.
# Recursively delete the inorder successor node from the right subtree.



# return root_node


# Purpose: Return the updated subtree root.
# Logic: After handling all cases, return the updated root node.
# Finding the Minimum Value Node



# def _min_value_node(self, node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current


# Purpose: Find the node with the minimum value in a given subtree.
# Logic:
# Start with the given node.
# Traverse to the leftmost node (since it has the smallest value in a BST).
# Return the leftmost node.
# Visualizing the Process
# Initial BST:


#      8
#     / \
#    3  10
#   / \   \
#  1   6   11
#         /
#        9
# Find Inorder Successor of 10:

# Right subtree of 10: 11 -> 9
# Inorder successor: 11 (leftmost node in the right subtree).
# Replace 10 with 11:


#      8
#     / \
#    3  11
#   / \   \
#  1   6   11
#         /
#        9
# Delete Original 11:


#      8
#     / \
#    3  11
#   / \  /
#  1   6 9
# By following these steps, you can understand how the delete function works and why certain operations are necessary to maintain the BST properties.








## Floor in BST (Binary Search Tree)








# Concept:
# The "floor" of a given value X in a BST is the greatest value in the tree that is less than or equal to X.

# Real-life usage:

# Financial Systems: Determining the maximum price that is less than or equal to a given budget.
# Inventory Management: Finding the largest quantity of an item that is less than or equal to the required quantity.
# Detailed Explanation with Example
# Consider the following BST:



#       8
#      / \
#     3  10
#    / \   \
#   1   6   14
#      / \
#     4   7




# If we want to find the floor of 7, we need the largest value in the BST that is less than or equal to 7. In this case, it would be 6.

# Floor Function Implementation
# Here’s how we can implement the floor function in Python:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root_node, data):
        if data < root_node.data:
            if root_node.left:
                self._insert(root_node.left, data)
            else:
                root_node.left = Node(data)
        elif data > root_node.data:
            if root_node.right:
                self._insert(root_node.right, data)
            else:
                root_node.right = Node(data)
        else:
            print('Data already exists in the BST')

    def floor(self, data):
        return self._floor(self.root, data)

    def _floor(self, root_node, data):
        if root_node is None:
            return None

        if root_node.data == data:
            return root_node.data

        if root_node.data > data:
            return self._floor(root_node.left, data)

        floor_value = self._floor(root_node.right, data)
        return floor_value if floor_value is not None else root_node.data

# Usage
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

print("Floor:", bst.floor(7))  # Output: 6



# Detailed Explanation with Comments
# Class Definitions:


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# Represents a node in the BST with data, left, and right attributes.
# BinarySearchTree Class:


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
# Initializes the BST with a root attribute.
# Insert Method:


# def insert(self, data):
#     if self.root is None:
#         self.root = Node(data)
#     else:
#         self._insert(self.root, data)

# def _insert(self, root_node, data):
#     if data < root_node.data:
#         if root_node.left:
#             self._insert(root_node.left, data)
#         else:
#             root_node.left = Node(data)
#     elif data > root_node.data:
#         if root_node.right:
#             self._insert(root_node.right, data)
#         else:
#             root_node.right = Node(data)
#     else:
#         print('Data already exists in the BST')
# Inserts data into the BST.
# The _insert method is a helper function that recursively finds the correct position for the new node.
# Floor Method:


# def floor(self, data):
#     return self._floor(self.root, data)
# Public method that starts the floor search from the root of the BST.
# _floor Helper Method:


# def _floor(self, root_node, data):
#     if root_node is None:
#         return None
# Base case: If the current node is None, return None indicating no floor found yet.
# Exact Match or Move Left:


# if root_node.data == data:
#     return root_node.data
# if root_node.data > data:
#     return self._floor(root_node.left, data)
# If the current node's data matches the key, return the current node's data.
# If the current node's data is greater than the key, move to the left subtree.
# Update Floor Value and Move Right:


# floor_value = self._floor(root_node.right, data)
# return floor_value if floor_value is not None else root_node.data
# If the current node's data is less than the key, move to the right subtree to find a potentially closer floor value.
# Update the floor value to the current node's data if no closer value is found.


# Visualizing the Process
# Initial BST:


#      8
#     / \
#    3  10
#   / \   \
#  1   6   14
#     / \
#    4   7


# Finding Floor of 7:

# Start at root (8): 8 is greater than 7, move to left child (3).
# At 3: 3 is less than 7, update floor value to 3, move to right child (6).
# At 6: 6 is less than 7, update floor value to 6, move to right child (7).
# At 7: 7 matches the key, return 7.


# Result:

# Floor value: 6






## Why Store floor_value Only When Going Right?



# When We Go Left:

# If we go to the left subtree, it means the current node's value is greater than the key x.
# In this case, we do not store the current node's value because we are looking for a value that is less than or equal to x.
# Any value found in the left subtree will naturally be smaller than the current node's value, but we don't need to store the current node's value since it's not a candidate for the floor.
# When We Go Right:

# If we go to the right subtree, it means the current node's value is less than or equal to x.
# We store the current node's value as a potential floor_value because it satisfies the condition of being less than or equal to x.
# We then continue to the right subtree to see if there is a closer value to x that still meets the condition.
# If a closer value is found in the right subtree, it will be returned. If not, the stored floor_value is used.







## Ceiling ( In short opposite of floor method )









# the ceiling method in the Binary Search Tree (BST) and explain why we use the left and right subtrees the way we do. The ceiling of a given key x in a BST is the smallest value in the BST that is greater than or equal to x.

# Explanation
# Root Node Comparison:

# If the root node is None, it means we've reached the end of the tree without finding a ceiling value, so we return None.
# If the root node's value is equal to the key x, we return the root node's value because it is the ceiling.
# If Root Node's Value is Less than x:

# We need a larger value, so we move to the right subtree where values are greater.
# We recursively call the _ceiling method on the right child of the root node.
# If Root Node's Value is Greater than x:

# We store the root node's value as a potential ceiling value and then move to the left subtree to see if there's a smaller value that is still greater than or equal to x.
# We recursively call the _ceiling method on the left child of the root node.
# If a smaller suitable value is found in the left subtree, it will be returned. If not, the stored root node's value (which is greater than x) is returned.
# Code with Comments
# Here's the code with detailed comments explaining each step:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root_node, data):
        if data < root_node.data:
            if root_node.left:
                self._insert(root_node.left, data)
            else:
                root_node.left = Node(data)
        elif data > root_node.data:
            if root_node.right:
                self._insert(root_node.right, data)
            else:
                root_node.right = Node(data)
        else:
            print('Data already exists in the BST')

    def ceiling(self, data):
        return self._ceiling(self.root, data)

    def _ceiling(self, root_node, data):
        if root_node is None:
            return None  # If node is None, we've reached the end without finding a ceiling

        if root_node.data == data:
            return root_node.data  # If node's data matches the key, return the data

        if root_node.data < data:
            # Go to right subtree because we need a greater value
            return self._ceiling(root_node.right, data)

        # Go to left subtree because we need a smaller value
        ceiling_value = self._ceiling(root_node.left, data)
        # If ceiling value found in left subtree, return it; otherwise, return current node's data
        return ceiling_value if ceiling_value is not None else root_node.data

# Usage
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

print("Ceiling:", bst.ceiling(7))  # Output: 8



# Visual Explanation
# Consider the same example BST:


#        8
#       / \
#      3   10
#     / \   / \
#    1   6 9  11


# Finding the ceiling of 7:

# Start at root (8):

# 7 < 8, store 8 as ceiling_value, go left (to 3).
# At 3:

# 7 > 3, go right (to 6).
# At 6:

# 7 > 6, go right (no right child).
# No more nodes:

# Return the last stored ceiling_value which is 8.
# By following this approach, we ensure we find the smallest value greater than or equal to the given key, effectively finding the ceiling in the BST.




# Why We Store and Return Values Differently


# Left Subtree: When moving to the left, we store the current node's value because we're looking for the smallest value that is still greater than or equal to x.
# Right Subtree: When moving to the right, we are looking for a greater value, so we don't need to store the current node's value. We only store a value when moving left because we want to ensure we have the smallest possible value greater than or equal to x.
# This logic ensures that we correctly find the ceiling value according to the properties of the BST.








##  Here's what we've covered so far:

# Code A contains all the methods we've discussed throughout this topic. There's also Code B, which implements the same functionality but in a more advanced and efficient way. If you understand Code A, Code B will be straightforward to grasp as well.

# We'll be using Code B moving forward, as it's more reliable and requires less code, making it a better approach for future implementations.







## Code A:



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, root_node, data):
        if data < root_node.data:
            if root_node.left:
                return self.insert_node(root_node.left, data)
            else:
                root_node.left = Node(data)
        elif data > root_node.data:
            if root_node.right:
                return self.insert_node(root_node.right, data)
            else:
                root_node.right = Node(data)

        else:
            print('Error')


    def inorder(self, root_node):
        if root_node:
            self.inorder(root_node.left)
            print(root_node.data, end=' -> ')
            self.inorder(root_node.right)

    def delete(self, data):
        self.root = self.delete_node(self.root, data)
    
    def delete_node(self, root_node, data):
        if root_node is None:
            return root_node
        
        if data < root_node.data:
            root_node.left = self.delete_node(root_node.left, data)
        elif data > root_node.data:
            root_node.right = self.delete_node(root_node.right, data)
        else:
            if root_node.left is None:
                return root_node.right
            elif root_node.right is None:
                return root_node.left
            
            min_node_val = self.find_min_node_val(root_node.right)
            root_node.data = min_node_val.data
            root_node.right = self.delete_node(root_node.right, min_node_val.data)

        return root_node

    def find_min_node_val(self, right_node):
        current = right_node
        while current.left is not None:
            current = current.left
        return current
    
    def floor(self, data):
        return self.find_floor(self.root, data)
    
    def find_floor(self, root_node, data):
        if root_node is None:
            return None
        
        if root_node.data == data:
            return root_node.data
        
        if data < root_node.data:
            return self.find_floor(root_node.left, data)
        
        floor_value = self.find_floor(root_node.right, data)
        return floor_value if floor_value is not None else root_node.data
    
    def ceiling(self, data):
        return self.find_ceiling(self.root, data)
    
    def find_ceiling(self, root_node, data):
        if root_node is None:
            return None
        
        if data > root_node.data:
            return self.find_ceiling(root_node.right, data)
        
        ceiling_value = self.find_ceiling(root_node.left, data)

        return ceiling_value if ceiling_value is not None else root_node.data


bt = BinaryTree()
bt.insert(8)
bt.insert(3)
bt.insert(10)
bt.insert(1)
bt.insert(6)
bt.insert(9)
bt.insert(11)

print("Floor:", bt.floor(7))  # Output: 6
print("Ceiling:", bt.ceiling(7))  # Output: 8

bt.inorder(bt.root)
bt.delete(10)
print('')
print('Node deleted')
bt.inorder(bt.root)








## Code B: 







class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root_node, data):
        if root_node is None:
            return Node(data)
        
        if data < root_node.data:
            root_node.left = self.insert(root_node.left, data)

        elif data > root_node.data:
            root_node.right = self.insert(root_node.right, data)

        else:
            print('Error')

        return root_node

    def preorder(self, root_node):
        if root_node:
            print(root_node.data, end=' -> ')
            self.preorder(root_node.left)
            self.preorder(root_node.right)

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
                temp = self.find_min_right_val(root_node.right)
                root_node.data = temp.data
                root_node.right = self.delete(root_node.right, temp.data)

        return root_node

    def find_min_right_val(self, root_node):
        current = root_node
        while current.left is not None:
            current = current.left
        return current
    
    def floor(self, root_node, data):
        if root_node is None:
            return None
        
        if data < root_node.data:
            return self.floor(root_node.left, data)
        
        floor_value = self.floor(root_node.right, data)
        return floor_value if floor_value is not None else root_node.data
    
    def ceiling(self, root_node, data):
        if root_node is None:
            return None
        
        if data > root_node.data:
            return self.ceiling(root_node.right, data)
        
        ceiling_value = self.ceiling(root_node.left, data)
        return ceiling_value if ceiling_value is not None else root_node.data
    
bt = BinaryTree()
root_node = None

elements = [8, 3, 10, 1, 6, 9, 11]

for elem in elements:
    root_node = bt.insert(root_node, elem)

print("Floor:", bt.floor(root_node, 7))  # Output: 6
print("Ceiling:", bt.ceiling(root_node, 7))  # Output: 8

bt.preorder(root_node)
bt.delete(root_node, 10)
print('')
print('Node deleted')
bt.preorder(root_node)



# Let's break down Code B in detail:

# Class Definitions
# Node Class:


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Purpose: Represents a node in the binary tree.

# Attributes:
# data: Stores the value of the node.
# left: Points to the left child node.
# right: Points to the right child node.
# BinaryTree Class:


# class BinaryTree:
#     def insert(self, root_node, data):
#         if root_node is None:
#             return Node(data)
        
#         if data < root_node.data:
#             root_node.left = self.insert(root_node.left, data)
#         elif data > root_node.data:
#             root_node.right = self.insert(root_node.right, data)
#         else:
#             print('Error')

#         return root_node


# Purpose: Manages the binary tree operations.



# Insert Method:

# def insert(self, root_node, data):
#     if root_node is None:
#         return Node(data)
    
#     if data < root_node.data:
#         root_node.left = self.insert(root_node.left, data)
#     elif data > root_node.data:
#         root_node.right = self.insert(root_node.right, data)
#     else:
#         print('Error')

#     return root_node


# Purpose: Inserts a new node with data into the binary tree.


# Parameters:
# root_node: The current root node of the subtree.
# data: The value to be inserted.
# Returns: The new root node after insertion.


# Details:
# If root_node is None, it creates a new Node with the data.
# If data is less than root_node.data, it inserts into the left subtree.
# If data is greater, it inserts into the right subtree.
# The else branch handles duplicates with an error message.



# Preorder Method:

# def preorder(self, root_node):
#     if root_node:
#         print(root_node.data, end=' -> ')
#         self.preorder(root_node.left)
#         self.preorder(root_node.right)


# Purpose: Performs a preorder traversal of the binary tree.
# Parameters:
# root_node: The current root node of the subtree.


# Details:
# Prints the data of the current node.
# Recursively traverses the left subtree.
# Recursively traverses the right subtree.



# Delete Method:

# def delete(self, root_node, data):
#     if root_node is None:
#         return None
    
#     if data < root_node.data:
#         root_node.left = self.delete(root_node.left, data)
#     elif data > root_node.data:
#         root_node.right = self.delete(root_node.right, data)
#     else:
#         if root_node.left is None:
#             return root_node.right
#         elif root_node.right is None:
#             return root_node.left
#         else:
#             temp = self.find_min_right_val(root_node.right)
#             root_node.data = temp.data
#             root_node.right = self.delete(root_node.right, temp.data)

#     return root_node

# Purpose: Deletes a node with data from the binary tree.
# Parameters:
# root_node: The current root node of the subtree.
# data: The value of the node to be deleted.
# Returns: The new root node after deletion.


# Details:
# If root_node is None, returns None.
# If data is less than root_node.data, it proceeds with deletion in the left subtree.
# If data is greater, it proceeds with deletion in the right subtree.
# If data matches root_node.data:
# If the node to be deleted has only one child or no children, it returns the child or None.
# If the node has two children, it finds the minimum value node in the right subtree (in-order successor), replaces the node’s data with this value, and then deletes the in-order successor.


# Find Minimum Right Value Method:

# def find_min_right_val(self, root_node):
#     current = root_node
#     while current.left is not None:
#         current = current.left
#     return current


# Purpose: Finds the node with the minimum value in the right subtree.
# Parameters:
# root_node: The root node of the right subtree.
# Returns: The node with the minimum value.


# Details:
# Traverses to the leftmost node of the right subtree.
# Floor Method:

# def floor(self, root_node, data):
#     if root_node is None:
#         return None
    
#     if data < root_node.data:
#         return self.floor(root_node.left, data)
    
#     floor_value = self.floor(root_node.right, data)
#     return floor_value if floor_value is not None else root_node.data


# Purpose: Finds the floor value (the largest value less than or equal to data).
# Parameters:
# root_node: The current root node of the subtree.
# data: The value to find the floor for.
# Returns: The floor value if found, otherwise None.


# Details:
# If data is less than root_node.data, recursively searches in the left subtree.
# Otherwise, searches in the right subtree.
# Returns the largest value that is less than or equal to data.



# Ceiling Method:

# def ceiling(self, root_node, data):
#     if root_node is None:
#         return None
    
#     if data > root_node.data:
#         return self.ceiling(root_node.right, data)
    
#     ceiling_value = self.ceiling(root_node.left, data)
#     return ceiling_value if ceiling_value is not None else root_node.data


# Purpose: Finds the ceiling value (the smallest value greater than or equal to data).
# Parameters:
# root_node: The current root node of the subtree.
# data: The value to find the ceiling for.
# Returns: The ceiling value if found, otherwise None.


# Details:
# If data is greater than root_node.data, recursively searches in the right subtree.
# Otherwise, searches in the left subtree.
# Returns the smallest value that is greater than or equal to data.








# Summary






# Code B is flexible and suitable for modifications to AVL trees or other balanced trees because it manages nodes in a recursive way and returns new root nodes after operations.
# Code A is simpler and manages its own root attribute internally, which may be less adaptable for trees that require balancing and root reassignments.
# In practice, Code B’s design is preferable for more advanced tree structures due to its return-based approach for node updates and better support for modifications, like turning the tree into an AVL tree.


# You can start learning AVL Tree now 😊




