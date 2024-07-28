# 1.1 Analysis of Algorithms (Background)
# Theory:
# The analysis of algorithms involves evaluating the efficiency and performance of an algorithm. The primary aspects of this analysis include time complexity (how the runtime of an algorithm grows with input size) and space complexity (how the memory usage grows with input size).

# Real-World Example:
# Consider an e-commerce platform like Amazon. To provide a seamless shopping experience, it's crucial to have efficient algorithms for searching products, processing orders, and recommending items. For instance, the search algorithm must quickly find products matching a user's query, even when there are millions of items in the database.

# Industrial Use:
# In industry, algorithm analysis is used to optimize performance and resource usage. For example, a financial company processing millions of transactions per second must ensure its algorithms are efficient to minimize latency and hardware costs.

# Code Example:
# Let's analyze a simple linear search algorithm, which searches for a target value in an unsorted list.


def lenear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
target = 10
index = lenear_search(arr, target)
print(f"Elemet is in: {index}")


# Time Complexity:

# Best Case: O(1) (when the target is at the first position)
# Average Case: O(n) (when the target is somewhere in the middle)
# Worst Case: O(n) (when the target is not in the list)
# Space Complexity:

# O(1), since no extra space is used other than the input array.

# Solved Example 1:
# Consider an array of user IDs and a target user ID. We want to find the index of the target user ID using linear search.


def find_user_id(user_ids, target_id):
    for i in range(len(user_ids)):
        if user_ids[i] == target_id:
            return i
    return -1

user_ids = [101, 202, 303, 404, 505]
target_id = 303
index = find_user_id(user_ids, target_id)
print(f"User ID found at index: {index}")


# In both examples, we are using a linear search algorithm to find the index of a target element in an array. The algorithm iterates through the array, compares each element with the target, and returns the index if a match is found. If no match is found, it returns -1.