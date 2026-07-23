# -----------------------------
# STRING SLICING BASICS
# -----------------------------

my_str = "Hello world"

# Access single characters (indexing)
print(my_str[0])   # H
print(my_str[6])   # w
print(my_str[-1])  # d


# -----------------------------
# BASIC SLICING [start:stop]
# -----------------------------

# Extract from index 1 to 4 (4 not included)
print(my_str[1:4])  # ell


# -----------------------------
# OMITTING START OR STOP
# -----------------------------

# From start to index 7 (not included)
print(my_str[:7])   # Hello w

# From index 8 to the end
print(my_str[8:])   # rld

# Whole string
print(my_str[:])    # Hello world


# -----------------------------
# ORIGINAL STRING IS NOT MODIFIED
# -----------------------------

slice_part = my_str[8:]
print(slice_part)   # rld
print(my_str)       # Hello world


# -----------------------------
# USING STEP [start:stop:step]
# -----------------------------

# Every 2 characters
print(my_str[0:11:2])  # Hlowrd


# -----------------------------
# REVERSE STRING (IMPORTANT TRICK)
# -----------------------------

reversed_str = my_str[::-1]
print(reversed_str)  # dlrow olleH