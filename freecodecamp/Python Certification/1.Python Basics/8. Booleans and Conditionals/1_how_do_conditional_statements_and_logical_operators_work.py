# =========================================================
# CONDITIONAL STATEMENTS AND LOGICAL OPERATORS IN PYTHON
# =========================================================

# ---------------------------------------------------------
# COMPARISON OPERATORS
# ---------------------------------------------------------
# Comparison operators compare values and return
# either True or False.

print(3 > 4)    # False
print(3 < 4)    # True
print(3 == 4)   # False
print(4 == 4)   # True
print(3 != 4)   # True
print(3 >= 4)   # False
print(3 <= 4)   # True

# ---------------------------------------------------------
# BOOLEAN VALUES
# ---------------------------------------------------------
# Booleans can only be True or False.

is_student = True
is_working = False

print(type(is_student))
print(type(is_working))

# Result:
# <class 'bool'>
# <class 'bool'>

# ---------------------------------------------------------
# IF STATEMENT
# ---------------------------------------------------------
# Executes code only when the condition is True.

age = 18

if age >= 18:
    print("You are an adult")

# Result:
# You are an adult

# ---------------------------------------------------------
# IF CONDITION IS FALSE
# ---------------------------------------------------------
# Nothing happens if the condition is False.

age = 12

if age >= 18:
    print("You are an adult")

# Result:
# No output

# ---------------------------------------------------------
# ELSE STATEMENT
# ---------------------------------------------------------
# Executes when the if condition is False.

age = 12

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")

# Result:
# You are not an adult yet

# ---------------------------------------------------------
# ELIF STATEMENT
# ---------------------------------------------------------
# Used to check additional conditions.

age = 15

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Result:
# You are a teenager

# ---------------------------------------------------------
# MULTIPLE ELIF STATEMENTS
# ---------------------------------------------------------
# You can add as many elif blocks as needed.

age = 2

if age >= 65:
    print("Senior citizen")
elif age >= 30:
    print("Adult")
elif age >= 18:
    print("Young adult")
elif age >= 13:
    print("Teenager")
elif age >= 3:
    print("Young child")
else:
    print("Toddler or infant")

# Result:
# Toddler or infant

# ---------------------------------------------------------
# LOGICAL OPERATOR: AND
# ---------------------------------------------------------
# Returns True only if BOTH conditions are True.

age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive")

# Result:
# Can drive

# ---------------------------------------------------------
# LOGICAL OPERATOR: OR
# ---------------------------------------------------------
# Returns True if AT LEAST ONE condition is True.

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today")

# Result:
# No work today

# ---------------------------------------------------------
# LOGICAL OPERATOR: NOT
# ---------------------------------------------------------
# Reverses a boolean value.

is_logged_in = False

if not is_logged_in:
    print("Please log in")

# Result:
# Please log in

# ---------------------------------------------------------
# COMBINING MULTIPLE CONDITIONS
# ---------------------------------------------------------

age = 25
has_license = True
has_car = False

if age >= 18 and has_license and has_car:
    print("Can travel independently")
else:
    print("Requirements not met")

# Result:
# Requirements not met

# ---------------------------------------------------------
# NESTED CONDITIONALS
# ---------------------------------------------------------
# Conditionals can be placed inside other conditionals.

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Needs a license")
else:
    print("Too young to drive")

# Result:
# Can drive

# ---------------------------------------------------------
# PASS KEYWORD
# ---------------------------------------------------------
# pass does nothing and is used as a placeholder.

age = 18

if age >= 18:
    pass

# No output

# ---------------------------------------------------------
# INDENTATION
# ---------------------------------------------------------
# Python uses indentation to define code blocks.
# Four spaces are recommended.

age = 18

if age >= 18:
    print("Correct indentation")

# ---------------------------------------------------------
# IMPORTANT SUMMARY
# =========================================================
#
# COMPARISON OPERATORS
#
# ==   Equal
# !=   Not equal
# >    Greater than
# <    Less than
# >=   Greater than or equal
# <=   Less than or equal
#
# LOGICAL OPERATORS
#
# and  -> Both conditions must be True
# or   -> At least one condition must be True
# not  -> Reverses True/False
#
# CONDITIONAL STATEMENTS
#
# if    -> Execute code when condition is True
# elif  -> Check additional conditions
# else  -> Execute code when all conditions are False
#
# pass  -> Placeholder that does nothing
#
# Python uses indentation to define code blocks.
#
# =========================================================