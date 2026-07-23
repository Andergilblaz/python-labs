# =========================================================
# PYTHON LOOPS
# =========================================================

# ---------------------------------------------------------
# FOR LOOP
# ---------------------------------------------------------
# Iterate through each element of an iterable.

languages = ["Rust", "Java", "Python", "C++"]

for language in languages:
    print(language)

# Result:
# Rust
# Java
# Python
# C++


# ---------------------------------------------------------
# INDENTATION
# ---------------------------------------------------------
# The code inside the loop MUST be indented.

# for language in languages:
# print(language)

# Result:
# IndentationError


# ---------------------------------------------------------
# ITERATING OVER A STRING
# ---------------------------------------------------------
# Strings are iterable.

for char in "code":
    print(char)

# Result:
# c
# o
# d
# e


# ---------------------------------------------------------
# NESTED FOR LOOPS
# ---------------------------------------------------------
# A loop inside another loop.

categories = ["Fruit", "Vegetable"]
foods = ["Apple", "Carrot", "Banana"]

for category in categories:
    for food in foods:
        print(category, food)

# Result:
# Fruit Apple
# Fruit Carrot
# Fruit Banana
# Vegetable Apple
# Vegetable Carrot
# Vegetable Banana


# ---------------------------------------------------------
# WHILE LOOP
# ---------------------------------------------------------
# Repeat while a condition is True.

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-5): "))

print("You got it!")

# Result:
# Keeps asking until the correct number is entered.


# ---------------------------------------------------------
# BREAK
# ---------------------------------------------------------
# Exit the loop immediately.

developers = ["Jess", "Naomi", "Tom"]

for developer in developers:
    if developer == "Naomi":
        break
    print(developer)

# Result:
# Jess


# ---------------------------------------------------------
# CONTINUE
# ---------------------------------------------------------
# Skip the current iteration.

developers = ["Jess", "Naomi", "Tom"]

for developer in developers:
    if developer == "Naomi":
        continue
    print(developer)

# Result:
# Jess
# Tom


# ---------------------------------------------------------
# LOOP ELSE
# ---------------------------------------------------------
# Executes only if the loop finishes WITHOUT break.

words = ["sky", "apple", "rhythm", "fly", "orange"]

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"{word} contains a vowel")
            break
    else:
        print(f"{word} has no vowels")

# Result:
# sky has no vowels
# apple contains a vowel
# rhythm has no vowels
# fly has no vowels
# orange contains a vowel


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# for item in iterable:
# Iterate over each element.

# while condition:
# Repeat while condition is True.

# break
# Exit the loop immediately.

# continue
# Skip the current iteration.

# else:
# Run only if the loop finishes normally (no break).

# =========================================================
# REMEMBER:
# for -> Iterate over an iterable.
# while -> Repeat while a condition is True.
# break -> Stop the loop.
# continue -> Skip one iteration.
# else -> Executes only if break was NOT used.
# Indentation is mandatory in Python.
# =========================================================