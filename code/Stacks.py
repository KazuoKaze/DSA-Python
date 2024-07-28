


# 12. Stacks



# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. Stacks are used in various applications, such as function call management in programming, expression evaluation, and backtracking algorithms.

# 12.1 Stack Data Structure
# Characteristics:
# LIFO (Last In, First Out): The last element added is the first to be removed.
# Operations:
# Push: Add an element to the top of the stack.
# Pop: Remove the top element from the stack.
# Peek/Top: Retrieve the top element without removing it.
# isEmpty: Check if the stack is empty.

# Real-Life Example:
# A stack of plates in a cafeteria is a real-life example of a stack data structure. The last plate placed on the stack is the first one to be removed.

# 12.2 Stack in Python
# Python provides a simple way to implement a stack using a list.

# Code Example:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

# Example usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()  # Output: [1, 2, 3]
print(s.pop())   # Output: 3
print(s.peek())  # Output: 2
print(s.is_empty())  # Output: False




# 12.3 Linked List Implementation of Stack in Python
# Using a linked list to implement a stack can provide better performance in some cases, as it avoids the overhead of dynamic array resizing.

# Code Example:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()  # Output: 3 -> 2 -> 1 -> None
print(s.pop())   # Output: 3
print(s.peek())  # Output: 2
print(s.is_empty())  # Output: False



# 12.4 Stack Applications
# Function Call Management: The call stack keeps track of function calls in programming languages.
# Expression Evaluation: Stacks are used in the evaluation and conversion of expressions (infix, prefix, postfix).
# Backtracking: Algorithms such as maze solving and puzzle solving use stacks to remember paths.
# Browser History: Navigating back and forth in a web browser.



# 12.5 Check for Balanced Parentheses in Python
# One common application of stacks is checking for balanced parentheses in an expression. This involves ensuring that every opening parenthesis has a corresponding closing parenthesis in the correct order.

# Code Example:


def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if not is_matching_pair(top_element, char):
                return False
    return stack.is_empty()

def is_matching_pair(opening, closing):
    pairs = { '(': ')', '[': ']', '{': '}' }
    return pairs.get(opening) == closing

# Example usage:
expression = "{[(a+b)*(c+d)]}"
print(is_balanced(expression))  # Output: True

expression = "{[(a+b)*(c+d)]"
print(is_balanced(expression))  # Output: False



# Detailed Breakdown of is_balanced:


def is_balanced(expression):
    stack = Stack()  # Initialize a stack to keep track of opening brackets
    for char in expression:
        if char in "([{":  # If the character is an opening bracket, push it onto the stack
            stack.push(char)
        elif char in ")]}":  # If the character is a closing bracket
            if stack.is_empty():  # If the stack is empty, return False (unmatched closing bracket)
                return False
            top_element = stack.pop()  # Pop the top element from the stack
            if not is_matching_pair(top_element, char):  # Check if the popped element matches the closing bracket
                return False
    return stack.is_empty()  # If the stack is empty, all brackets were matched; otherwise, return False

def is_matching_pair(opening, closing):
    pairs = { '(': ')', '[': ']', '{': '}' }  # Dictionary of matching pairs
    return pairs.get(opening) == closing  # Return True if the opening and closing brackets match


# Initialize a Stack:



stack = Stack()
# This creates an empty stack to keep track of opening brackets.

# Iterate through the Expression:



# for char in expression:
# Loop through each character in the given expression.

# Push Opening Brackets:



# if char in "([{":
#     stack.push(char)
# If the character is an opening bracket, push it onto the stack.

# Handle Closing Brackets:



# elif char in ")]}":
#     if stack.is_empty():
#         return False
#     top_element = stack.pop()
#     if not is_matching_pair(top_element, char):
#         return False
# If the character is a closing bracket:

# Check if the stack is empty. If it is, return False because there's no matching opening bracket.
# Pop the top element from the stack.
# Check if the popped element matches the closing bracket using the is_matching_pair function. If it doesn't, return False.
# Check for Remaining Opening Brackets:



# return stack.is_empty()
# If the stack is empty at the end, all brackets were matched; otherwise, return False.




class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def get_stack(self):
        return self.items
    

def reverse_string(stack, inp_str):
    for i in range(len(inp_str)):
        stack.push(inp_str[i])
    the_str = ""
    while not stack.is_empty():
        the_str += stack.pop()

    return the_str


st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
# st.push(4)
# print(st.get_stack())

inp_str = 'Hello'
# print(inp_str[::-1])

reve = reverse_string(st, inp_str)
print(reve)



class Stack:
    def __init__(self):
        self.set = []

    def push(self, data):
        self.set.append(data)

    def pop(self):
        return self.set.pop()
    
    def is_empty(self):
        if self.set == []:
            return True
        return False
    
    def peek(self):
        return self.set[-1]
    
    def print(self):
        return self.set
    
    
def int_to_bin(stack, num):
    while num // 2 != 0:
        prev_num = num
        num = num // 2
        stack.push(prev_num % 2)

    stack.push(num % 2)
    new_num = ''
    
    while not stack.is_empty():
        new_num += str(stack.pop())

    return new_num
    

st = Stack()
num = 242
ss = int_to_bin(st, num)
print(ss)