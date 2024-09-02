

# 8.1 Strings in Python




# Strings in Python are sequences of characters enclosed in quotes (single, double, or triple). They are immutable, meaning once created, they cannot be changed. Strings are widely used in various applications, from data processing to web development, because they handle textual data.

# Real-Life and Industry Usage
# Web Development: Strings are used for rendering HTML, handling URLs, and managing form data.
# Data Processing: Parsing and manipulating textual data in logs, files, or user inputs.
# Automation: Automating repetitive tasks often involves string manipulations, like renaming files or formatting text.


# Example Code with Line-by-Line Breakdown


# # Defining a string
name = "John Doe"  # Creates a string variable 'name' with the value "John Doe"

# # Accessing characters
first_letter = name[0]  # Accesses the first character 'J' from the string

# # Slicing strings
surname = name[5:]  # Slices the string to get "Doe" starting from index 5 to the end

# # String length
length = len(name)  # Calculates the length of the string, which is 8 in this case

# # String concatenation
full_name = name + " Jr."  # Concatenates " Jr." to the original string, resulting in "John Doe Jr."

# # Checking substrings
has_doe = "Doe" in name  # Checks if the substring "Doe" exists in the string, returns True

# # String repetition
repeat_name = name * 2  # Repeats the string twice, resulting in "John DoeJohn Doe"


# # Changing case
upper_name = name.upper()  # Converts the string to uppercase, resulting in "JOHN DOE"



# 8.2 Escape Sequences and Raw Strings




# Escape sequences in strings allow you to include special characters like newline (\n), tab (\t), or quotes (\") within strings. Raw strings (r"text") treat backslashes as literal characters, making them useful for regular expressions or file paths.

# Real-Life and Industry Usage

# File Paths: Windows paths use backslashes, making raw strings convenient to avoid escape confusion.
# Regex Patterns: Writing complex regex patterns often involves backslashes, making raw strings easier to manage.
# Formatting Output: Escape sequences help format outputs neatly in console applications.


# Example Code with Line-by-Line Breakdown


# # Using escape sequences
newline_example = "Hello\nWorld"  # Includes a newline, printing "Hello" and "World" on separate lines

quote_example = "She said, \"Hello!\""  # Includes double quotes within the string

# # Using raw strings
file_path = r"C:\Users\John\Documents"  # Treats backslashes as literal characters, no need to escape

# # Special characters
tab_example = "Column1\tColumn2"  # Includes a tab space between "Column1" and "Column2"





# 8.3 Formatted Strings in Python





# Formatted strings allow you to include variables or expressions directly within strings. Python offers several ways to format strings: using the % operator, str.format(), and f-strings (formatted string literals introduced in Python 3.6).

# Real-Life and Industry Usage


# Logging and Debugging: Formatted strings help generate detailed log messages or debug outputs.
# User Interfaces: Dynamically display data in applications, like showing user names, scores, or messages.
# Reports and Documentation: Automated generation of formatted reports or documents with data inclusion.



# Example Code with Line-by-Line Breakdown


# Old style with %
name = "John"
age = 30
formatted_str_percent = "Name: %s, Age: %d" % (name, age)  # Uses % formatting to insert 'name' and 'age'

# # Using str.format()
formatted_str_format = "Name: {}, Age: {}".format(name, age)  # Uses str.format() for the same result

# # Using f-strings (Python 3.6+)
formatted_str_f = f"Name: {name}, Age: {age}"  # Directly inserts variables using f-strings

# # Expression in f-strings
calculation = f"Five years later, age will be {age + 5}"  # Performs the calculation inside the f-string

# # Formatting numbers
pi = 3.14159265
formatted_pi = f"Pi rounded to two decimal places: {pi:.2f}"  # Rounds 'pi' to two decimal places



# 8.4 String Comparison in Python



# String comparison in Python is used to determine if two strings are equal, or if one is greater or lesser than the other. Python allows comparing strings using operators like ==, !=, <, >, <=, and >=. Comparisons are based on the lexicographical order, similar to dictionary order, and are case-sensitive by default.

# Real-Life and Industry Usage
# Authentication: Checking if user-entered passwords match the stored passwords.
# Sorting and Ordering: Sorting names, titles, or other text data alphabetically.
# Filtering: Comparing user input against a list of options or restricted words.
# Example Code with Line-by-Line Breakdown


# Simple equality check
string1 = "apple"
string2 = "orange"

is_equal = string1 == string2  # Compares if 'string1' is equal to 'string2', returns False

# Lexicographical comparison
is_less = string1 < string2  # Compares lexicographically, 'apple' comes before 'orange', returns True

# Case-sensitive comparison
string3 = "Apple"
is_equal_case = string1 == string3  # Compares 'apple' with 'Apple', returns False because comparison is case-sensitive

# Case-insensitive comparison
is_equal_ignore_case = string1.lower() == string3.lower()  # Converts both strings to lowercase before comparing, returns True

# Greater than or equal comparison
is_greater_equal = string2 >= string1  # Checks if 'orange' is greater than or equal to 'apple', returns True



# 8.5 String Operations Part (1)



# String operations include a wide range of methods for manipulating strings, such as concatenation, slicing, and modifying strings through built-in functions like upper(), lower(), replace(), and split(). These operations are fundamental in text processing tasks.

# Real-Life and Industry Usage

# Data Cleaning: Removing unwanted characters or whitespace in data preprocessing.
# Text Transformation: Converting text to lowercase or uppercase for consistency.
# Dynamic String Generation: Creating custom messages, emails, or templates by manipulating string content.


# Example Code with Line-by-Line Breakdown


# Concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"  # Concatenates strings with a comma and exclamation, resulting in "Hello, Alice!"

# Slicing
substring = message[7:12]  # Slices the string from index 7 to 11, resulting in "Alice"

# Converting to upper case
upper_message = message.upper()  # Converts the entire string to uppercase, resulting in "HELLO, ALICE!"

# Replacing substrings
replaced_message = message.replace("Alice", "Bob")  # Replaces "Alice" with "Bob" in the string, resulting in "Hello, Bob!"

# Splitting strings
words = message.split()  # Splits the string into a list of words based on whitespace, resulting in ['Hello,', 'Alice!']



# 8.6 String Operations Part (2)




# This part delves into more advanced string operations, including joining lists into strings, formatting strings, trimming whitespace, and using string methods like find(), index(), startswith(), and endswith().

# Real-Life and Industry Usage

# Log Parsing: Extracting specific patterns or segments from log files.
# Input Validation: Checking if inputs conform to expected formats (e.g., email addresses).
# User Interface: Displaying and formatting strings based on conditions in user interfaces.


# Example Code with Line-by-Line Breakdown

# Joining a list of strings into one string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)  # Joins the list into a single string with spaces, resulting in "Python is awesome"

# Trimming whitespace
whitespace_str = "   Hello, World!   "
trimmed_str = whitespace_str.strip()  # Removes leading and trailing whitespace, resulting in "Hello, World!"

# Finding substrings
position = sentence.find("is")  # Finds the position of "is" in the string, returns 7

# Checking if string starts with a substring
starts_with = sentence.startswith("Python")  # Checks if the string starts with "Python", returns True

# Checking if string ends with a substring
ends_with = sentence.endswith("awesome")  # Checks if the string ends with "awesome", returns True

# Index of substring (throws error if not found)
index = sentence.index("is")  # Finds the position of "is" in the string, raises an error if not found, returns 7



# 8.7 Reverse a String in Python




# Reversing a string means rearranging its characters in the opposite order. This operation is straightforward in Python due to its powerful slicing capabilities.

# Real-Life and Industry Usage
# Text Processing: Reversing text for formatting purposes or encryption.
# Algorithms: In certain algorithms, reversing strings can be a step in data manipulation or transformation.
# Palindrome Check: Reversing a string is a common step in checking if a string is a palindrome.
# Example Code with Line-by-Line Breakdown

# Using slicing to reverse a string
original = "Hello, World!"
reversed_str = original[::-1]  # Slices the string from end to start, reversing it, resulting in "!dlroW ,olleH"

# Using a loop to reverse a string
reversed_str_loop = ""
for char in original:
    reversed_str_loop = char + reversed_str_loop  # Prepends each character to the start of the new string

# Using the reversed() function and join()
reversed_str_func = ''.join(reversed(original))  # Reverses the iterable returned by reversed(), then joins into a string




# 8.8 Check if String is Rotated




# Checking if one string is a rotation of another involves determining if one string can be shifted circularly to become the other. This can be efficiently solved by concatenating one string with itself and checking if the other string is a substring.

# Real-Life and Industry Usage
# Data Rotation: Used in circular data structures or cyclic algorithms where the sequence order matters.
# Textual Comparisons: Comparing rotated versions of strings in cyclic shifts, like clock sequences or periodic data.
# Example Code with Line-by-Line Breakdown

def is_rotated(s1, s2):
    # First, check if lengths match; if not, they cannot be rotations
    if len(s1) != len(s2):
        return False
    
    # Concatenate s1 with itself
    temp = s1 + s1  # Creates a string twice the length of s1
    
    # Check if s2 is a substring of this concatenated string
    result = s2 in temp  # Uses 'in' operator to check if s2 is within the concatenated string
    return result

# Example usage
s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotated(s1, s2))  # Returns True, because s2 is a rotation of s1




# 8.9 Check for Palindrome in Python





# A palindrome is a string that reads the same backward as forward. Checking for palindromes is commonly used in text validation and formatting tasks.

# Real-Life and Industry Usage
# Data Validation: Ensuring specific text fields conform to palindrome criteria.
# Genetics: Palindromic sequences are significant in DNA strand studies.
# Cryptography: Palindromes can be part of cryptographic functions or checks.
# Example Code with Line-by-Line Breakdown

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase for uniformity
    cleaned = ''.join(char.lower() for char in s if char.isalnum())  # Removes punctuation and spaces
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]  # Uses slicing to compare the string with its reverse

# Example usage
string = "A man, a plan, a canal: Panama"
print(is_palindrome(string))  # Returns True, as it is a palindrome after cleaning




# 8.10 Check if a String is a Subsequence of Another




# A subsequence of a string is a sequence derived by deleting some or no characters without changing the order of the remaining characters. Checking for subsequences is important in dynamic programming and sequence matching problems.

# Real-Life and Industry Usage
# Search Algorithms: Checking if user input matches a pattern within data (like in autocomplete systems).
# Bioinformatics: Comparing genetic sequences to identify similarities or subsequences.
# Text Editing: Validating input sequences in text editors or coding environments.

# Example Code with Line-by-Line Breakdown

def is_subsequence(s1, s2):
    # Initialize pointers for both strings
    i, j = 0, 0
    
    # Loop until we reach the end of either string
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:  # If characters match, move the pointer for s1
            i += 1
        j += 1  # Always move the pointer for s2
    
    # Check if we've traversed all of s1
    return i == len(s1)

# Example usage
s1 = "abc"
s2 = "ahbgdc"
print(is_subsequence(s1, s2))  # Returns True, as "abc" is a subsequence of "ahbgdc"




# 8.11 Check for Anagram in Python




# An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once. Checking for anagrams involves determining if two strings contain the exact same characters with the same frequency.

# Real-Life and Industry Usage
# Text Analysis: Anagram checks can be used in text-based games, puzzles, or cryptography.
# DNA Sequence Analysis: Identifying genetic sequences that match in composition.
# Plagiarism Detection: Anagram checks can help in finding rearranged content.
# Example Code with Line-by-Line Breakdown


def is_anagram(s1, s2):
    # Convert both strings to lowercase and remove spaces
    s1 = s1.replace(" ", "").lower()  # Cleans and standardizes s1
    s2 = s2.replace(" ", "").lower()  # Cleans and standardizes s2
    
    # Compare sorted versions of the strings
    return sorted(s1) == sorted(s2)  # Sorting both strings and comparing lists of characters

# Example usage
s1 = "Listen"
s2 = "Silent"
print(is_anagram(s1, s2))  # Returns True because "Listen" and "Silent" are anagrams




# Efficient Anagram Check Using a Dictionary


def is_anagram_efficient(s1, s2):
    if len(s1) != len(s2):
        return False

    # Create a frequency dictionary for s1
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1  # Counts occurrences of each character in s1
    
    # Decrease the frequency for characters in s2
    for char in s2:
        if char in count:
            count[char] -= 1  # Decrease count for matching characters
            if count[char] == 0:
                del count[char]  # Remove key if count is zero
        else:
            return False  # If a character in s2 is not in s1
    
    return len(count) == 0  # True if all counts are zero

print(is_anagram_efficient(s1, s2))  # Also returns True





# 8.12 Leftmost Repeating Character





# Finding the leftmost repeating character means identifying the first character in a string that repeats. This operation helps in various applications, such as data validation, text parsing, and debugging code.

# Real-Life and Industry Usage
# Data Parsing: Helps in identifying repeated or redundant elements.
# Input Validation: Detects repeated entries or characters in user inputs.
# Example Code with Line-by-Line Breakdown


def leftmost_repeating_char(s):
    # Create a dictionary to store the first occurrence of each character
    count = {}
    for i, char in enumerate(s):
        if char in count:
            return char  # Return the character if it's found again
        else:
            count[char] = i  # Store the index of the first occurrence

    return None  # Return None if no repeating character is found

# Example usage
s = "geeksforgeeks"
print(leftmost_repeating_char(s))  # Returns 'g' as it is the first repeating character




# 8.13 Leftmost Non-Repeating Element




# Finding the leftmost non-repeating element involves identifying the first character in a string that appears only once. This is useful in character recognition, data cleaning, and optimizing searches.

# Real-Life and Industry Usage
# Text Processing: Filtering unique identifiers or attributes.
# Optimizing Search Algorithms: Helps in quickly identifying distinct elements.
# Example Code with Line-by-Line Breakdown


def leftmost_non_repeating_char(s):
    # Create a dictionary to store frequency of each character
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1  # Increment frequency of each character

    # Check for the first character with frequency 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return char  # Return the first non-repeating character

    return None  # Return None if no non-repeating character is found

# Example usage
s = "geeksforgeeks"
print(leftmost_non_repeating_char(s))  # Returns 'f', as it is the first non-repeating character




# 8.14 Reverse Words in a String




# Reversing words in a string involves rearranging the order of words while keeping the words themselves unchanged. This operation is common in text formatting and data presentation.

# Real-Life and Industry Usage
# Text Formatting: Reversing sentences or phrases in documents and displays.
# Natural Language Processing: Inverting word order in translation or parsing.
# Example Code with Line-by-Line Breakdown


def reverse_words(s):
    # Split the string by spaces into a list of words
    words = s.split()  # Splits string into a list ['Hello,', 'how', 'are', 'you?']
    
    # Reverse the list of words
    reversed_words = words[::-1]  # Reverses the list order ['you?', 'are', 'how', 'Hello,']
    
    # Join the reversed list back into a string with spaces
    reversed_sentence = ' '.join(reversed_words)  # Joins the list into 'you? are how Hello,'
    
    return reversed_sentence

# Example usage
s = "Hello, how are you?"
print(reverse_words(s))  # Returns "you? are how Hello,"




