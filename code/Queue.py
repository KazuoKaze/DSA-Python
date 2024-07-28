## Please Read this.. starting para

# Understanding Queues
# You can read and understand the entire section on queues, or simply check out the final code example provided. This example is sufficient for understanding the concept of queues.

# Additionally, you can use this example both with and without a maxsize, and with a while loop. However, be sure to read the last paragraph before implementing the while loop to ensure you have all the necessary context.

# Also check out Implementation of Queue using Array cause thats also important

# 13.1 Queue in Python


# A queue is a linear data structure that follows the First In First Out (FIFO) principle, where the first element added to the queue is the first one to be removed. Think of it like a line of people waiting to buy tickets. The first person in line is the first one to get the ticket.

# 13.2 Queue Data Structure
# Real-life examples:

# Waiting lines (e.g., ticket counters, checkout lines at stores)
# Printer queues
# Task scheduling (e.g., CPU task scheduling)
# Operations:

# Enqueue: Add an element to the end of the queue.
# Dequeue: Remove an element from the front of the queue.
# Peek/Front: Get the front element without removing it.
# IsEmpty: Check if the queue is empty.
# IsFull: Check if the queue is full (in case of bounded queues).


# 13.3 Application of Queue Data Structure
# Applications:



# Task Scheduling: Operating systems use queues to manage processes in a multitasking environment.
# Breadth-First Search (BFS): Graph traversal algorithms use queues.
# Buffering: Queues are used in buffering (e.g., keyboard buffer, IO buffer).
# Simulations: Queues are used in simulations of real-world systems like traffic management, customer service centers, etc.



# 13.1 Queue in Python
# Python provides a built-in queue module, which has the Queue class for implementing queue data structures.

# Example using Python's built-in queue module:


from queue import Queue

# Create a queue
q = Queue(maxsize=5)

# Add elements to the queue
q.put(1)
q.put(2)
q.put(3)

# Remove elements from the queue
print(q.get())  # Output: 1
print(q.get())  # Output: 2

# Check if the queue is empty
print(q.empty())  # Output: False

# Check if the queue is full
print(q.full())  # Output: False

# Code Breakdown:

# from queue import Queue: Imports the Queue class from the queue module.
# q = Queue(maxsize=5): Creates a queue with a maximum size of 5.
# q.put(1), q.put(2), q.put(3): Adds elements 1, 2, and 3 to the queue.
# print(q.get()): Removes and prints the first element added to the queue (FIFO order).
# print(q.empty()): Checks if the queue is empty.
# print(q.full()): Checks if the queue is full.
# 13.2 Queue Data Structure
# A queue can be implemented using an array or a linked list. Here, we'll implement a queue using an array.


# 13.4 Implementation of Queue using Array

class ArrayQueue:
    def __init__(self, maxsize):
        self.queue = []
        self.maxsize = maxsize

    def enqueue(self, item):
        if len(self.queue) < self.maxsize:
            self.queue.append(item)
        else:
            print("Queue is full")

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.maxsize

    def size(self):
        return len(self.queue)


# Code Breakdown:

# class ArrayQueue: Defines a new class called ArrayQueue.
# def __init__(self, maxsize): Initializes the queue with an empty list and a maximum size.
# self.queue = []: Creates an empty list to store queue elements.
# self.maxsize = maxsize: Sets the maximum size of the queue.
# def enqueue(self, item): Adds an element to the end of the queue if it's not full.
# def dequeue(self): Removes and returns the first element from the queue if it's not empty.
# def is_empty(self): Checks if the queue is empty.
# def is_full(self): Checks if the queue is full.
# def size(self): Returns the current size of the queue.
# Example:


# q = ArrayQueue(3)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# print(q.dequeue())  # Output: 1
# print(q.is_empty())  # Output: False
# print(q.is_full())  # Output: True
# print(q.size())  # Output: 2


# 13.5 Linked List Implementation of Queue in Python


# A queue can also be implemented using a linked list where each node contains data and a reference to the next node.

# Linked List Node Class:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue Class Using Linked List:


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    

# Code Breakdown:

# class Node: Defines a new class called Node for the linked list node.
# def __init__(self, data): Initializes a node with data and sets the next pointer to None.
# class LinkedListQueue: Defines a new class called LinkedListQueue.
# def __init__(self): Initializes the queue with front and rear pointers set to None.
# def enqueue(self, item): Adds a new node with the given item to the end of the queue.
# def dequeue(self): Removes and returns the front node of the queue.
# def is_empty(self): Checks if the queue is empty.
# def peek(self): Returns the front node's data without removing it.
# Example:


# q = LinkedListQueue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# print(q.dequeue())  # Output: 1
# print(q.is_empty())  # Output: False
# print(q.peek())  # Output: 2


# 13.3 Application of Queue Data Structure
# Queues are used in various applications, including:

# CPU Scheduling: Jobs waiting for CPU time are stored in a queue.
# Printer Spooling: Documents waiting to be printed are stored in a queue.
# Call Center Systems: Calls waiting to be answered are queued.
# Breadth-First Search: In graph traversal algorithms, a queue is used to keep track of nodes to be visited.


# Queue Implementation in LinkedList with also the maxsize value


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, maxsize):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
        self.size = 0

    def put(self, data):
        if self.size < self.maxsize:
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.size += 1
        else:
            raise Exception('Out of maxsize')

    def get(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        the_head = self.head
        self.head = self.head.next
        self.size -= 1
        return the_head.data
    
    def is_empty(self):
        return self.size == 0
        
    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.head.data
    
    def print_queue_in_ll(self):
        if not self.is_empty():
            the_head = self.head
            while the_head:
                print(the_head.data, end=' -> ')
                the_head = the_head.next
            print('None')
    
q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
q.print_queue_in_ll()

print(q.get())
print(q.is_empty())
print(q.peek())

q.print_queue_in_ll()


## Please Read this



# using a tail pointer has some advantages in terms of efficiency:

# Efficiency: Using a tail pointer allows direct access to the end of the queue, making the insertion operation (put) O(1) instead of O(n) (where n is the number of elements in the queue). Without a tail pointer, you need to traverse the entire queue to find the end, which can be time-consuming for large queues.

# Simpler Code: Using a tail pointer simplifies the code for insertion. You don't need to handle a special case for the empty queue separately.

