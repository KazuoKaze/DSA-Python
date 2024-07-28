
# https://www.youtube.com/watch?v=s9NEaxVvQnQ&list=PL5tcWHG-UPH2_HEOezeYqtMDoS6dOeNZ6&pp=iAQB

# go to this link to understand whole concept nicely

# 9. Linked Lists



# Linked lists are a fundamental data structure in computer science, providing a dynamic and flexible way to manage collections of data.


# 9.1 Problems with Array Data Structure


# Arrays have several limitations:

# Fixed Size: Arrays have a fixed size, which means once they are created, their size cannot be changed. This can lead to wasted memory if the array is too large or out-of-memory errors if the array is too small.
# Costly Insertions and Deletions: Inserting or deleting elements in an array requires shifting elements, which can be costly in terms of time complexity.
# Contiguous Memory: Arrays require contiguous blocks of memory, which might not always be available, especially for large arrays.


# 9.2 Linked List Introduction in Python


# Linked lists overcome many of the limitations of arrays. Each element in a linked list is a node, and each node contains:

# Data: The value of the node.
# Next Pointer: A reference to the next node in the list.


# 9.3 Simple Linked List Implementation in Python



class Node:
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list


# Explanation:

# Node Class: This class is used to create individual nodes. Each node has data and a next pointer.
# LinkedList Class: This class manages the linked list, starting with a head pointer.



# 9.4 Applications of Linked List



# Linked lists are used in various applications:

# Dynamic Memory Allocation: Linked lists can grow and shrink in size dynamically.
# Implementing Stacks and Queues: Linked lists can be used to implement stack and queue data structures.
# Adjacency List for Graphs: Used to represent graphs.
# Hash Tables with Chaining: Handle collisions in hash tables.



# 9.5 Traversing a Linked List in Python




def traverse(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next
# Explanation:

# Start from the head and move to each next node, printing the data.



# 9.6 Search in Linked List




def search(self, key):
    current = self.head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False
# Explanation:

# Traverse the list and check if any node's data matches the key.



# 9.7 Insert at the Beginning of Linked List in Python




def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
# Explanation:

# Create a new node and point its next to the current head, then update the head to this new node.



# 9.8 Insert at the End of Linked List


def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    last_node = self.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
# Explanation:

# Traverse to the end of the list and link the new node there.


# 9.9 Insert at a Given Position in Singly Linked List



def insert_at_position(self, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return
    current_node = self.head
    for _ in range(position - 1):
        if current_node is None:
            raise Exception("Position out of bounds")
        current_node = current_node.next
    new_node.next = current_node.next
    current_node.next = new_node
# Explanation:

# Traverse to the node just before the position and insert the new node there.



# 9.10 Delete First Node of Linked List in Python



def delete_first(self):
    if self.head:
        self.head = self.head.next
# Explanation:

# Move the head pointer to the next node.


# 9.11 Delete Last Node of Linked List



def delete_last(self):
    if not self.head:
        return
    if not self.head.next:
        self.head = None
        return
    second_last = self.head
    while second_last.next.next:
        second_last = second_last.next
    second_last.next = None
# Explanation:

# Traverse to the second last node and unlink the last node.


# 9.12 Delete a Node with Pointer Given to It



def delete_node(self, node):
    if node and node.next:
        node.data = node.next.data
        node.next = node.next.next
# Explanation:

# Copy data from the next node to the current node and unlink the next node.



# 9.13 Sorted Insert Linked List in Python




def sorted_insert(self, data):
    new_node = Node(data)
    if not self.head or self.head.data >= data:
        new_node.next = self.head
        self.head = new_node
        return
    current_node = self.head
    while current_node.next and current_node.next.data < data:
        current_node = current_node.next
    new_node.next = current_node.next
    current_node.next = new_node
# Explanation:

# Traverse to the correct position and insert the new node in a sorted manner.


# 9.14 Middle of Linked List




def find_middle(self):
    slow_ptr = self.head
    fast_ptr = self.head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.data
# Explanation:

# Use two pointers, slow and fast, to find the middle node.



# 9.15 Nth Node from End of Linked List



def nth_from_end(self, n):
    main_ptr = self.head
    ref_ptr = self.head
    for _ in range(n):
        if not ref_ptr:
            return None
        ref_ptr = ref_ptr.next
    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    return main_ptr.data
# Explanation:

# Use two pointers to find the nth node from the end.


# 9.16 Remove Duplicates from a Sorted Singly Linked List




def remove_duplicates(self):
    current_node = self.head
    while current_node and current_node.next:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
# Explanation:

# Traverse the list and skip nodes with duplicate data.



# 9.17 Reverse a Linked List in Python



def reverse(self):
    prev_node = None
    current_node = self.head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    self.head = prev_node
# Explanation:

# Reverse the links between nodes iteratively.



# 9.18 Recursive Reverse a Linked List (Part 1)




def recursive_reverse(self, node):
    if not node or not node.next:
        return node
    new_head = self.recursive_reverse(node.next)
    node.next.next = node
    node.next = None
    return new_head
# Explanation:

# Reverse the list recursively by updating the next pointers.



# 9.19 Recursive Reverse a Linked List (Part 2)




def recursive_reverse(self):
    def _reverse_recursive(current, previous):
        if not current:
            return previous
        next_node = current.next
        current.next = previous
        return _reverse_recursive(next_node, current)
    self.head = _reverse_recursive(self.head, None)
# Explanation:

# Reverse the list recursively using a helper function.


# Real-World Applications


# Dynamic Memory Allocation: Linked lists can be used in dynamic memory allocation to manage free and used memory blocks.
# Implementing Data Structures: Linked lists are used to implement other data structures like stacks, queues, and graphs.
# Undo Functionality in Text Editors: A linked list of states can be used to implement undo functionality in text editors.
# Music Playlist: In music players, a linked list can be used to represent the playlist, allowing easy addition and removal of songs.


# Advantages of Linked Lists


# Dynamic Size: Can grow and shrink in size dynamically.
# Ease of Insertions/Deletions: Insertions and deletions are easier and more efficient than in arrays.


# Disadvantages of Linked Lists


# Memory Overhead: Requires extra memory for pointers.
# No Random Access: Elements cannot be accessed directly by index.
# Cache Unfriendly: Nodes may not be stored contiguously in memory, leading to cache inefficiency.




# Here's the full code with detailed comments explaining each line:






class Node:
    def __init__(self, data):
        # Initialize a node with data and a next pointer
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node, initially None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with head set to None
        self.head = None  # Head of the list

    def append(self, data):
        # Append a new node with the given data to the end of the list
        new_node = Node(data)  # Create a new node
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        last_node = self.head  # Start from the head
        while last_node.next:
            # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the new node at the end

    def prepend(self, data):
        # Prepend a new node with the given data to the beginning of the list
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Set the new node as the head

    def insert_at_position(self, data, position):
        # Insert a new node with the given data at the specified position
        new_node = Node(data)  # Create a new node
        if position == 0:
            # If position is 0, prepend the new node
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head  # Start from the head
        for _ in range(position - 1):
            # Traverse to the node just before the specified position
            if current_node is None:
                raise Exception("Position out of bounds")
            current_node = current_node.next
        new_node.next = current_node.next  # Link the new node to the next node
        current_node.next = new_node  # Link the current node to the new node

    def delete_first(self):
        # Delete the first node of the list
        if self.head:
            self.head = self.head.next  # Move the head to the next node

    def delete_last(self):
        # Delete the last node of the list
        if not self.head:
            return
        if not self.head.next:
            # If there's only one node, set head to None
            self.head = None
            return
        second_last = self.head  # Start from the head
        while second_last.next.next:
            # Traverse to the second last node
            second_last = second_last.next
        second_last.next = None  # Unlink the last node

    def delete_node(self, node):
        # Delete a node given only a pointer to it
        if node and node.next:
            node.data = node.next.data  # Copy data from the next node to the current node
            node.next = node.next.next  # Link to the node after the next node

    def sorted_insert(self, data):
        # Insert a new node with the given data in a sorted manner
        new_node = Node(data)  # Create a new node
        if not self.head or self.head.data >= data:
            # If list is empty or new node should be inserted before the head
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head  # Start from the head
        while current_node.next and current_node.next.data < data:
            # Traverse to the correct insertion point
            current_node = current_node.next
        new_node.next = current_node.next  # Link the new node to the next node
        current_node.next = new_node  # Link the current node to the new node

    def find_middle(self):
        # Find and return the middle element of the list
        slow_ptr = self.head  # Slow pointer moves one step at a time
        fast_ptr = self.head  # Fast pointer moves two steps at a time
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.data  # Slow pointer will be at the middle

    def nth_from_end(self, n):
        # Find and return the nth node from the end
        main_ptr = self.head
        ref_ptr = self.head
        for _ in range(n):
            # Move ref_ptr n steps ahead
            if not ref_ptr:
                return None
            ref_ptr = ref_ptr.next
        while ref_ptr:
            # Move both pointers until ref_ptr reaches the end
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        return main_ptr.data  # main_ptr will be at the nth node from the end

    def remove_duplicates(self):
        # Remove duplicates from a sorted list
        current_node = self.head
        while current_node and current_node.next:
            if current_node.data == current_node.next.data:
                # If current node's data is equal to next node's data, skip the next node
                current_node.next = current_node.next.next
            else:
                # Otherwise, move to the next node
                current_node = current_node.next

    def reverse(self):
        # Reverse the linked list iteratively
        prev_node = None  # Previous node starts as None
        current_node = self.head  # Current node starts as head
        while current_node:
            next_node = current_node.next  # Store the next node
            current_node.next = prev_node  # Reverse the link
            prev_node = current_node  # Move prev_node one step ahead
            current_node = next_node  # Move current_node one step ahead
        self.head = prev_node  # Update head to the new first node

    def recursive_reverse(self, node):
        # Reverse the linked list recursively (part 1)
        if not node or not node.next:
            return node  # Base case: if node is None or node is the last node
        new_head = self.recursive_reverse(node.next)  # Reverse the rest of the list
        node.next.next = node  # Make the next node point to the current node
        node.next = None  # Set the next pointer of the current node to None
        return new_head  # Return the new head of the reversed list

    def recursive_reverse(self):
        # Reverse the linked list recursively (part 2)
        def _reverse_recursive(current, previous):
            if not current:
                return previous  # Base case: if current is None, return the previous node
            next_node = current.next  # Store the next node
            current.next = previous  # Reverse the link
            return _reverse_recursive(next_node, current)  # Recur for the next node
        self.head = _reverse_recursive(self.head, None)  # Update head to the new first node

    def print_list(self):
        # Print all elements of the linked list
        current_node = self.head  # Start from the head
        while current_node:
            print(current_node.data)  # Print the data of the current node
            current_node = current_node.next  # Move to the next node

# Example usage:
ll = LinkedList()
ll.append(1)  # Append 1 to the list
ll.append(2)  # Append 2 to the list
ll.append(3)  # Append 3 to the list
ll.print_list()  # Output: 1 2 3

ll.prepend(0)  # Prepend 0 to the list
ll.print_list()  # Output: 0 1 2 3

ll.insert_at_position(1.5, 2)  # Insert 1.5 at position 2
ll.print_list()  # Output: 0 1 1.5 2 3

ll.delete_first()  # Delete the first node
ll.print_list()  # Output: 1 1.5 2 3

ll.delete_last()  # Delete the last node
ll.print_list()  # Output: 1 1.5 2

middle = ll.find_middle()  # Find the middle element
print("Middle element:", middle)  # Output: 1.5

nth_node = ll.nth_from_end(2)  # Find the 2nd node from the end
print("2nd node from end:", nth_node)  # Output: 1.5

ll.remove_duplicates()  # Remove duplicates from the list
ll.print_list()  # Output: 1 1.5 2

ll.reverse()  # Reverse the list
ll.print_list()  # Output: 2 1.5 1

ll.head = ll.recursive_reverse(ll.head)  # Reverse the list recursively
ll.print_list()  # Output: 1 1.5 2


# Linked List Basics
# How it Works:

# Each node contains data and a reference to the next node.
# The list starts with a head pointer, which points to the first node.
# Things to Remember:

# Dynamic Size: Linked lists can grow and shrink in size by adding or removing nodes.
# Efficient Insertions/Deletions: Operations are efficient as they involve changing pointers.
# Traversal: To access elements, you must traverse from the head to the desired node.




# all the other test thing and prcatice thing to learn

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## we get 2 diffent keys, keys is just data element in nodes then swap the nodes 

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def swap(self, first_node, second_node):
        ## 1 2 3 4 5
        the_first_node_prev_node = None
        the_first_node_head = self.head

        while the_first_node_head and the_first_node_head.data != first_node:
            the_first_node_prev_node = the_first_node_head
            the_first_node_head = the_first_node_head.next

        the_second_node_prev_node = None
        the_second_node_head = self.head

        while the_second_node_head and the_second_node_head.data != second_node:
            the_second_node_prev_node = the_second_node_head
            the_second_node_head = the_second_node_head.next

        if the_first_node_prev_node:
            the_first_node_prev_node.next = the_second_node_head
        else:
            self.head = the_second_node_head
        
        if the_second_node_prev_node:
            the_second_node_prev_node.next = the_first_node_head
        else:
            self.head = the_first_node_head

        the_first_node_head.next, the_second_node_head.next = the_second_node_head.next, the_first_node_head.next


    def print_list(self):
        the_head = self.head
        while the_head:
            print(the_head.data)
            the_head = the_head.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print_list()
ll.swap(1, 3)

print('the swap list is:')
ll.print_list()



## calcukating the length og the linked list 
## In both way iterative and recursive


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        the_head = self.head
        while the_head.next:
            the_head = the_head.next

        the_head.next = new_node

    def len_iterative(self):
        the_head = self.head
        count = 0
        while the_head:
            count += 1
            the_head = the_head.next
        
        print('the len of the ll is', count)

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def print(self):
        the_head = self.head
        while the_head:
            print(the_head.data)
            the_head = the_head.next 
        

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()
ll.len_iterative()
print('recursive length is: ',  ll.len_recursive(ll.head))




## Delete operation 
## delete a node and delete on a position both 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        the_head = self.head
        while the_head.next:
            the_head = the_head.next
        the_head.next = new_node

    def deletion(self, data):
        the_head = self.head
        the_prev_node = None
        while the_head and the_head.data != data:
            the_prev_node = the_head
            the_head = the_head.next

        if the_head:
            if the_prev_node:
                the_prev_node.next = the_head.next
                the_head.next = None
                the_head.data = None
            else:
                self.head = the_head.next
                the_head.next = None
                the_head.data = None
        else:
            print('node not found')

    def del_at_position(self, position):
        the_head = self.head
        count = 0
        prev_node = None

        while the_head and count != position:
            prev_node = the_head
            count += 1
            the_head = the_head.next

        if the_head:
            if prev_node:
                prev_node.next = the_head.next
            else:
                self.head = the_head.next
        else:
            print('node not found')

    def print(self):
        the_head = self.head
        while the_head:
            print(the_head.data)
            the_head = the_head.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.del_at_position(0)
ll.print()
ll.deletion(3)
print('after del')
ll.print()


## reverse the Linked List with iterative and recursive both

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        the_head = self.head
        prev_node = None
        while the_head:
            next_node = the_head.next
            the_head.next = prev_node
            prev_node = the_head
            the_head = next_node
        self.head = prev_node

    def reverse_reursive(self):
        def _revesre_recursive(the_head, prev_node):
            if not the_head:
                return prev_node
            next_node = the_head.next
            the_head.next = prev_node
            prev_node = the_head
            the_head = next_node
            return _revesre_recursive(the_head, prev_node)
        self.head = _revesre_recursive(self.head, None)

    def upend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        the_head = self.head
        self.head = new_node
        new_node.next = the_head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        the_head = self.head
        while the_head.next:
            the_head = the_head.next
        the_head.next = new_node

    def append_at_pos(self, data, pos):
        new_node = Node(data)
        prev_node = None
        count = 0
        the_head = self.head
        while the_head and count != pos:
            prev_node = the_head
            count += 1
            the_head = the_head.next

        if the_head:
            if prev_node:
                prev_node.next = new_node
                new_node.next = the_head
            else:
                self.head = new_node
                new_node.next = the_head
        else:
            print('cant insert the node position not found')

    def delete(self, data):
        the_head = self.head
        prev_node = None
        while the_head and the_head.data != data:
            prev_node = the_head
            the_head = the_head.next

        if the_head:
            if prev_node:
                prev_node.next = the_head.next
            else:
                self.head = the_head.next
        else:
            print('cant find the node with this data')

    def print(self):
        the_head = self.head
        while the_head:
            print(the_head.data)
            the_head = the_head.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()
print('after reverse')
ll.reverse()
ll.reverse_reursive()
ll.print()
print('after append pos')
ll.append_at_pos(6, 2)
ll.print()
print('after del')
ll.delete(6)
ll.print()



## merge 2 sorted LinkedList 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        the_head = self.head
        while the_head.next:
            the_head = the_head.next
        the_head.next = new_node

    def print(self):
        the_head = self.head
        while the_head:
            print(the_head.data, end=" -> ")
            the_head = the_head.next
        print("None")

def merge_list(l1, l2):
    a_dumby_node = Node(0)
    tail = a_dumby_node

    p = l1.head
    q = l2.head

    while p and q:
        if p.data <= q.data:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next

        tail = tail.next

    if p:
        tail.next = p
    if q:
        tail.next = q

    return a_dumby_node.next
            

ll = LinkedList()
ll.append(1)
ll.append(5)
ll.append(7) 
ll.append(9)
ll.append(10)

ll2 = LinkedList()
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(6)
ll2.append(8)

merge_head = merge_list(ll, ll2)
merge_list = LinkedList()
merge_list.head = merge_head
merge_list.print()
