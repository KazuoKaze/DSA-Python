


# Trie Data Structure: In-Depth Explanation



# What is a Trie?


# A Trie (pronounced "try") is a tree-like data structure that is used to store a dynamic set or associative array where the keys are usually strings. Unlike a binary search tree, where nodes represent a single value, each node in a Trie represents a part of a key (like a single character in a string).




# Structure of a Trie


# Root Node: The root node doesn't contain any character but serves as the starting point of the Trie.
# Children: Each node in the Trie can have multiple children, each representing a different character.
# Leaf Nodes: These nodes signify the end of a key (or word).
# Each path down the tree may represent a word or part of a word, making it highly efficient for prefix-based searches.



# Real-Life Usage
# Auto-Complete/Search Suggestions: When typing in a search bar, the application suggests words or phrases that match the prefix you have typed so far. Tries can quickly find all words with a common prefix.
# Spell Checking: Tries can be used to store a dictionary of words and efficiently check if a word exists or find possible corrections.
# IP Routing: In networking, Tries can store IP addresses to make routing decisions based on the longest prefix match.
# Word Games: Used in games like Scrabble or Boggle to quickly find valid words.




# Industry Applications
# Search Engines: To provide real-time suggestions and efficient searches.
# Text Editors: For implementing spell checkers and auto-correct features.
# Routers: In computer networks, for efficient IP address lookup.
# Natural Language Processing (NLP): For efficient storage and retrieval of word sequences.




# Trie Implementation in Python:



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _delete(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0
            return False
        
        _delete(self.root, word, 0)


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: False
trie.insert("app")
print(trie.search("app"))    # Output: True
trie.delete("app")
print(trie.search("app"))    # Output: False








# Trie Implementation in Python: Code Breakdown





# Let's break down the implementation of a Trie data structure.



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# TrieNode class: Represents each node in the Trie.
# self.children: A dictionary to store children nodes where each key is a character, and the value is another TrieNode.
# self.is_end_of_word: A boolean flag indicating if the node represents the end of a valid word.


class Trie:
    def __init__(self):
        self.root = TrieNode()


# Trie class: Encapsulates the entire Trie structure.
# self.root: Initializes the root of the Trie, which is an instance of TrieNode.


def insert(self, word):
    current = self.root
    for char in word:
        if char not in current.children:
            current.children[char] = TrieNode()
        current = current.children[char]
    current.is_end_of_word = True


# insert(self, word) method: Adds a word to the Trie.
# current = self.root: Start from the root node.
# for char in word:: Iterate over each character in the word.
# if char not in current.children:: If the character is not in the current node's children, add it as a new TrieNode.
# current = current.children[char]: Move to the child node associated with the character.
# current.is_end_of_word = True: After all characters are added, mark the last node as the end of the word.


def search(self, word):
    current = self.root
    for char in word:
        if char not in current.children:
            return False
        current = current.children[char]
    return current.is_end_of_word


# search(self, word) method: Checks if a word exists in the Trie.
# current = self.root: Start from the root node.
# for char in word:: Iterate over each character in the word.
# if char not in current.children:: If the character is not found, the word does not exist in the Trie.
# current = current.children[char]: Move to the child node associated with the character.
# return current.is_end_of_word: Return True if the current node marks the end of a word, otherwise False.


def starts_with(self, prefix):
    current = self.root
    for char in prefix:
        if char not in current.children:
            return False
        current = current.children[char]
    return True


# starts_with(self, prefix) method: Checks if there is any word in the Trie that starts with the given prefix.
# current = self.root: Start from the root node.
# for char in prefix:: Iterate over each character in the prefix.
# if char not in current.children:: If the character is not found, no word with that prefix exists.
# current = current.children[char]: Move to the child node associated with the character.
# return True: If all characters are found, return True indicating the prefix exists.



# Example Usage


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.starts_with("app"))  # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True

# Inserting words: We insert "apple" and "app" into the Trie.
# Searching: We search for "apple" (returns True because it exists), "app" (returns False because it doesn't exist as a complete word initially).
# Prefix check: starts_with("app") returns True because "app" is a valid prefix of "apple".
# Inserting and searching again: After inserting "app", searching for "app" returns True.






# Revised Visualization and Explanation




# 1. Initial Trie Structure
# Let's assume our Trie contains the following words:

# "cat"
# "car"
# "cart"
# "dog"
# The Trie structure looks like this:



#        (root)
#         /   \
#       c      d
#      / \      \
#     a   a      o
#    /     \      \
#   t       r      g
#            \
#             t



# Now, we want to delete the word "car".

# Step-by-Step Explanation


# 2. Traversing Through the Trie



# Function Call: self._delete(self.root, "car", 0)
# Start at the root and move through 'c', 'a', and 'r' nodes.



# 3. Reaching the Last Character ('r')



# Check if End of Word: Once we reach the 'r' node:


# if index == len(word):
#     if not root_node.is_end_of_word:
#         return False
#     root_node.is_end_of_word = False
#     return len(root_node.children) == 0


# Visual: At the 'r' node:
# The is_end_of_word flag is set to True because 'r' marks the end of "car".
# After deleting "car", we set is_end_of_word = False for the 'r' node.



#   r  # is_end_of_word = False  
#    \
#     t  # (child from "cart")


# Explanation:
# We don't delete 'r' because it has a child node 't' (from "cart"). The is_end_of_word flag is removed, but the node remains because it's still part of "cart".



# 4. Backtracking After Unmarking 'r'



# Function Backtracks:
# The function checks if 'r' can be deleted, which it cannot, because it still has a child ('t').
# The function continues backtracking to 'a', but does nothing further since 'r' wasn't deleted.



# 5. Final Trie Structure
# After deleting "car", the Trie now looks like this:


#        (root)
#         /   \
#       c      d
#      / \      \
#     a   a      o
#    /     \      \
#   t       r      g
#            \
#             t



# Explanation:
# The 'r' node is no longer the end of "car", but it still exists because it's part of "cart". The Trie is correctly adjusted, and "car" is no longer considered a valid word, but the structure is maintained for "cart".


# Conclusion
# In summary:

# Unmarking the End of Word: The node 'r' is unmarked as the end of the word "car".
# Not Deleting 'r': 'r' isn't deleted because it still has a child 't' (which is part of the word "cart").
# Trie Integrity: The Trie structure remains intact, allowing "cat" and "cart" to remain in the Trie while "car" is successfully removed.


