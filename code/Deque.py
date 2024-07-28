

# 14. Deque (Double-Ended Queue)


# A deque (pronounced "deck") is a linear data structure that allows insertion and deletion of elements from both ends (front and rear). It can be seen as a generalization of both stacks and queues.

# 14.1 Deque Introduction
# Definition:
# A deque is a data structure that allows elements to be added or removed from either end, making it a versatile structure for various applications.

# Operations:

# Insert Front: Add an element at the front.
# Insert Rear: Add an element at the rear.
# Delete Front: Remove an element from the front.
# Delete Rear: Remove an element from the rear.
# Get Front: Get the front element.
# Get Rear: Get the rear element.
# Is Empty: Check if the deque is empty.
# Is Full: Check if the deque is full (in case of bounded deques).
# 14.2 Deque Applications
# Applications:

# Palindromes: Checking if a word is a palindrome.
# Sliding Window: Finding the maximum or minimum in a sliding window of fixed size.
# Undo Operations: Implementing undo functionality in applications.
# Task Scheduling: Efficiently managing tasks with priority or time constraints.


# 14.3 Deque in Python
# Python provides a built-in module collections that includes the deque class, which supports thread-safe, memory-efficient operations.

# Example:


from collections import deque

# Create a deque
dq = deque()

# Add elements to the deque
dq.append(10)    # Add to the rear
dq.appendleft(20)  # Add to the front

# Remove elements from the deque
dq.pop()         # Remove from the rear
dq.popleft()     # Remove from the front

# Check the front and rear elements
front_element = dq[0]
rear_element = dq[-1]

# Check if deque is empty
is_empty = len(dq) == 0

# Output the deque
print(dq)


# 14.4 List Implementation of Deque in Python
# List-based Deque Implementation:


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

# Usage
dq = Deque()
dq.add_rear(10)
dq.add_front(20)
print(dq.remove_front())  # Output: 20
print(dq.remove_rear())   # Output: 10
print(dq.size())          # Output: 0



# 14.5 Linked List Implementation of Deque
# Node Class:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Linked List-based Deque Implementation:


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data

    def remove_rear(self):
        if self.is_empty():
            return None
        temp = self.rear
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return temp.data

    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            return None
        return self.rear.data

# Usage
dq = Deque()
dq.add_rear(10)
dq.add_front(20)
print(dq.remove_front())  # Output: 20
print(dq.remove_rear())   # Output: 10
# Detailed Breakdown
# List Implementation
# Initialization:


# class Deque:
#     def __init__(self):
#         self.items = []
# self.items: Initializes an empty list to store deque elements.
# Add to Front:


# def add_front(self, item):
#     self.items.insert(0, item)
# self.items.insert(0, item): Inserts an item at the front of the deque.
# Add to Rear:


# def add_rear(self, item):
#     self.items.append(item)
# self.items.append(item): Appends an item at the rear of the deque.
# Remove from Front:


# def remove_front(self):
#     if not self.is_empty():
#         return self.items.pop(0)
#     return None
# self.items.pop(0): Removes and returns the front item if the deque is not empty.
# Remove from Rear:


# def remove_rear(self):
#     if not self.is_empty():
#         return self.items.pop()
#     return None
# self.items.pop(): Removes and returns the rear item if the deque is not empty.
# Linked List Implementation
# Add to Front:


# def add_front(self, item):
#     new_node = Node(item)
#     if self.is_empty():
#         self.front = self.rear = new_node
#     else:
#         new_node.next = self.front
#         self.front.prev = new_node
#         self.front = new_node
# Creates a new node.
# If the deque is empty, both front and rear point to the new node.
# Otherwise, links the new node to the front and updates the front pointer.
# Add to Rear:


# def add_rear(self, item):
#     new_node = Node(item)
#     if self.is_empty():
#         self.front = self.rear = new_node
#     else:
#         new_node.prev = self.rear
#         self.rear.next = new_node
#         self.rear = new_node
# Creates a new node.
# If the deque is empty, both front and rear point to the new node.
# Otherwise, links the new node to the rear and updates the rear pointer.
# Remove from Front:


# def remove_front(self):
#     if self.is_empty():
#         return None
#     temp = self.front
#     self.front = self.front.next
#     if self.front is None:
#         self.rear = None
#     else:
#         self.front.prev = None
#     return temp.data
# Checks if the deque is empty.
# Removes the front node and updates the front pointer.
# If the deque becomes empty, sets rear to None.
# Remove from Rear:


# def remove_rear(self):
#     if self.is_empty():
#         return None
#     temp = self.rear
#     self.rear = self.rear.prev
#     if self.rear is None:
#         self.front = None
#     else:
#         self.rear.next = None
#     return temp.data
# Checks if the deque is empty.
# Removes the rear node and updates the rear pointer.
# If the deque becomes empty, sets front to None.