# =========================================================
# PYTHON LIST COMPREHENSIONS, filter(), map() AND sum()
# =========================================================

# ---------------------------------------------------------
# LIST COMPREHENSION
# ---------------------------------------------------------
# Create a new list in a single line.

even_numbers = [num for num in range(21) if num % 2 == 0]

print(even_numbers)

# Result:
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# ---------------------------------------------------------
# LIST COMPREHENSION WITH IF/ELSE
# ---------------------------------------------------------
# Apply different values depending on a condition.

numbers = [1, 2, 3, 4, 5]

result = [
    (num, "Even") if num % 2 == 0 else (num, "Odd")
    for num in numbers
]

print(result)

# Result:
# [(1, 'Odd'),
#  (2, 'Even'),
#  (3, 'Odd'),
#  (4, 'Even'),
#  (5, 'Odd')]


# ---------------------------------------------------------
# FILTER()
# ---------------------------------------------------------
# Keep only the elements that satisfy a condition.

words = ["tree", "sky", "mountain", "river", "cloud", "sun"]

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))

print(long_words)

# Result:
# ['mountain', 'river', 'cloud']


# ---------------------------------------------------------
# MAP()
# ---------------------------------------------------------
# Apply a function to every element of an iterable.

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))

print(fahrenheit)

# Result:
# [32.0, 50.0, 68.0, 86.0, 104.0]


# ---------------------------------------------------------
# SUM()
# ---------------------------------------------------------
# Calculate the total of all elements.

numbers = [5, 10, 15, 20]

total = sum(numbers)

print(total)

# Result:
# 50


# ---------------------------------------------------------
# SUM() WITH START VALUE
# ---------------------------------------------------------
# Add an initial value before summing.

numbers = [5, 10, 15, 20]

print(sum(numbers, 10))          # Positional argument
print(sum(numbers, start=10))    # Keyword argument

# Result:
# 60
# 60


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# [expression for item in iterable]
# Create a new list.

# [expression for item in iterable if condition]
# Create a filtered list.

# [A if condition else B for item in iterable]
# Conditional expression inside a list comprehension.

# filter(function, iterable)
# Keep only matching elements.

# map(function, iterable)
# Transform every element.

# sum(iterable)
# Sum all values.

# sum(iterable, start)
# Sum values with an initial value.


# =========================================================
# REMEMBER:
# List comprehensions create lists in a concise way.
# filter() selects elements that meet a condition.
# map() transforms every element in an iterable.
# sum() adds all values together.
# filter() and map() return iterators, so use list() if needed.
# =========================================================