# =========================================================
# TRUTHY, FALSY VALUES AND BOOLEAN OPERATORS IN PYTHON
# =========================================================

# ---------------------------------------------------------
# TRUTHY AND FALSY VALUES
# ---------------------------------------------------------
# Every value in Python has a boolean equivalent.
#
# Truthy values evaluate to True.
# Falsy values evaluate to False.

# Common falsy values:

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))

# Result:
# False
# False
# False
# False
# False

# Common truthy values:

print(bool(True))
print(bool(1))
print(bool(-5))
print(bool(3.14))
print(bool("Hello"))

# Result:
# True
# True
# True
# True
# True

# ---------------------------------------------------------
# bool() FUNCTION
# ---------------------------------------------------------
# Converts any value into True or False.

print(bool("Python"))
print(bool(""))
print(bool(100))
print(bool(0))

# Result:
# True
# False
# True
# False

# ---------------------------------------------------------
# BOOLEAN OPERATOR: AND
# ---------------------------------------------------------
# Returns the first falsy value found.
# If all values are truthy, returns the last value.
#
# Both operands must be truthy for the expression
# to evaluate as truthy.

print(True and True)
print(True and False)

# Result:
# True
# False

# Example with values:

is_citizen = True
age = 25

print(is_citizen and age)

# Result:
# 25

# Because:
# True and 25 -> returns 25

# ---------------------------------------------------------
# USING AND IN CONDITIONALS
# ---------------------------------------------------------

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Result:
# Eligible to vote

# ---------------------------------------------------------
# BOOLEAN OPERATOR: OR
# ---------------------------------------------------------
# Returns the first truthy value found.
# If all values are falsy, returns the last value.
#
# At least one operand must be truthy.

print(True or False)
print(False or False)

# Result:
# True
# False

# Example with values:

age = 19
is_employed = False

print(age or is_employed)

# Result:
# 19

# Because:
# 19 is already truthy

# ---------------------------------------------------------
# USING OR IN CONDITIONALS
# ---------------------------------------------------------

age = 19
is_student = True

if age < 18 or is_student:
    print("Eligible for student discount")
else:
    print("Not eligible for student discount")

# Result:
# Eligible for student discount

# ---------------------------------------------------------
# BOOLEAN OPERATOR: NOT
# ---------------------------------------------------------
# Reverses a boolean value.
#
# Truthy -> False
# Falsy  -> True

print(not "")
print(not "Hello")

print(not 0)
print(not 1)

print(not False)
print(not True)

# Result:
# True
# False
# True
# False
# True
# False

# ---------------------------------------------------------
# USING NOT IN CONDITIONALS
# ---------------------------------------------------------

is_admin = False

if not is_admin:
    print("Access denied")
else:
    print("Welcome administrator")

# Result:
# Access denied

# ---------------------------------------------------------
# SHORT-CIRCUITING WITH AND
# ---------------------------------------------------------
# Python evaluates from left to right.
# It stops as soon as the final result is known.

print(False and "Hello")

# Result:
# False

# Python never evaluates "Hello"
# because False already determines the result.

# Another example:

print(0 and 100)

# Result:
# 0

# ---------------------------------------------------------
# SHORT-CIRCUITING WITH OR
# ---------------------------------------------------------
# Python stops when it finds the first truthy value.

print("Python" or "Java")

# Result:
# Python

# Python never evaluates "Java"
# because the result is already known.

# Another example:

print(10 or 20)

# Result:
# 10

# ---------------------------------------------------------
# REPLACING NESTED IF STATEMENTS
# ---------------------------------------------------------
# Boolean operators often make code cleaner.

# Nested version:

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print("Eligible to vote")

# Cleaner version:

if is_citizen and age >= 18:
    print("Eligible to vote")

# Result:
# Eligible to vote

# ---------------------------------------------------------
# COMBINING MULTIPLE CONDITIONS
# ---------------------------------------------------------

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Result:
# Login successful

# ---------------------------------------------------------
# IMPORTANT SUMMARY
# =========================================================
#
# TRUTHY VALUES
#
# True
# Non-zero numbers
# Non-empty strings
# Non-empty collections
#
# FALSY VALUES
#
# False
# None
# 0
# 0.0
# ""
# Empty collections
#
# BOOLEAN OPERATORS
#
# and -> Returns first falsy value,
#         otherwise returns last value
#
# or  -> Returns first truthy value,
#         otherwise returns last value
#
# not -> Always returns True or False
#         and reverses the boolean value
#
# SHORT-CIRCUITING
#
# and -> Stops at first falsy value
# or  -> Stops at first truthy value
#
# =========================================================