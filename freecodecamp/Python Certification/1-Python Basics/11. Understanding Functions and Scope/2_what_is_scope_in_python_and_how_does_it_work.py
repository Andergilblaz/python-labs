# =========================================================
# SCOPE IN PYTHON
# =========================================================

# ---------------------------------------------------------
# WHAT IS SCOPE?
# ---------------------------------------------------------
# Scope determines where a variable can be accessed
# in a program.
#
# Python follows the LEGB rule to resolve variables:
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in

# ---------------------------------------------------------
# LEGB RULE
# ---------------------------------------------------------
#
# Local     -> Variables inside functions or classes.
# Enclosing -> Variables inside outer functions.
# Global    -> Variables defined at module level.
# Built-in  -> Python reserved functions and objects.
#
# Python searches for variables in this order:
#
# Local -> Enclosing -> Global -> Built-in

# =========================================================
# LOCAL SCOPE
# =========================================================

# ---------------------------------------------------------
# LOCAL VARIABLES
# ---------------------------------------------------------
# Variables created inside a function only exist
# inside that function.

def my_func():
    my_var = 10
    print(my_var)

my_func()

# Result:
# 10

# ---------------------------------------------------------
# LOCAL VARIABLES CANNOT BE ACCESSED OUTSIDE
# ---------------------------------------------------------

def my_func():
    my_var = 10
    print(my_var)

my_func()

# print(my_var)

# Result:
# NameError
#
# my_var only exists inside my_func()

# =========================================================
# ENCLOSING SCOPE
# =========================================================

# ---------------------------------------------------------
# NESTED FUNCTIONS
# ---------------------------------------------------------
# Inner functions can access variables from
# their enclosing functions.

def outer_func():
    msg = "Hello there!"

    def inner_func():
        print(msg)

    inner_func()

outer_func()

# Result:
# Hello there!

# ---------------------------------------------------------
# INNER FUNCTIONS CAN ACCESS OUTER VARIABLES
# ---------------------------------------------------------

def outer_func():
    name = "Ander"

    def inner_func():
        print(name)

    inner_func()

outer_func()

# Result:
# Ander

# ---------------------------------------------------------
# OUTER FUNCTIONS CANNOT ACCESS INNER VARIABLES
# ---------------------------------------------------------

def outer_func():

    def inner_func():
        res = "Hello"

    inner_func()

    # print(res)

outer_func()

# Result:
# NameError
#
# res only exists inside inner_func()

# ---------------------------------------------------------
# NONLOCAL KEYWORD
# ---------------------------------------------------------
# Allows a nested function to modify variables
# from the enclosing scope.

def outer_func():
    message = ""

    def inner_func():
        nonlocal message
        message = "Updated message"

    inner_func()

    print(message)

outer_func()

# Result:
# Updated message

# =========================================================
# GLOBAL SCOPE
# =========================================================

# ---------------------------------------------------------
# GLOBAL VARIABLES
# ---------------------------------------------------------
# Variables defined outside functions are global.

my_var = 100

def show_var():
    print(my_var)

show_var()

print(my_var)

# Result:
# 100
# 100

# ---------------------------------------------------------
# GLOBAL VARIABLES CAN BE USED ANYWHERE
# ---------------------------------------------------------

username = "Ander"

def greet():
    print(username)

greet()

# Result:
# Ander

# =========================================================
# GLOBAL KEYWORD
# =========================================================

# ---------------------------------------------------------
# CREATE GLOBAL VARIABLES INSIDE FUNCTIONS
# ---------------------------------------------------------

def create_variable():
    global score
    score = 50

create_variable()

print(score)

# Result:
# 50

# score is now available globally.

# ---------------------------------------------------------
# MODIFY GLOBAL VARIABLES
# ---------------------------------------------------------

counter = 1

def update_counter():
    global counter
    counter = 2

update_counter()

print(counter)

# Result:
# 2

# Without global, Python would create a new local variable.

# =========================================================
# BUILT-IN SCOPE
# =========================================================

# ---------------------------------------------------------
# PYTHON BUILT-IN FUNCTIONS
# ---------------------------------------------------------
# Python provides built-in functions that are
# available everywhere.

print(str(45))

# Result:
# "45"

print(type(3.14))

# Result:
# <class 'float'>

print(isinstance(3, str))

# Result:
# False

# ---------------------------------------------------------
# BUILT-IN OBJECTS
# ---------------------------------------------------------
# Functions like print(), len(), str(), int(),
# float(), type() and many others belong to
# Python's built-in scope.

numbers = [1, 2, 3, 4]

print(len(numbers))

# Result:
# 4

# =========================================================
# LEGB SEARCH ORDER EXAMPLE
# =========================================================

name = "Global"

def outer():

    name = "Enclosing"

    def inner():

        name = "Local"

        print(name)

    inner()

outer()

# Result:
# Local
#
# Python finds the variable in Local scope first,
# so it stops searching.

# =========================================================
# IMPORTANT SUMMARY
# =========================================================
#
# LEGB RULE
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in
#
# SEARCH ORDER
#
# Local
# ↓
# Enclosing
# ↓
# Global
# ↓
# Built-in
#
# LOCAL
#
# Variables only accessible inside the function.
#
# ENCLOSING
#
# Variables from outer functions available to
# nested functions.
#
# GLOBAL
#
# Variables defined outside functions.
#
# BUILT-IN
#
# Python predefined functions and objects.
#
# KEYWORDS
#
# global   -> Modify or create global variables.
# nonlocal -> Modify enclosing variables.
#
# =========================================================