# =========================================================
# PYTHON TUPLES
# =========================================================

# ---------------------------------------------------------
# CREATING A TUPLE
# ---------------------------------------------------------
# Tuples store an ordered collection of values.
# They can contain different data types.

developer = ("Alice", 34, "Rust Developer")

print(developer)

# Result:
# ('Alice', 34, 'Rust Developer')


# ---------------------------------------------------------
# IMMUTABLE
# ---------------------------------------------------------
# Tuples cannot be modified after creation.

languages = ("Python", "Java", "C++", "Rust")

# languages[0] = "JavaScript"

# Result:
# TypeError: 'tuple' object does not support item assignment


# ---------------------------------------------------------
# ACCESSING ELEMENTS
# ---------------------------------------------------------
# Access elements using their index.

developer = ("Alice", 34, "Rust Developer")

print(developer[1])

# Result:
# 34


# ---------------------------------------------------------
# NEGATIVE INDEXING
# ---------------------------------------------------------
# Negative indexes count from the end.

numbers = (1, 2, 3, 4, 5)

print(numbers[-2])

# Result:
# 4


# ---------------------------------------------------------
# INDEX ERROR
# ---------------------------------------------------------
# Accessing an invalid index raises IndexError.

numbers = (1, 2, 3, 4, 5)

# print(numbers[7])

# Result:
# IndexError: tuple index out of range


# ---------------------------------------------------------
# tuple() CONSTRUCTOR
# ---------------------------------------------------------
# Creates a tuple from any iterable.

name = "Jessica"

letters = tuple(name)

print(letters)

# Result:
# ('J', 'e', 's', 's', 'i', 'c', 'a')


# ---------------------------------------------------------
# MEMBERSHIP TEST
# ---------------------------------------------------------
# Use "in" to check if an element exists.

languages = ("Python", "Java", "C++", "Rust")

print("Rust" in languages)

# Result:
# True

print("JavaScript" in languages)

# Result:
# False


# ---------------------------------------------------------
# TUPLE UNPACKING
# ---------------------------------------------------------
# Assign tuple elements to variables.

developer = ("Alice", 34, "Rust Developer")

name, age, job = developer

print(name)
print(age)
print(job)

# Result:
# Alice
# 34
# Rust Developer


# ---------------------------------------------------------
# UNPACKING WITH *
# ---------------------------------------------------------
# Collect remaining elements into a list.

developer = ("Alice", 34, "Rust Developer")

name, *rest = developer

print(name)
print(rest)

# Result:
# Alice
# [34, 'Rust Developer']


# ---------------------------------------------------------
# SLICING
# ---------------------------------------------------------
# Extract part of a tuple.

desserts = ("cake", "pie", "cookies", "ice cream")

print(desserts[1:3])

# Result:
# ('pie', 'cookies')


# ---------------------------------------------------------
# DELETING ELEMENTS
# ---------------------------------------------------------
# Individual elements cannot be removed.

developer = ("Jane Doe", 23, "Python Developer")

# del developer[1]

# Result:
# TypeError: 'tuple' object doesn't support item deletion


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# (value1, value2, ...)
# Create a tuple.

# tuple(iterable)
# Create a tuple from an iterable.

# tuple[index]
# Access an element.

# tuple[-1]
# Access from the end.

# value in tuple
# Check if an element exists.

# a, b, c = tuple
# Unpack tuple values.

# a, *rest = tuple
# Collect remaining elements into a list.

# tuple[start:end]
# Slice a tuple.

# =========================================================
# REMEMBER:
# Tuples are ordered and immutable.
# They can store mixed data types.
# They support indexing, slicing and unpacking.
# Use tuples when data should not change.
# =========================================================