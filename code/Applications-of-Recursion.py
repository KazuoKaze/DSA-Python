# 4.1 Applications of Recursion


# Definition
# Recursion is a method of solving problems where a function calls itself as a subroutine. This allows the function to be repeated several times as it can call itself during its execution.

# Real-World Use Cases
# Divide and Conquer Algorithms: Algorithms like merge sort and quick sort use recursion to break down problems into smaller subproblems.
# Tree Traversal: Traversing binary trees (inorder, preorder, postorder) is naturally done using recursion.
# Dynamic Programming: Problems like Fibonacci sequence, knapsack problem, etc., use recursion along with memoization.
# Solving Puzzles: Recursive solutions are used for puzzles like the Tower of Hanoi, Sudoku solver, and N-Queens problem.
# Example
# Factorial Calculation: Calculating the factorial of a number is a common example of recursion.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# 4.2 Writing Base Cases in Recursion


# Definition
# The base case is a condition within the recursive function that stops the recursion. Without a base case, the function would call itself indefinitely, resulting in a stack overflow.

# Example
# Factorial Calculation with Base Case:


def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
# In this example, the base case is if n == 0: return 1. This prevents the function from calling itself indefinitely.



# 4.3 Tail Recursion



# Definition
# Tail recursion is a special case of recursion where the recursive call is the last thing executed by the function. This allows for optimizations by the compiler or interpreter, converting the recursive calls into a loop to save stack space.

# Example
# Tail Recursive Factorial:


def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial(n - 1, n * accumulator)

print(factorial(5))  # Output: 120
# Here, the recursive call to factorial is the last operation, making it a tail recursive function.



# 4.4 Print N to 1 using Recursion



# Example

def print_n_to_1(n):
    if n < 1:
        return
    print(n)
    print_n_to_1(n - 1)

print_n_to_1(5)
# Explanation
# The base case is if n < 1: return, which stops the recursion when n is less than 1.
# The function prints n and then calls itself with n-1, decrementing n each time.




# 4.5 Print 1 to N using Recursion




# Example

def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current)
    print_1_to_n(n, current + 1)

print_1_to_n(5)
# Explanation
# The base case is if current > n: return, which stops the recursion when current exceeds n.
# The function prints current and then calls itself with current + 1, incrementing current each time.




# 4.6 Sum of Natural Numbers Using Recursion



# Example

def sum_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural_numbers(n - 1)

print(sum_natural_numbers(5))  # Output: 15
# Explanation
# The base case is if n == 0: return 0, which stops the recursion when n is zero.
# The function adds n to the result of sum_natural_numbers(n - 1), summing up the numbers recursively.



# 4.7 Sum of Digits Using Recursion



# Example

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # Output: 10
# Explanation
# The base case is if n == 0: return 0, which stops the recursion when n is zero.
# The function adds the last digit (n % 10) to the result of sum_of_digits(n // 10), summing up the digits recursively.



# 4.8 Palindrome Check using Recursion



# Example

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False


# Explanation
# The base case is if len(s) <= 1: return True, which stops the recursion when the string length is 1 or 0 (which is inherently a palindrome).
# The function checks if the first and last characters are the same. If not, it returns False.
# If the first and last characters are the same, it recursively calls itself with the substring s[1:-1]