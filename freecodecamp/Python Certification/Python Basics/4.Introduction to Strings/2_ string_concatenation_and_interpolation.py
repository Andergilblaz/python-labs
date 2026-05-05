# -----------------------------
# STRING CONCATENATION
# -----------------------------

my_str_1 = 'Hello'
my_str_2 = "World"

# Basic concatenation
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)  # Hello World


# -----------------------------
# CONCATENATION ERROR (TYPE)
# -----------------------------

name = 'John Doe'
age = 26

# Uncomment to see the error:
# name_and_age = name + age  # TypeError


# Fix using str()
name_and_age = name + str(age)
print(name_and_age)  # John Doe26


# -----------------------------
# USING += OPERATOR
# -----------------------------

name_and_age = name  # Start with name
name_and_age += str(age)  # Append age

print(name_and_age)  # John Doe26


# -----------------------------
# STRING INTERPOLATION (F-STRINGS)
# -----------------------------

name = 'John Doe'
age = 26

# Basic interpolation
name_and_age = f"My name is {name} and I am {age} years old"
print(name_and_age)


# Expressions inside f-strings
num1 = 5
num2 = 10

print(f"The sum of {num1} and {num2} is {num1 + num2}")


# -----------------------------
# CLEANER OUTPUT COMPARISON
# -----------------------------

# Concatenation way (more manual)
text_concat = "My name is " + name + " and I am " + str(age) + " years old"
print(text_concat)

# f-string way (cleaner and recommended)
text_fstring = f"My name is {name} and I am {age} years old"
print(text_fstring)