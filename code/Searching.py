# 5.1 Binary Search in Python
# Concept:
# Binary Search is an efficient algorithm for finding an element in a sorted array. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the search continues in the lower half, or in the upper half if the value is greater.

# Real-life Usage:

# Phonebooks: Searching for a contact by name.
# Library: Finding a book by its catalog number.
# Banking Systems: Searching for transaction records.
# Industry Usage:

# Databases: Quick lookups in sorted datasets.
# Gaming: Binary search in algorithms for enemy AI or pathfinding.
# E-commerce: Efficient searching for products based on price, rating, or relevance.


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1



# def binary_search(arr, x)::
# Defines the binary_search function, taking a sorted array arr and the target element x.

# left, right = 0, len(arr) - 1:
# Initializes two pointers: left at the beginning (index 0) and right at the end (len(arr) - 1).

# while left <= right::
# Loop continues as long as the search space is valid (left pointer is less than or equal to right).

# mid = left + (right - left) // 2:
# Calculates the middle index (mid). Using (right - left) // 2 avoids overflow issues.

# if arr[mid] == x::
# If the element at mid is equal to x, return the index mid.

# elif arr[mid] < x::
# If x is greater than arr[mid], ignore the left half by moving the left pointer to mid + 1.

# else::
# If x is smaller, ignore the right half by moving the right pointer to mid - 1.

# return -1:
# If x is not found, return -1.




# 5.2 Recursive Binary Search in Python




# Concept:
# Recursive Binary Search is a variant where the search logic is implemented through recursion instead of iteration.

# Real-life Usage:

# Genealogy Trees: Searching for ancestors in a family tree.
# Decision Making: Recursive problem-solving scenarios.
# Industry Usage:

# Compilers: Searching through syntax trees.
# Machine Learning: Recursive algorithms in decision trees.


def recursive_binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return recursive_binary_search(arr, left, mid - 1, x)
        
        else:
            return recursive_binary_search(arr, mid + 1, right, x)
    
    return -1



# def recursive_binary_search(arr, left, right, x)::
# Defines the recursive_binary_search function, taking a sorted array arr, left and right bounds, and the target element x.

# if right >= left::
# Base condition to continue the recursion if the bounds are valid.

# mid = left + (right - left) // 2:
# Calculates the middle index.

# if arr[mid] == x::
# If the element at mid matches x, return the index mid.

# elif arr[mid] > x::
# If x is smaller, search in the left half (left to mid-1).

# else::
# If x is larger, search in the right half (mid+1 to right).

# return -1:
# If x is not found, return -1.





# 5.3 Analysis of Binary Search





# Concept:
# Analyzing Binary Search involves understanding its time complexity, space complexity, and efficiency compared to other search algorithms.

# Time Complexity:

# Best Case: O(1) (When the element is found at the middle in the first attempt)
# Average Case: O(log n) (Dividing the search space in half each time)
# Worst Case: O(log n) (When the element is at one of the extremes or not present)
# Space Complexity:

# Iterative Version: O(1)
# Recursive Version: O(log n) (Due to call stack)
# Efficiency: Binary Search is very efficient for large datasets that are already sorted. However, it requires the array to be sorted, and insertion/deletion operations can be costly.







# 5.4 Index of First Occurrence in a Sorted Array





# Concept:
# Finding the index of the first occurrence of a target value in a sorted array involves modifying Binary Search to continue searching in the left half even after finding the target.

# Real-life Usage:

# Medical Data: Finding the first record of a specific symptom.
# Event Logs: Finding the first occurrence of an error in a log file.
# Industry Usage:

# Text Processing: Finding the first occurrence of a word in sorted text data.
# Financial Data: Finding the first instance of a stock reaching a specific price.


def first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            result = mid
            right = mid - 1
        
        elif arr[mid] < x:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return result



# def first_occurrence(arr, x)::
# Defines the first_occurrence function.

# result = -1:
# Initializes result to -1, which will store the index of the first occurrence if found.

# while left <= right::
# Continues the search while the search space is valid.

# if arr[mid] == x::
# If x is found, store mid in result and continue searching in the left half (right = mid - 1).

# return result:
# Returns the index of the first occurrence or -1 if not found.







# 5.5 Index of Last Occurrence






# Concept:
# Similar to finding the first occurrence, but the algorithm is adjusted to continue searching in the right half after finding the target.

# Real-life Usage:

# Customer Service: Finding the last time a customer made a purchase.
# System Monitoring: Finding the last occurrence of a system event.
# Industry Usage:

# Data Analysis: Finding the last instance of a specific data point.
# Search Engines: Finding the last occurrence of a keyword in sorted search results.


def last_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            result = mid
            left = mid + 1
        
        elif arr[mid] < x:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return result



# result = -1:
# Stores the index of the last occurrence if found.

# if arr[mid] == x::
# If x is found, store mid in result and continue searching in the right half (left = mid + 1).






# 5.6 Count Occurrences in a Sorted Array






# Concept:
# Counting the occurrences of a target value can be done by combining the results of finding the first and last occurrences.

# Real-life Usage:

# Survey Data: Counting how many times a specific response appears.
# Retail: Counting the number of times a product is sold at a particular price.
# Industry Usage:

# Data Warehousing: Counting occurrences of specific events in large datasets.
# User Behavior Analytics: Counting actions taken by users in a sorted log.


def count_occurrences(arr, x):
    first = first_occurrence(arr, x)
    if first == -1:
        return 0
    
    last = last_occurrence(arr, x)
    
    return last - first + 1



# first = first_occurrence(arr, x):
# Finds the index of the first occurrence of x.

# if first == -1::
# If x is not found, return 0.

# last = last_occurrence(arr, x):
# Finds the index of the last occurrence of x.

# return last - first + 1:
# Returns the count of occurrences by subtracting the index of the first occurrence from the last and adding one.





# 5.7 Count 1s in a Sorted Binary Array






# Concept:
# In a sorted binary array (containing only 0s and 1s), counting the number of 1s can be efficiently done by finding the first occurrence of 1 and calculating the difference from the end of the array.

# Real-life Usage:

# Digital Signals: Counting 1s in a binary sequence to measure signal strength.
# Voting Systems: Counting votes in a binary format (Yes/No).
# Industry Usage:

# Networking: Counting bits in data packets.
# Compression Algorithms: Analyzing binary data for compression.


def count_ones(arr):
    first = first_occurrence(arr, 1)
    if first == -1:
        return 0
    
    return len(arr) - first



# first = first_occurrence(arr, 1):
# Finds the index of the first occurrence of 1.

# return len(arr) - first:
# Returns the count of 1s by subtracting the index of the first 1 from the total length of the array.