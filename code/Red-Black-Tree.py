
## Important: 

# Prerequisites

# Before diving in, it's essential that you have a solid understanding of AVL Trees, especially the concept of rotations and how they work.



# Learning Resources

# I couldn't find a YouTube video as good as the previous ones, but I've compiled some resources and done my best to explain and break down the code clearly for you.

# YT video: ( https://www.youtube.com/watch?v=qvZGUFHWChY&list=PL9xmBV_5YoZNqDI8qfOZgzbqahCUmUEin )



# Important:

# Just like in the AVL Tree file, I’ve divided the code into two parts—Code A and Code B.

# Code A: This is the more traditional way of writing a Red-Black Tree, but it can be a bit challenging for beginners to grasp.
# Code B: Here, I’ve simplified the variable names and the structure to make it easier for everyone to understand what’s happening.


# I encourage you to start with Code A and try to understand the logic. If you find it difficult, then move on to Code B, where I’ve explained everything in simpler terms.



# Overview




# A Red-Black Tree is a self-balancing binary search tree (BST) where each node contains an extra bit for storing color information, either red or black. This color is used to ensure the tree remains balanced during insertions and deletions, thus ensuring that operations like search, insertion, and deletion can be performed efficiently.





## Important:




# Properties of a Red-Black Tree


# Node Color: Each node is either red or black.
# Root Property: The root of the tree is always black.
# Leaf Property: All leaves (NIL nodes) are black.
# Red Property: If a red node has children, then the children must be black (no two red nodes can be adjacent).
# Depth Property: Every path from a node to its descendant NIL nodes has the same number of black nodes.
# These properties ensure that the tree remains approximately balanced, meaning that the longest path from the root to a leaf is no more than twice as long as the shortest path. This guarantees that the tree operations (insert, delete, search) have a time complexity of O(log n).



# Real-Life Example: Database Indexing


# Imagine a database system where records are stored and retrieved based on certain keys. To speed up retrieval, the database uses an index structure like a Red-Black Tree. The self-balancing nature of the tree ensures that no matter how records are added or removed, the tree remains balanced, providing quick lookup times for the records.

# For example, if a bank uses a Red-Black Tree to manage customer accounts by account number, the tree ensures that operations such as finding, inserting, or deleting an account are always efficient, even as the number of accounts grows.










## Code A: 


## Insertion Method: 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        root_node = self.root

        while root_node != self.NIL:
            parent = root_node
            if new_node.data < root_node.data:
                root_node = root_node.left
            else:
                root_node = root_node.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent 
                        self.left_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotation(node.parent.parent)

        self.root.color = 'black'

    def left_rotation(self, node):
        new_node = node.right
        new_node_left = new_node.left

        new_node.left = node
        node.right = new_node_left

        if new_node_left != self.NIL:
            new_node_left.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        
        node.parent = new_node

    def right_rotation(self, node):
        new_node = node.left
        new_node_right = new_node.right

        new_node.right = node
        node.left = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent

        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        node.parent = new_node

    def pre_order(self, root_node):
        if root_node != self.NIL:
            print(f'{root_node.data}({root_node.color})', end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root)


## Explaination of the above code




# Node Class


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

# class Node: This defines a Node class, which represents each node in the Red-Black Tree.
# def __init__(self, data): This is the initializer method (constructor) for the Node class. It sets up the initial state of each node when it is created.
# self.data = data: Stores the value (data) passed during the creation of the node.
# self.left = None: Initializes the left child of the node to None.
# self.right = None: Initializes the right child of the node to None.
# self.color = 'red': Sets the color of the node to 'red'. In Red-Black Trees, new nodes are always inserted as red.
# self.parent = None: Initializes the parent of the node to None.


# RedBlackTree Class


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

# class RedBlackTree: This defines the RedBlackTree class, which represents the entire Red-Black Tree.
# def __init__(self): The constructor for the RedBlackTree class. It sets up the initial state of the tree.
# self.NIL = Node(None): Creates a special node, NIL, which represents all the None leaves in the tree. This NIL node is used instead of None to simplify the implementation and ensure that every node has both left and right children, even if they are just sentinel nodes.
# self.NIL.color = 'black': Sets the color of the NIL node to 'black'. By definition, NIL nodes in a Red-Black Tree are always black.
# self.root = self.NIL: Initializes the root of the tree to the NIL node, indicating that the tree is initially empty.


# Insertion Method



def insert(self, data):
    new_node = Node(data)
    new_node.left = self.NIL
    new_node.right = self.NIL

    parent = None
    root_node = self.root

    while root_node != self.NIL:
        parent = root_node
        if new_node.data < root_node.data:
            root_node = root_node.left
        else:
            root_node = root_node.right

    new_node.parent = parent

    if parent is None:
        self.root = new_node
    elif new_node.data < parent.data:
        parent.left = new_node
    else:
        parent.right = new_node

    if new_node.parent is None:
        new_node.color = 'black'
        return
    
    if new_node.parent.parent is None:
        return
    
    self.fix_insert(new_node)


# def insert(self, data): Defines the insert method, which adds a new node with the given data to the Red-Black Tree.
# new_node = Node(data): Creates a new node with the provided data.
# new_node.left = self.NIL and new_node.right = self.NIL: Sets the left and right children of the new node to the NIL node, as it's a new leaf.
# parent = None: Initializes a parent variable to keep track of the parent of the new node.
# root_node = self.root: Starts the insertion process from the root of the tree.
# while root_node != self.NIL: Traverses the tree to find the correct position for the new node. The loop continues until it reaches a NIL node.
# parent = root_node: Updates the parent to the current node in the traversal.
# if new_node.data < root_node.data: Checks if the new node's data is less than the current node's data.
# root_node = root_node.left: If true, it moves to the left child.
# else:
# root_node = root_node.right: Otherwise, it moves to the right child.
# new_node.parent = parent: After finding the correct position, assigns the parent to the new node.
# if parent is None: Checks if the tree was initially empty.
# self.root = new_node: If true, sets the new node as the root.
# elif new_node.data < parent.data: If the new node's data is less than the parent's data:
# parent.left = new_node: Sets the new node as the left child of the parent.
# else:
# parent.right = new_node: Otherwise, sets the new node as the right child of the parent.
# if new_node.parent is None: Checks if the new node is the root (i.e., it has no parent).
# new_node.color = 'black': If true, changes its color to black since the root must always be black.
# return: Ends the method.
# if new_node.parent.parent is None: Checks if the new node's grandparent is None (i.e., the tree has only the root and one child).
# return: Ends the method, as no fixing is required.
# self.fix_insert(new_node): If the tree might be unbalanced, calls the fix_insert method to restore the Red-Black Tree properties.



# Fix Insert Method



def fix_insert(self, node):
    while node != self.root and node.parent.color == 'red':
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            if uncle.color == 'red':
                node.parent.color = 'black'
                uncle.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    node = node.parent 
                    self.left_rotation(node)
                node.parent.color = 'black'
                node.parent.parent.color = 'red'
                self.right_rotation(node.parent.parent)
        else:
            uncle = node.parent.parent.left
            if uncle.color == 'red':
                node.parent.color = 'black'
                uncle.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    node = node.parent
                    self.right_rotation(node)
                node.parent.color = 'black'
                node.parent.parent.color = 'red'
                self.left_rotation(node.parent.parent)

    self.root.color = 'black'


# def fix_insert(self, node): This method restores the Red-Black Tree properties after an insertion.
# while node != self.root and node.parent.color == 'red': Continues fixing as long as the node is not the root and its parent is red.
# if node.parent == node.parent.parent.left: Checks if the node's parent is a left child.
# uncle = node.parent.parent.right: Sets the uncle node to the right child of the grandparent.
# if uncle.color == 'red': If the uncle is red:
# node.parent.color = 'black': Recolors the parent to black.
# uncle.color = 'black': Recolors the uncle to black.
# node.parent.parent.color = 'red': Recolors the grandparent to red.
# node = node.parent.parent: Moves the node pointer to the grandparent.
# else: If the uncle is black:
# if node == node.parent.right: If the node is a right child:
# node = node.parent: Moves the node pointer to the parent.
# self.left_rotation(node): Performs a left rotation on the parent.
# node.parent.color = 'black': Recolors the parent to black.
# node.parent.parent.color = 'red': Recolors the grandparent to red.
# self.right_rotation(node.parent.parent): Performs a right rotation on the grandparent.
# else: If the node's parent is a right child:
# uncle = node.parent.parent.left: Sets the uncle node to the left child of the grandparent.
# if uncle.color == 'red': If the uncle is red:
# node.parent.color = 'black': Recolors the parent to black.
# uncle.color = 'black': Recolors the uncle to black.
# node.parent.parent.color = 'red': Recolors the grandparent to red.
# node = node.parent.parent: Moves the node pointer to the grandparent.
# else: If the uncle is black:
# if node == node.parent.left: If the node is a left child:
# node = node.parent: Moves the node pointer to the parent. This is done to prepare for a rotation.
# self.right_rotation(node): Performs a right rotation on the parent. This operation helps in balancing the tree by rotating the subtree rooted at the parent node to the right.
# node.parent.color = 'black': After the rotation, the parent of the current node is recolored to black to maintain the Red-Black Tree property that requires children of red nodes to be black.
# node.parent.parent.color = 'red': The grandparent of the current node is recolored to red to maintain the overall balance of the tree. This helps to prepare for any further rotations or recoloring needed.
# self.left_rotation(node.parent.parent): A left rotation is performed on the grandparent node to fix the tree's structure and ensure that it adheres to the Red-Black Tree properties. This rotation helps to reduce the height of the tree and maintain balance.

# Final Recoloring

# self.root.color = 'black': After exiting the loop, the root of the tree is always recolored to black to ensure that the tree remains a valid Red-Black Tree. This step is essential because the root node must always be black in a Red-Black Tree.




# Left Rotation Method



def left_rotation(self, node):
    new_node = node.right
    new_node_left = new_node.left

    new_node.left = node
    node.right = new_node_left

    if new_node_left != self.NIL:
        new_node_left.parent = node

    new_node.parent = node.parent
    if node.parent is None:
        self.root = new_node
    elif node == node.parent.left:
        node.parent.left = new_node
    else:
        node.parent.right = new_node
    
    node.parent = new_node

# def left_rotation(self, node): Defines the left_rotation method, which performs a left rotation on the subtree rooted at node.
# new_node = node.right: Assigns the right child of node to new_node. This new_node will become the new root of the rotated subtree.
# new_node_left = new_node.left: Stores the left child of new_node in new_node_left as it will be reassigned later.
# new_node.left = node: The current node becomes the left child of new_node, effectively rotating the tree to the left.
# node.right = new_node_left: The left child of new_node (which was stored in new_node_left) becomes the right child of the current node. This step preserves the tree structure.
# if new_node_left != self.NIL: Checks if new_node_left is not the NIL node (i.e., not a leaf node).
# new_node_left.parent = node: If true, updates the parent of new_node_left to be the current node.
# new_node.parent = node.parent: The parent of new_node is updated to be the parent of the current node. This step ensures that the rotated subtree is properly connected to the rest of the tree.
# if node.parent is None: If the current node was the root of the tree:
# self.root = new_node: The new node becomes the root of the entire tree.
# elif node == node.parent.left: If the current node was a left child:
# node.parent.left = new_node: The new node becomes the left child of the current node's parent.
# else:
# node.parent.right = new_node: Otherwise, the new node becomes the right child of the current node's parent.
# node.parent = new_node: Finally, the parent of the current node is updated to be new_node, completing the rotation.




# Right Rotation Method




def right_rotation(self, node):
    new_node = node.left
    new_node_right = new_node.right

    new_node.right = node
    node.left = new_node_right

    if new_node_right != self.NIL:
        new_node_right.parent = node

    new_node.parent = node.parent

    if node.parent is None:
        self.root = new_node
    elif node == node.parent.left:
        node.parent.left = new_node
    else:
        node.parent.right = new_node

    node.parent = new_node


# def right_rotation(self, node): Defines the right_rotation method, which performs a right rotation on the subtree rooted at node.
# new_node = node.left: Assigns the left child of node to new_node. This new_node will become the new root of the rotated subtree.
# new_node_right = new_node.right: Stores the right child of new_node in new_node_right as it will be reassigned later.
# new_node.right = node: The current node becomes the right child of new_node, effectively rotating the tree to the right.
# node.left = new_node_right: The right child of new_node (which was stored in new_node_right) becomes the left child of the current node. This step preserves the tree structure.
# if new_node_right != self.NIL: Checks if new_node_right is not the NIL node (i.e., not a leaf node).
# new_node_right.parent = node: If true, updates the parent of new_node_right to be the current node.
# new_node.parent = node.parent: The parent of new_node is updated to be the parent of the current node. This step ensures that the rotated subtree is properly connected to the rest of the tree.
# if node.parent is None: If the current node was the root of the tree:
# self.root = new_node: The new node becomes the root of the entire tree.
# elif node == node.parent.left: If the current node was a left child:
# node.parent.left = new_node: The new node becomes the left child of the current node's parent.
# else:
# node.parent.right = new_node: Otherwise, the new node becomes the right child of the current node's parent.
# node.parent = new_node: Finally, the parent of the current node is updated to be new_node, completing the rotation.



# Pre-Order Traversal Method




def pre_order(self, root_node):
    if root_node != self.NIL:
        print(f'{root_node.data}({root_node.color})', end=' ')
        self.pre_order(root_node.left)
        self.pre_order(root_node.right)

# def pre_order(self, root_node): Defines the pre_order method, which performs a pre-order traversal of the Red-Black Tree. In a pre-order traversal, the root node is visited first, followed by the left subtree, and then the right subtree.
# if root_node != self.NIL: Checks if the current node is not the NIL node (i.e., not a leaf node). If the node is NIL, the method returns without doing anything.
# print(f'{root_node.data}({root_node.color})', end=' ') Prints the data and color of the current node. The end=' ' ensures that the output remains on the same line.
# self.pre_order(root_node.left): Recursively calls the pre_order method on the left child of the current node.
# self.pre_order(root_node.right): Recursively calls the pre_order method on the right child of the current node.


# Example Usage

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root)


# rbt = RedBlackTree(): Creates a new instance of the RedBlackTree class, initializing an empty Red-Black Tree.
# elements = [10, 20, 30, 40, 50, 25, 60]: A list of elements to be inserted into the tree.
# for elm in elements: A loop that iterates over each element in the elements list.
# rbt.insert(elm): Inserts the current element into the Red-Black Tree using the insert method.
# print("Pre-order traversal of the constructed Red-Black tree is:"): Prints a message indicating that the pre-order traversal of the tree will be displayed.
# rbt.pre_order(rbt.root): Performs a pre-order traversal of the tree starting from the root and prints the result.












## Delete Method 







class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        root_node = self.root

        while root_node != self.NIL:
            parent = root_node
            if new_node.data < root_node.data:
                root_node = root_node.left
            else:
                root_node = root_node.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

    def delete(self, data):
        node_to_delete = self.search(self.root, data)
        if node_to_delete == self.NIL:
            return

        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            y = self.find_min_right_val(node_to_delete.right)
            original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self.transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        if original_color == 'black':
            self.fix_delete(x)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def find_min_right_val(self, node):
        current = node
        while current.left != self.NIL:
            current = current.left
        return current

    def fix_delete(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotation(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotation(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotation(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotation(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotation(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotation(node.parent)
                    node = self.root
        node.color = 'black'

    def search(self, node, key):
        if node == self.NIL or key == node.data:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent 
                        self.left_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotation(node.parent.parent)

        self.root.color = 'black'

    def left_rotation(self, node):
        new_node = node.right
        new_node_left = new_node.left

        new_node.left = node
        node.right = new_node_left

        if new_node_left != self.NIL:
            new_node_left.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        
        node.parent = new_node

    def right_rotation(self, node):
        new_node = node.left
        new_node_right = new_node.right

        new_node.right = node
        node.left = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent

        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        node.parent = new_node

    def pre_order(self, root_node):
        if root_node != self.NIL:
            print(f'{root_node.data}({root_node.color})', end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root)


## Explaination of the above code



# 1. Node Class




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

# Purpose: Represents a single node in the Red-Black Tree.
# Attributes:
# data: Holds the value of the node.
# left: Points to the left child node.
# right: Points to the right child node.
# color: Stores the color of the node (initially set to 'red').
# parent: Points to the parent node.



# 2. RedBlackTree Class
# Constructor: __init__




class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

# Purpose: Initializes the Red-Black Tree.
# Attributes:
# NIL: A sentinel node representing the leaf nodes (None). It's black by default and used to simplify tree operations.
# root: Initially set to NIL, this will later point to the actual root of the tree.











# Method: delete







def delete(self, data):
    node_to_delete = self.search(self.root, data)
    if node_to_delete == self.NIL:
        return
    
# Purpose: Deletes a node from the Red-Black Tree.
# Steps:
# node_to_delete = self.search(self.root, data): Searches for the node with the given data.
# if node_to_delete == self.NIL: If the node is not found (i.e., it's NIL), the function exits early.




    original_color = node_to_delete.color
    if node_to_delete.left == self.NIL:
        x = node_to_delete.right
        self.transplant(node_to_delete, node_to_delete.right)

# Purpose: Handles the case where the node to delete has no left child.
# Steps:
# original_color = node_to_delete.color: Stores the color of the node to be deleted for later use in the fix-up process.
# if node_to_delete.left == self.NIL: Checks if the node has no left child.
# x = node_to_delete.right: Assigns the right child to x (the child that will replace the deleted node).
# self.transplant(node_to_delete, node_to_delete.right): Replaces node_to_delete with its right child.




    elif node_to_delete.right == self.NIL:
        x = node_to_delete.left
        self.transplant(node_to_delete, node_to_delete.left)

# Purpose: Handles the case where the node to delete has no right child.
# Steps:
# elif node_to_delete.right == self.NIL: Checks if the node has no right child.
# x = node_to_delete.left: Assigns the left child to x.
# self.transplant(node_to_delete, node_to_delete.left): Replaces node_to_delete with its left child.




    else:
        y = self.find_min_right_val(node_to_delete.right)
        original_color = y.color
        x = y.right

# Purpose: Handles the case where the node has both children.
# Steps:
# y = self.find_min_right_val(node_to_delete.right): Finds the smallest node in the right subtree (in-order successor).
# original_color = y.color: Stores the color of y for later use.
# x = y.right: Assigns x to the right child of y.




        if y.parent == node_to_delete:
            x.parent = y
        else:
            self.transplant(y, y.right)
            y.right = node_to_delete.right
            y.right.parent = y

# Purpose: Handles the transplant and adjusts pointers.
# Steps:
# if y.parent == node_to_delete: Checks if y is a direct child of node_to_delete.
# x.parent = y: Sets y as the parent of x.
# else: If y is not a direct child, performs the transplant.
# self.transplant(y, y.right): Replaces y with its right child.
# y.right = node_to_delete.right: Sets y.right to the right child of node_to_delete.
# y.right.parent = y: Updates the parent of y.right to be y.




        self.transplant(node_to_delete, y)
        y.left = node_to_delete.left
        y.left.parent = y
        y.color = node_to_delete.color

# Purpose: Finalizes the deletion and adjusts pointers.
# Steps:
# self.transplant(node_to_delete, y): Replaces node_to_delete with y.
# y.left = node_to_delete.left: Updates the left child of y.
# y.left.parent = y: Updates the parent pointer of y.left.
# y.color = node_to_delete.color: Sets the color of y to the color of the deleted node.




    if original_color == 'black':
        self.fix_delete(x)

# Purpose: Calls the fix_delete method if the original node was black.
# Steps:
# if original_color == 'black': Checks if the deleted node was black.
# self.fix_delete(x): Calls fix_delete to restore Red-Black Tree properties.


# Method: transplant




def transplant(self, u, v):
    if u.parent is None:
        self.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent


# Purpose: Replaces one subtree with another.
# Steps:
# if u.parent is None: If u is the root, replace it with v.
# elif u == u.parent.left: If u is the left child, update the parent's left child to v.
# else: Otherwise, update the parent's right child to v.
# v.parent = u.parent: Set the parent of v to be the parent of u.


# Method: find_min_right_val




def find_min_right_val(self, node):
    current = node
    while current.left != self.NIL:
        current = current.left
    return current

# Purpose: Finds the smallest node in a subtree.
# Steps:
# current = node: Start from the given node.
# while current.left != self.NIL: Traverse left until a NIL node is found.
# return current: Return the smallest node found.



# Method: fix_delete




def fix_delete(self, node):
    while node != self.root and node.color == 'black':
        if node == node.parent.left:
            sibling = node.parent.right
            if sibling.color == 'red':
                sibling.color = 'black'
                node.parent.color = 'red'
                self.left_rotation(node.parent)
                sibling = node.parent.right

# Purpose: Fixes the tree after deletion to maintain Red-Black properties.
# Steps:
# while node != self.root and node.color == 'black': Loop until node is the root or it's not black.
# if node == node.parent.left: Check if node is the left child.
# sibling = node.parent.right: Get the right sibling.
# if sibling.color == 'red': If the sibling is red:
# Change sibling to black, parent to red, and perform a left rotation on the parent.
# sibling = node.parent.right: Update the sibling after rotation.




            if sibling.left.color == 'black' and sibling.right.color == 'black':
                sibling.color = 'red'
                node = node.parent
            else:
                if sibling.right.color == 'black':
                    sibling.left.color = 'black'
                    sibling.color = 'red'
                    self.right_rotation(sibling)
                    sibling = node.parent.right


# Purpose: Handle cases where the sibling's children are black.
# Steps:
# if sibling.left.color == 'black' and sibling.right.color == 'black': If both children are black:
# Recolor the sibling red and move up to the parent.
# else: Handle the case where at least one child is not black.
# Perform a right rotation if necessary, then update the sibling.



                sibling.color = node.parent.color
                node.parent.color = 'black'
                sibling.right.color = 'black'
                self.left_rotation(node.parent)
                node = self.root


# Purpose: Final adjustments to maintain the tree properties.
# Steps:
# Set the sibling's color to the parent's color, then make the parent and sibling's right child black.
# Perform a left rotation on the parent, and set node to the root to exit the loop.


            #else: ( This else is their, I commented just so it dont show any error, in orginal code you need to include this too. )
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotation(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotation(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotation(node.parent)
                    node = self.root

# Purpose: Handle the mirror case where the node is the right child of its parent.
# Steps:
# else: This handles the scenario where node is the right child.

# sibling = node.parent.left: The sibling is now the left child of the parent.

# if sibling.color == 'red': If the sibling is red:

# Change the sibling to black, the parent to red, and perform a right rotation on the parent.
# Update the sibling after the rotation.
# if sibling.right.color == 'black' and sibling.left.color == 'black': If both of the sibling's children are black:

# Recolor the sibling to red and move up to the parent.
# else: Handle the case where at least one child is not black.

# If the left child of the sibling is black, perform a left rotation on the sibling and update the sibling.
# Set the sibling's color to the parent's color, make the parent and the sibling's left child black, and perform a right rotation on the parent.
# Set node to the root to exit the loop.
#     node.color = 'black'
# Purpose: Ensure that the node is colored black before exiting the function.
# Steps:
# node.color = 'black': If the node reached this point and is still not black, it is set to black to maintain Red-Black Tree properties.


# Method: search


def search(self, node, key):
    if node == self.NIL or key == node.data:
        return node
    if key < node.data:
        return self.search(node.left, key)
    return self.search(node.right, key)

# Purpose: Searches for a node with a specific key in the Red-Black Tree.
# Steps:
# if node == self.NIL or key == node.data: If the node is NIL (i.e., not found) or matches the key, return the node.
# if key < node.data: If the key is less than the current node's data, recursively search the left subtree.
# return self.search(node.right, key): Otherwise, recursively search the right subtree.




# Final Explanation



# The delete method in the Red-Black Tree implementation handles the deletion of a node while maintaining the essential properties of the Red-Black Tree. The fix_delete method plays a crucial role in ensuring that the tree remains balanced and adheres to the Red-Black Tree rules after a deletion operation.



# Here's a quick summary of the key points:

# Transplanting Nodes: The transplant method replaces one subtree with another, effectively removing the node that needs to be deleted.
# Fixing the Tree: After a node is deleted, the fix_delete method is called if the deleted node was black. This method ensures that the tree remains balanced and retains its Red-Black properties.
# Searching Nodes: The search method helps locate the node to be deleted, and it works by recursively traversing the tree based on the value of the key.











### The whole Red-Black-Tree












class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        root_node = self.root

        while root_node != self.NIL:
            parent = root_node
            if new_node.data < root_node.data:
                root_node = root_node.left
            else:
                root_node = root_node.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

    def delete(self, data):
        node_to_delete = self.search(self.root, data)
        if node_to_delete == self.NIL:
            return

        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            y = self.find_min_right_val(node_to_delete.right)
            original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self.transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        if original_color == 'black':
            self.fix_delete(x)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def find_min_right_val(self, node):
        current = node
        while current.left != self.NIL:
            current = current.left
        return current

    def fix_delete(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotation(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotation(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotation(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotation(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotation(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotation(node.parent)
                    node = self.root
        node.color = 'black'

    def search(self, node, key):
        if node == self.NIL or key == node.data:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent 
                        self.left_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotation(node.parent.parent)

        self.root.color = 'black'

    def left_rotation(self, node):
        new_node = node.right
        new_node_left = new_node.left

        new_node.left = node
        node.right = new_node_left

        if new_node_left != self.NIL:
            new_node_left.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        
        node.parent = new_node

    def right_rotation(self, node):
        new_node = node.left
        new_node_right = new_node.right

        new_node.right = node
        node.left = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent

        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        node.parent = new_node

    def pre_order(self, root_node):
        if root_node != self.NIL:
            print(f'{root_node.data}({root_node.color})', end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root)



















## Code B: 









## In this part I try to breakdown code more and try to explain it in simple words and how things are done








## Insert Method 







## lets start with the node class
# so every node will have the some properties but in red black tree you have 2 extra one, color and other is parent, every node will have a color either it is red or black and every node will have a parent too, or a parent node, if no parent or no parent node it means it is just a root node which you can assign as 
# self.root = that node 
## also remeber this self.root or root node will always have the color black
## but we defining it red as now cause its just a node not the root node so every node will go as a red node in red black tree but after we will change that

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

class RedBlackTree:
    ## first we will define some pointer 
    # the NIL you can see its just leave node or you can say just Null node cause you see the data in that Node is None 
    # we just establishing how a leave node will look, the color of that node will be black and for starter if there is no root node, then we assign root as that null node for now
    def __init__(self):
        self.NIL = Node(None) ## NIl node will be a node with a data of None
        self.NIL.color = 'black' ## that NIL node color will be black
        self.root = self.NIL # and if no root node for now we assign this NULL node as root

    # Now we need to insert a data in our red black tree we pass the data what we wanna insert
    def insert(self, data):
        new_node = Node(data) # we make a new node with that given data 
        new_node.left = self.NIL # and we give that newnode right and left child as NUll node 
        new_node.right = self.NIL

        # we define 2 variable rn. one is parent cause all node will have parent and the second one is root_node cause if there is a root_node then we need to go through the tree to find wehere that new_node belong and we will insert it over their
        parent = None
        root_node = self.root

        # here we finding were we need to put that new_node in tree so we started a while loop and go through the tree 
        while root_node != self.NIL: # if root_node != self.NIL we just say if root_node is not NULL then go throught the tree
            parent = root_node # we assign parent as root_node
            if new_node.data < root_node.data: # we see if new_node, data is less then my root_node, data then go to the left
                root_node = root_node.left
            else:
                root_node = root_node.right # or else go to right
            
        new_node.parent = parent # now as our var we got the node to which after our new_node will be attach so we give our new_node.parent to be this parent 
        if parent is None: # but if the parent is None, so obv the tree is empty and its our first node so thats why we assign root as the new_node
            self.root = new_node
        elif new_node.data < parent.data: # but if parent is not none, then we chaeck if our newnode data is less then parent data, if it is then we just assign our newnode in left side of that parent  
            parent.left = new_node
        else:
            parent.right = new_node # or else on the right side of our parent

        if new_node.parent is None: # we check if parent is none that means our newnode is now rootnode so that means we need to change the color cause thats the rule of red black tree that rootnode will always hava a color of black, so we did it
            new_node.color = 'black'
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

    def fix_insert(self, node):
        # We start by checking if the node is not the root and if its parent's color is red. This is important because if a red node has a red parent, it violates the Red-Black Tree properties. ( if you remeber every node we insert at first will have a color red ( see starting Node class ) )
        while node != self.root and node.parent.color == 'red':
            # We first check if the parent of our node is on the left side of its parent (our grandparent).
            #      6 ( grandparent )
            #     /
            #    2 ( parent )
            #   /
            #  1 ( our node )
            if node.parent == node.parent.parent.left:
                # Then, we look at the "uncle" node (the sibling of our parent). The uncle is the node on the right side of the grandparent.
            #      6 ( grandparent )
            #     / \
            #    2   8 ( uncle node )
            #   /
            #  1 ( our node )
                uncle = node.parent.parent.right
                # If the uncle is red, we have a situation where the tree is unbalanced.
                if uncle.color == 'red':
                    # We fix this by turning both the parent and the uncle black, and the grandparent red.
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    # Then, we move up the tree and continue checking the new node’s grandparent to see if more fixes are needed.
                    node = node.parent.parent
                else: # If the uncle is black, the tree is still unbalanced, but we handle it differently.
                    # If our node is a right child, we first rotate the parent to the left to make our node a left child.
                    if node == node.parent.right:
                        # If our node is a right child, we first rotate the parent to the left to make our node a left child.
                        node = node.parent
                        #     6 (grandparent)                                                  
                        #    / \
                        #   2   8 (uncle)    ---> original tree structure
                        #  /
                        # 1 (our node)

                        ## after rotation 

                        #     6 (grandparent)                                                  
                        #    / \
                        #   1   8 (uncle)    ---> left rotation
                        #    \
                        #     2

                        self.left_rotation(node)
                    # Then, we switch the colors of the parent and grandparent and perform a right rotation on the grandparent.
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                        #     6 (grandparent)                                                  
                        #    / \
                        #   1   8 (uncle)    ---> original tree structure
                        #    \
                        #     2

                        ## after right rotation 

                        #     2                                                  
                        #    / \
                        #   1   6 
                        #        \
                        #         8
                    self.right_rotation(node.parent.parent)
            else: # This is just the mirror image of if we see above just look at it it all opposite .
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotation(node.parent.parent)
        # Finally, after all these rotations and color changes, we make sure the root is always black. This is a rule in Red-Black Trees.
        self.root.color = 'black'

    # If you've worked with AVL Trees before, you're likely familiar with the concept of rotations. In Red-Black Trees, rotations work similarly, with the main difference being that instead of updating the height of nodes, we update the parent pointers.
    def left_rotation(self, node):
        new_node = node.right
        new_node_right = new_node.left

        new_node.left = node
        node.right = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        # This is the same logic as in the insert method above, where we update the parent pointers.
        # If there is no parent, we make `new_node` the new root.
        # If there is a parent, we check where to place `new_node` in relation to it.
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left: # If our `node` is on the left of its parent, we replace it with `new_node`.
            node.parent.left = new_node
        else:
            node.parent.right = new_node # Otherwise, we replace the right child with `new_node`.
        
        node.parent = new_node

    # Right Rotation is just the mirror image of left rotation you just need to do everything opposite and other things are same 
    def right_rotation(self, node):
        new_node = node.left
        new_node_right = new_node.right

        new_node.right = node
        node.left = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        node.parent = new_node
        
    def pre_order(self, root_node):
        if root_node != self.NIL:
            print(f'{root_node.data}({root_node.color})', end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root) # 20(black) 10(black) 40(red) 30(black) 25(red) 50(black) 60(red)
print('')








## Delete Method :  ( No explaination for rotation and insert cause I did in above code )








class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        root_node = self.root

        while root_node != self.NIL:
            parent = root_node
            if new_node.data < root_node.data:
                root_node = root_node.left
            else:
                root_node = root_node.right
            
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotation(node.parent.parent)
        self.root.color = 'black'

    ## deleting in red black tree is quite hard then insert, but lets see
    # we pass the data which we wanna delete 
    def delete(self, data):
        node_to_delete = self.find_the_node(self.root, data) ## we make a method `find_the_node` it will give us the node which we wanna delete
        if node_to_delete == self.NIL: ## we check if the node we wanna delete is NULL then we just return 
            return
        original_color = node_to_delete.color ## we save the color of the node which we wanna delete
        ## now if you did AVL tree then its quite similar
        # first we check if, the node that we wanna delete only have right child then we replace that right child of that node with that node 
        # same goes if we only have left child 
        # but if the node which we wanna delete have both the child, then we thorught the right part of that node and then keep going through left until we find the last node. 
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.change_node(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.change_node(node_to_delete, node_to_delete.left)
        else:
            temp = self.find_min_right_val(node_to_delete.right) # Find the minimum node in the right subtree of node_to_delete (temp).
            original_color = temp.color # we save the original color
            x = temp.right # cause this time we have both child we store our right child in a variable
            if temp.parent == node_to_delete: ## we check if my temp parent is the node that i wanna delete then
                x.parent = temp # we update x.parent to temp
            else:
                self.change_node(temp, temp.right) # If temp is not a direct child, update its right child and its parent.
                temp.right = node_to_delete.right
                temp.right.parent = temp
            self.change_node(node_to_delete, temp)  # Replace node_to_delete with temp.
            temp.left = node_to_delete.left #  Update the parent of node_to_delete to point to temp. Set temp's left child and its color. temp becomes the new node in place of node_to_delete.
            temp.left.parent = temp
            temp.color = node_to_delete.color

        if original_color == 'black':
            self.fix_delete(x) # # Fix the tree if the deleted node was black.

    def fix_delete(self, node):
        while node != self.root and node.color == 'black': ## we check if node is not root and node color is black, Black nodes are critical for maintaining the Black-Height property, so if a black node is deleted, the balance of the tree might be disturbed. We need to handle this by potentially performing rotations and color changes.
            if node == node.parent.left: # Check if the node is the left child of its parent.
                #     6 ( parent )                                                 
                #    / \
            #(node) 1   8 ( sibling )
                sibling = node.parent.right
                if sibling.color == 'red': # If the sibling is red, we can perform a rotation to balance the tree. By changing the sibling's color to black and the parent’s color to red, we can then perform a left rotation to fix the imbalance.
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotation(node.parent) # Perform a left rotation around the parent to balance the tree.
                    sibling = node.parent.right # Update the sibling reference to the new right child of the parent after rotation.
                if sibling.left.color == 'black' and sibling.right.color == 'black': # Check if both children of the sibling are black. If both children are black, the sibling is effectively a black hole. By making the sibling red, we are trying to propagate the need for rebalancing up the tree. Move up to the parent to continue fixing the tree.
                    sibling.color = 'red' # If both children are black, change the sibling’s color to red.
                    node = node.parent # Move up the tree by setting node to its parent.
                else:
                    if sibling.right.color == 'black': # Handle the case where the sibling’s right child is black.
                        # If the sibling’s right child is black, we need to make the sibling color red, sibling leftnode color black too, and rotate right around the sibling to ensure that the red node moves to the sibling’s right child position. This helps balance the tree.
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotation(sibling)
                        sibling = node.parent.right
                    sibling.right.color = 'black' # Perform final adjustments if the sibling’s left child is black. After rotations, set the sibling’s right child to black and update colors to ensure the Red-Black Tree properties are maintained. Perform a left rotation to balance the tree and set the node to the root to exit the loop.
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    self.left_rotation(node.parent)
                    node = self.root
            else: ## this will be opoosite of the upper if statement
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotation(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotation(sibling)
                        sibling = node.parent.left
                    sibling.left.color = 'black'
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    self.right_rotation(node.parent)
                    node = self.root
        node.color = 'black' # Ensure the node color is black after all fixes. The root of the tree must always be black, and the final step ensures that if the node is the root, its color is black.

    # Finds the most left child node in right side of the tree
    def find_min_right_val(self, root_node):
        current = root_node # now current var store the node value
        while current.left != self.NIL: # we just checking if our current node has a left node then keep on going and once its left node is NULL then return that node 
            current = current.left 
        return current

    def change_node(self, root_node, change_node):
        # if our root_node is 1 and our put_this_node is 2 then
        #     6                                                
        #    / \
        #   1   8               ----> suppose this is orginal tree
        #    \
        #     2
        if root_node.parent is None:
            self.root = change_node # if no parent then we just make our `put_this_node` to root 
        else:
            if root_node == root_node.parent.left: # if `root_node` is in left then put `put_this_node` on that side only
                root_node.parent.left = change_node
            else:
                root_node.parent.right = change_node # if `root_node` is in right then put `put_this_node` on that side only

        if change_node is not None:
            change_node.parent = root_node.parent # update our `put_this_node` parent to `root_node` parent
        else:
            change_node = self.NIL

        ## after all this node, the tree will look like this
        #     6                                                
        #    / \
        #   2   8  

    def find_the_node(self, root_node, data): # This method searches for a node in the tree that contains the given data.
        if root_node == self.NIL or root_node.data == data: # The first condition checks if root_node is NIL (meaning we've reached the end of a branch without finding the data) or if root_node contains the data we're looking for. If either condition is true, the method returns the current root_node.
            return root_node

        if data < root_node.data: # If the data we're searching for is less than the root_node's data, we recursively search in the left subtree of the current root_node.
            return self.find_the_node(root_node.left, data)
        return self.find_the_node(root_node.right, data) # If the data is greater than or equal to the root_node's data, we recursively search in the right subtree of the current root_node.

    def left_rotation(self, node):
        new_node = node.right
        new_node_right = new_node.left

        new_node.left = node
        node.right = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        
        node.parent = new_node

    def right_rotation(self, node):
        new_node = node.left
        new_node_right = new_node.right

        new_node.right = node
        node.left = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        node.parent = new_node
        
    def pre_order(self, root_node):
        if root_node != self.NIL:
            print(f'{root_node.data}({root_node.color})', end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root) # 20(black) 10(black) 40(red) 30(black) 25(red) 50(black) 60(red)
print('')

rbt.delete(10)

print("After deleting 10, Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root) # 40(black) 25(red) 20(black) 30(black) 50(black) 60(red)











### Whole Red-Black-Tree 











class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'red'
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        root_node = self.root

        while root_node != self.NIL:
            parent = root_node
            if new_node.data < root_node.data:
                root_node = root_node.left
            else:
                root_node = root_node.right
            
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    uncle.color = 'black'
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotation(node.parent.parent)
        self.root.color = 'black'

    def delete(self, data):
        node_to_delete = self.find_the_node(self.root, data)
        if node_to_delete == self.NIL:
            return
        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.change_node(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.change_node(node_to_delete, node_to_delete.left)
        else:
            temp = self.find_min_right_val(node_to_delete.right)
            original_color = temp.color
            x = temp.right
            if temp.parent == node_to_delete:
                x.parent = temp
            else:
                self.change_node(temp, temp.right)
                temp.right = node_to_delete.right
                temp.right.parent = temp
            self.change_node(node_to_delete, temp)
            temp.left = node_to_delete.left
            temp.left.parent = temp
            temp.color = node_to_delete.color

        if original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotation(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotation(sibling)
                        sibling = node.parent.right
                    sibling.right.color = 'black'
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    self.left_rotation(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotation(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotation(sibling)
                        sibling = node.parent.left
                    sibling.left.color = 'black'
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    self.right_rotation(node.parent)
                    node = self.root
        node.color = 'black'

    def find_min_right_val(self, root_node):
        current = root_node
        while current.left != self.NIL:
            current = current.left
        return current

    def change_node(self, root_node, change_node):
        if root_node.parent is None:
            self.root = change_node
        else:
            if root_node == root_node.parent.left:
                root_node.parent.left = change_node
            else:
                root_node.parent.right = change_node

        if change_node is not None:
            change_node.parent = root_node.parent
        else:
            change_node = self.NIL

    def find_the_node(self, root_node, data):
        if root_node == self.NIL or root_node.data == data:
            return root_node

        if data < root_node.data:
            return self.find_the_node(root_node.left, data)
        return self.find_the_node(root_node.right, data)

    def left_rotation(self, node):
        new_node = node.right
        new_node_right = new_node.left

        new_node.left = node
        node.right = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        
        node.parent = new_node

    def right_rotation(self, node):
        new_node = node.left
        new_node_right = new_node.right

        new_node.right = node
        node.left = new_node_right

        if new_node_right != self.NIL:
            new_node_right.parent = node

        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node

        node.parent = new_node
        
    def pre_order(self, root_node):
        if root_node != self.NIL:
            print(f'{root_node.data}({root_node.color})', end=' ')
            self.pre_order(root_node.left)
            self.pre_order(root_node.right)

# Example usage
rbt = RedBlackTree()
elements = [10, 20, 30, 40, 50, 25, 60]

for elm in elements:
    rbt.insert(elm)

print("Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root)
print('')

rbt.delete(10)

print("After deleting 10, Pre-order traversal of the constructed Red-Black tree is:")
rbt.pre_order(rbt.root)
