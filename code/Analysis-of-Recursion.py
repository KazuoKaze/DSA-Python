## no need to understand everything just read the first intro para and the sumary just go through it ###


# Analysis of Recursion

# Recursion is a method where a function calls itself to solve smaller instances of the same problem. Analyzing recursion involves understanding how these recursive calls stack up and contribute to the overall complexity of the algorithm.

# 1. Recursion Tree Method
# The Recursion Tree Method is a visual tool used to understand the cost of recursive calls by drawing a tree where each node represents a function call.

# Example: Fibonacci Sequence

# Let's consider the Fibonacci sequence, where each number is the sum of the two preceding ones. Here's the recursive function:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Recursion Tree:
# To find fibonacci(4), the recursion tree looks like this:

#            fibonacci(4)
#            /         \
#      fibonacci(3)    fibonacci(2)
#      /      \         /      \
# fibonacci(2) fibonacci(1) fibonacci(1) fibonacci(0)
#  /     \
# fibonacci(1) fibonacci(0)

# fibonacci(4) calls fibonacci(3) and fibonacci(2).
# fibonacci(3) calls fibonacci(2) and fibonacci(1).
# And so on.
# How to Use:

# Draw the recursion tree.
# Count the number of nodes at each level.
# Sum the costs of all levels.
# Cost Calculation:

# Each call fibonacci(n) does constant work plus the work of its two recursive calls.
# At each level, the number of nodes doubles.
# The depth of the tree is n, resulting in a total of 2^n nodes.
# Time Complexity:

# The total cost is the sum of nodes at each level: O(2^n), which is exponential.

# 2. Solving Recurrences
# A recurrence relation is an equation that defines a function in terms of its value on smaller inputs. This is common in recursive algorithms.

# Example: Merge Sort

# Merge Sort is a classic example of a divide-and-conquer algorithm:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return (left, right)


# Recurrence Relation:

# Let T(n) be the time complexity for sorting an array of size n.
# Splitting the array takes constant time.
# Merging two sorted halves takes linear time O(n).
# Recurrence: T(n) = 2T(n/2) + O(n)
# Solving the Recurrence:
# Using the Master Theorem:

# Compare f(n) = O(n) with n^log_b(a):
# Here, a = 2, b = 2, so n^log_b(a) = n^log_2(2) = n.
# Since f(n) is O(n^log_b(a)), by Case 2 of the Master Theorem, T(n) = O(n log n).
# Time Complexity:

# Merge Sort's time complexity is O(n log n).


# 3. Upper Bound using Recursion Tree Method
# The Recursion Tree Method can also help find the upper bound for complex recurrences.

# Example: Complex Recursive Function

def complex_function(n):
    if n <= 1:
        return 1
    else:
        return 2 * complex_function(n/2) + n
    
# Recurrence Relation:
# T(n) = 2T(n/2) + n

# Recursion Tree:

# Draw the tree

#             T(n)
#           /      \
#      T(n/2)     T(n/2)
#     /   \        /    \
    
# T(n/4) T(n/4) T(n/4) T(n/4)

# Cost Calculation:

# There are n levels.
# Total cost is n * O(1) = O(n).
# Time Complexity:

# The time complexity of the factorial function is O(n).


# Summary
# Recursion Tree Method: Visual tool to analyze recursive calls.
# Solving Recurrences: Use recurrence relations to express time complexity.
# Upper Bound using Recursion Tree Method: Helps find the upper bound of complex recurrences.