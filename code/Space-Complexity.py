# Space Complexity


# Theory:
# Space complexity is a measure of the amount of working storage an algorithm needs. It is important to consider both the memory required by the variables used in the algorithm and any additional memory allocated during its execution. Understanding space complexity helps in optimizing algorithms to use memory efficiently, which is crucial in resource-constrained environments.

# Measuring Space Complexity
# Components of Space Complexity:

# Fixed Part: This includes the space required for:
# Input variables.
# Constant variables.
# Simple variables.
# Variable Part: This includes the space required for:
# Dynamic memory allocation.
# Recursion stack space.
# Auxiliary data structures (like arrays, lists, etc.).
# Real-World Example: Space Complexity in Practice
# Consider a web application where a server processes multiple requests simultaneously. Each request requires some memory for processing, and the server must manage these efficiently to handle high traffic without crashing.

# Industrial Use:
# In industry, space complexity is crucial for optimizing systems that handle large amounts of data, such as databases, big data processing frameworks, and embedded systems with limited memory.

# Example: Linear Search
# Let's analyze the space complexity of a simple linear search algorithm:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
index = linear_search(arr, target)
print(f"Element found at index: {index}") 

# Space Complexity Analysis:

# Input Variables: The input array arr and the target target.
# Fixed Space: Space for the input array and the target variable (O(1) each).
# Variable Space: No additional data structures are used.
# Total Space Complexity: O(1) (constant space).
# Example: Recursive Factorial
# Let's analyze the space complexity of a recursive factorial algorithm:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 

# Space Complexity Analysis:

# Input Variables: The input number n.
# Fixed Space: Space for the input variable n (O(1)).
# Variable Space:
# The recursion stack grows with each recursive call.
# For factorial(n), the stack depth is n (since each call to factorial calls factorial with n-1).
# Total Space Complexity: O(n) (linear space due to recursion).
# Example: Merge Sort
# Let's analyze the space complexity of the merge sort algorithm:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))

# Space Complexity Analysis:

# Input Variables: The input array arr.
# Fixed Space: Space for the input array arr (O(n)).
# Variable Space:
# The recursion stack: The depth of the recursion is log n (since the array is halved each time).
# Temporary arrays: Each recursive call creates new arrays for left and right.
# Total Space Complexity: O(n log n)
# Auxiliary Space: Due to the creation of new arrays at each level of recursion.
# Stack Space: Due to the depth of the recursion stack.
# Summary
# Fixed Part: Constant space used by input variables and constants.
# Variable Part: Space used by dynamic memory allocation, recursion stack, and auxiliary data structures.
# Space Complexity Examples:
# Linear Search: O(1) space.
# Recursive Factorial: O(n) space due to recursion stack.
# Merge Sort: O(n log n) space due to auxiliary arrays and recursion stack.