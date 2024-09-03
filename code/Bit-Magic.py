


# Converting numbers between different number systems—such as binary, decimal, and hexadecimal—is fundamental in computer science and programming. Let's break down how these conversions work, starting from the basics and including examples for each type of conversion.

# Number Systems Basics:
# Decimal (Base 10): The most common number system, which uses digits from 0 to 9. For example, the number 345 in decimal is 3 * 10^2 + 4 * 10^1 + 5 * 10^0.

# Binary (Base 2): Uses only two digits, 0 and 1. It’s used internally by almost all modern computers and devices because it aligns with the on/off state of transistors.

# Octal (Base 8): Uses digits from 0 to 7. It's less commonly used but can be seen in some computing contexts.

# Hexadecimal (Base 16): Uses digits 0 to 9 and letters A to F (which represent values 10 to 15). It's commonly used in computing for a more human-readable representation of binary-coded values.

# Decimal to Binary Conversion
# Method: Repeatedly divide the decimal number by 2 and record the remainders. The binary representation is the sequence of remainders read from bottom to top.


# Example: Convert 45 to binary
# 45 ÷ 2 = 22 remainder 1
# 22 ÷ 2 = 11 remainder 0
# 11 ÷ 2 = 5 remainder 1
# 5 ÷ 2 = 2 remainder 1
# 2 ÷ 2 = 1 remainder 0
# 1 ÷ 2 = 0 remainder 1
# Binary representation: 101101



def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

print(decimal_to_binary(45))  # Output: 101101





# Binary to Decimal Conversion




# Method: Multiply each bit by 2 raised to the position's index, starting from 0 on the right.



def binary_to_decimal(b):
    decimal = 0
    for i in range(len(b)):
        decimal += int(b[-(i + 1)]) * (2 ** i)
    return decimal

print(binary_to_decimal('101101'))  # Output: 45




# Decimal to Octal Conversion



# Method: Similar to decimal to binary, but divide by 8 instead of 2.

# Example: Convert 45 to octal
# 45 ÷ 8 = 5 remainder 5
# 5 ÷ 8 = 0 remainder 5
# Octal representation: 55



def decimal_to_octal(n):
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

print(decimal_to_octal(45))  # Output: 55




# Octal to Decimal Conversion



# Method: Multiply each digit by 8 raised to the position's index, starting from 0 on the right.



def octal_to_decimal(o):
    decimal = 0
    for i in range(len(o)):
        decimal += int(o[-(i + 1)]) * (8 ** i)
    return decimal

print(octal_to_decimal('55'))  # Output: 45



# Decimal to Hexadecimal Conversion



# Method: Divide by 16 and use remainders, using A to F for remainders 10 to 15.

# Example: Convert 45 to hexadecimal
# 45 ÷ 16 = 2 remainder 13 (D in hexadecimal)
# 2 ÷ 16 = 0 remainder 2
# Hexadecimal representation: 2D



def decimal_to_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal

print(decimal_to_hexadecimal(45))  # Output: 2D




# Hexadecimal to Decimal Conversion




# Method: Multiply each digit by 16 raised to the position's index, using 10 to 15 for A to F.



def hexadecimal_to_decimal(h):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    for i in range(len(h)):
        decimal += hex_chars.index(h[-(i + 1)]) * (16 ** i)
    return decimal

print(hexadecimal_to_decimal('2D'))  # Output: 45




# Binary to Hexadecimal Conversion



# Method: Group the binary number into sets of 4 bits (from right to left) and convert each group to a hexadecimal digit.

# Example: Convert 101101 to hexadecimal
# Group as 10 1101 (padding with 0 to make full groups of 4: 0010 1101)
# Convert: 0010 is 2, 1101 is D
# Hexadecimal representation: 2D



def binary_to_hexadecimal(b):
    return hex(int(b, 2))[2:].upper()

print(binary_to_hexadecimal('101101'))  # Output: 2D



# Hexadecimal to Binary Conversion




# Method: Convert each hexadecimal digit to its 4-bit binary equivalent.

# Example: Convert 2D to binary
# 2 is 0010, D is 1101
# Binary representation: 101101



def hexadecimal_to_binary(h):
    return bin(int(h, 16))[2:]

print(hexadecimal_to_binary('2D'))  # Output: 101101




# Summary:
# Use repeated division for conversions from decimal.
# For binary and hexadecimal conversions, group digits for easier translation.
# In Python, built-in functions like bin(), int(), hex() simplify these conversions.







# What Are Bits?






# Before diving into the operators, it's important to understand that computers represent data using binary, which consists of only two digits: 0 and 1. Each binary digit is called a "bit." Bitwise operations are operations that directly manipulate these bits.



# 1. Bitwise AND (&)
# Operation: Compares each bit of two numbers and returns 1 if both bits are 1, otherwise returns 0.
# Use: Often used to clear specific bits (set them to 0).


# Example:


# # Let's take two numbers in binary:
# # 5 in binary is 0101
# # 3 in binary is 0011

# # Applying Bitwise AND:
# # 0101
# # 0011
# # ----
# # 0001  (This is 1 in decimal)

a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Bitwise AND
print(result)  # Output: 1



# Explanation: Compare each bit:

# 1st bit: 1 AND 1 = 1
# 2nd bit: 0 AND 1 = 0
# 3rd bit: 1 AND 0 = 0
# 4th bit: 0 AND 0 = 0
# Result: 0001 (decimal 1).




# 2. Bitwise OR (|)


# Operation: Compares each bit of two numbers and returns 1 if at least one of the bits is 1, otherwise returns 0.
# Use: Used to set specific bits to 1.
# Example:


# # Let's take two numbers in binary:
# # 5 in binary is 0101
# # 3 in binary is 0011

# # Applying Bitwise OR:
# # 0101
# # 0011
# # ----
# # 0111  (This is 7 in decimal)

a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a | b  # Bitwise OR
print(result)  # Output: 7



# Explanation: Compare each bit:

# 1st bit: 1 OR 1 = 1
# 2nd bit: 0 OR 1 = 1
# 3rd bit: 1 OR 0 = 1
# 4th bit: 0 OR 0 = 0
# Result: 0111 (decimal 7).





# 3. Bitwise XOR (^)




# Operation: Compares each bit of two numbers and returns 1 if the bits are different, otherwise returns 0.
# Use: Used to toggle bits (flip from 1 to 0 or vice versa).
# Example:


# # Let's take two numbers in binary:
# # 5 in binary is 0101
# # 3 in binary is 0011

# # Applying Bitwise XOR:
# # 0101
# # 0011
# # ----
# # 0110  (This is 6 in decimal)

a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a ^ b  # Bitwise XOR
print(result)  # Output: 6



# Explanation: Compare each bit:

# 1st bit: 1 XOR 1 = 0
# 2nd bit: 0 XOR 1 = 1
# 3rd bit: 1 XOR 0 = 1
# 4th bit: 0 XOR 0 = 0
# Result: 0110 (decimal 6).




# 4. Bitwise NOT (~)



# Operation: Inverts all the bits of the number (turns 0 into 1 and 1 into 0).
# Use: Used to flip bits.
# Example:


# # Let's take the number 5 in binary:
# # 5 in binary is 0101

# # Applying Bitwise NOT:
# # ~0101
# # ----
# # 1010  (In binary)

# # Note: In Python, this actually results in -6 due to how negative numbers are represented.

a = 5  # Binary: 0101
result = ~a  # Bitwise NOT
print(result)  # Output: -6

# Explanation:

# ~0101 inverts all bits: becomes 1010.
# Due to how Python represents negative numbers, 1010 is interpreted as -6 in decimal.





# 5. Bitwise LEFT SHIFT (<<)



# Operation: Shifts all bits in the number to the left by the specified number of positions. Fills the right with 0s.
# Use: Used to multiply by powers of two.
# Example:


# # Let's take the number 5 in binary:
# # 5 in binary is 0101

# # Applying Bitwise LEFT SHIFT by 1 position:
# # 0101 << 1
# # ----
# # 1010  (This is 10 in decimal)

a = 5  # Binary: 0101
result = a << 1  # Left shift by 1
print(result)  # Output: 10


# Explanation:

# 0101 << 1 shifts all bits left: becomes 1010 (binary) = 10 (decimal).
# 6. Bitwise RIGHT SHIFT (>>)
# Operation: Shifts all bits in the number to the right by the specified number of positions. Fills the left with 0s (or 1s if the number is negative in some languages, but in Python, it fills with 0).
# Use: Used to divide by powers of two.
# Example:


# # Let's take the number 5 in binary:
# # 5 in binary is 0101

# # Applying Bitwise RIGHT SHIFT by 1 position:
# # 0101 >> 1
# # ----
# # 0010  (This is 2 in decimal)

a = 5  # Binary: 0101
result = a >> 1  # Right shift by 1
print(result)  # Output: 2


# Explanation:

# 0101 >> 1 shifts all bits right: becomes 0010 (binary) = 2 (decimal).




# Summary:
# AND (&): Both bits must be 1 to result in 1.
# OR (|): At least one bit must be 1 to result in 1.
# XOR (^): Bits must be different to result in 1.
# NOT (~): Inverts all bits.
# LEFT SHIFT (<<): Shifts bits to the left, filling with 0s.
# RIGHT SHIFT (>>): Shifts bits to the right, filling with 0s.







# 18.2 Bitwise Operator in Python - Part 2





# This section covers more advanced bit manipulation techniques such as:

# Checking if a Number is Even or Odd
# Swapping Numbers without a Temporary Variable
# Setting, Clearing, and Toggling Bits
# Counting Set Bits


# 1. Checking if a Number is Even or Odd


def is_odd(n):
    return (n & 1) == 1

print(is_odd(5))  # Output: True (Odd)
print(is_odd(4))  # Output: False (Even)


# Explanation:

# If the least significant bit (rightmost bit) of a number is 1, the number is odd. Using n & 1, we can check this quickly.




# 2. Swapping Numbers without a Temporary Variable


# a = 5   # Binary: 0101
# b = 3   # Binary: 0011

a = a ^ b   # a becomes 0110 (6)
b = a ^ b   # b becomes 0101 (5)
a = a ^ b   # a becomes 0011 (3)

print(a, b)  # Output: 3 5


# Explanation:

# XORing a and b helps swap them without using a temporary variable due to the properties of XOR.



# 3. Setting, Clearing, and Toggling Bits
# Setting a Bit: Use OR with a mask.



n = 5  # Binary: 0101
pos = 1
mask = 1 << pos

n = n | mask  # Set bit at position 1
print(bin(n)) # Output: 0b111


# Clearing a Bit: Use AND with a negated mask.



n = 5  # Binary: 0101
pos = 2
mask = ~(1 << pos)

n = n & mask  # Clear bit at position 2
print(bin(n)) # Output: 0b1


# Toggling a Bit: Use XOR with a mask.



n = 5  # Binary: 0101
pos = 0
mask = 1 << pos

n = n ^ mask  # Toggle bit at position 0
print(bin(n)) # Output: 0b100



# 4. Counting Set Bits


def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

print(count_set_bits(5))  # Output: 2 (Binary: 0101)


# Explanation:

# Counting set bits involves shifting bits to the right and counting how many 1s are encountered using n & 1.
# Real-Life and Industry Usage
# Efficient Memory Use: Operations like setting, clearing, and toggling bits are used in systems where memory and performance are critical.
# Microcontroller Programming: Bit manipulation is essential in embedded systems to control hardware registers.
# Gaming: Graphics and game engines use bit manipulation for texture handling and game state management.
# Security: Many hashing functions and security protocols rely on precise bit manipulation to ensure data integrity and confidentiality.




# 18.3 Check Kth Bit is Set or Not






# To check if the Kth bit of a number is set (i.e., it is 1), you can use a bitwise AND operation with a mask where only the Kth bit is 1.



def is_kth_bit_set(n, k):
    # Create a mask with only the kth bit set
    mask = 1 << k
    
    # Perform bitwise AND between the number and the mask
    return (n & mask) != 0

# Test
print(is_kth_bit_set(5, 0))  # Output: True (Binary: 0101, 0th bit is set)
print(is_kth_bit_set(5, 1))  # Output: False (Binary: 0101, 1st bit is not set)


# Explanation:

# 1 << k shifts the number 1 left by k positions, creating a mask where only the Kth bit is 1.
# n & mask checks if the Kth bit of n is set. If it is, the result will be non-zero.


# Real-Life Usage:
# Flag Checking: This technique is used in flags or settings where each bit represents a specific option or state.
# Networking: Used to check specific bits in network packets for protocols.
# 18.4 Count Set Bits
# Counting the number of set bits (i.e., bits that are 1) in a binary representation of a number is a common bit manipulation task.



def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Check if the least significant bit is set
        n >>= 1         # Shift bits to the right
    return count

# Test
print(count_set_bits(9))  # Output: 2 (Binary: 1001, 2 bits are set)


# Explanation:

# n & 1 checks if the least significant bit is set.
# n >>= 1 shifts the number to the right, effectively discarding the checked bit.
# The loop continues until all bits are checked.



# Real-Life Usage:
# Population Count in CPUs: Counting set bits is essential in CPU operations like Hamming weight calculation.
# Digital Signal Processing: Used to count occurrences of binary 1s in data streams.




# 18.5 Power of Two



# To check if a number is a power of two, you can use the property that powers of two have only one set bit in their binary representation.



def is_power_of_two(n):
    # A number is a power of two if it has only one set bit
    return n > 0 and (n & (n - 1)) == 0

# Test
print(is_power_of_two(4))  # Output: True (Binary: 100)
print(is_power_of_two(5))  # Output: False (Binary: 101)


# Explanation:

# n & (n - 1) clears the lowest set bit of n. If the result is 0, then n had only one set bit.
# The check n > 0 ensures that n is positive.


# Real-Life Usage:
# Memory Allocation: Powers of two are used in buffer sizes, memory blocks, and other areas where alignment is critical.
# Binary Tree Operations: Checking for powers of two is useful in determining complete binary trees.




# 18.6 One Odd Occurring




# Given an array where all elements occur even times except one, find the odd occurring element.



def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num  # XOR operation
    return result

# Test
print(find_odd_occurrence([4, 3, 3, 4, 4, 4, 5, 5, 6]))  # Output: 6



# Explanation:

# XORing a number with itself results in 0, and XORing with 0 results in the number itself.
# This property helps in canceling out pairs, leaving the odd-occurring number.



# Real-Life Usage:
# Error Detection: XOR is used in parity checks and other error detection algorithms.
# Data Encryption: XOR is a fundamental operation in some encryption algorithms like OTP (One-Time Pad).





# 18.7 Two Odd Occurring




# Given an array where all elements occur even times except two, find those two odd occurring elements.



def find_two_odd_occurrences(arr):
    xor = 0
    for num in arr:
        xor ^= num  # XOR all numbers
    # Find rightmost set bit
    set_bit = xor & -xor

    x = 0
    y = 0
    # Divide numbers into two sets and XOR separately
    for num in arr:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    return x, y

# Test
print(find_two_odd_occurrences([4, 3, 3, 4, 5, 4, 4, 6, 7, 7]))  # Output: (5, 6)

# Explanation:

# XOR of the entire array results in xor which is the XOR of the two odd numbers.
# xor & -xor isolates the rightmost set bit to divide the numbers into two sets.
# XORing the numbers in each set results in the two odd occurring numbers.
# Real-Life Usage:
# Debugging: Finding odd occurrences can help in identifying anomalies in data.
# Signal Processing: Used in finding unmatched signals or corrupted data.




# 18.8 Power Set Using Bitwise




# Generating all subsets (power set) of a set can be efficiently done using bitwise operations.



def power_set(s):
    n = len(s)
    subsets = []
    for i in range(1 << n):  # Loop over 2^n combinations
        subset = [s[j] for j in range(n) if (i & (1 << j))]
        subsets.append(subset)
    return subsets

# Test
print(power_set([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]



# Explanation:

# 1 << n calculates 2^n, which represents all possible combinations of subsets.
# For each number i from 0 to 2^n - 1, i & (1 << j) checks if the j-th bit is set, including the j-th element in the subset.



# Real-Life Usage:
# Combinatorial Problems: Power sets are used in solving problems like the knapsack, subset sum, and other combinatorial algorithms.
# Configuration Testing: Used in testing all possible configurations or scenarios in software testing.



