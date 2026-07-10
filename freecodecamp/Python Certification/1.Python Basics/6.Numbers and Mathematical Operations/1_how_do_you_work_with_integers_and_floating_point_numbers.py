# =========================================================
# INTEGERS AND FLOATS IN PYTHON
# =========================================================

# ---------------------------------------------------------
# INTEGERS (int)
# ---------------------------------------------------------
# Integers are whole numbers without decimal places.
# They can be positive or negative.

my_int_1 = 56
my_int_2 = -4

# type() returns the data type of a variable
print(type(my_int_1))
print(type(my_int_2))

# Result:
# <class 'int'>
# <class 'int'>

# ---------------------------------------------------------
# INTEGER ADDITION
# ---------------------------------------------------------

my_int_1 = 56
my_int_2 = 12

# + adds two numbers
sum_ints = my_int_1 + my_int_2

print('Integer Addition:', sum_ints)

# Result:
# Integer Addition: 68

# ---------------------------------------------------------
# INTEGER SUBTRACTION
# ---------------------------------------------------------

my_int_1 = 56
my_int_2 = 12

# - subtracts numbers
diff_ints = my_int_1 - my_int_2

print('Integer Subtraction:', diff_ints)

# Result:
# Integer Subtraction: 44

# ---------------------------------------------------------
# INTEGER MULTIPLICATION
# ---------------------------------------------------------

my_int_1 = 12
my_int_2 = 4

# * multiplies numbers
product_ints = my_int_1 * my_int_2

print('Integer Multiplication:', product_ints)

# Result:
# Integer Multiplication: 48

# ---------------------------------------------------------
# INTEGER DIVISION
# ---------------------------------------------------------

my_int_1 = 56
my_int_2 = 12

# / divides numbers
# IMPORTANT:
# Division ALWAYS returns a float in Python

div_ints = my_int_1 / my_int_2

print('Integer Division:', div_ints)

# Result:
# Integer Division: 4.666666666666667

# ---------------------------------------------------------
# FLOATS (float)
# ---------------------------------------------------------
# Floats are decimal numbers.

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1))
print(type(my_float_2))

# Result:
# <class 'float'>
# <class 'float'>

# ---------------------------------------------------------
# FLOAT ADDITION
# ---------------------------------------------------------

my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2

print('Float Addition:', float_addition)

# Result:
# Float Addition: 17.4

# ---------------------------------------------------------
# FLOAT SUBTRACTION
# ---------------------------------------------------------

my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1

print('Float Subtraction:', float_subtraction)

# Result:
# Float Subtraction: 6.6

# ---------------------------------------------------------
# FLOAT MULTIPLICATION
# ---------------------------------------------------------

my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1

print('Float Multiplication:', float_multiplication)

# Result:
# Float Multiplication: 64.80000000000001


# ---------------------------------------------------------
# FLOAT DIVISION
# ---------------------------------------------------------

my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1

print('Float Division:', float_division)

# Result:
# Float Division: 2.222222222222222

# ---------------------------------------------------------
# MIXING INTS AND FLOATS
# ---------------------------------------------------------
# If you combine an int and a float,
# Python automatically converts the result to float.

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float)
print(type(sum_int_and_float))

# Result:
# 61.4
# <class 'float'>

# ---------------------------------------------------------
# MODULO OPERATOR (%)
# ---------------------------------------------------------
# Returns the remainder of a division.

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints)
print('Float Modulo:', mod_floats)

# Result:
# Integer Modulo: 8
# Float Modulo: 1.1999999999999993

# ---------------------------------------------------------
# FLOOR DIVISION (//)
# ---------------------------------------------------------
# Removes decimal places from division result.

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints)
print('Float Floor Division:', floor_div_floats)

# Result:
# Integer Floor Division: 4
# Float Floor Division: 2.0
# For example 4.6666 would be 4 

# ---------------------------------------------------------
# EXPONENTIATION (**)
# ---------------------------------------------------------
# Raises a number to the power of another.

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints)
print('Float Exponentiation:', exp_floats)

# Result:
# Integer Exponentiation: 951166013805414055936
# Float Exponentiation: 614787626.1765089

# ---------------------------------------------------------
# FLOAT PRECISION PROBLEM
# ---------------------------------------------------------
# Some decimal numbers cannot be represented exactly.

print(0.1 + 0.2)

# Result:
# 0.30000000000000004

# This happens because floats are stored in binary format.

# ---------------------------------------------------------
# CONVERT INT TO FLOAT
# ---------------------------------------------------------

my_int_1 = 56

# float() converts values into float type
my_float_1 = float(my_int_1)

print(my_float_1)
print(type(my_float_1))

# Result:
# 56.0
# <class 'float'>

# ---------------------------------------------------------
# CONVERT FLOAT TO INT
# ---------------------------------------------------------

my_float = 12.92563

# int() removes decimal part
my_int = int(my_float)

print(my_int)
print(type(my_int))

# Result:
# 12
# <class 'int'>

# IMPORTANT:
# int() DOES NOT round.
# It simply removes decimals.

# ---------------------------------------------------------
# CONVERT STRINGS TO NUMBERS
# ---------------------------------------------------------

my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))
print(converted_float, type(converted_float))

# Result:
# 45 <class 'int'>
# 7.8 <class 'float'>

# ---------------------------------------------------------
# round()
# ---------------------------------------------------------
# Rounds numbers.

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1)
print(rounded_int_2)

# Result:
# 5
# 4.3

# ---------------------------------------------------------
# abs()
# ---------------------------------------------------------
# Returns absolute value.
# Removes negative sign.

num = -15

absolute_value = abs(num)

print(absolute_value)

# Result:
# 15

# ---------------------------------------------------------
# pow()
# ---------------------------------------------------------
# Raises numbers to powers.

result_1 = pow(2, 3)

print(result_1)

# Result:
# 8

# ---------------------------------------------------------
# pow() WITH MODULO
# ---------------------------------------------------------
# Equivalent to:
# (2 ** 3) % 5

result_2 = pow(2, 3, 5)

print(result_2)

# Result:
# 3

# ---------------------------------------------------------
# IMPORTANT SUMMARY
# =========================================================
#
# int     -> Whole numbers
# float   -> Decimal numbers
#
# +       -> Addition
# -       -> Subtraction
# *       -> Multiplication
# /       -> Division
# %       -> Modulo
# //      -> Floor division
# **      -> Exponentiation
#
# int()   -> Convert to integer
# float() -> Convert to float
# round() -> Round numbers
# abs()   -> Absolute value
# pow()   -> Power
#
# =========================================================