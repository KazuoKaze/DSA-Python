
# Learning Resources


# YT videos: ( https://www.youtube.com/watch?v=jalSiaIi8j4&pp=ygUScm9hZG1hcCBzaCBoYXNobWFw )



# 7.1 Introduction to Hashing



# What is Hashing?
# Hashing is a process used to map data of arbitrary size to fixed-size values, typically through the use of a hash function. These fixed-size values are called hash codes, hash values, or simply hashes. Hashing is widely used in various fields of computer science, particularly in data storage, retrieval, and cryptography.

# Real-Life Usage

# Password Storage: Hashing is used to store passwords securely. Instead of storing the actual password, a hash of the password is stored. When a user enters a password, the system hashes the entered password and compares it with the stored hash.

# Data Retrieval: Hashing is used in hash tables and hash maps, which allow for fast data retrieval. For example, a database might use hashing to quickly locate a record based on a key.

# Digital Signatures: Hashing is used in cryptography for creating digital signatures, ensuring the integrity and authenticity of a message or document.

# Industry Usage
# Databases: Databases like MySQL and PostgreSQL use hashing in indexing to improve search efficiency.
# Caching Systems: Caching systems like Redis and Memcached use hashing to store and retrieve data efficiently.
# Blockchain: Cryptographic hashing is a fundamental part of blockchain technology, used in the creation of blocks and ensuring data integrity.


# Code Breakdown (Hash Function Example in Python)

def hash_function(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % 10

# def hash_function(key):: This defines a simple hash function that takes a key as input.
# hash_value = 0: Initialize a variable hash_value to store the computed hash value.
# for char in key:: Loop through each character in the key.
# hash_value += ord(char): Add the ASCII value of the character to hash_value.
# return hash_value % 10: Return the hash value modulo 10. This ensures that the hash value falls within a specific range (0-9 in this case).




# 7.2 Hashing Applications





# Common Applications of Hashing
# Hash Tables/Hash Maps:

# Hash tables use a hash function to compute an index into an array of buckets, where the desired value can be found. This allows for average-case O(1) time complexity for search, insert, and delete operations.
# Real-Life Example: Using a phonebook where names (keys) are hashed to find corresponding phone numbers (values).
# Cryptographic Hashing:

# Used in encryption and data integrity verification. Functions like SHA-256 generate a fixed-size hash, ensuring that even a small change in input results in a significantly different hash.
# Real-Life Example: Verifying the integrity of downloaded files by comparing the hash provided by the source with the hash of the downloaded file.


# Load Balancing:

# Hashing can distribute incoming requests across multiple servers by hashing the client's IP address to determine which server to route the request to.
# Real-Life Example: Content delivery networks (CDNs) use hashing to distribute content across multiple servers.
# Data Deduplication:

# Hashing is used to identify duplicate files or data blocks by hashing the data and comparing hash values.

# Real-Life Example: Cloud storage services use hashing to save space by avoiding storing duplicate copies of the same file.





# 7.3 Direct Address Table






# What is a Direct Address Table?
# A Direct Address Table is a simple form of a hash table where the universe of keys is relatively small and all possible keys are directly mapped to indices in an array. Each index in the array corresponds to a key, and the value at that index is the data associated with that key.

# Real-Life Usage
# Sparse Arrays: Direct Address Tables are used in cases where you have a large but sparse array, where only a few positions have non-zero values. For example, managing a sparse matrix or adjacency matrix in a graph.
# Simple Caching Mechanisms: Direct Address Tables can be used in simple caching mechanisms where the key space is small and predictable.
# Industry Usage
# Operating Systems: In some operating systems, Direct Address Tables are used in the management of processes where process IDs are directly mapped to process control blocks.
# Embedded Systems: Direct Address Tables are used in embedded systems where memory is limited and the key space is small and known in advance.
# Code Breakdown (Direct Address Table Example in Python)

class DirectAddressTable:
    def __init__(self, size):
        self.table = [None] * size

    def insert(self, key, value):
        self.table[key] = value

    def delete(self, key):
        self.table[key] = None

    def search(self, key):
        return self.table[key]
    

# class DirectAddressTable:: Defines a class DirectAddressTable for creating a direct address table.
# def __init__(self, size):: The constructor initializes the table with a fixed size.
# self.table = [None] * size: Creates a list of the given size initialized with None.
# def insert(self, key, value):: This method inserts a value at the index specified by key.
# self.table[key] = value: Stores the value at the position key.
# def delete(self, key):: This method deletes the value at the index specified by key.
# self.table[key] = None: Sets the position key to None.
# def search(self, key):: This method searches for the value at the index specified by key.
# return self.table[key]: Returns the value at the position key.





# 7.4 Hashing Functions






# Introduction
# A hashing function is a crucial part of a hashing-based data structure. It maps input data (keys) to a fixed-size value, typically an integer, which is used as an index in a hash table. The goal is to distribute keys uniformly across the hash table to minimize collisions (i.e., different keys being hashed to the same index).

# Real-Life Usage
# Data Storage: Hashing functions are used in databases to quickly locate records.
# Cryptography: Hashing is essential in securing data (e.g., passwords, digital signatures).
# Cache Management: Hashing is used to store and retrieve cached data efficiently.
# Checksums: Hashing helps in detecting data corruption by generating unique checksums.
# Industry Applications
# Database Indexing: Hashing functions are used to create indexes, speeding up query processing.
# Load Balancing: Hashing distributes tasks among servers in a balanced way.
# Compiler Design: Hashing is used in symbol tables to store variable names and their corresponding values.



# Code Breakdown
# Here's a simple example of a hashing function in Python:


def simple_hash(key, table_size):
    return key % table_size


# Explanation:

# key: The input data that needs to be hashed.
# table_size: The size of the hash table.
# key % table_size: This is the hashing function, which takes the modulus of the key with the table size, ensuring the result is within the bounds of the table.




# 7.5 Collision Handling




# Introduction
# Collisions occur when two keys hash to the same index in a hash table. Collision handling is crucial to ensure that the hash table continues to function correctly and efficiently.

# Methods of Collision Handling

# Chaining: Each index in the hash table points to a linked list of entries that hash to the same index.

# Open Addressing: All elements are stored in the hash table itself, and if a collision occurs, the algorithm searches for the next free slot (e.g., linear probing, quadratic probing).

# Double Hashing: A secondary hashing function is used to determine the step size when a collision occurs.


# Real-Life Usage
# Databases: Effective collision handling ensures efficient data retrieval.
# Caches: Handling collisions well improves cache hit rates.
# Industry Applications
# Compiler Design: Symbol tables use collision handling to store multiple identifiers.
# Networking: Routing tables in routers use collision handling to manage multiple entries.




# 7.6 Chaining



# Introduction
# Chaining is a collision resolution method where each slot in the hash table contains a linked list. When a collision occurs, the new element is added to the linked list at the corresponding index.

# Real-Life Usage
# Load Balancing: Chaining can be used to manage requests that hash to the same server.
# Cache Management: Handling multiple items that map to the same cache line.
# Industry Applications
# Database Management: Chaining helps in managing indexes that might have multiple entries for the same key.
# Memory Management: In systems with hash-based memory allocation, chaining helps resolve conflicts when different requests hash to the same memory block.



# Code Breakdown
# Here's an example of how chaining can be implemented in Python:


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    

# Explanation:

# __init__: Initializes the hash table with a given size, creating an empty list for each index.
# hash_function: Maps the key to an index based on the size of the table.
# insert: Inserts a key-value pair into the hash table. If a collision occurs, the pair is added to the list at the corresponding index.
# search: Searches for a value by its key. It traverses the list at the computed index to find the key.






# 7.8 Open Addressing





# Introduction
# Open Addressing is a collision resolution technique used in hash tables. Unlike chaining, which stores all elements that hash to the same index in a linked list, open addressing stores all elements directly in the hash table itself. When a collision occurs, the algorithm searches for the next available slot based on a defined probing sequence.

# Types of Probing

# Linear Probing: The simplest form of open addressing, where the table is searched sequentially from the point of collision.

# Quadratic Probing: Instead of searching sequentially, the algorithm jumps by a quadratic amount to find the next available slot.

# Double Hashing: Uses a secondary hash function to calculate the step size, avoiding primary clustering.


# Real-Life Usage
# Caching: Open addressing is often used in cache systems where quick access is necessary, and the memory footprint should be minimal.
# Memory Allocation: In systems with fixed memory size, open addressing can efficiently manage memory allocation without needing additional data structures like linked lists.
# Industry Applications
# Networking: Hash tables using open addressing can efficiently store and retrieve routing information in routers.
# Databases: When building hash indexes in databases, open addressing can be used to minimize memory usage while maintaining fast access times.
# Code Breakdown
# Here's an example of open addressing using linear probing in Python:


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:  # Table is full
                raise Exception("Hash Table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                return None  # Key not found
        return None
    


# Explanation:

# __init__: Initializes the hash table with a given size, creating an array of None values.
# hash_function: Maps the key to an index within the bounds of the table.
# insert: Inserts a key-value pair into the hash table. If a collision occurs, the algorithm searches for the next available slot using linear probing.
# index = (index + 1) % self.size: This line implements linear probing, ensuring the index wraps around if it exceeds the table size.
# if index == original_index: This condition checks if the entire table has been searched, indicating the table is full.
# search: Searches for a value by its key. It probes through the table starting from the computed index and returns the value if found.





# 7.9 Double Hashing





# Introduction
# Double Hashing is an advanced form of open addressing that uses two hash functions to resolve collisions. When a collision occurs, the second hash function is used to calculate the step size (or interval) between probes, reducing the chances of clustering (where multiple keys compete for the same set of slots).

# Real-Life Usage
# Cryptography: Double hashing is used in password hashing schemes to add an extra layer of security.
# Network Protocols: Hash functions in network protocols (e.g., DHCP) may use double hashing to ensure even distribution and minimize collisions.
# Industry Applications
# Distributed Systems: Double hashing helps in load balancing by evenly distributing tasks across nodes in distributed systems.
# Database Indexing: Double hashing is employed in hash-based indexing systems to improve performance and reduce clustering.
# Code Breakdown
# Here’s how double hashing can be implemented in Python:


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def primary_hash(self, key):
        return key % self.size

    def secondary_hash(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key, value):
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        original_index = index

        while self.table[index] is not None:
            index = (index + step_size) % self.size
            if index == original_index:
                raise Exception("Hash Table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step_size) % self.size
            if index == original_index:
                return None  # Key not found
        return None
    


# Explanation:

# __init__: Initializes the hash table with a fixed size.
# primary_hash: The first hash function, similar to the one used in open addressing.
# secondary_hash: The second hash function, which determines the step size for probing.
# return 1 + (key % (self.size - 1)): This ensures the step size is not zero and is within the table bounds.
# insert: Similar to open addressing, but with double hashing. It calculates both the primary index and the step size. If a collision occurs, the algorithm uses the step size from the secondary hash function to find the next available slot.
# search: Searches for a value using double hashing. It starts from the primary index and moves by the step size until it finds the key or determines the key is not in the table.



# Benefits of Double Hashing:

# Reduces Clustering: By using a second hash function, double hashing distributes keys more evenly, reducing the chance of clustering.
# Efficient: Double hashing maintains efficient insertion and search operations even with high load factors.






# 7.11 Chaining vs Open Addressing






# Introduction
# Chaining and Open Addressing are two fundamental techniques used to handle collisions in hash tables.

# Chaining: When a collision occurs, all elements that hash to the same index are stored in a linked list or another collection at that index.
# Open Addressing: All elements are stored within the hash table itself. When a collision occurs, the algorithm searches for the next available slot using a probing technique.

# Real-Life Usage
# Chaining: Ideal for applications where the number of collisions is expected to be high, as it can handle large clusters of collisions efficiently.

# Databases: Hash-based indexing in databases often uses chaining, as it can handle high load factors and provide fast access times.
# Memory-Constrained Systems: Systems with abundant memory may prefer chaining, as it avoids the complexity of probing sequences and allows easy handling of collisions.

# Open Addressing: Useful when memory is limited, and you want to avoid the overhead of linked lists or other collections.

# Caches: Open addressing is often used in caches, where the hash table needs to be compact and efficient, and the load factor is typically kept low.
# Embedded Systems: Open addressing is common in embedded systems where memory is scarce, and a compact data structure is preferred.







# 7.12 Set in Python





# Introduction
# A set in Python is an unordered collection of unique elements. It is implemented using a hash table, which allows for fast membership tests, insertion, and deletion.


# Real-Life Usage


# Deduplication: Sets are commonly used to remove duplicates from a list of items.
# Membership Testing: Sets are ideal for checking whether an element exists in a collection, such as checking for banned users in an application.
# Operations on Collections: Sets support operations like union, intersection, and difference, making them useful in scenarios like managing user permissions across different groups.
# Industry Applications
# Data Analysis: Sets are used in data processing pipelines to ensure uniqueness, like when processing large datasets to remove duplicate entries.
# Security: Used in access control systems to manage and verify user permissions.



# Code Breakdown
# Here's a simple example of using a set in Python:


# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(3)

# Checking membership
if 4 in my_set:
    print("4 is in the set")

# Union of two sets
another_set = {5, 6, 7}
union_set = my_set.union(another_set)

# Intersection of two sets
intersection_set = my_set.intersection(another_set)


# Explanation:

# my_set = {1, 2, 3, 4, 5}: Initializes a set with unique elements.
# add(6): Adds an element to the set.
# remove(3): Removes an element from the set. If the element doesn’t exist, it raises a KeyError.
# 4 in my_set: Checks if 4 is a member of the set, returning True or False.
# union_set = my_set.union(another_set): Combines two sets, returning a new set with all unique elements.
# intersection_set = my_set.intersection(another_set): Returns a new set with elements common to both sets.





# 7.13 Dictionary in Python





# Introduction
# A dictionary in Python is an unordered collection of key-value pairs, where keys are unique. It's implemented using a hash table, making lookups, insertions, and deletions very fast.

# Real-Life Usage
# Configuration Settings: Dictionaries are often used to store configuration settings where quick access to values by their names (keys) is needed.
# Caching: In web applications, dictionaries can be used to cache data, where the key might be a URL and the value the HTML content.
# Data Mapping: Used for mapping identifiers to objects, such as mapping user IDs to user information in a web application.


# Industry Applications
# Web Development: Dictionaries are extensively used in frameworks like Django or Flask to manage settings, route mappings, and more.
# Data Processing: In data processing pipelines, dictionaries can map data from one format to another or store intermediate results.
# Code Breakdown
# Here’s an example of using a dictionary in Python:


# Creating a dictionary
user_info = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com'
}

# Accessing a value
print(user_info['name'])

# Adding a new key-value pair
user_info['location'] = 'New York'

# Removing a key-value pair
del user_info['age']

# Checking if a key exists
if 'email' in user_info:
    print("Email is present")

# Iterating through the dictionary
for key, value in user_info.items():
    print(f"{key}: {value}")



# Explanation:

# user_info = { ... }: Creates a dictionary with initial key-value pairs.
# user_info['name']: Accesses the value associated with the key 'name'.
# user_info['location'] = 'New York': Adds a new key-value pair to the dictionary.
# del user_info['age']: Deletes the key 'age' and its associated value from the dictionary.
# 'email' in user_info: Checks if the key 'email' exists in the dictionary.
# for key, value in user_info.items(): Iterates through all key-value pairs in the dictionary, allowing you to process or print each one.


# Advantages:

# Efficiency: Fast lookups and modifications due to the underlying hash table.
# Flexibility: Keys can be any immutable type, making dictionaries very versatile.
# Limitations:

# Memory Usage: Since dictionaries are implemented as hash tables, they may consume more memory compared to other data structures like lists or tuples.


