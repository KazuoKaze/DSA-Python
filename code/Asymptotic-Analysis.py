#### Dont need to undestand exmaple of this rn... just read ####


# 1.2 Asymptotic Analysis
# Theory:
# Asymptotic analysis is a method of describing the efficiency of an algorithm as the input size grows towards infinity. It provides a way to compare algorithms based on their growth rates rather than their actual runtime, which can be influenced by hardware, implementation, and other factors. The primary goal is to express the algorithm's performance in terms of input size (n).

# Asymptotic Notations:

# Upper bound : The maximum time a program can take to produce outputs, expressed in terms of the size of the inputs (worst-case scenario). Lower bound : The minimum time a program will take to produce outputs, expressed in terms of the size of the inputs (best-case scenario).

# Big O (O): Represents the upper bound of an algorithm's runtime. It provides the worst-case scenario.
# Omega (Ω): Represents the lower bound of an algorithm's runtime. It provides the best-case scenario.
# Theta (Θ): Represents the tight bound of an algorithm's runtime. It provides both the upper and lower bounds.
# Real-World Example:
# Consider a function that sorts a list of employee names. The performance of different sorting algorithms can vary based on the size of the list. Asymptotic analysis helps us understand which algorithm will perform better as the number of employees increases.

# Industrial Use:
# In industry, asymptotic analysis is used to select the most appropriate algorithms for large-scale applications, such as search engines, databases, and data processing systems, where efficiency is critical.

# Big O Notation
# Big O Notation:

# Used to describe the worst-case scenario of an algorithm.
# Focuses on the upper bound of the runtime.
# Ignores constant factors and lower-order terms.
# Examples:
# Constant Time (O(1)):

# Description: The algorithm takes a constant amount of time, regardless of the input size.
# Example: Accessing an element in an array by index.

def get_element(arr, index):
    return arr[index]

arr = [10, 20, 30, 40, 50]
print(get_element(arr, 2))  # Output: 30

# Linear Time (O(n)):

# Description: The runtime grows linearly with the input size.
# Example: Finding the maximum element in an array.

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

arr = [10, 20, 30, 40, 50]
print(find_max(arr))  # Output: 50

# Quadratic Time (O(n^2)):

# Description: The runtime grows quadratically with the input size.
# Example: Bubble sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]

# Omega Notation
# Omega (Ω) Notation:

# Used to describe the best-case scenario of an algorithm.
# Focuses on the lower bound of the runtime.
# Useful for understanding the minimum time required by an algorithm.
# Examples:
# Omega of Linear Search (Ω(1)):

# Description: In the best case, the target element is found at the first position.
# Example: Linear search algorithm.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
target = 10
print(linear_search(arr, target))  # Output: 0

# Omega of Bubble Sort (Ω(n)):

# Description: In the best case, the array is already sorted, and only one pass is needed.
# Example: Bubble sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]

# Theta Notation
# Theta (Θ) Notation:

# Used to describe the tight bound of an algorithm.
# Represents both the upper and lower bounds.
# Provides a more precise analysis of the algorithm's performance.
# Examples:
# Theta of Linear Search (Θ(n)):

# Description: In the average case, the target element is somewhere in the middle of the array.
# Example: Linear search algorithm.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(linear_search(arr, target))  # Output: 2

# Theta of Bubble Sort (Θ(n^2)):

# Description: In the average case, the array elements are in random order.
# Example: Bubble sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]

# Practice Problems
# Problem: Implement and analyze the time complexity of insertion sort.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]

# Time Complexity:

# Best Case: O(n) (when the array is already sorted)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Problem: Analyze the time complexity of the selection sort algorithm.


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# arr = [64, 25, 12, 22, 11]
# print(selection_sort(arr))  # Output: [11, 12, 22, 25, 64]
# Time Complexity:

# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Explanation:
# In both insertion sort and selection sort, the outer loop runs n times, and the inner loop runs a decreasing number of times (n-1, n-2, ...). This results in a quadratic time complexity for the average and worst cases. However, insertion sort can achieve linear time complexity in the best case if the array is already sorted.