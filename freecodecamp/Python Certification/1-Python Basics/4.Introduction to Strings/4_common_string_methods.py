# -----------------------------
# COMMON STRING METHODS
# -----------------------------

my_str = '  hello world  '

# upper() -> converts all characters to uppercase
print(my_str.upper())  # "  HELLO WORLD  "

# lower() -> converts all characters to lowercase
print(my_str.lower())  # "  hello world  "

# strip() -> removes leading and trailing whitespace
print(my_str.strip())  # "hello world"


# -----------------------------
# replace()
# -----------------------------

text = 'hello world'

# replace(old, new) -> replaces all occurrences of 'old' with 'new'
print(text.replace('hello', 'hi'))  # hi world


# -----------------------------
# split()
# -----------------------------

text = 'hello world'

# split() -> splits string into a list (default separator is space)
words = text.split()
print(words)  # ['hello', 'world']


# -----------------------------
# join()
# -----------------------------

word_list = ['hello', 'world']

# join(iterable) -> joins list elements into a string using a separator
joined = ' '.join(word_list)
print(joined)  # hello world


# -----------------------------
# startswith() and endswith()
# -----------------------------

text = 'hello world'

# startswith(prefix) -> checks if string starts with given prefix
print(text.startswith('hello'))  # True

# endswith(suffix) -> checks if string ends with given suffix
print(text.endswith('world'))    # True


# -----------------------------
# find()
# -----------------------------

text = 'hello worlde'

# find(substring) -> returns index of first occurrence, or -1 if not found
print(text.find('world'))  # 6
print(text.find('xyz'))    # -1
print(text.rfind("e"))     # 11 (this reads from right to left to find the last one)


# -----------------------------
# count()
# -----------------------------

text = 'hello world'

# count(substring) -> counts occurrences of substring
print(text.count('o'))  # 2


# -----------------------------
# capitalize()
# -----------------------------

text = 'hello world'

# capitalize() -> capitalizes first character, lowers the rest
print(text.capitalize())  # Hello world


# -----------------------------
# isupper() and islower()
# -----------------------------

text = 'hello world'

# isupper() -> returns True if all letters are uppercase
print(text.isupper())  # False

# islower() -> returns True if all letters are lowercase
print(text.islower())  # True


# -----------------------------
# title()
# -----------------------------

text = 'hello world'

# title() -> capitalizes first letter of each word
print(text.title())  # Hello World