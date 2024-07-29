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


# Deque Implementation Using List in Python
# Python's collections module provides a deque class which is optimized for quick append and pop operations from both ends.

# Here is a basic implementation of a deque using a list in Python:


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items.append(item)  # Adds an item to the rear of the deque

    def appendleft(self, item):
        self.items.insert(0, item)  # Adds an item to the front of the deque

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        return self.items.pop()  # Removes and returns an item from the rear

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        return self.items.pop(0)  # Removes and returns an item from the front

    def size(self):
        return len(self.items)  # Returns the number of items in the deque

    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.items[0]  # Peeks at the front item without removing it

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.items[-1]  # Peeks at the rear item without removing it

# Example usage
deque = Deque()
deque.append(1)
deque.append(2)
deque.appendleft(0)
print("Deque after appending 1, 2 and appendleft 0:", deque.items)  # [0, 1, 2]
print("Pop from rear:", deque.pop())  # 2
print("Pop from front:", deque.popleft())  # 0
print("Peek front:", deque.peek_front())  # 1
print("Is empty:", deque.is_empty())  # False
print("Size:", deque.size())  # 1


# Breakdown of the Code:
# __init__(self):

# Initializes the deque with an empty list (self.items).
# self.items = []
# is_empty(self):

# Checks if the deque is empty by returning the result of len(self.items) == 0.
# append(self, item):

# Adds an item to the rear of the deque using self.items.append(item).
# appendleft(self, item):

# Adds an item to the front of the deque using self.items.insert(0, item).
# pop(self):

# Removes and returns an item from the rear of the deque using self.items.pop().
# Raises an IndexError if the deque is empty.
# popleft(self):

# Removes and returns an item from the front of the deque using self.items.pop(0).
# Raises an IndexError if the deque is empty.
# size(self):

# Returns the number of items in the deque using len(self.items).
# peek_front(self):

# Returns the front item without removing it using self.items[0].
# Raises an IndexError if the deque is empty.
# peek_rear(self):

# Returns the rear item without removing it using self.items[-1].
# Raises an IndexError if the deque is empty.



# Deque Implementation Using Linked List in Python
# Here is an implementation of a deque using a linked list:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Deque is empty
            self.head = new_node
            self.tail = new_node
        else:  # Add to the end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendLeft(self, data):
        new_node = Node(data)
        if not self.head:  # Deque is empty
            self.head = new_node
            self.tail = new_node
        else:  # Add to the front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        the_tail = self.tail
        if self.tail.prev:  # More than one element
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # Only one element
            self.head = None
            self.tail = None
        self.size -= 1
        return the_tail.data
        
    def popLeft(self):
        if self.is_empty():
            return None
        the_head = self.head
        if self.head.next:  # More than one element
            self.head = self.head.next
            self.head.prev = None
        else:  # Only one element
            self.head = None
            self.tail = None
        self.size -= 1
        return the_head.data
        
    def peek_front(self):
        if not self.is_empty():
            return self.head.data
        return None
    
    def peek_rear(self):
        if not self.is_empty():
            return self.tail.data
        return None
        
    def print_deque(self):
        the_head = self.head
        while the_head:
            print(the_head.data, end=' -> ')
            the_head = the_head.next
        print('None')

# Example usage
deque = Deque()
deque.append(1)
deque.append(2)
deque.appendLeft(0)
deque.print_deque()
print("Pop from rear:", deque.pop())  # 2
deque.print_deque()
print("Pop from front:", deque.popLeft())  # 0
deque.print_deque()
print("Peek front:", deque.peek_front())  # 1
deque.print_deque()
print("Is empty:", deque.is_empty())  # False
deque.print_deque()
print("Size:", deque.size)  # 1
deque.print_deque()


# Breakdown of Code:
# Node Class:

# __init__(self, data): Initializes a node with data, next, and prev pointers set to None.
# Deque Class:

# __init__(self): Initializes the deque with head and tail pointers set to None and size set to 0.
# is_empty(self): Checks if the deque is empty.
# append(self, data): Adds a new node to the end of the deque.
# Creates a new node.
# Checks if the deque is empty; if yes, sets both head and tail to the new node.
# Otherwise, links the new node to the current tail and updates the tail.
# appendLeft(self, data): Adds a new node to the front of the deque.
# Creates a new node.
# Checks if the deque is empty; if yes, sets both head and tail to the new node.
# Otherwise, links the new node to the current head and updates the head.
# pop(self): Removes and returns the node from the end of the deque.
# Checks if the deque is empty; if yes, returns None.
# Otherwise, removes the tail node and updates the tail pointer.
# popLeft(self): Removes and returns the node from the front of the deque.
# Checks if the deque is empty; if yes, returns None.
# Otherwise, removes the head node and updates the head pointer.
# peek_front(self): Returns the data of the front node without removing it.
# peek_rear(self): Returns the data of the rear node without removing it.
# print_deque(self): Prints all elements in the deque from head to tail.


## My code with a slight different approch

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendLeft(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        else:
            the_head = self.head
            the_head.prev = new_node
            new_node.prev = None
            new_node.next = the_head
            self.head = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            the_tail = self.tail
            self.tail.prev.next = the_tail.next
            self.tail = the_tail.prev
            self.size -= 1
            return the_tail.data
        else:
            return None
        
    def popLeft(self):
        if not self.is_empty():
            the_head = self.head
            self.head = self.head.next
            self.size -= 1
            return the_head.data
        else:
            return None
        
    def peek_front(self):
        if not self.is_empty():
            return self.head.data
        else:
            return None
    
    def peek_rear(self):
        if not self.is_empty():
            return self.tail.data
        else:
            return None
        
    def print_deque(self):
        the_head = self.head
        while the_head:
            print(the_head.data, end=' -> ')
            the_head = the_head.next
        print('None')
        

deque = Deque()
deque.append(1)
deque.append(2)
deque.appendLeft(0)
# deque.print_deque()
print("Pop from rear:", deque.pop())  # 2
# deque.print_deque()
print("Pop from front:", deque.popLeft())  # 0
# deque.print_deque()
print("Peek front:", deque.peek_front())  # 1
# deque.print_deque()
print("Is empty:", deque.is_empty())  # False
# deque.print_deque()
print("Size:", deque.size)  # 1
# deque.print_deque()
