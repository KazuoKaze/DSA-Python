

# 6. Sorting


# 6.1 Introduction to Sorting


# Definition:
# Sorting is the process of arranging elements in a specific order. The most common orders are numerical and lexicographical (alphabetical). Sorting is a fundamental operation in computer science, used in various applications such as searching, data organization, and optimization.

# Types of Sorting Algorithms:

# Bubble Sort: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.
# Selection Sort: Divides the list into a sorted and an unsorted region and repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the sorted region.
# Insertion Sort: Builds the sorted list one element at a time by repeatedly picking the next element and inserting it into its correct position.
# Merge Sort: A divide-and-conquer algorithm that splits the list into halves, recursively sorts them, and then merges the sorted halves.
# Quick Sort: Another divide-and-conquer algorithm that selects a 'pivot' element and partitions the list into elements less than the pivot and elements greater than the pivot. It recursively sorts the partitions.
# Heap Sort: Converts the list into a heap data structure, then repeatedly extracts the maximum element from the heap and reconstructs the heap until the list is sorted.
# Radix Sort: A non-comparative sorting algorithm that sorts numbers by processing individual digits.
# Real-World Uses:

# Database indexing: Efficient searching and retrieval.
# E-commerce websites: Sorting products by price, popularity, or ratings.
# Computer graphics: Sorting elements for rendering.
# Data analysis: Organizing data for better readability and processing.
# 6.2 List Sort in Python
# Python provides built-in support for sorting lists, making it easy and efficient to sort collections of data. The primary method for sorting lists is the sort() method, which sorts the list in place, and the sorted() function, which returns a new sorted list.

# Examples and Code Breakdown:

# Using the sort() Method:


# # Example list
numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list in ascending order
numbers.sort()
print("Sorted list:", numbers)  # Output: [1, 2, 5, 5, 6, 9]

# Sorting the list in descending order
numbers.sort(reverse=True)
print("Sorted list (descending):", numbers)  # Output: [9, 6, 5, 5, 2, 1]

# numbers.sort() sorts the list in place, meaning it modifies the original list.
# The reverse=True parameter sorts the list in descending order.
# Using the sorted() Function:


# # Example list
numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list in ascending order
sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]

# The original list remains unchanged
print("Original list:", numbers)  # Output: [5, 2, 9, 1, 5, 6]

# Sorting the list in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Sorted list (descending):", sorted_numbers_desc)  # Output: [9, 6, 5, 5, 2, 1]

# sorted(numbers) returns a new sorted list, leaving the original list unchanged.
# The reverse=True parameter sorts the list in descending order.
# Sorting with a Custom Key:


# # Example list of tuples
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]

# Sorting by the second element (age)
students.sort(key=lambda student: student[1])
print("Sorted by age:", students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Sorting by the first element (name)
sorted_students = sorted(students, key=lambda student: student[0])
print("Sorted by name:", sorted_students)  # Output: [('Alice', 25), ('Bob', 20), ('Charlie', 23)]

# The key parameter specifies a function to be called on each list element prior to making comparisons.
# In this example, lambda student: student[1] sorts the list by the second element of each tuple (age).
# Industrial Uses of Sorting:

# Financial Systems: Sorting transactions by date or amount.
# Logistics: Sorting packages by destination or priority.
# Healthcare: Sorting patient records by appointment times or urgency.
# Search Engines: Sorting search results by relevance or ranking.


# 6.5 Bubble Sort



# Explanation:
# Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list of items to be sorted, comparing adjacent items and swapping them if they are in the wrong order. This process is repeated until the entire list is sorted.

# Algorithm:

# Start with the first element and compare it with the next element.
# If the current element is greater than the next element, swap them.
# Continue comparing and swapping adjacent elements until you reach the end of the list.
# Repeat the above steps for each element in the list until no swaps are needed, which indicates that the list is sorted.
# Example:
# Let's go through the code step by step:


def bubble_sort(nums):
    n = len(nums)  # Get the number of elements in the list
    # Outer loop for traversing through all elements
    for i in range(n):
        swapped = False  # Flag to indicate if a swap occurred
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if necessary
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap
                swapped = True  # Set swapped flag to True
        # If no elements were swapped in a pass, the list is already sorted
        if not swapped:
            break

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted list using Bubble Sort:", numbers)
# Code Breakdown:

# nums: This is the list of numbers that we want to sort.
# n = len(nums): This gets the length of the list, which tells us how many elements are in it.
# for i in range(n): This loop iterates through each element in the list.
# for j in range(0, n - i - 1): This inner loop compares each element with its neighbor and swaps them if they are in the wrong order (nums[j] > nums[j + 1]).
# nums[j], nums[j + 1] = nums[j + 1], nums[j]: This line swaps the elements if they are out of order.
# swapped: This boolean variable keeps track of whether any swaps were made in a pass through the list.
# The outer loop (for i in range(n)) continues until no more swaps are needed (swapped remains False), meaning the list is sorted.
# Complexity:

# Time Complexity:
# Best Case: O(n) - When the list is already sorted.
# Average Case: O(n^2) - When elements are in random order.
# Worst Case: O(n^2) - When elements are sorted in reverse order.
# Space Complexity: O(1) - Bubble Sort is an in-place sorting algorithm, meaning it doesn't require additional space proportional to the input size.


# 6.6 Selection Sort


# Explanation:
# Selection Sort is another simple sorting algorithm that works by repeatedly finding the minimum (or maximum) element from the unsorted portion of the list and swapping it with the first unsorted element. This process is repeated until the entire list is sorted.

# Algorithm:

# Find the smallest element in the unsorted portion of the list.
# Swap it with the first unsorted element.
# Move the boundary between the sorted and unsorted portions one element to the right.
# Repeat steps 1-3 until the list is sorted.
# Example:
# Now, let's go through the Selection Sort code step by step:


def selection_sort(nums):
    n = len(nums)  # Get the number of elements in the list
    # Traverse through all elements in the list
    for i in range(n):
        min_index = i  # Assume the current index is the minimum
        # Find the index of the smallest element in remaining unsorted array
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j  # Update the index of minimum element
        # Swap the found minimum element with the first element of the unsorted array
        nums[i], nums[min_index] = nums[min_index], nums[i]

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
selection_sort(numbers)
print("Sorted list using Selection Sort:", numbers)
# Code Breakdown:

# nums: This is the list of numbers that we want to sort.
# n = len(nums): This gets the length of the list, which tells us how many elements are in it.
# for i in range(n): This outer loop iterates through each element in the list.
# min_index = i: We assume the current index (i) is the index of the minimum element.
# for j in range(i + 1, n): This inner loop finds the index of the smallest element in the remaining unsorted portion of the list (nums[i+1:]).
# if nums[j] < nums[min_index]: If we find an element smaller than our assumed minimum (nums[min_index]), we update min_index to j.
# nums[i], nums[min_index] = nums[min_index], nums[i]: After finding the smallest element (nums[min_index]), we swap it with the current element (nums[i]).
# The outer loop (for i in range(n)) continues until the entire list is sorted.
# Complexity:

# Time Complexity:
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2) - Selection Sort always performs O(n^2) comparisons, regardless of the input.
# Space Complexity: O(1) - Selection Sort is an in-place sorting algorithm, meaning it doesn't require additional space proportional to the input size.


# 6.7 Insertion Sort in Python


# Explanation:
# Insertion Sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It iterates through the list, removes one element from the list, finds its correct position in the sorted part of the list, and inserts it there. This process repeats until the whole list is sorted.

# Algorithm:

# Start with the second element (index 1) in the list, as the first element is trivially sorted.
# Compare the current element with the largest element in the sorted part of the list.
# Shift all elements larger than the current element to one position ahead of their current position.
# Insert the current element into the correct position in the sorted part of the list.
# Repeat steps 2-4 until the entire list is sorted.
# Example:
# Now, let's go through the Insertion Sort code step by step:


def insertion_sort(nums):
    n = len(nums)  # Get the number of elements in the list
    # Traverse through all elements in the list, starting from the second element
    for i in range(1, n):
        current = nums[i]  # Store the current element to be inserted
        j = i - 1  # Initialize a pointer to the last element of the sorted part of the list
        # Shift elements of nums[0..i-1], that are greater than current, to one position ahead of their current position
        while j >= 0 and current < nums[j]:
            nums[j + 1] = nums[j]  # Shift the element to the right
            j -= 1  # Move to the previous element
        nums[j + 1] = current  # Insert the current element into the correct position

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(numbers)
print("Sorted list using Insertion Sort:", numbers)
# Code Breakdown:

# nums: This is the list of numbers that we want to sort.
# n = len(nums): This gets the length of the list, which tells us how many elements are in it.
# for i in range(1, n): This loop starts from the second element (i = 1) and iterates through each element in the list.
# current = nums[i]: Store the current element (nums[i]) to be inserted into the correct position in the sorted part of the list.
# j = i - 1: Initialize a pointer (j) to the last element of the sorted part of the list.
# while j >= 0 and current < nums[j]: This loop compares current with each element in the sorted part of the list (nums[0..i-1]) and shifts elements to the right (nums[j + 1] = nums[j]) until we find the correct position for current.
# nums[j + 1] = current: Insert current into the correct position in the sorted part of the list.
# The outer loop (for i in range(1, n)) continues until the entire list is sorted.
# Complexity:

# Time Complexity:
# Best Case: O(n) - When the list is already sorted.
# Average Case: O(n^2)
# Worst Case: O(n^2) - When the list is sorted in reverse order.
# Space Complexity: O(1) - Insertion Sort is an in-place sorting algorithm, meaning it doesn't require additional space proportional to the input size.



# 6.8 Merge Sort Algorithm



# Explanation:
# Merge Sort is an efficient, stable, comparison-based sorting algorithm. It divides the input array into two halves, recursively sorts each half, and then merges the two sorted halves to produce a sorted array.

# Algorithm:

# Divide the unsorted list into two halves.
# Recursively sort each half.
# Merge the sorted halves to produce a sorted array.
# Example:
# Now, let's go through the Merge Sort code step by step:


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2  # Find the middle of the list
        left_half = nums[:mid]  # Divide the list into two halves
        right_half = nums[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for left_half, right_half, and nums

        # Merge the sorted halves into nums[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in left_half
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in right_half
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
merge_sort(numbers)
print("Sorted list using Merge Sort:", numbers)
# Code Breakdown:

# nums: This is the list of numbers that we want to sort.
# if len(nums) > 1: Check if the list has more than one element to divide it into halves.
# mid = len(nums) // 2: Calculate the midpoint of the list to divide it into left_half and right_half.
# left_half = nums[:mid], right_half = nums[mid:]: Divide the list into two halves (left_half and right_half).
# merge_sort(left_half), merge_sort(right_half): Recursively call merge_sort on left_half and right_half to sort them.
# i, j, k = 0: Initialize indices for left_half, right_half, and nums.
# while i < len(left_half) and j < len(right_half): Merge left_half and right_half into nums in sorted order.
# nums[k] = left_half[i], nums[k] = right_half[j]: Merge elements from left_half and right_half into nums.
# The last two while loops (while i < len(left_half) and while j < len(right_half)) copy any remaining elements from left_half and right_half to nums.
# Complexity:

# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n) - Merge Sort has a consistent time complexity regardless of the input.
# Space Complexity: O(n) - Merge Sort requires additional memory proportional to the size of the input array for storing temporary arrays during the merge process.



# 6.9 Merge Two Sorted Arrays




# Explanation:
# Merging two sorted arrays is a fundamental operation in sorting and searching algorithms. Given two sorted arrays, the task is to merge them into a single sorted array without using extra space. This is often done using the merge operation similar to Merge Sort.

# Algorithm:

# Initialize three pointers: one for each array (arr1, arr2) and one for the merged result.
# Compare elements at the current pointers of both arrays.
# Append the smaller element to the merged result array and move the respective pointer forward.
# Continue this process until all elements from both arrays are merged into the result array.
# Example:
# Let's look at the code for merging two sorted arrays:


def merge_sorted_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    merged = [0] * (m + n)
    i = j = k = 0

    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1

    while i < m:
        merged[k] = arr1[i]
        i += 1
        k += 1

    while j < n:
        merged[k] = arr2[j]
        j += 1
        k += 1

    return merged

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_array = merge_sorted_arrays(arr1, arr2)
print("Merged Sorted Array:", merged_array)
# Code Breakdown:

# m, n = len(arr1), len(arr2): Get the lengths of arr1 and arr2.
# merged = [0] * (m + n): Initialize a new list merged to store the merged result with enough space.
# i, j, k = 0: Initialize pointers i, j for arr1, arr2 respectively, and k for merged.
# while i < m and j < n: Compare elements at arr1[i] and arr2[j], and append the smaller element to merged.
# while i < m: Append remaining elements from arr1 to merged.
# while j < n: Append remaining elements from arr2 to merged.
# return merged: Return the merged sorted array.
# Complexity:

# Time Complexity: O(m + n) - Where m and n are the lengths of arr1 and arr2 respectively. The algorithm performs a single pass through each array.
# Space Complexity: O(m + n) - Additional space is used to store the merged array.



# 6.10 Merge Subarrays




# Explanation:
# In the context of algorithms like Merge Sort, merging subarrays is a crucial step. When dividing an array into smaller subarrays recursively, merging these subarrays back together in sorted order is essential to achieve the final sorted array.

# Algorithm:

# Given an array, divide it into two halves.
# Recursively divide each half until you have subarrays of size 1 (base case).
# Merge these subarrays back together in sorted order using the merge operation.
# Example:
# Let's extend the previous Merge Sort example to include the merging of subarrays:


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_half = arr[left:left + n1]
    right_half = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
# Code Breakdown:

# merge(arr, left, mid, right): The merge function merges two subarrays arr[left...mid] and arr[mid+1...right] into a single sorted subarray arr[left...right].
# merge_sort(arr, left, right): The merge_sort function recursively divides the array arr into halves until left < right. It then sorts and merges the subarrays using merge.
# Complexity:

# Time Complexity: O(n log n) - Merge Sort has a time complexity of O(n log n) because it divides the array into halves recursively and merges them back together.
# Space Complexity: O(n) - Merge Sort requires additional memory proportional to the size of the input array for storing temporary arrays during the merge process.



# 6.11 Count Inversions in Array



# Explanation:
# An inversion in an array is a pair of indices (i, j) such that i < j and arr[i] > arr[j]. Counting inversions is useful in scenarios like collaborative filtering, where determining similarity between users or items involves counting such pairs.

# Algorithm:

# Use a modified version of Merge Sort to count inversions during the merge step.
# Whenever an element from the right half of the array is smaller than an element from the left half (arr[j] < arr[i]), all remaining elements in the left half form inversions with the current element in the right half.
# Example:
# Here's how you can count inversions using a modified Merge Sort algorithm:


def count_inversions(arr):
    if len(arr) < 2:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_inversions = count_inversions(arr[:mid])
    right_half, right_inversions = count_inversions(arr[mid:])
    merged_array, merge_inversions = merge_and_count_split_inv(left_half, right_half)
    
    total_inversions = left_inversions + right_inversions + merge_inversions
    return merged_array, total_inversions

def merge_and_count_split_inv(left, right):
    i = j = 0
    merged = []
    split_inversions = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, split_inversions

# Example usage:
arr = [1, 20, 6, 4, 5]
sorted_arr, inversions = count_inversions(arr)
print("Sorted Array:", sorted_arr)
print("Number of Inversions:", inversions)
# Code Breakdown:

# count_inversions(arr): This function recursively divides the array into halves (left_half and right_half), counts inversions in each half, and then counts inversions across the split using merge_and_count_split_inv.
# merge_and_count_split_inv(left, right): This function merges two sorted arrays left and right, counting inversions where an element in right is smaller than an element in left.
# Complexity:

# Time Complexity: O(n log n) - Counting inversions using Merge Sort has the same time complexity as Merge Sort itself, due to the recursive division and merging of the array.
# Space Complexity: O(n) - Additional space is used to store temporary arrays during the merge process.



# 6.12 Merge Sort Analysis




# Explanation:
# Merge Sort is an efficient, stable, and comparison-based sorting algorithm that divides the input array into smaller halves, recursively sorts them, and merges them back together. Here, we analyze its time and space complexities.

# Algorithm:

# Divide the array into two halves.
# Recursively sort each half.
# Merge the sorted halves back together.
# Time Complexity:

# Best Case: O(n log n) - When the array is already sorted, Merge Sort still divides the array into halves but requires fewer comparisons during merging.
# Average Case: O(n log n) - Merge Sort consistently divides the array into halves and merges them in O(n) time.
# Worst Case: O(n log n) - Even in the worst case, Merge Sort divides the array into halves and merges them efficiently.
# Space Complexity:

# Space: O(n) - Merge Sort requires additional space proportional to the size of the input array for storing temporary arrays during the merge process.
# Stability:

# Merge Sort is stable, meaning it preserves the relative order of equal elements in the sorted output.
# Example:
# Let's recap the example usage of Merge Sort shown previously for sorting an array:


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Divide the list into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for left_half, right_half, and arr

        # Merge the sorted halves into arr[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
merge_sort(numbers)
print("Sorted list using Merge Sort:", numbers)
# Code Breakdown:

# merge_sort(arr): This function sorts the array arr using the Merge Sort algorithm, dividing it into halves, recursively sorting each half, and merging them back together.



# 6.13 Quick Sort Introduction




# Explanation:
# Quick Sort is a highly efficient sorting algorithm based on the divide-and-conquer strategy. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

# Algorithm:

# Partitioning: Choose a pivot element (commonly the last element) and rearrange the array so that elements less than the pivot are on its left, and elements greater than the pivot are on its right.
# Recursively Apply: Recursively apply the partitioning process to the left and right sub-arrays.
# Example:
# Here's a basic implementation of Quick Sort:


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("Sorted list using Quick Sort:", sorted_numbers)
# Code Breakdown:

# quick_sort(arr): This function recursively sorts the input array arr using the Quick Sort algorithm.
# pivot = arr[len(arr) // 2]: Selects the middle element as the pivot. Alternatively, you can choose the first or last element as the pivot.
# left, middle, right: Partition the array into three parts based on elements less than, equal to, and greater than the pivot.
# return quick_sort(left) + middle + quick_sort(right): Recursively apply Quick Sort to the left and right sub-arrays and concatenate the sorted results with the middle part.
# Complexity:

# Time Complexity: O(n log n) on average and O(n^2) in the worst case. Quick Sort typically performs well due to its average-case time complexity.
# Space Complexity: O(log n) due to the recursive nature of the algorithm. Additional space is used for function calls and recursion stack.




# 6.14 Partition a Given Array





# Explanation:
# Partitioning an array is a crucial step in several algorithms, including Quick Sort and Quick Select. The goal is to rearrange the elements in the array around a pivot element such that all elements less than the pivot are on its left and all elements greater than the pivot are on its right.

# Algorithm:

# Choose a Pivot: Select a pivot element from the array (commonly the last element).
# Reorder Elements: Rearrange the array such that elements less than the pivot are moved to its left, and elements greater than the pivot are moved to its right.
# Return Pivot Index: Return the index of the pivot element after partitioning.
# Example:
# Here's how you can partition an array:


def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
pivot_index = partition(arr, 0, len(arr) - 1)
print("Array after partitioning:", arr)
print("Pivot Index:", pivot_index)
# Code Breakdown:

# partition(arr, low, high): This function partitions the array arr between indices low and high around a pivot element (arr[high]).
# pivot = arr[high]: Choose the last element as the pivot.
# i = low - 1: Initialize i to the index of the smaller element.
# Iterate through the array from low to high - 1:
# If an element arr[j] is less than or equal to the pivot, swap arr[j] with arr[i + 1] and increment i.
# Swap arr[i + 1] with arr[high] to place the pivot in its correct position.
# Return i + 1, which is the index of the pivot after partitioning.
# Complexity:

# Time Complexity: O(n) - Partitioning an array of n elements takes linear time.
# Space Complexity: O(1) - Partitioning is done in-place without using extra space.



# 6.15 Lomuto Partition



# Explanation:
# Lomuto Partition Scheme is another method for partitioning an array around a pivot element, commonly used in Quick Sort. It is simpler to implement but may not perform as well as the Hoare partition scheme in certain cases.

# Algorithm:

# Choose a Pivot: Select the last element of the array as the pivot.
# Partitioning Process:
# Initialize i to low - 1 as the index of the smaller element.
# Iterate through the array from low to high - 1.
# If an element is less than or equal to the pivot, swap it with the element at i + 1 and increment i.
# Final Swap: Swap the pivot element (arr[high]) with arr[i + 1] to place the pivot in its correct sorted position.
# Return Pivot Index: Return i + 1, which is the index of the pivot after partitioning.
# Example:
# Here's how Lomuto Partition works:


def lomuto_partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
pivot_index = lomuto_partition(arr, 0, len(arr) - 1)
print("Array after Lomuto partitioning:", arr)
print("Pivot Index:", pivot_index)
# Code Breakdown:

# lomuto_partition(arr, low, high): This function implements the Lomuto Partition Scheme to partition the array arr between indices low and high around a pivot element (arr[high]).
# pivot = arr[high]: Choose the last element as the pivot.
# i = low - 1: Initialize i to the index of the smaller element.
# Iterate through the array from low to high - 1:
# If an element arr[j] is less than or equal to the pivot, swap arr[j] with arr[i + 1] and increment i.
# Swap arr[i + 1] with arr[high] to place the pivot in its correct position.
# Return i + 1, which is the index of the pivot after partitioning.
# Complexity:

# Time Complexity: O(n) - Lomuto Partitioning takes linear time to partition an array of n elements.
# Space Complexity: O(1) - Partitioning is done in-place without using extra space.




# 6.16 Hoare's Partition




# Explanation:
# Hoare's Partition Scheme is another method for partitioning an array around a pivot element, used in Quick Sort. It is more efficient than Lomuto's Partition Scheme in some cases because it does fewer swaps on average.

# Algorithm:

# Choose a Pivot: Select a pivot element (commonly the first element).
# Partitioning Process:
# Initialize i to low - 1 (leftmost index) and j to high + 1 (rightmost index).
# Increment i until you find an element greater than the pivot.
# Decrement j until you find an element less than the pivot.
# Swap the elements at i and j.
# Repeat until i is greater than or equal to j.
# Return Pivot Index: Return j, which is the index where the pivot should be placed.
# Example:
# Here's how Hoare's Partition works:


def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as the pivot
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
pivot_index = hoare_partition(arr, 0, len(arr) - 1)
print("Array after Hoare's partitioning:", arr)
print("Pivot Index:", pivot_index)
# Code Breakdown:

# hoare_partition(arr, low, high): This function implements Hoare's Partition Scheme to partition the array arr between indices low and high around a pivot element (arr[low]).
# pivot = arr[low]: Choose the first element as the pivot.
# i = low - 1, j = high + 1: Initialize i to the leftmost index and j to the rightmost index.
# Loop:
# Increment i until arr[i] is greater than or equal to the pivot.
# Decrement j until arr[j] is less than or equal to the pivot.
# Swap arr[i] and arr[j] if i is less than j.
# Return j, which is the index where the pivot should be placed.
# Complexity:

# Time Complexity: O(n) - Hoare's Partitioning takes linear time to partition an array of n elements on average.
# Space Complexity: O(1) - Partitioning is done in-place without using extra space.



# 6.17 Quick Sort using Lomuto Partition



# Explanation:
# Quick Sort using Lomuto Partition is a recursive sorting algorithm that uses Lomuto's Partitioning Scheme to sort an array efficiently.

# Algorithm:

# Base Case: If the array has fewer than two elements, it is already sorted.
# Partitioning: Use Lomuto's Partition to rearrange the array around a pivot element.
# Recursive Sort: Recursively apply Quick Sort to the left and right sub-arrays.
# Example:
# Here's an implementation of Quick Sort using Lomuto's Partition Scheme:


def quick_sort_lomuto(arr, low, high):
    if low < high:
        pivot_index = lomuto_partition(arr, low, high)
        quick_sort_lomuto(arr, low, pivot_index - 1)
        quick_sort_lomuto(arr, pivot_index + 1, high)

def lomuto_partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort_lomuto(arr, 0, len(arr) - 1)
print("Array after Quick Sort (Lomuto):", arr)
# Code Breakdown:

# quick_sort_lomuto(arr, low, high): This function recursively sorts the array arr using Quick Sort with Lomuto's Partition Scheme.
# if low < high: Base case checks if there are more than one element in the sub-array.
# pivot_index = lomuto_partition(arr, low, high): Partition the array using Lomuto's Partition and get the pivot index.
# Recursively sort the left sub-array (quick_sort_lomuto(arr, low, pivot_index - 1)) and the right sub-array (quick_sort_lomuto(arr, pivot_index + 1, high)).
# Complexity:

# Time Complexity: O(n log n) on average and O(n^2) in the worst case (when the pivot is consistently the smallest or largest element).
# Space Complexity: O(log n) due to the recursive calls and function call stack.




# 6.18 Quick Sort using Hoare's Partition




# Explanation:
# Quick Sort using Hoare's Partition is another variant of the Quick Sort algorithm that uses Hoare's Partition Scheme for partitioning the array.

# Algorithm:

# Base Case: If the array has fewer than two elements, it is already sorted.
# Partitioning: Use Hoare's Partition to rearrange the array around a pivot element.
# Recursive Sort: Recursively apply Quick Sort to the left and right sub-arrays.
# Example:
# Here's an implementation of Quick Sort using Hoare's Partition Scheme:


def quick_sort_hoare(arr, low, high):
    if low < high:
        pivot_index = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pivot_index)
        quick_sort_hoare(arr, pivot_index + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as the pivot
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort_hoare(arr, 0, len(arr) - 1)
print("Array after Quick Sort (Hoare):", arr)
# Code Breakdown:

# quick_sort_hoare(arr, low, high): This function recursively sorts the array arr using Quick Sort with Hoare's Partition Scheme.
# if low < high: Base case checks if there are more than one element in the sub-array.
# pivot_index = hoare_partition(arr, low, high): Partition the array using Hoare's Partition and get the pivot index.
# Recursively sort the left sub-array (quick_sort_hoare(arr, low, pivot_index)) and the right sub-array (quick_sort_hoare(arr, pivot_index + 1, high)).
# Complexity:

# Time Complexity: O(n log n) on average and O(n^2) in the worst case (when the pivot is consistently the smallest or largest element).
# Space Complexity: O(log n) due to the recursive calls and function call stack.




# 6.19 Analysis of Quick Sort





# Explanation:
# Quick Sort is a highly efficient sorting algorithm based on divide-and-conquer principles. It divides the array into smaller sub-arrays based on a chosen pivot element, recursively sorts these sub-arrays, and then combines them to achieve a sorted array.

# Algorithm:

# Choose a Pivot: Select a pivot element (commonly the first or last element).
# Partitioning: Rearrange the array so that elements less than the pivot are on the left, and elements greater than the pivot are on the right.
# Recursive Sort: Recursively apply Quick Sort to the left and right sub-arrays.
# Example:
# Here's a basic implementation of Quick Sort in Python:


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
sorted_arr = quick_sort(arr)
print("Sorted array using Quick Sort:", sorted_arr)
# Code Breakdown:

# quick_sort(arr): This function recursively sorts the array arr using Quick Sort.
# Base case (if len(arr) <= 1): If the array has one or zero elements, it is already sorted.
# pivot = arr[len(arr) // 2]: Choose the middle element as the pivot.
# Partition the array into left, middle, and right sub-arrays based on the pivot.
# Recursively sort left and right sub-arrays and concatenate them with middle.
# Complexity:

# Time Complexity: O(n log n) on average and O(n^2) in the worst case (when the pivot is consistently the smallest or largest element).
# Space Complexity: O(log n) due to the recursive calls and function call stack.
# 6.20 Space Analysis of Quick Sort
# Quick Sort typically has a space complexity of O(log n) due to the recursive calls that consume space on the call stack. Each recursive call takes up space until it reaches the base case (when the array size is 1 or 0). The space complexity of O(log n) arises because the depth of the recursion tree is logarithmic with respect to the size of the input array.




# 6.21 Heap Sort




# Explanation:
# Heap Sort is another efficient sorting algorithm based on the heap data structure. It involves building a max heap (for ascending order) or min heap (for descending order) from the array, repeatedly removing the root element (which is the largest or smallest depending on the heap type), and reconstructing the heap until the array is sorted.

# Algorithm:

# Build Heap: Build a max heap from the array.
# Heapify: Repeatedly remove the root (largest element for max heap, smallest for min heap), swap it with the last element of the heap, and maintain the heap property.
# Sort: Continue heapifying the reduced heap until the entire array is sorted.
# Example:
# Here's an implementation of Heap Sort in Python:


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with last element
        heapify(arr, i, 0)  # Heapify root element

# Example usage:
arr = [10, 80, 30, 90, 40, 50, 70]
heap_sort(arr)
print("Sorted array using Heap Sort:", arr)
# Code Breakdown:

# heapify(arr, n, i): This function maintains the heap property (max heap in this case) of the subtree rooted at index i of size n.
# heap_sort(arr): This function sorts the array arr in ascending order using Heap Sort.
# Build max heap: Convert the array into a max heap by calling heapify on non-leaf nodes.
# Extract elements: Extract elements from the heap one by one by swapping the root with the last element and then heapifying the reduced heap.
# Complexity:

# Time Complexity: O(n log n) for both average and worst cases.
# Space Complexity: O(1) auxiliary space (in-place sorting), but O(n) total space due to heapify calls.