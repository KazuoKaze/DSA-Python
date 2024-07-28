

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



# 13.4 Implementation of Queue using Array
# Array Implementation:


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued {item}")
        return item

    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[self.front]

    def rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[self.rear]

# Usage
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue()
queue.dequeue()
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)  # Queue is full



# 13.5 Linked List Implementation of Queue in Python
# Linked List Implementation:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear is None
        print(f"Dequeued {temp.data}")
        return temp.data

    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.front.data

    def rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.rear.data

# Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.dequeue()
queue.enqueue(40)
queue.enqueue(50)
# Detailed Breakdown


# Array Implementation
# Initialization:


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1
# self.capacity: Maximum capacity of the queue.
# self.queue: List to store queue elements.
# self.front: Index of the front element.
# self.size: Current size of the queue.
# self.rear: Index of the rear element.



# Enqueue Operation:


def enqueue(self, item):
    if self.isFull():
        print("Queue is full")
        return
    self.rear = (self.rear + 1) % self.capacity
    self.queue[self.rear] = item
    self.size += 1
    print(f"Enqueued {item}")
# Check if the queue is full.
# Update self.rear to the next position (circularly).
# Add the item at the rear.
# Increase the size.
# Dequeue Operation:


# def dequeue(self):
#     if self.isEmpty():
#         print("Queue is empty")
#         return
#     item = self.queue[self.front]
#     self.front = (self.front + 1) % self.capacity
#     self.size -= 1
#     print(f"Dequeued {item}")
#     return item
# Check if the queue is empty.
# Get the item at the front.
# Update self.front to the next position (circularly).
# Decrease the size.
# Linked List Implementation
# Initialization:


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# self.data: Stores the data.
# self.next: Points to the next node.
# Queue Initialization:


# class Queue:
#     def __init__(self):
#         self.front = self.rear = None
# self.front: Points to the front node.
# self.rear: Points to the rear node.
# Enqueue Operation:


# def enqueue(self, item):
#     new_node = Node(item)
#     if self.rear is None:
#         self.front = self.rear = new_node
#         return
#     self.rear.next = new_node
#     self.rear = new_node
#     print(f"Enqueued {item}")
# Create a new node with the item.
# If the queue is empty, both front and rear point to the new node.
# Otherwise, link the new node to the end of the queue and update rear.
# Dequeue Operation:


# def dequeue(self):
#     if self.isEmpty():
#         print("Queue is empty")
#         return
#     temp = self.front
#     self.front = temp.next
#     if self.front is None:
#         self.rear is None
#     print(f"Dequeued {temp.data}")
#     return temp.data
# Check if the queue is empty.
# Get the front node.
# Update front to the next node.
# If the queue becomes empty, set rear to None.