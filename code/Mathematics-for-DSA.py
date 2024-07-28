# 2.1 Count Digits
# Problem: Count the number of digits in a given integer.

# Example:

# Input: 12345
# Output: 5
# Algorithm:

# If the number is 0, it has 1 digit.
# Otherwise, repeatedly divide the number by 10 until it becomes 0, counting the number of divisions.
# Code:


def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

# Test cases
print(count_digits(12345))  # Output: 5
print(count_digits(0))      # Output: 1
print(count_digits(987654321))  # Output: 9
# Code Breakdown:

# def count_digits(n)::
# def defines a function named count_digits that takes an integer n as an argument.
# if n == 0::
# Checks if n is 0.
# return 1:
# If n is 0, the function returns 1 since 0 has one digit.
# count = 0:
# Initializes a counter count to 0.
# while n != 0::
# Starts a loop that continues until n becomes 0.
# n //= 10:
# Divides n by 10 using integer division and updates n.
# count += 1:
# Increments the counter count by 1.
# return count:
# Returns the total count of digits.


# 2.2 Palindrome Number
# Problem: Check if a given number is a palindrome.

# Example:

# Input: 121
# Output: True
# Algorithm:

# Reverse the digits of the number.
# Compare the reversed number with the original number.
# Code:


def is_palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10 ## get the last degit
        reversed_num = reversed_num * 10 + digit
        n //= 10 ## remove the last digit
    return original == reversed_num

# Test cases
print(is_palindrome(121))   # Output: True
print(is_palindrome(123))   # Output: False
print(is_palindrome(1221))  # Output: True
# Code Breakdown:

# def is_palindrome(n)::
# def defines a function named is_palindrome that takes an integer n as an argument.
# original = n:
# Stores the original value of n in the variable original.
# reversed_num = 0:
# Initializes reversed_num to 0.
# while n > 0::
# Starts a loop that continues as long as n is greater than 0.
# digit = n % 10:
# Extracts the last digit of n using the modulus operator.
# reversed_num = reversed_num * 10 + digit:
# Adds the extracted digit to reversed_num after shifting the current digits left by one position (multiplying by 10).
# n //= 10:
# Removes the last digit of n using integer division.
# return original == reversed_num:
# Compares the original number with the reversed number and returns True if they are equal, otherwise False.


# 2.3 Factorial of a Number
# Problem: Compute the factorial of a non-negative integer n.

# Example:

# Input: 5
# Output: 120 (since 5! = 5 * 4 * 3 * 2 * 1 = 120)
# Algorithm:

# Initialize fact to 1.
# Multiply fact by numbers from 1 to n.
# Code:


def factorial(n):
    fact = 1
    for i in range(1, n + 1): 
        fact *= i
    return fact

# Test cases
print(factorial(5))   # Output: 120
print(factorial(0))   # Output: 1 (by definition, 0! = 1)
# Code Breakdown:

# def factorial(n)::
# def defines a function named factorial that takes an integer n as an argument.
# fact = 1:
# Initializes fact to 1.
# for i in range(1, n + 1)::
# Starts a loop that runs from 1 to n (inclusive).
# fact *= i:
# Multiplies fact by i and updates fact.
# return fact:
# Returns the computed factorial value.


# 2.4 Trailing Zeros in Factorial
# Problem: Count the number of trailing zeros in n! (factorial of n).

# Example:

# Input: 10
# Output: 2 (since 10! = 3628800 has 2 trailing zeros)
# Algorithm:

# Initialize count to 0.
# Divide n by powers of 5 and add to count until n becomes 0.
# Code:


def trailing_zeros_in_factorial(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

# Test cases
print(trailing_zeros_in_factorial(10))   # Output: 2
print(trailing_zeros_in_factorial(5))    # Output: 1
print(trailing_zeros_in_factorial(25))   # Output: 6
# Code Breakdown:

# def trailing_zeros_in_factorial(n)::
# def defines a function named trailing_zeros_in_factorial that takes an integer n as an argument.
# count = 0:
# Initializes count to 0.
# i = 5:
# Initializes i to 5.
# while n // i > 0::
# Starts a loop that continues as long as n divided by i is greater than 0.
# count += n // i:
# Adds the result of n divided by i to count.
# i *= 5:
# Multiplies i by 5.
# return count:
# Returns the total count of trailing zeros.


# 2.5 GCD and HCF of Two Numbers
# Problem: Compute the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of two integers a and b.

# Example:

# Input: a = 12, b = 18
# Output: 6 (since GCD of 12 and 18 is 6)
# Algorithm:

# Use Euclid's algorithm: gcd(a, b) = gcd(b, a % b) until b becomes 0.
# Code:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
print(gcd(12, 18))   # Output: 6
print(gcd(5, 7))     # Output: 1 (since GCD of prime numbers is always 1)
# Code Breakdown:

# def gcd(a, b)::
# def defines a function named gcd that takes two integers a and b as arguments.
# while b != 0::
# Starts a loop that continues as long as b is not 0.
# a, b = b, a % b:
# Updates a to b and b to a % b.
# return a:
# Returns the GCD of a and b.


# 2.6 LCM of Two Numbers
# Problem: Compute the Least Common Multiple (LCM) of two integers a and b.

# Example:

# Input: a = 12, b = 18
# Output: 36 (since LCM of 12 and 18 is 36)
# Algorithm:

# LCM of a and b is a * b / gcd(a, b).
# Code:


def lcm(a, b):
    return (a * b) // gcd(a, b)  # using gcd function from previous example

# Test cases
print(lcm(12, 18))   # Output: 36
print(lcm(5, 7))     # Output: 35 (since LCM of prime numbers is their product)
# Code Breakdown:

# def lcm(a, b)::
# def defines a function named lcm that takes two integers a and b as arguments.
# return (a * b) // gcd(a, b):
# Computes the LCM of a and b using the formula LCM(a, b) = (a * b) / GCD(a, b) and returns it.


# 2.7 Check for Prime


# Problem: Check if a given integer n is a prime number.

# Example:

# Input: 7
# Output: True
# Algorithm:

# Check divisibility of n by numbers from 2 to sqrt(n).
# Code:


import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(7))    # Output: True
print(is_prime(16))   # Output: False
print(is_prime(23))   # Output: True

# Code Breakdown:

# import math:
# Imports the math module to use the sqrt function.
# def is_prime(n)::
# def defines a function named is_prime that takes an integer n as an argument.
# if n <= 1::
# Checks if n is less than or equal to 1.
# return False:
# Returns False since numbers less than or equal to 1 are not prime.
# if n == 2::
# Checks if n is 2.
# return True:
# Returns True since 2 is a prime number.
# if n % 2 == 0::
# Checks if n is divisible by 2.
# return False:
# Returns False since even numbers greater than 2 are not prime.
# sqrt_n = int(math.sqrt(n)) + 1:
# Computes the square root of n and adds 1.
# for i in range(3, sqrt_n, 2)::
# Starts a loop that runs from 3 to sqrt_n (exclusive) with a step of 2.
# if n % i == 0::
# Checks if n is divisible by i.
# return False:
# Returns False since n is divisible by a number other than 1 and itself.
# return True:
# Returns True if n is not divisible by any number up to its square root.


# 2.8 Prime Factors
# Problem: Compute prime factors of a given integer n.

# Example:

# Input: 315
# Output: [3, 3, 5, 7] (since 315 = 3 * 3 * 5 * 7)
# Algorithm:

# Divide n by the smallest prime numbers and continue until n becomes 1.
# Code:


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(prime_factors(315))   # Output: [3, 3, 5, 7]
print(prime_factors(60))    # Output: [2, 2, 3, 5]
print(prime_factors(29))    # Output: [29] (since 29 is a prime number)
# Code Breakdown:

# def prime_factors(n)::
# def defines a function named prime_factors that takes an integer n as an argument.
# factors = []:
# Initializes an empty list factors to store the prime factors.
# i = 2:
# Initializes i to 2.
# while i * i <= n::
# Starts a loop that continues as long as i * i is less than or equal to n.
# while n % i == 0::
# Starts an inner loop that continues as long as n is divisible by i.
# factors.append(i):
# Appends i to the list factors.
# n //= i:
# Divides n by i using integer division.
# i += 1:
# Increments i by 1.
# if n > 1::
# Checks if n is greater than 1 after the loop.
# factors.append(n):
# Appends n to the list factors (if n is a prime number greater than 1).
# return factors:
# Returns the list of prime factors.
# 2.9 All Divisors of a Number
# Problem: Find all divisors of a given integer n.

# Example:

# Input: 30
# Output: [1, 2, 3, 5, 6, 10, 15, 30]
# Algorithm:

# Iterate from 1 to sqrt(n) and for each i, if i divides n, then both i and n/i are divisors.
# Code:


def all_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

# Test cases
print(all_divisors(30))    # Output: [1, 2, 3, 5, 6, 10, 15, 30]
print(all_divisors(64))    # Output: [1, 2, 4, 8, 16, 32, 64]
print(all_divisors(17))    # Output: [1, 17] (since 17 is a prime number)
# Code Breakdown:

# def all_divisors(n)::
# def defines a function named all_divisors that takes an integer n as an argument.
# divisors = []:
# Initializes an empty list divisors to store the divisors.
# i = 1:
# Initializes i to 1.
# while i * i <= n::
# Starts a loop that continues as long as i * i is less than or equal to n.
# if n % i == 0::
# Checks if n is divisible by i.
# divisors.append(i):
# Appends i to the list divisors.
# if i != n // i::
# Checks if i is not equal to n // i.
# divisors.append(n // i):
# Appends n // i to the list divisors.
# i += 1:
# Increments i by 1.
# return sorted(divisors):
# Returns the sorted list of divisors.
# 2.10 Sieve of Eratosthenes
# Problem: Generate all prime numbers up to a given integer n.

# Example:

# Input: 30
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Algorithm:

# Create a boolean array is_prime of size n+1 initialized to True.
# Mark multiples of each prime starting from 2 as False.
# Code:


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers

# Test cases
print(sieve_of_eratosthenes(30))    # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(sieve_of_eratosthenes(20))    # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(sieve_of_eratosthenes(10))    # Output: [2, 3, 5, 7]
# Code Breakdown:

# def sieve_of_eratosthenes(n)::
# def defines a function named sieve_of_eratosthenes that takes an integer n as an argument.
# is_prime = [True] * (n + 1):
# Creates a list is_prime of size n + 1 initialized to True.
# p = 2:
# Initializes p to 2.
# while p * p <= n::
# Starts a loop that continues as long as p * p is less than or equal to n.
# if is_prime[p]::
# Checks if p is a prime number.
# for i in range(p * p, n + 1, p)::
# Starts an inner loop that runs from p * p to n with a step of p.
# is_prime[i] = False:
# Marks multiples of p as False.
# p += 1:
# Increments p by 1.
# prime_numbers = []:
# Initializes an empty list prime_numbers to store the prime numbers.
# for p in range(2, n + 1)::
# Starts a loop that runs from 2 to n.
# if is_prime[p]::
# Checks if p is a prime number.
# prime_numbers.append(p):
# Appends p to the list prime_numbers.
# return prime_numbers:
# Returns the list of prime numbers.
# 2.11 Computing Power
# Problem: Compute a raised to the power b (a^b).

# Example:

# Input: a = 3, b = 4
# Output: 81 (since 3^4 = 81)
# Algorithm:

# Multiply a by itself b times.
# Code:


def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Test cases
print(power(3, 4))    # Output: 81
print(power(2, 5))    # Output: 32
print(power(5, 3))    # Output: 125
# Code Breakdown:

# def power(a, b)::
# def defines a function named power that takes two integers a and b as arguments.
# result = 1:
# Initializes result to 1.
# for _ in range(b)::
# Starts a loop that runs b times. The underscore _ is used as a variable name when the variable is not needed.
# result *= a:
# Multiplies result by a and updates result.
# return result:
# Returns the computed power value.


# 2.12 Iterative Power
# Problem: Compute a raised to the power b (a^b) using an iterative approach.

# Example:

# Input: a = 3, b = 4
# Output: 81 (since 3^4 = 81)
# Algorithm: Use the method of exponentiation by squaring, which is an efficient way to compute powers. The basic idea is:

# If b is even, a^b = (a^(b/2))^2.
# If b is odd, a^b = a * a^(b-1).
# This reduces the number of multiplications needed, leading to a logarithmic time complexity.
# Code:


def iterative_power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:   # if b is odd
            result *= a
        a *= a            # square the base
        b //= 2           # divide the power by 2
    return result

# Test cases
print(iterative_power(3, 4))    # Output: 81
print(iterative_power(2, 5))    # Output: 32
print(iterative_power(5, 3))    # Output: 125
# Code Breakdown
# Function Definition:

# def iterative_power(a, b):
# Defines a function named iterative_power that takes two arguments: a (the base) and b (the exponent).
# Initialization:

# result = 1
# Initializes a variable result to 1. This will hold the final result of a^b.
# While Loop:

# while b > 0:
# The loop continues as long as b is greater than 0.
# Odd Exponent Handling:

# if b % 2 == 1:
# Checks if b is odd by using the modulus operator. If b is odd (b % 2 equals 1):
# result *= a
# Multiplies result by a and updates result.
# Squaring the Base:

# a *= a
# Squares the base a. This is equivalent to a = a * a.
# Halving the Exponent:

# b //= 2
# Divides b by 2 using integer division and updates b.
# Return Statement:

# return result
# Returns the computed value of a^b.