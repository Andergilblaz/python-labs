# -----------------------------
# STRING BASICS IN PYTHON
# -----------------------------

# 1. Creating strings
my_str_1 = 'Hello'
my_str_2 = "World"

print(my_str_1)
print(my_str_2)


# 2. Multiline strings
my_str_3 = """Multiline
string"""

my_str_4 = '''Another
multiline
string'''

print(my_str_3)
print(my_str_4)


# 3. Quotes inside strings

# Using different quotes
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

print(msg)
print(quote)

# Using escape characters
msg_escape = 'It\'s a sunny day'
quote_escape = "She said, \"Hello!\""

print(msg_escape)
print(quote_escape)


# 4. Checking if a substring exists (in operator)
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('e' in my_str)      # True
print('f' in my_str)      # False


# 5. Length of a string
print(len(my_str))  # 11


# 6. Indexing (access characters)
print(my_str[0])  # H
print(my_str[6])  # w


# 7. Negative indexing
print(my_str[-1])  # d
print(my_str[-2])  # l


# 8. Immutability demonstration

greeting = 'hi'

# Reassignment (allowed)
greeting = 'hello'
print(greeting)


# Attempt to modify (NOT allowed)
# Uncomment to see the error:
# greeting[0] = 'H'  # TypeError


# 9. Workaround for immutability (create a new string)

greeting = 'hi'
new_greeting = 'H' + greeting[1:]

print(new_greeting)  # Hi