# =========================================================
# FUNCTIONS IN PYTHON
# =========================================================

# ---------------------------------------------------------
# WHAT IS A FUNCTION?
# ---------------------------------------------------------
# A function is a reusable block of code that performs
# a specific task.
#
# Functions allow you to write code once and use it
# multiple times.

# ---------------------------------------------------------
# BUILT-IN FUNCTIONS
# ---------------------------------------------------------
# Python includes many functions ready to use.

print("Hello World")

# Result:
# Hello World

# ---------------------------------------------------------
# INPUT FUNCTION
# ---------------------------------------------------------
# input() allows the user to enter data.

name = input("What is your name?")

print("Hello", name)

# Example:
# User enters: Ander
#
# Result:
# Hello Ander

# ---------------------------------------------------------
# INT FUNCTION
# ---------------------------------------------------------
# int() converts values to integers.

print(int(3.14))
print(int("42"))
print(int(True))
print(int(False))

# Result:
# 3
# 42
# 1
# 0

# ---------------------------------------------------------
# CREATING A FUNCTION
# ---------------------------------------------------------
# Use the def keyword to create your own functions.

def hello():
    print("Hello World")

# Function created but not executed yet.

# ---------------------------------------------------------
# CALLING A FUNCTION
# ---------------------------------------------------------
# To execute a function, use its name followed by ().

hello()

# Result:
# Hello World

# ---------------------------------------------------------
# FUNCTION PARAMETERS
# ---------------------------------------------------------
# Parameters are variables that receive values when
# the function is called.

def calculate_sum(a, b):
    print(a + b)

# a and b are parameters.

# ---------------------------------------------------------
# FUNCTION ARGUMENTS
# ---------------------------------------------------------
# Arguments are the actual values passed to a function.

calculate_sum(3, 1)

# Result:
# 4

# Here:
# a = 3
# b = 1

# ---------------------------------------------------------
# PARAMETERS VS ARGUMENTS
# ---------------------------------------------------------

def greet(name):
    print("Hello", name)

greet("Ander")

# Parameter:
# name
#
# Argument:
# "Ander"
#
# Result:
# Hello Ander

# ---------------------------------------------------------
# MISSING ARGUMENTS
# ---------------------------------------------------------
# Calling a function without the required arguments
# causes an error.

def multiply(a, b):
    print(a * b)

# multiply()

# Result:
# TypeError

# ---------------------------------------------------------
# RETURN KEYWORD
# ---------------------------------------------------------
# return sends a value back from the function.

def calculate_sum(a, b):
    return a + b

result = calculate_sum(3, 1)

print(result)

# Result:
# 4

# ---------------------------------------------------------
# FUNCTION WITHOUT RETURN
# ---------------------------------------------------------
# If a function does not use return, Python returns None.

def calculate_sum(a, b):
    print(a + b)

result = calculate_sum(3, 1)

print(result)

# Result:
# 4
# None

# ---------------------------------------------------------
# PRINT VS RETURN
# ---------------------------------------------------------

def print_example():
    print(5)

def return_example():
    return 5

# print() displays information.
# return sends information back.

number = return_example()

print(number * 2)

# Result:
# 10

# ---------------------------------------------------------
# WHY USE RETURN?
# ---------------------------------------------------------
# Returned values can be stored in variables,
# reused in calculations, or passed to other functions.

def square(number):
    return number * number

result = square(4)

print(result)

# Result:
# 16

# ---------------------------------------------------------
# IMPORTANT SUMMARY
# =========================================================
#
# BUILT-IN FUNCTIONS
#
# print() -> Display information
# input() -> Get user input
# int()   -> Convert value to integer
#
# CUSTOM FUNCTIONS
#
# def function_name():
#     code
#
# PARAMETERS
#
# Variables received by a function.
#
# ARGUMENTS
#
# Values passed to a function.
#
# RETURN
#
# Sends a value back from a function.
#
# PRINT VS RETURN
#
# print()  -> Show information
# return   -> Return information
#
# If a function does not use return,
# Python returns None by default.
#
# =========================================================