
# Learning Resources


# YT videos: ( https://www.youtube.com/watch?v=AE5I0xACpZs&pp=ygULYmluYXJ5IGhlYXA%3D )


# Important:

# Just like in the AVL Tree file, I’ve divided the code into two parts—Code A and Code B.

# Code A: This is the more traditional way of writing a Binary Heap, but it can be a bit challenging for beginners to grasp.

# Code B: Here, I’ve simplified the variable names and the structure to make it easier for everyone to understand what’s happening.



# 17. Heap
# A Heap is a specialized tree-based data structure that satisfies the heap property. There are two main types of heaps:

# Max-Heap: In a Max-Heap, for any given node I, the value of I is greater than or equal to the values of its children. The maximum value is at the root.

# Min-Heap: In a Min-Heap, for any given node I, the value of I is less than or equal to the values of its children. The minimum value is at the root.


# 17.1 Binary Heap Introduction



# What is a Binary Heap?

# A Binary Heap is a complete binary tree that satisfies the heap property. A complete binary tree is a binary tree in which every level is fully filled except possibly the last, which is filled from left to right.


# Properties of Binary Heap:

# Shape Property: The tree is a complete binary tree.
# Heap Property: In a Max-Heap, every node is greater than or equal to its children, and in a Min-Heap, every node is less than or equal to its children.
# Operations on a Binary Heap:



# Insert: Add a new element to the heap and ensure the heap property is maintained.
# Delete/Extract: Remove the root (maximum or minimum element) and ensure the heap property is maintained.
# Peek/Top: Return the root element without removing it.
# Heapify: Ensure that the heap property is maintained throughout the tree.
# Real-Life Example:
# Consider a priority queue where tasks are prioritized based on urgency. A binary heap can efficiently manage this queue by always providing the highest priority task (in a Max-Heap) or the lowest priority task (in a Min-Heap).




# Industry Uses:


# Priority Queues: Used in various algorithms like Dijkstra's shortest path algorithm, Huffman coding, etc.
# Scheduling: In operating systems, heaps are used for job scheduling where jobs with higher priority need to be processed first.
# Graph Algorithms: Heaps are widely used in graph algorithms like Prim's and Dijkstra's for efficient extraction of minimum or maximum elements.








# Min-Heap ( Code A )




class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap the current node with its parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to the root and reduce the heap size
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            # Swap the current node with the smallest of its children
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        self._heapify_up(i)

    def delete(self, i):
        # Decrease the value to negative infinity and extract the minimum
        self.decrease_key(i, float('-inf'))
        self.extract_min()

    def build_heap(self, arr):
        self.heap = arr[:]
        # Start heapifying from the last non-leaf node down to the root
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def print_heap(self):
        print("Heap array:", self.heap)
    

min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)
min_heap.insert(15)
min_heap.insert(5)
min_heap.insert(4)
min_heap.insert(45)

min_heap.print_heap()  # Output: Heap array: [1, 3, 2, 15, 5, 4, 45]

print("Extracted Min:", min_heap.extract_min())  # Output: Extracted Min: 1
min_heap.print_heap()  # Output: Heap array: [2, 3, 4, 15, 5, 45]

min_heap.delete(1)
min_heap.print_heap()  # Output: Heap array: [2, 5, 4, 15, 45]





## Code Breakdown






# Class Definition and Initialization

class MinHeap:
    def __init__(self):
        self.heap = []

# class MinHeap:: This defines the MinHeap class, which will implement a min-heap data structure.
# def __init__(self):: The constructor method initializes an empty list heap to store the heap elements.




# Utility Methods for Tree Structure

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2
    
# def parent(self, i):: Returns the index of the parent node for the element at index i.
# Formula: (i - 1) // 2 calculates the parent node index in a binary tree represented as an array.
# def left_child(self, i):: Returns the index of the left child of the node at index i.
# Formula: 2 * i + 1 calculates the left child node index.
# def right_child(self, i):: Returns the index of the right child of the node at index i.
# Formula: 2 * i + 2 calculates the right child node index.



# Insertion Method

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)


# def insert(self, key):: Inserts a new key into the heap.
# self.heap.append(key):: Adds the new key to the end of the heap list.
# self._heapify_up(len(self.heap) - 1):: Calls the _heapify_up method to maintain the min-heap property by adjusting the position of the newly added key.



# Heapify Up Method (for Insertion)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


# def _heapify_up(self, i):: Ensures the min-heap property is maintained by moving the element at index i up the tree if it's smaller than its parent.
# while i > 0 and self.heap[self.parent(i)] > self.heap[i]:: Continues to swap the current element with its parent as long as it's smaller and hasn't reached the root.
# self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]:: Swaps the current element with its parent.
# i = self.parent(i):: Updates i to the parent's index to continue the process.



# Extract Min Method

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    

# def extract_min(self):: Removes and returns the smallest element (the root) from the heap.
# if len(self.heap) == 0:: Checks if the heap is empty; if so, returns None.
# if len(self.heap) == 1:: If there's only one element, it pops and returns that element.
# root = self.heap[0]:: Stores the root value (smallest element).
# self.heap[0] = self.heap.pop():: Replaces the root with the last element in the heap and removes the last element.
# self._heapify_down(0):: Calls the _heapify_down method to maintain the min-heap property by adjusting the position of the new root.
# return root:: Returns the extracted minimum value.



# Heapify Down Method (for Extract Min)

    def _heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)


# def _heapify_down(self, i):: Ensures the min-heap property is maintained by moving the element at index i down the tree if it's larger than its children.
# smallest = i:: Initializes the smallest index as the current node.
# left = self.left_child(i): and right = self.right_child(i):: Calculates the indices of the left and right children.
# if left < len(self.heap) and self.heap[left] < self.heap[smallest]:: If the left child exists and is smaller, update smallest.
# if right < len(self.heap) and self.heap[right] < self.heap[smallest]:: If the right child exists and is smaller, update smallest.
# if smallest != i:: If the smallest child is not the current node, swap them.
# self._heapify_down(smallest):: Recursively heapify down the affected subtree.



# Decrease Key Method

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        self._heapify_up(i)

# def decrease_key(self, i, new_val):: Decreases the value of the element at index i to new_val and restores the heap property.
# self.heap[i] = new_val:: Updates the value at index i.
# self._heapify_up(i):: Calls _heapify_up to maintain the min-heap property after the decrease.



# Delete Method

    def delete(self, i):
        self.decrease_key(i, float('-inf'))
        self.extract_min()

# def delete(self, i):: Deletes the element at index i.
# self.decrease_key(i, float('-inf')):: Sets the value of the element to negative infinity (smallest possible value) and heapifies up to move it to the root.
# self.extract_min():: Extracts the root, effectively removing the element.



# Build Heap Method

    def build_heap(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

# def build_heap(self, arr):: Builds a heap from an arbitrary array arr.
# self.heap = arr[:]:: Copies the array into the heap list.
# for i in range(len(self.heap) // 2 - 1, -1, -1):: Starts heapifying from the last non-leaf node up to the root.
# self._heapify_down(i):: Ensures the min-heap property for each subtree.


# Print Heap Method

    def print_heap(self):
        print("Heap array:", self.heap)

# def print_heap(self):: Prints the current state of the heap.


# Example Usage

# min_heap = MinHeap()
# min_heap.insert(3)
# min_heap.insert(2)
# min_heap.insert(1)
# min_heap.insert(15)
# min_heap.insert(5)
# min_heap.insert(4)
# min_heap.insert(45)
# min_heap.print_heap()  # Output: Heap array: [1, 3, 2, 15, 5, 4, 45]

# print("Extracted Min:", min_heap.extract_min())  # Output: Extracted Min: 1
# min_heap.print_heap()  # Output: Heap array: [2, 3, 4, 15, 5, 45]

# min_heap.delete(1)
# min_heap.print_heap()  # Output: Heap array: [2, 5, 4, 15, 45]
# min_heap.insert(x): Inserts elements into the min-heap.
# min_heap.print_heap(): Displays the heap after insertion.
# min_heap.extract_min(): Removes and displays the smallest element.
# min_heap.delete(1): Deletes the element at index 1 and then prints the heap.













# Min-Heap ( Code B )












## Read This:

## If you saw the YT video you already know how this binary heap works 


# First we will have some method to get the parent, left child, and right child of any given node
# Then we gonna insert data in our heap we use the append function for that and then we gonna move up in our tree
# The move_up method will see if our node is less than the parent node, move up our node 
#     5                                                                      
#    / \   ----->  After move_up function we have ---->                     
#   2            
# 
# after move_up function we have
# 
#      
#     2                                                                      
#    / \                      
#   5               
#                                         
# Now all heap properties are satisfied

## Delete method

# if we wanna remove a node in our binary heap, then we replace that node value with another value in this case we do '-inf'. why -inf? cause -inf will be the smallest number in our tree as when we do call move_up function, the '-inf' node will go to the top of the tree 
# As I explained above we do the same in  the delete and change_node function
# after our root node or top node is '-inf' ( which is the smallest ) we will replace this with the last inserted value in our tree 
# It means if we inserted [1, 3, 2, 15, 5, 4, 45] This all value then our top/root node will be 45 cause that's last
# After replacing we just do the opposite of move_up we do move_down 
# We check if our node, left and right child and if it is smaller than our node we swap the values, we do this recursively so all nodes will be in the right position



class MinHeap:
    def __init__(self):
        self.heap = [] # Declare a heap

    def parent(self, node):
        return ( node - 1) // 2 # return the parnent node of a given node, `( node - 1) // 2` this is the formula
    
    def left_child(self, node):
        return 2 * node + 1 # return the left child of a given node 
    
    def right_child(self, node):
        return 2 * node + 2 # return the right child of a given node
    
    def insert(self, data): # we are inserting a data 
        self.heap.append(data) # put the new data in last of our heap
        self.move_up(len(self.heap) - 1) # 

    def move_up(self, node_index):
        while node_index > 0 and self.heap[node_index] < self.heap[self.parent(node_index)]: # check if our node value is less then our parent value
            self.heap[self.parent(node_index)], self.heap[node_index] = self.heap[node_index], self.heap[self.parent(node_index)] # if it is swap the values
            node_index = self.parent(node_index) # keep doing this until tree is balanced

    def delete(self, node): # delete a given node
        self.change_node(node, float('-inf')) # we replace that node value with '-inf'
        self.extract_last_node()

    def change_node(self, node, new_val): 
        self.heap[node] = new_val # change our node value to new_val
        self.move_up(node) # move up and balance the tree 

    def extract_last_node(self):
        if len(self.heap) == 0: # if heap is empty return none
            return 
        
        if len(self.heap) == 1: # if heap len is 1 just pop the element
            return self.heap.pop()
        
        root_node = self.heap[0] # save our first heap value in root_node
        self.heap[0] = self.heap.pop() # replace heap first value with last
        self.move_down(0) # move down to balance the tree
        return root_node
    
    def move_down(self, node):
        largest = node 
        left = self.left_child(node) # got the left child of node
        right = self.right_child(node) # got the right child of node

        if left < len(self.heap) and self.heap[left] < self.heap[largest]: # if left child of our node is less then our node we update laregest to left
            largest = left

        if right < len(self.heap) and self.heap[right] < self.heap[largest]: # if right child of our node is less then our node we update laregest to right
            largest = right

        if largest != node: # if largest is not the same node 
            self.heap[node], self.heap[largest] = self.heap[largest], self.heap[node] # we swap the our node and largest node
            self.move_down(largest) # recursily doing so tree will be balance 

    def build_heap(self, arr):
        self.heap = arr[:]
        # Start heapifying from the last non-leaf node down to the root
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def print_heap(self):
        print("Heap array:", self.heap)
    

# Example Usage
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)
min_heap.insert(15)
min_heap.insert(5)
min_heap.insert(4)
min_heap.insert(45)

min_heap.print_heap()  # Output: Heap array: [1, 3, 2, 15, 5, 4, 45]

print("Extracted Min:", min_heap.extract_last_node())  # Output: Extracted Min: 1
min_heap.print_heap()  # Output: Heap array: [2, 3, 4, 15, 5, 45]

min_heap.delete(1)
min_heap.print_heap()  # Output: Heap array: [2, 5, 4, 15, 45]











## Max-Heap ( if you understand Min-Heap then max heap its just the opposite of that you can just take a look and you will understand ) 









class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return ( i - 1) // 2
    
    def left_child(self, node):
        return 2 * node + 1
    
    def right_child(self, node):
        return 2 * node + 2
    
    def insert(self, data):
        self.heap.append(data)
        self.move_up(len(self.heap) - 1)

    def move_up(self, node_index):
        while node_index > 0 and self.heap[node_index] > self.heap[self.parent(node_index)]:
            self.heap[self.parent(node_index)], self.heap[node_index] = self.heap[node_index], self.heap[self.parent(node_index)]
            node_index = self.parent(node_index)

    def delete(self, node):
        self.change_node(node, float('inf'))
        self.extract_last_node()

    def change_node(self, node, new_val):
        self.heap[node] = new_val
        self.move_up(node)

    def extract_last_node(self):
        if len(self.heap) == 0:
            return 
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.move_down(0)
        return root_node
    
    def move_down(self, node):
        largest = node
        left = self.left_child(node)
        right = self.right_child(node)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != node:
            self.heap[node], self.heap[largest] = self.heap[largest], self.heap[node]
            self.move_down(largest)

    def build_heap(self, arr):
        self.heap = arr[:]
        # Start heapifying from the last non-leaf node down to the root
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def print_heap(self):
        print("Heap array:", self.heap)
    

# Example Usage
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(1)
max_heap.insert(15)
max_heap.insert(5)
max_heap.insert(4)
max_heap.insert(45)

max_heap.print_heap()  # Output: Heap array: [45, 5, 15, 2, 3, 1, 4]

print("Extracted Max:", max_heap.extract_last_node())  # Output: Extracted Max: 45
max_heap.print_heap()  # Output: Heap array: [15, 5, 4, 2, 3, 1]

max_heap.delete(1)
max_heap.print_heap()  # Output: Heap array: [15, 3, 4, 2, 1]















## 17.7 Heap Sort










# Overview
# Heap Sort is a comparison-based sorting technique based on a binary heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end. The process is repeated for the remaining elements.

# Steps to Perform Heap Sort
# Build a Max-Heap from the input data. This step ensures that the largest element is at the root of the heap.
# Swap the root (maximum value) with the last element of the heap.
# Reduce the heap size by one and call the heapify function on the root of the heap to restore the max-heap property.
# Repeat steps 2 and 3 until the heap size is reduced to 1.


# Example
# Let's say we have an array [4, 10, 3, 5, 1] that we want to sort.

# Build Max-Heap:

# Initial array: [4, 10, 3, 5, 1]
# Convert to max-heap: [10, 5, 3, 4, 1]
# Sort the array:

# Swap the first and last element: [1, 5, 3, 4, 10]
# Heapify the reduced heap: [5, 4, 3, 1, 10]
# Repeat until the entire array is sorted: [1, 3, 4, 5, 10]



# Code Implementation

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example Usage
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print("Sorted array is", arr)


# Explanation of the Code




# heapify: Ensures that the subtree rooted at i satisfies the heap property. If the subtree violates the heap property, the method swaps the element at i with the largest of its children and recursively heapifies the affected subtree.
# heap_sort: Builds the heap, then repeatedly extracts the maximum element and heapifies the reduced heap.

# 1. Building the Heap: for i in range(arr_len // 2 - 1, -1, -1):
# Purpose: To convert the array into a valid max-heap.

# Explanation:

# Loop Range: range(arr_len // 2 - 1, -1, -1)
# Starts at arr_len // 2 - 1 (last non-leaf node).
# Ends at -1 (inclusive lower bound).
# Steps by -1 (decrements).
# Why this loop is necessary:

# Initial Heap Construction:

# The array is initially just a list of elements, not necessarily in any heap order.
# To sort the array using heap sort, we need to first ensure that the array satisfies the heap property.
# Heapify Process:

# From Bottom to Top: This loop ensures that all subtrees of the array are heapified, starting from the last non-leaf node all the way up to the root. This process is known as "heapifying" and is essential to create a valid heap.
# Reason for arr_len // 2 - 1: Leaf nodes (nodes that don’t have children) are inherently heaps by themselves. Thus, the process starts from the last non-leaf node, which is at index arr_len // 2 - 1. We then move upwards to ensure that all nodes follow the heap property.



# 2. Sorting the Heap: for i in range(arr_len - 1, 0, -1):
# Purpose: To sort the array using the max-heap property.

# Explanation:

# Loop Range: range(arr_len - 1, 0, -1)
# Starts at the last index (arr_len - 1).
# Ends at 1 (inclusive lower bound).
# Steps by -1 (decrements).
# Why this loop is necessary:

# Extract Max Element:

# Swap Root with Last Element: The root of the max-heap (which is the largest element) is swapped with the last element in the array. This places the largest element at the end of the array (the correct position for a sorted array).
# Heapify the Reduced Heap: After removing the largest element, the heap property might be violated, so we call heapify to restore the heap property on the reduced heap.


# Continue Sorting:

# This process is repeated for the reduced heap size (i decreasing with each iteration) until the entire array is sorted.



# Summary
# First Loop (for i in range(arr_len // 2 - 1, -1, -1)): Ensures that the entire array is a valid heap.
# Second Loop (for i in range(arr_len - 1, 0, -1)): Extracts elements from the heap one by one and sorts them.
# Both loops are essential: the first for building the heap and the second for sorting it.







# Real-Life Example and Industry Uses


# Heap Sort is used in scenarios where the entire data set needs to be sorted, and it's particularly useful when we have limited memory since it is an in-place sorting algorithm. While it is not as widely used as quicksort or mergesort due to its slower average-case performance, it is used in systems where reliability is more critical than performance, such as embedded systems.








# 17.8 heapq in Python








# Overview
# heapq is a module in Python that provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. It supports functions to add and remove the smallest elements in a heap.

# Common Functions in heapq


# heapq.heappush(heap, item): Pushes the item onto the heap, maintaining the heap invariant.
# heapq.heappop(heap): Pops the smallest item from the heap, maintaining the heap invariant.
# heapq.heappushpop(heap, item): Pushes a new item on the heap and then pops and returns the smallest item from the heap.
# heapq.heapreplace(heap, item): Pops the smallest item and pushes the new item onto the heap.
# heapq.heapify(x): Transforms the list x into a heap, in-place, in linear time.
# heapq.nlargest(n, iterable, key=None): Returns a list with the n largest elements from the dataset defined by iterable.
# heapq.nsmallest(n, iterable, key=None): Returns a list with the n smallest elements from the dataset defined by iterable.



# Example Usage

import heapq

# Create a heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

# Pop the smallest element
print(heapq.heappop(heap))  # Output: 1

# Push and pop in one operation
print(heapq.heappushpop(heap, 3))  # Output: 3

# Replace the smallest element
print(heapq.heapreplace(heap, 2))  # Output: 5

# Get the 2 largest elements
print(heapq.nlargest(2, heap))  # Output: [10, 2]

# Get the 2 smallest elements
print(heapq.nsmallest(2, heap))  # Output: [2, 10]



# Explanation of the Code



# The heap is created by pushing elements using heappush.
# heappop removes and returns the smallest element.
# heappushpop combines pushing a new item and popping the smallest item.
# heapreplace pops the smallest item and pushes a new item.
# nlargest and nsmallest are used to find the largest or smallest elements in the heap.




# Real-Life Example and Industry Uses


# heapq is useful in scenarios where you need to efficiently manage and retrieve the smallest (or largest) elements, such as in priority queues, job scheduling systems, and algorithms like Dijkstra's shortest path, which require efficiently fetching the next closest node.




