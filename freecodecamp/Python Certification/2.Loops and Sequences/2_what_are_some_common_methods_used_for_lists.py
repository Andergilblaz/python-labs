# =========================================================
# COMMON LIST METHODS
# =========================================================

# ---------------------------------------------------------
# APPEND()
# ---------------------------------------------------------
# Adds a single element to the end of the list.

numbers = [1, 2, 3, 4, 5]

numbers.append(6)

print(numbers)

# Result:
# [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------
# APPENDING A LIST
# ---------------------------------------------------------
# The entire list is added as a nested list.

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)

print(numbers)

# Result:
# [1, 2, 3, 4, 5, [6, 8, 10]]

# ---------------------------------------------------------
# EXTEND()
# ---------------------------------------------------------
# Adds all elements from another list individually.

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)

print(numbers)

# Result:
# [1, 2, 3, 4, 5, 6, 8, 10]

# ---------------------------------------------------------
# INSERT()
# ---------------------------------------------------------
# Inserts an element at a specific index.

numbers = [1, 2, 3, 4, 5]

numbers.insert(2, 2.5)

print(numbers)

# Result:
# [1, 2, 2.5, 3, 4, 5]


# ---------------------------------------------------------
# REMOVE ONLY FIRST MATCH
# ---------------------------------------------------------
# remove() does not remove all occurrences.
# Removes the first occurrence of a value.

numbers = [10, 20, 30, 40, 50, 50, 50]

numbers.remove(50)

print(numbers)

# Result:
# [10, 20, 30, 40, 50, 50]

# ---------------------------------------------------------
# POP()
# ---------------------------------------------------------
# Removes and returns an element by index.

numbers = [1, 2, 3, 4, 5]

removed = numbers.pop(1)

print(removed)

# Result:
# 2

print(numbers)

# Result:
# [1, 3, 4, 5]

# ---------------------------------------------------------
# POP LAST ELEMENT
# ---------------------------------------------------------
# If no index is specified, the last element is removed.

numbers = [1, 2, 3, 4, 5]

removed = numbers.pop()

print(removed)

# Result:
# 5

print(numbers)

# Result:
# [1, 2, 3, 4]

# ---------------------------------------------------------
# CLEAR()
# ---------------------------------------------------------
# Removes all elements from the list.

numbers = [1, 2, 3, 4, 5]

numbers.clear()

print(numbers)

# Result:
# []

# ---------------------------------------------------------
# SORT()
# ---------------------------------------------------------
# Sorts the list in place.

numbers = [19, 2, 35, 1, 67, 41]

numbers.sort()

print(numbers)

# Result:
# [1, 2, 19, 35, 41, 67]

# ---------------------------------------------------------
# SORTED()
# ---------------------------------------------------------
# Returns a new sorted list without modifying the original.

numbers = [19, 2, 35, 1, 67, 41]

sorted_numbers = sorted(numbers)

print(numbers)

# Result:
# [19, 2, 35, 1, 67, 41]

print(sorted_numbers)

# Result:
# [1, 2, 19, 35, 41, 67]

# ---------------------------------------------------------
# REVERSE()
# ---------------------------------------------------------
# Reverses the order of elements in place.

numbers = [6, 5, 4, 3, 2, 1]

numbers.reverse()

print(numbers)

# Result:
# [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------
# INDEX()
# ---------------------------------------------------------
# Returns the index of the first matching element.

languages = ["Rust", "Java", "Python", "C++"]

print(languages.index("Java"))

# Result:
# 1

# ---------------------------------------------------------
# INDEX ERROR
# ---------------------------------------------------------
# Raises ValueError if the element is not found.

# languages.index("JavaScript")

# Result:
# ValueError: 'JavaScript' is not in list

# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# append(value)
# Add one element to the end.

# extend(iterable)
# Add multiple elements.

# insert(index, value)
# Insert element at a specific position.

# remove(value)
# Remove first matching value.

# pop(index)
# Remove and return element by index.

# pop()
# Remove and return last element.

# clear()
# Remove all elements.

# sort()
# Sort list in place.

# sorted(iterable)
# Return a new sorted list.

# reverse()
# Reverse list in place.

# index(value)
# Return index of first match.

# =========================================================
# REMEMBER:
# append() adds one item.
# extend() adds multiple items.
# sort() modifies the original list.
# sorted() returns a new list.
# pop() removes and returns an element.
# =========================================================