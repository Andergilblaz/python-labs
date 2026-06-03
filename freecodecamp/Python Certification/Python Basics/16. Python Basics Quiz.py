"""
============================================================
PYTHON BASICS QUIZ - QUESTIONS & ANSWERS
============================================================
"""

# ============================================================
# QUESTION 1
# ============================================================

"""
Which of the following functions is used to check if a variable
matches a specific data type?

A) isdata()
B) istype()
C) isvariable()
D) isinstance()
"""

# ANSWER:
# D) isinstance()

print(isinstance("Ander", str))

# ============================================================
# QUESTION 2
# ============================================================

"""
Which of the following is NOT a form of string concatenation?

A)
developer = 'Jessica'
age = 30
greeting = 'My name is ' + developer + ' and I am ' + str(age) + ' years old.'

B)
greeting = 'My name is '
developer = 'Jessica'
greeting += developer

C)
developer = 'Jessica'
greeting = x'My name is {developer}.'

D)
developer = 'Jessica'
greeting = 'My name is ' + developer + '.'
"""

# ANSWER:
# C) greeting = x'My name is {developer}.'

# Correct f-string:
developer = "Jessica"
greeting = f"My name is {developer}."
print(greeting)

# ============================================================
# QUESTION 3
# ============================================================

"""
Which function returns the number of characters in a string?

A) counting()
B) length()
C) len()
D) iscount()
"""

# ANSWER:
# C) len()

print(len("Python"))

# ============================================================
# QUESTION 4
# ============================================================

"""
What will result be?

developer = 'Naomi'
result = developer.endswith('N')

A) Undefined
B) None
C) True
D) False
"""

# ANSWER:
# D) False

developer = "Naomi"
print(developer.endswith("N"))

# ============================================================
# QUESTION 5
# ============================================================

"""
What happens when you add a float and an integer?

A) Error
B) Integer
C) Float
D) None
"""

# ANSWER:
# C) Float

print(5 + 2.5)

# ============================================================
# QUESTION 6
# ============================================================

"""
Which is the correct way to define a function?

A) set get_sum(...)
B) def get_sum(...)
C) function get_sum(...)
D) define get_sum(...)
"""

# ANSWER:
# B)

def get_sum(num1, num2):
    return num1 + num2

print(get_sum(3, 4))

# ============================================================
# QUESTION 7
# ============================================================

"""
What will be printed?

def greet():
    pass

print(greet())

A) None
B) RangeError
C) Null
D) TypeError
"""

# ANSWER:
# A) None

def greet():
    pass

print(greet())

# ============================================================
# QUESTION 8
# ============================================================

"""
Which statement is FALSE?

A) Cannot use reserved keywords
B) Cannot start with numbers
C) Variables must be max 10 characters
D) Only alphanumeric and underscore
"""

# ANSWER:
# C)

long_variable_name_that_is_perfectly_valid = 123
print(long_variable_name_that_is_perfectly_valid)

# ============================================================
# QUESTION 9
# ============================================================

"""
Which is NOT a Python data type?

A) Generic
B) int
C) float
D) None
"""

# ANSWER:
# A) Generic

# ============================================================
# QUESTION 10
# ============================================================

"""
Which converts all characters to uppercase?

A) toUpper()
B) up()
C) upper()
D) isupper()
"""

# ANSWER:
# C)

developer = "Jessica"
print(developer.upper())

# ============================================================
# QUESTION 11
# ============================================================

"""
Which function gets user input?

A) input()
B) prompt()
C) read()
D) cout()
"""

# ANSWER:
# A)

# username = input("Enter your name: ")

# ============================================================
# QUESTION 12
# ============================================================

"""
What is the output?

message = 'Python is fun!'
print(message[0:6])

A) Py
B) fun
C) Python
D) is
"""

# ANSWER:
# C)

message = "Python is fun!"
print(message[0:6])

# ============================================================
# QUESTION 13
# ============================================================

"""
What does split() do?

A) Split tuple
B) Split string into list
C) Split float
D) Split dictionary
"""

# ANSWER:
# B)

text = "one,two,three"
print(text.split(","))

# ============================================================
# QUESTION 14
# ============================================================

"""
What will be printed?

example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)

A) dashed name
B) example dashed name
C) None
D) TypeError
"""

# ANSWER:
# B)

example_list = ["example", "dashed", "name"]

joined_str = " ".join(example_list)
print(joined_str)

# ============================================================
# QUESTION 15
# ============================================================

"""
Which creates a translation table?

A) str.translations()
B) str.maketrans()
C) str.tran()
D) str.gettranslate()
"""

# ANSWER:
# B)

table = str.maketrans("abc", "123")
print("abc".translate(table))

# ============================================================
# QUESTION 16
# ============================================================

"""
What is the result?

int_1 = 4
int_2 = 2

print(int_1 ** int_2)

A) 2
B) 4
C) 8
D) 16
"""

# ANSWER:
# D)

print(4 ** 2)

# ============================================================
# QUESTION 17
# ============================================================

"""
What will find() return if the substring is not found?

A) 1
B) 0
C) -2
D) -1
"""

# ANSWER:
# D)

print("Python".find("Java"))

# ============================================================
# QUESTION 18
# ============================================================

"""
Which counts occurrences of a substring?

A) counter()
B) counting()
C) count()
D) hascount()
"""

# ANSWER:
# C)

print("banana".count("a"))

# ============================================================
# QUESTION 19
# ============================================================

"""
What does floor division do?

A) Convert float to int
B) Divide and round down
C) Multiply and round up
D) Power operation
"""

# ANSWER:
# B)

print(10 // 3)

# ============================================================
# QUESTION 20
# ============================================================

"""
Which rounds to the nearest whole number?

A) ceil()
B) floor()
C) float()
D) round()
"""

# ANSWER:
# D)

print(round(3.7))

# ============================================================
# FINAL ANSWER SHEET
# ============================================================

answers = {
    1: "D - isinstance()",
    2: "C - x'My name is {developer}.'",
    3: "C - len()",
    4: "D - False",
    5: "C - Float",
    6: "B - def",
    7: "A - None",
    8: "C - Max 10 characters",
    9: "A - Generic",
    10: "C - upper()",
    11: "A - input()",
    12: "C - Python",
    13: "B - Split string into list",
    14: "B - example dashed name",
    15: "B - str.maketrans()",
    16: "D - 16",
    17: "D - -1",
    18: "C - count()",
    19: "B - Divide and round down",
    20: "D - round()"
}

print("\n=== ANSWER SHEET ===")

for question, answer in answers.items():
    print(f"{question}: {answer}")