# =========================================================
# PYTHON LAMBDA FUNCTIONS
# =========================================================

# ---------------------------------------------------------
# BASIC LAMBDA FUNCTION
# ---------------------------------------------------------
# Anonymous function used for a single expression.

square = lambda num: num ** 2

print(square(4))

# Result:
# 16


# ---------------------------------------------------------
# LAMBDA WITH FILTER()
# ---------------------------------------------------------
# Keep only the elements that satisfy a condition.

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# Result:
# [2, 4]


# ---------------------------------------------------------
# LAMBDA WITH MAP()
# ---------------------------------------------------------
# Apply a transformation to every element.

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)

# Result:
# [1, 4, 9, 16, 25]


# ---------------------------------------------------------
# REGULAR FUNCTION (BETTER WHEN REUSING CODE)
# ---------------------------------------------------------
# Use def instead of assigning a lambda to a variable.

numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))

print(squared_numbers)

# Result:
# [1, 4, 9, 16, 25]


# ---------------------------------------------------------
# AVOID COMPLEX LAMBDAS
# ---------------------------------------------------------
# If the logic becomes difficult to read,
# use a regular function instead.

def calculate_expression(x):
    if x > 0:
        return x ** 2 + 2 * x - 1
    return x ** 3 - x + 4

print(calculate_expression(3))

# Result:
# 14


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# lambda arguments: expression
# Create an anonymous function.

# filter(lambda x: condition, iterable)
# Filter elements.

# map(lambda x: expression, iterable)
# Transform elements.

# def function(...):
# Preferred when the function is reused
# or contains multiple statements.


# =========================================================
# REMEMBER:
# Lambda functions are anonymous functions.
# They are best for short, single-expression operations.
# Commonly used with filter(), map(), and sorted().
# Avoid assigning lambdas to variables.
# Use regular functions (def) for complex or reusable logic.
# =========================================================