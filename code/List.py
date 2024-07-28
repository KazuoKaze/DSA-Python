# 3.1 Introduction to List


# Introduction
# In Python, a list is a versatile data structure that allows you to store and manipulate collections of items. Lists are mutable, meaning they can be changed after creation, and they can contain elements of different data types. Lists are defined by enclosing comma-separated values within square brackets [ ].

# Real-World Uses
# Data Storage and Processing: Lists are commonly used for storing and processing data in various applications such as:

# Database Management: Storing query results, managing database entries, and representing relationships between data entities.
# Business Applications: Managing customer records, sales data, and inventory lists.
# Scientific Computing: Storing experimental data, results of simulations, and mathematical computations.
# User Interface and Interaction: Lists are used to manage and display user choices, preferences, and selections in user interfaces, web applications, and interactive software.

# Industrial Uses
# E-commerce Platforms: Lists are integral to e-commerce platforms for managing product catalogs, shopping cart items, and user preferences.

# Financial Applications: Lists are used to store financial data, track transactions, and manage portfolio holdings in banking and investment applications.

# Code Example and Breakdown

# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Accessing elements in the list
print(numbers[0])   # Output: 1
print(numbers[2])   # Output: 3

# Modifying elements in the list
numbers[1] = 10
print(numbers)      # Output: [1, 10, 3, 4, 5]

# Adding elements to the list
numbers.append(6)
print(numbers)      # Output: [1, 10, 3, 4, 5, 6]

# Removing elements from the list
numbers.remove(3)
print(numbers)      # Output: [1, 10, 4, 5, 6]

# Iterating through the list
for num in numbers:
    print(num)

# Output:
# 1
# 10
# 4
# 5
# 6

# Explanation
# Creating a List: Lists are created by enclosing elements within square brackets [ ].

# Accessing Elements: Elements in a list are accessed using index notation, starting from 0.

# Modifying Elements: Lists are mutable, so you can change the value of elements directly using their index.

# Adding Elements: append() method adds elements to the end of the list.

# Removing Elements: remove() method removes the first occurrence of a specified value from the list.

# Iterating through a List: Lists can be iterated using a for loop to perform operations on each element sequentially.

# 3.2 Working of List in Python

# Explanation
# Dynamic Sizing: Lists in Python are dynamic arrays, which means they automatically resize as elements are added or removed. This dynamic sizing allows for efficient memory management and flexibility in handling varying amounts of data.

# Element Access: Elements in a list are accessed using their index, which allows for fast retrieval and manipulation of specific elements within the list.

# Mutability: Lists are mutable, meaning you can modify individual elements, change the order of elements, or replace the entire list with a new list without creating a new list object.

# Real-World Uses
# Data Analysis and Processing: Lists are used extensively in data science and analytics for storing, processing, and analyzing datasets.

# Web Development: Lists are utilized in web applications for managing user sessions, storing form data, and handling user interactions.

# Industrial Uses
# Content Management Systems: Lists are employed in CMS platforms to manage content items, user permissions, and content revisions.

# Social Media Platforms: Lists are used to manage user profiles, friends' lists, and posts in social networking applications.

# Code Example and Breakdown

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Length of the list
print(len(fruits))   # Output: 3

# Iterating through the list using index
for i in range(len(fruits)):
    print(fruits[i])

# Output:
# apple
# banana
# cherry

# List comprehension to create a new list
upper_case_fruits = [fruit.upper() for fruit in fruits]
print(upper_case_fruits)   # Output: ['APPLE', 'BANANA', 'CHERRY']

# Sorting a list
fruits.sort()
print(fruits)   # Output: ['apple', 'banana', 'cherry']

# Reversing a list
fruits.reverse()
print(fruits)   # Output: ['cherry', 'banana', 'apple']


# Explanation
# Length of List: The len() function returns the number of elements in the list.

# Iterating through a List: Lists can be iterated using a for loop or list comprehension to perform operations on each element.

# List Comprehension: List comprehensions provide a concise way to create new lists by iterating over existing lists and applying operations to each element.

# Sorting and Reversing: Lists can be sorted using the sort() method and reversed using the reverse() method to change their order.

# 3.3 Average or Mean of a List


# Explanation
# Calculating the average or mean of a list involves summing all the elements in the list and dividing by the number of elements. This is a basic statistical operation useful for analyzing data sets.

# Real-World Uses
# Data Analysis: Average is used extensively in data science and analytics to summarize numerical data.
# Performance Metrics: Average performance metrics in engineering or business contexts.
# Grade Calculation: Computing average scores in educational systems.
# Industrial Uses
# Financial Analysis: Average daily returns in financial markets.
# Quality Control: Average defect rates in manufacturing processes.
# Code Example and Breakdown

def average_of_list(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print("Average:", average_of_list(numbers))  # Output: 3.0

# Explanation:
# Function Definition: average_of_list(nums) calculates the average of the numbers in the list nums.
# Edge Case Handling: Checks if the list is empty to avoid division by zero.
# Calculation: Uses sum(nums) to compute the total sum of elements and divides by len(nums) to get the average.


# 3.4 Separate Even and Odd


# Explanation
# Separating even and odd numbers from a list involves partitioning the elements based on their divisibility by 2.

# Real-World Uses
# Data Filtering: Separating data based on specific criteria (e.g., even or odd).
# Performance Optimization: Algorithms that benefit from segregating elements based on parity.
# Industrial Uses
# Data Processing: Filtering out specific types of data in various applications.
# Resource Allocation: Assigning resources based on different criteria.
# Code Example and Breakdown

def separate_even_odd(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 != 0]
    return even_nums, odd_nums

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = separate_even_odd(numbers)
print("Even numbers:", evens)   # Output: [2, 4, 6, 8, 10]
print("Odd numbers:", odds)     # Output: [1, 3, 5, 7, 9]

# Explanation:
# List Comprehension: Constructs two lists (even_nums and odd_nums) based on whether the number is even or odd.
# Filtering: Uses the condition num % 2 == 0 for even numbers and num % 2 != 0 for odd numbers.


# 3.5 Get Smaller Elements


# Explanation
# Getting smaller elements from a list involves finding elements that are less than a specified threshold value.

# Real-World Uses
# Data Filtering: Selecting data points below a certain threshold.
# Decision Making: Identifying conditions or criteria that are not met.
# Industrial Uses
# Quality Control: Identifying defective products based on predefined standards.
# Risk Assessment: Evaluating risks based on certain thresholds.
# Code Example and Breakdown

def get_smaller_elements(nums, threshold):
    smaller_nums = [num for num in nums if num < threshold]
    return smaller_nums

# Example usage:
numbers = [10, 20, 5, 15, 30, 25]
threshold = 20
smaller_than_20 = get_smaller_elements(numbers, threshold)
print("Numbers smaller than", threshold, ":", smaller_than_20)  # Output: [10, 5, 15]

# Explanation:
# Function Definition: get_smaller_elements(nums, threshold) returns a list of numbers from nums that are smaller than threshold.
# List Comprehension: Creates smaller_nums list by iterating through nums and selecting numbers less than threshold.


# 3.6 Slicing (List, Tuple, and String)


# Explanation
# Slicing is a powerful feature in Python that allows you to extract a subset of elements from a sequence (like lists, tuples, or strings) based on specified indices.

# Real-World Uses
# Data Extraction: Selecting specific portions of data for analysis.
# String Manipulation: Extracting substrings or segments of text.
# Data Transformation: Converting and reshaping data based on slicing operations.
# Industrial Uses
# Data Processing Pipelines: Extracting features or columns from datasets.
# Text Processing: Segmenting text data into tokens or sentences.
# Image Processing: Extracting regions of interest from images.
# Code Example and Breakdown

# Slicing examples for lists
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice from index 2 to 5 (exclusive)
slice_1 = my_list[2:5]
print("Slice 1:", slice_1)  # Output: [3, 4, 5]

# Slice from start to index 7 (exclusive)
slice_2 = my_list[:7]
print("Slice 2:", slice_2)  # Output: [1, 2, 3, 4, 5, 6, 7]

# Slice from index 3 to end
slice_3 = my_list[3:]
print("Slice 3:", slice_3)  # Output: [4, 5, 6, 7, 8, 9, 10]

# Slicing examples for strings
my_string = "Hello, World!"

# Slice from index 1 to 7 (exclusive)
slice_str = my_string[1:7]
print("Slice string:", slice_str)  # Output: "ello, "

# Negative indices for slicing
slice_negative = my_list[-3:]
print("Slice negative:", slice_negative)  # Output: [8, 9, 10]


# Explanation:
# Syntax: sequence[start_index:end_index:step]
# List Slicing: Extracts elements from start_index to end_index-1.
# String Slicing: Extracts characters from start_index to end_index-1.
# Negative Indices: Allows slicing from the end of the sequence.


# 3.7 Comprehensions in Python


# Explanation
# Comprehensions are concise and efficient ways to create lists, dictionaries, or sets in Python by applying an expression to each item in an iterable.

# Real-World Uses
# Data Transformation: Creating new data structures based on existing data.
# Filtering Data: Selecting elements that meet specific criteria.
# Dictionary and Set Construction: Building dictionaries and sets dynamically.
# Industrial Uses
# Data Cleaning: Filtering out invalid or outlier data points.
# Feature Engineering: Creating new features based on existing ones.
# Performance Optimization: Improving code readability and execution speed.
# Code Example and Breakdown

# List comprehension example
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Conditional list comprehension
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Even squares:", even_squares)  # Output: [4, 16]

# Dictionary comprehension example
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print("Name lengths:", name_lengths)  # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Set comprehension example
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print("Unique numbers:", unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Explanation:

# Syntax: [expression for item in iterable if condition]
# List Comprehension: Creates a new list (squares) by squaring each element in numbers.
# Conditional Comprehension: Filters elements (even_squares) that satisfy the condition (x % 2 == 0).
# Dictionary Comprehension: Constructs a dictionary (name_lengths) mapping names to their lengths.
# Set Comprehension: Builds a set (unique_numbers) containing unique elements from numbers.


# 3.8 Largest Element in a List


# Explanation
# Finding the largest element in a list involves iterating through the list to identify the maximum value.

# Real-World Uses
# Maximum Value Detection: Identifying the peak or highest value in a dataset.
# Resource Allocation: Determining the largest resource demand in a system.
# Performance Evaluation: Evaluating the worst-case scenario or bottleneck.
# Industrial Uses
# Inventory Management: Identifying the most demanded product.
# System Optimization: Allocating resources based on peak demands.
# Financial Analysis: Finding the highest revenue-generating asset.
# Code Example and Breakdown

def find_largest_element(nums):
    if not nums:
        return None
    largest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
    return largest

# Example usage:
numbers = [12, 45, 23, 67, 89, 34]
print("Largest element:", find_largest_element(numbers))  # Output: 89

# Explanation:
# Function Definition: find_largest_element(nums) finds the largest number in the list nums.
# Initialization: Sets largest to the first element of nums.
# Iteration: Compares each subsequent element (num) with largest and updates largest if num is larger.


# 3.9 Second Largest Element in a List


# Explanation
# Finding the second largest element in a list involves identifying the maximum value excluding the largest element.

# Real-World Uses
# Runner-Up Determination: Identifying the second-highest score or value in a competition.
# Backup or Alternate: Selecting an alternative option when the primary choice is unavailable.
# Risk Assessment: Evaluating the next critical or significant value in a risk hierarchy.
# Industrial Uses
# Performance Ranking: Identifying the second best-performing entity or solution.
# Resource Allocation: Allocating resources to backup or contingency plans.
# Decision Making: Considering alternatives or fallback options.
# Code Example and Breakdown

def find_second_largest(nums):
    if not nums or len(nums) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None

# Example usage:
numbers = [12, 45, 23, 67, 89, 34]
print("Second largest element:", find_second_largest(numbers))  # Output: 67

# Explanation:
# Function Definition: find_second_largest(nums) finds the second largest number in the list nums.
# Initialization: Initializes largest and second_largest to very low values (float('-inf')).
# Iteration: Updates largest and second_largest based on conditions ensuring second_largest is not equal to largest and is larger than other elements.


# 3.10 Check if a List is Sorted


# Explanation
# Checking if a list is sorted involves verifying whether the elements are arranged in either ascending or descending order.

# Real-World Uses
# Data Validation: Ensuring that data entries are in the expected order.
# Algorithmic Requirements: Verifying sorted inputs for certain algorithms.
# Quality Control: Checking sorted order in manufacturing or production processes.
# Industrial Uses
# Financial Data: Verifying chronological or numerical order in financial records.
# Inventory Management: Checking product lists for proper ordering.
# Logistics: Ensuring correct sequence of tasks or operations.
# Code Example and Breakdown

def is_sorted(nums):
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

# Example usage:
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [7, 2, 4, 1, 9]

print("Is numbers1 sorted?", is_sorted(numbers1))  # Output: True
print("Is numbers2 sorted?", is_sorted(numbers2))  # Output: False


# Explanation:
# Function Definition: is_sorted(nums) checks if the list nums is sorted in non-decreasing order.
# Iteration: Uses a generator expression with all() to iterate through pairs of consecutive elements (nums[i] and nums[i + 1]) and check if each pair satisfies the condition nums[i] <= nums[i + 1].
# Return Value: Returns True if all pairs satisfy the condition, indicating the list is sorted; otherwise, returns False.


# 3.11 Find the Only Odd


# Explanation
# Finding the only odd number in a list involves identifying the element that is not divisible by 2.

# Real-World Uses
# Error Detection: Identifying an unexpected or outlier value in a dataset.
# Unique Element Identification: Locating the only element with specific properties.
# Condition Verification: Checking for special cases or unique conditions.
# Industrial Uses
# Quality Control: Identifying irregularities or exceptions in manufacturing processes.
# Financial Transactions: Detecting unusual or singular transactions in a sequence.
# Logistics: Confirming unique items or scenarios in operational workflows.
# Code Example and Breakdown

def find_only_odd(nums):
    odd_count = 0
    odd_number = None
    for num in nums:
        if num % 2 != 0:
            odd_count += 1
            odd_number = num
    if odd_count == 1:
        return odd_number
    return None

# Example usage:
numbers1 = [2, 4, 6, 8, 7]
numbers2 = [1, 2, 3, 4, 5]

print("Only odd number in numbers1:", find_only_odd(numbers1))  # Output: 7
print("Only odd number in numbers2:", find_only_odd(numbers2))  # Output: 5

# Explanation:
# Function Definition: find_only_odd(nums) identifies the only odd number in the list nums.
# Iteration: Iterates through each number in nums and checks if it is odd (num % 2 != 0).
# Counting: Keeps track of the count of odd numbers (odd_count) and stores the odd number (odd_number) if found.
# Result: Returns odd_number if there is exactly one odd number (odd_count == 1), otherwise returns None.


# 3.12 Reverse a List in Python


# Explanation
# Reversing a list involves flipping the order of elements from the last to the first.

# Real-World Uses
# Data Transformation: Inverting sequences for different processing requirements.
# Output Formatting: Reversing output order for presentation or readability.
# Algorithm Reversal: Manipulating data flow in certain algorithms.
# Industrial Uses
# Data Analysis: Inverting temporal or spatial sequences for analysis purposes.
# User Interface: Modifying display order for user interaction.
# Decision Making: Adjusting sequences for optimal decision pathways.
# Code Example and Breakdown

def reverse_list(nums):
    return nums[::-1]

# Example usage:
numbers = [1, 2, 3, 4, 5]

print("Reversed list:", reverse_list(numbers))  # Output: [5, 4, 3, 2, 1]

# Explanation:
# Function Definition: reverse_list(nums) returns a new list that is the reverse of nums.
# Slicing: Uses Python's slicing feature nums[::-1] to create a reversed copy of the list.
# Efficiency: Slicing is an efficient way to reverse a list without modifying the original list.
# Return Value: Returns the reversed list as the output.



# 3.13 Remove Duplicates from Sorted Array



# Explanation
# Removing duplicates from a sorted array involves retaining only unique elements while maintaining the sorted order. Since the array is sorted, duplicates will be consecutive.

# Real-World Uses
# Data Cleaning: Removing redundant entries in databases or datasets.
# Efficiency Improvement: Optimizing search and retrieval operations.
# Memory Optimization: Reducing storage space in memory-constrained environments.
# Industrial Uses
# Database Operations: Ensuring uniqueness in primary or indexed fields.
# Financial Data: Processing transaction records to avoid duplicate entries.
# Web Applications: Managing user input to maintain integrity and performance.
# Code Example and Breakdown

def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Initialize a pointer to track the position of the next unique element
    unique_index = 0
    
    # Iterate through the array
    for i in range(1, len(nums)):
        # If current element is different from the previous unique element
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    
    # Length of the array with unique elements
    return unique_index + 1

# Example usage:
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(nums)
print("Array after removing duplicates:", nums[:length])  # Output: [1, 2, 3, 4, 5]


# Explanation:
# Function Definition: remove_duplicates(nums) modifies the list nums to remove duplicates and returns the length of the new array with unique elements.
# Pointer Approach: Uses a pointer (unique_index) to track the position of the next unique element.
# Iteration: Iterates through the array (nums) and compares each element with the previous unique element. If different, updates unique_index and stores the new unique element.
# Efficiency: Runs in O(n) time complexity, where n is the number of elements in the array, and modifies the array in-place without using extra space (except for the pointer).


# 3.14 Move Zeros to End



# Explanation
# Moving zeros to the end of an array involves rearranging elements so that all zeros are at the end while maintaining the relative order of non-zero elements.

# Real-World Uses
# Data Filtering: Processing sensor data where zero readings are irrelevant.
# Algorithm Optimization: Enhancing search algorithms by excluding non-relevant data.
# Performance Tuning: Improving computational efficiency in data-driven applications.
# Industrial Uses
# Environmental Monitoring: Filtering out zero-valued measurements for accurate analysis.
# Financial Analysis: Processing financial data with irrelevant zero-value entries.
# Manufacturing: Managing production data by excluding zero readings from quality checks.
# Code Example and Breakdown

def move_zeros_to_end(nums):
    # Count non-zero elements
    non_zero_count = 0
    
    # Traverse the array, move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_count], nums[i] = nums[i], nums[non_zero_count]
            non_zero_count += 1
    
    # All non-zero elements are moved to the beginning, fill remaining with zeros
    for i in range(non_zero_count, len(nums)):
        nums[i] = 0
    
    return nums

# Example usage:
nums = [0, 1, 0, 3, 12]
print("Array after moving zeros to end:", move_zeros_to_end(nums))  # Output: [1, 3, 12, 0, 0]

# Explanation:
# Function Definition: move_zeros_to_end(nums) modifies the list nums to move all zeros to the end while maintaining the order of non-zero elements.
# Two-Pointer Technique: Uses two pointers where non_zero_count tracks the position to place the next non-zero element encountered.
# Iteration: First iteration moves all non-zero elements to the front of the array. Second iteration fills the remaining positions with zeros.
# Efficiency: Runs in O(n) time complexity, where n is the number of elements in the array, and modifies the array in-place.


# 3.15 Leaders in an Array Problem


# Explanation
# Finding leaders in an array involves identifying elements that are greater than all elements to their right.

# Real-World Uses
# Stock Market Analysis: Identifying stocks that outperform others in a given period.
# Performance Evaluation: Highlighting top-performing entities in various sectors.
# Resource Allocation: Optimizing resource distribution based on performance metrics.
# Industrial Uses
# Business Analytics: Identifying top-selling products or profitable ventures.
# Healthcare: Identifying effective treatments or medical procedures.
# Education: Recognizing high-performing students or educational programs.
# Code Example and Breakdown

def find_leaders(nums):
    leaders = []
    max_from_right = float('-inf')
    
    # Traverse the array from right to left
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > max_from_right:
            max_from_right = nums[i]
            leaders.append(max_from_right)
    
    # Reverse leaders list to match original order
    leaders.reverse()
    return leaders

# Example usage:
nums = [16, 17, 4, 3, 5, 2]
print("Leaders in the array:", find_leaders(nums))  # Output: [17, 5, 2]


# Explanation:
# Function Definition: find_leaders(nums) identifies and returns the leaders (elements greater than all elements to their right) in the list nums.
# Traverse from Right to Left: Starts from the end of the array and tracks the maximum element encountered (max_from_right). If a new leader is found, adds it to the leaders list.
# Reverse: Since the result needs to match the original order of elements, reverses the leaders list before returning.
# Efficiency: Runs in O(n) time complexity, where n is the number of elements in the array, and uses O(1) additional space besides the leaders list.