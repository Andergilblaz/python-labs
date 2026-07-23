# =========================================================
# PYTHON range()
# =========================================================

# ---------------------------------------------------------
# BASIC RANGE
# ---------------------------------------------------------
# Generates a sequence of integers.
# The stop value is NOT included.

for num in range(3):
    print(num)

# Result:
# 0
# 1
# 2


# ---------------------------------------------------------
# RANGE WITH START
# ---------------------------------------------------------
# Specify where the sequence begins.

for num in range(1, 5):
    print(num)

# Result:
# 1
# 2
# 3
# 4


# ---------------------------------------------------------
# RANGE WITH STEP
# ---------------------------------------------------------
# Change the increment between numbers.

for num in range(2, 11, 2):
    print(num)

# Result:
# 2
# 4
# 6
# 8
# 10


# ---------------------------------------------------------
# NEGATIVE STEP
# ---------------------------------------------------------
# Count backwards using a negative step.

for num in range(40, 0, -10):
    print(num)

# Result:
# 40
# 30
# 20
# 10


# ---------------------------------------------------------
# RANGE TO LIST
# ---------------------------------------------------------
# Convert a range into a list.

numbers = list(range(2, 11, 2))

print(numbers)

# Result:
# [2, 4, 6, 8, 10]


# ---------------------------------------------------------
# RANGE ERROR
# ---------------------------------------------------------
# At least one argument is required.

# range()

# Result:
# TypeError: range expected at least 1 argument, got 0


# ---------------------------------------------------------
# FLOAT ERROR
# ---------------------------------------------------------
# range() only accepts integers.

# range(1.5, 5.5)

# Result:
# TypeError: 'float' object cannot be interpreted as an integer


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# range(stop)
# Generate numbers from 0 to stop - 1.

# range(start, stop)
# Generate numbers from start to stop - 1.

# range(start, stop, step)
# Generate numbers using a custom step.

# list(range(...))
# Convert the range into a list.

# =========================================================
# REMEMBER:
# range(stop)           -> Starts at 0.
# range(start, stop)    -> Custom start.
# range(start, stop, step) -> Custom increment/decrement.
# The stop value is NEVER included.
# step can be negative for countdowns.
# range() only accepts integers.
# =========================================================