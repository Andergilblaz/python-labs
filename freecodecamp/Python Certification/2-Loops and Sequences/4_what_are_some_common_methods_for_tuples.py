# =========================================================
# COMMON TUPLE METHODS
# =========================================================

# ---------------------------------------------------------
# COUNT()
# ---------------------------------------------------------
# Returns the number of times a value appears.

languages = ("Rust", "Java", "Python", "C++", "Rust")

print(languages.count("Rust"))

# Result:
# 2


# ---------------------------------------------------------
# COUNT() NOT FOUND
# ---------------------------------------------------------
# Returns 0 if the value is not present.

languages = ("Rust", "Java", "Python", "C++", "Rust")

print(languages.count("JavaScript"))

# Result:
# 0


# ---------------------------------------------------------
# COUNT() ERROR
# ---------------------------------------------------------
# count() requires exactly one argument.

# languages.count()

# Result:
# TypeError: tuple.count() takes exactly one argument (0 given)


# ---------------------------------------------------------
# INDEX()
# ---------------------------------------------------------
# Returns the index of the first matching value.

languages = ("Rust", "Java", "Python", "C++", "Rust")

print(languages.index("Java"))

# Result:
# 1


# ---------------------------------------------------------
# INDEX() NOT FOUND
# ---------------------------------------------------------
# Raises ValueError if the value does not exist.

# languages.index("JavaScript")

# Result:
# ValueError: tuple.index(x): x not in tuple


# ---------------------------------------------------------
# INDEX() WITH START
# ---------------------------------------------------------
# Start searching from a specific index.

languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")

print(languages.index("Python", 3))

# Result:
# 5


# ---------------------------------------------------------
# INDEX() WITH START AND STOP
# ---------------------------------------------------------
# Search only within a specific range.
# The stop index is NOT included.

languages = (
    "Rust",
    "Java",
    "Python",
    "C++",
    "Rust",
    "Python",
    "JavaScript",
    "Python"
)

print(languages.index("Python", 2, 5))

# Result:
# 2


# ---------------------------------------------------------
# SORTED()
# ---------------------------------------------------------
# Returns a NEW sorted list.
# The original tuple is not modified.

numbers = (13, 2, 78, 3, 45, 67, 18, 7)

sorted_numbers = sorted(numbers)

print(sorted_numbers)

# Result:
# [2, 3, 7, 13, 18, 45, 67, 78]


# ---------------------------------------------------------
# SORTED() WITH KEY
# ---------------------------------------------------------
# Sort values using a custom rule.

languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")

print(sorted(languages, key=len))

# Result:
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']


# ---------------------------------------------------------
# SORTED() WITH REVERSE
# ---------------------------------------------------------
# Sort values in descending order.

languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")

print(sorted(languages, reverse=True))

# Result:
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# tuple.count(value)
# Count occurrences of a value.

# tuple.index(value)
# Return index of first match.

# tuple.index(value, start)
# Search from a specific index.

# tuple.index(value, start, stop)
# Search within a range.

# sorted(tuple)
# Return a new sorted list.

# sorted(tuple, key=function)
# Sort using a custom key.

# sorted(tuple, reverse=True)
# Sort in descending order.

# =========================================================
# REMEMBER:
# Tuples only have two built-in methods:
# - count()
# - index()
#
# sorted() is NOT a tuple method.
# It is a built-in function that works with any iterable.
# It always returns a NEW list.
# =========================================================