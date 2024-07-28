## If you are beginner please use vs code debug tool to understand the code visually ( much better ) ###


# Analysis of Common Loops
# Understanding the time complexity of loops is fundamental in analyzing the efficiency of algorithms. We will examine the time complexity of single loops, nested loops, and multiple loops with practical examples.


# 1. Single Loop
# A single loop runs a fixed number of times, typically dependent on the input size 
# 𝑛
# n.

# Example:

def single_loop(arr):
    for i in range(len(arr)): # (0 to 4)
        print(arr[i])

arr = [10, 20, 30, 40, 50]
single_loop(arr)

# Explanation:

# Code Breakdown:

# for i in range(len(arr)):: This loop iterates over each element in the array arr.
# print(arr[i]): During each iteration, the element at index i is printed.
# Functionality:

# The function single_loop prints each element of the input array arr.
# Given the array [10, 20, 30, 40, 50], the function will output

# Time Complexity:

# The loop runs 𝑛 times, where n is the length of the array.
# Each iteration performs a constant-time operation (printing an element).
# Total Time Complexity: O(n)


# 2. Nested Loops
# Nested loops involve a loop inside another loop, often resulting in higher time complexity.

# Example:

def nested_loops(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

arr = [10, 20, 30]
nested_loops(arr)

# Explanation:

# Code Breakdown:

# for i in range(len(arr)):: The outer loop iterates over each element in the array arr.
# for j in range(len(arr)):: The inner loop also iterates over each element in the array arr.
# print(arr[i], arr[j]): During each iteration of the inner loop, the elements at indices i and j are printed.

# Time Complexity:

# The outer loop runs n times.
# For each iteration of the outer loop, the inner loop runs 
# n times.
# Each pair of iterations performs a constant-time operation (printing a pair of elements).
# Total Time Complexity: O(n^2)


# 3. Multiple Loops
# Multiple loops can be either independent or dependent. We will analyze both scenarios.

# 3.1 Independent Loops
# Independent loops run sequentially, and their complexities are added.

# Example:

def independent_loops(arr):
    for i in range(len(arr)):
        print(arr[i])
    
    for j in range(len(arr)):
        print(arr[j])

arr = [10, 20, 30, 40, 50]
independent_loops(arr)


# Explanation:

# Code Breakdown:

# The first for loop iterates over each element in the array arr and prints it.
# The second for loop also iterates over each element in the array arr and prints it.
    
# Time Complexity:

# The first loop runs 
# n times.
# The second loop also runs 
# n times.
# Since these loops are independent, their complexities add up.
# Total Time Complexity: O(n) + O(n) = O(2n) = O(n)


# 3.2 Dependent Loops
# Dependent loops occur when the iteration of one loop depends on the iteration of another loop.

# Example:

def dependent_loops(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i], arr[j])

arr = [10, 20, 30, 40]
dependent_loops(arr)

# Explanation:

# Code Breakdown:

# for i in range(len(arr)):: The outer loop iterates over each element in the array arr.
# for j in range(i, len(arr)):: The inner loop starts from index i and iterates to the end of the array.
# print(arr[i], arr[j]): During each iteration of the inner loop, the elements at indices i and j are printed.


# Practice Problems
# Problem: Analyze the time complexity of the following function.

def example_function(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                print(arr[i], arr[j], arr[k])

arr = [1, 2, 3, 4]
example_function(arr)


# Explanation:

# Code Breakdown:

# The outer loop iterates 
# n times.
# The second loop starts from 
# 𝑖 + 1
# i+1 and iterates to the end of the array.
# The third loop starts from 
# 𝑗 + 1
# j+1 and iterates to the end of the array.
# Each combination of three elements is printed.



# Problem: Write a function that sums all elements of a 2D array and analyze its time complexity.

def sum_2d_array(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            total += matrix[i][j]
    return total

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_2d_array(matrix))


# Explanation:

# Code Breakdown:

# total = 0: Initialize a variable to store the sum.
# for i in range(len(matrix)):: The outer loop iterates over each row.
# for j in range(len(matrix[0])):: The inner loop iterates over each column in the current row.
# total += matrix[i][j]: Add the current element to the total sum.


