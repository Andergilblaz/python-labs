# =========================================================
# PYTHON LISTS (LISTAS)
# =========================================================

# WHAT IS A LIST?
# - Ordered collection of elements.
# - Can store strings, numbers, booleans, or other lists.
# - Mutable (can be modified).
# - Uses zero-based indexing.

cities = ["Los Angeles", "London", "Tokyo"]

# ---------------------------------------------------------
# ACCESSING ELEMENTS
# ---------------------------------------------------------

cities[0]    # First element -> "Los Angeles"
cities[1]    # Second element -> "London"
cities[-1]   # Last element -> "Tokyo"

# ---------------------------------------------------------
# CREATING LISTS WITH list()
# ---------------------------------------------------------

name = "Jessica"

letters = list(name)
# ['J', 'e', 's', 's', 'i', 'c', 'a']

# ---------------------------------------------------------
# GETTING THE LENGTH OF A LIST
# ---------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

len(numbers)  # 5

# ---------------------------------------------------------
# MODIFYING ELEMENTS
# ---------------------------------------------------------

languages = ["Python", "Java", "C++"]

languages[0] = "JavaScript"

# Result:
# ["JavaScript", "Java", "C++"]

# ---------------------------------------------------------
# INDEX ERROR
# ---------------------------------------------------------

# languages[10] = "Rust"
# IndexError: list assignment index out of range

# ---------------------------------------------------------
# REMOVING ELEMENTS
# ---------------------------------------------------------

developer = ["Jane Doe", 23, "Python Developer"]

del developer[1]

# Result:
# ["Jane Doe", "Python Developer"]

# ---------------------------------------------------------
# CHECKING IF AN ELEMENT EXISTS
# ---------------------------------------------------------

languages = ["Python", "Java", "C++", "Rust"]

"Rust" in languages        # True
"JavaScript" in languages  # False

# ---------------------------------------------------------
# NESTED LISTS
# ---------------------------------------------------------

developer = ["Alice", 25, ["Python", "Rust", "C++"]]

developer[2]
# ["Python", "Rust", "C++"]

developer[2][1]
# "Rust"

# ---------------------------------------------------------
# UNPACKING LISTS
# ---------------------------------------------------------

developer = ["Alice", 34, "Rust Developer"]

name, age, job = developer

# name = "Alice"
# age = 34
# job = "Rust Developer"

# ---------------------------------------------------------
# USING * TO COLLECT REMAINING VALUES
# ---------------------------------------------------------

developer = ["Alice", 34, "Rust Developer"]

name, *rest = developer

# name = "Alice"
# rest = [34, "Rust Developer"]

# ---------------------------------------------------------
# UNPACKING ERROR
# ---------------------------------------------------------

# name, age, job, city = developer
# ValueError: not enough values to unpack

# ---------------------------------------------------------
# SLICING
# ---------------------------------------------------------

desserts = ["Cake", "Cookies", "Ice Cream", "Pie", "Brownies"]

desserts[1:4]

# Result:
# ["Cookies", "Ice Cream", "Pie"]

# ---------------------------------------------------------
# SLICING WITH STEP
# ---------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

numbers[1::2]

# Result:
# [2, 4, 6]

# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# Create list:
# my_list = [1, 2, 3]

# First element:
# my_list[0]

# Last element:
# my_list[-1]

# Length:
# len(my_list)

# Modify:
# my_list[0] = 100

# Delete:
# del my_list[0]

# Check existence:
# value in my_list

# Slice:
# my_list[start:end]

# Slice with step:
# my_list[start:end:step]

# Nested list:
# my_list[0][1]

# Unpacking:
# a, b, c = my_list

# Remaining values:
# a, *rest = my_list

# =========================================================
# REMEMBER:
# Lists are ordered, mutable, and zero-indexed.
# =========================================================