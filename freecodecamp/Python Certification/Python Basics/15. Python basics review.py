"""
============================================================
PYTHON BASICS REVIEW
============================================================

Quick review of the most important Python concepts.

Topics:
- Variables
- Data types
- Strings
- Operators
- Functions
- Scope
- Conditionals
- Truthy/Falsy values
- Boolean operators

============================================================
"""

# ============================================================
# VARIABLES
# ============================================================

name = "Ander"
age = 20
height = 1.68
is_student = True

print(name)
print(age)

# ============================================================
# DATA TYPES
# ============================================================

my_int = 10
my_float = 3.14
my_str = "Hello World"
my_bool = True

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {
    "name": "Ander",
    "age": 20
}

my_none = None

print(type(my_int))
print(type(my_float))
print(type(my_str))
print(type(my_bool))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))
print(type(my_none))

# ============================================================
# TYPE CHECKING
# ============================================================

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(height, float))

# ============================================================
# STRINGS
# ============================================================

message = "Python is awesome"

# Access characters
print(message[0])
print(message[-1])

# Slicing
print(message[0:6])
print(message[7:])
print(message[::2])

# Length
print(len(message))

# Concatenation
developer = "Ander"
greeting = "Hello " + developer
print(greeting)

# f-string
greeting = f"Hello {developer}"
print(greeting)

# Escape characters
quote = "It's a sunny day"
print(quote)

# ============================================================
# STRING METHODS
# ============================================================

text = "  hello world  "

print(text.upper())
print(text.lower())
print(text.strip())

print("hello world".replace("hello", "hi"))

words = "one,two,three".split(",")
print(words)

joined = " ".join(words)
print(joined)

print("Python".startswith("Py"))
print("Python".endswith("on"))

print("Python".find("th"))
print("banana".count("a"))

print("hello world".title())
print("hello world".capitalize())

# ============================================================
# IN OPERATOR
# ============================================================

print("Python" in message)
print("Java" in message)

# ============================================================
# MATHEMATICAL OPERATIONS
# ============================================================

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Modulo
print(a % b)

# Floor division
print(a // b)

# Power
print(a ** b)

# ============================================================
# TYPE CONVERSIONS
# ============================================================

print(float(5))
print(int(5.8))
print(str(123))
print(bool(1))
print(bool(0))

# ============================================================
# USEFUL FUNCTIONS
# ============================================================

print(round(3.6))
print(abs(-15))
print(pow(2, 3))

# ============================================================
# AUGMENTED ASSIGNMENTS
# ============================================================

counter = 10

counter += 5
print(counter)

counter -= 2
print(counter)

counter *= 3
print(counter)

counter /= 2
print(counter)

counter //= 2
print(counter)

counter %= 3
print(counter)

counter **= 2
print(counter)

# ============================================================
# FUNCTIONS
# ============================================================

def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(5, 7)
print(result)

# Default arguments

def multiply(number, factor=2):
    return number * factor


print(multiply(5))
print(multiply(5, 4))

# Function without return

def greet():
    print("Hello")


returned_value = greet()
print(returned_value)

# ============================================================
# INPUT
# ============================================================

# Uncomment to test
# username = input("Enter your name: ")
# print(f"Hello {username}")

# ============================================================
# SCOPE
# ============================================================

global_tax = 0.21


def calculate_total(price):
    return price + (price * global_tax)


print(calculate_total(100))


def outer_function():
    message = "Hello from outer scope"

    def inner_function():
        print(message)

    inner_function()


outer_function()

# ============================================================
# COMPARISON OPERATORS
# ============================================================

print(10 == 10)
print(10 != 5)

print(10 > 5)
print(10 < 5)

print(10 >= 10)
print(10 <= 5)

# ============================================================
# IF / ELIF / ELSE
# ============================================================

age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Nested if

is_citizen = True

if is_citizen:
    if age >= 18:
        print("Eligible to vote")
else:
    print("Not eligible")

# ============================================================
# TRUTHY AND FALSY VALUES
# ============================================================

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))

print(bool(True))
print(bool(1))
print(bool("Python"))

# ============================================================
# BOOLEAN OPERATORS
# ============================================================

is_citizen = True
age = 25

print(is_citizen and age)

print(age > 18 and is_citizen)

is_student = True

print(age < 18 or is_student)

print(not is_student)

# ============================================================
# SHORT CIRCUITING
# ============================================================

print(False and print("This will not execute"))
print(True or print("This will not execute"))

# ============================================================
# TRANSLATION TABLE
# ============================================================

translation_table = str.maketrans("abc", "123")

print("abcabc".translate(translation_table))

# ============================================================
# RANGE
# ============================================================

numbers = range(5)

print(numbers)

for number in numbers:
    print(number)

# ============================================================
# MUTABLE VS IMMUTABLE
# ============================================================

# Mutable
sample_list = [1, 2, 3]
sample_list.append(4)

print(sample_list)

# Immutable
sample_string = "Python"


# sample_string[0] = "J"
# This would raise an error

# ============================================================
# END OF REVIEW
# ============================================================

print("\nPython Basics Review Completed Successfully!")

