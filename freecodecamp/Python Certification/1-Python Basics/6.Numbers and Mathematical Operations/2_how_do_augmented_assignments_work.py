# =========================================================
# AUGMENTED ASSIGNMENTS IN PYTHON
# =========================================================

# ---------------------------------------------------------
# WHAT IS AN AUGMENTED ASSIGNMENT?
# ---------------------------------------------------------
# Augmented assignment combines:
# 1. An operation
# 2. An assignment
#
# Into a single line of code.

# Basic syntax:
# variable <operator>= value

# Equivalent to:
# variable = variable <operator> value

# ---------------------------------------------------------
# ADDITION ASSIGNMENT (+=)
# ---------------------------------------------------------

my_var = 10

# Add 5 to my_var
my_var += 5 

print(my_var)

# Result:
# 15

# Equivalent to:
# my_var = my_var + 5

# ---------------------------------------------------------
# SUBTRACTION ASSIGNMENT (-=)
# ---------------------------------------------------------

count = 14

# Subtract 3 from count
count -= 3

print(count)

# Result:
# 11

# ---------------------------------------------------------
# MULTIPLICATION ASSIGNMENT (*=)
# ---------------------------------------------------------

product = 5

# Multiply product by 4
product *= 4

print(product)

# Result:
# 20

# ---------------------------------------------------------
# DIVISION ASSIGNMENT (/=)
# ---------------------------------------------------------

price = 100

# Divide price by 4
price /= 4

print(price)

# Result:
# 25.0

# ---------------------------------------------------------
# FLOOR DIVISION ASSIGNMENT (//=)
# ---------------------------------------------------------

pages = 23

# Floor divide pages by 5
pages //= 5

print(pages)

# Result:
# 4

# ---------------------------------------------------------
# MODULO ASSIGNMENT (%=)
# ---------------------------------------------------------

bits = 35

# Store the remainder of division
bits %= 2

print(bits)

# Result:
# 1

# ---------------------------------------------------------
# EXPONENTIATION ASSIGNMENT (**=)
# ---------------------------------------------------------

power = 2

# Raise power to exponent 3
power **= 3

print(power)

# Result:
# 8

# ---------------------------------------------------------
# STRING CONCATENATION WITH +=
# ---------------------------------------------------------

greet = 'Hello'

# Concatenate strings
greet += ' World'

print(greet)

# Result:
# Hello World

# ---------------------------------------------------------
# STRING REPETITION WITH *=
# ---------------------------------------------------------

greet = 'Hello'

# Repeat string 3 times
greet *= 3

print(greet)

# Result:
# HelloHelloHello

# ---------------------------------------------------------
# INVALID STRING OPERATIONS
# ---------------------------------------------------------
# Some augmented assignments do not work with strings.

# greet = 'Hello'
# greet -= ' World'

# Result:
# TypeError

# ---------------------------------------------------------
# INCREMENT AND DECREMENT
# ---------------------------------------------------------
# Python does NOT support:
# x++
# x--

# Use += or -= instead.

my_var = 5

my_var += 1

print(my_var)

# Result:
# 6

# ---------------------------------------------------------
# IMPORTANT NOTE ABOUT ++
# ---------------------------------------------------------
# ++ does NOT increment values in Python.
# It only applies the unary plus operator multiple times.

my_var = 5

print(+my_var)
print(++my_var)
print(+++my_var)

# Result:
# 5
# 5
# 5

# ---------------------------------------------------------
# IMPORTANT SUMMARY
# =========================================================
#
# +=   -> Addition assignment
# -=   -> Subtraction assignment
# *=   -> Multiplication assignment
# /=   -> Division assignment
# //=  -> Floor division assignment
# %=   -> Modulo assignment
# **=  -> Exponentiation assignment
#
# =========================================================