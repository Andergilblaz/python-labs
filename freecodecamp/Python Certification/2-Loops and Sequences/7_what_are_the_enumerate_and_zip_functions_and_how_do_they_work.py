# =========================================================
# PYTHON enumerate() AND zip()
# =========================================================

# ---------------------------------------------------------
# ENUMERATE()
# ---------------------------------------------------------
# Iterate with both index and value.

languages = ["Spanish", "English", "Russian", "Chinese"]

for index, language in enumerate(languages):
    print(index, language)

# Result:
# 0 Spanish
# 1 English
# 2 Russian
# 3 Chinese


# ---------------------------------------------------------
# ENUMERATE OBJECT
# ---------------------------------------------------------
# enumerate() returns an iterator of tuples.

languages = ["Spanish", "English", "Russian", "Chinese"]

print(list(enumerate(languages)))

# Result:
# [(0, 'Spanish'),
#  (1, 'English'),
#  (2, 'Russian'),
#  (3, 'Chinese')]


# ---------------------------------------------------------
# ENUMERATE WITH START
# ---------------------------------------------------------
# Start counting from a custom value.

languages = ["Spanish", "English", "Russian", "Chinese"]

for index, language in enumerate(languages, 1):
    print(index, language)

# Result:
# 1 Spanish
# 2 English
# 3 Russian
# 4 Chinese


# ---------------------------------------------------------
# ZIP()
# ---------------------------------------------------------
# Combine multiple iterables into pairs.

developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

# Result:
# [('Naomi', 1),
#  ('Dario', 2),
#  ('Jessica', 3),
#  ('Tom', 4)]


# ---------------------------------------------------------
# ZIP() IN A LOOP
# ---------------------------------------------------------
# Iterate over multiple iterables at the same time.

developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {id}")

# Result:
# Name: Naomi
# ID: 1
# Name: Dario
# ID: 2
# Name: Jessica
# ID: 3
# Name: Tom
# ID: 4


# ---------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------

# enumerate(iterable)
# Return (index, value) pairs.

# enumerate(iterable, start)
# Start counting from a custom value.

# zip(iterable1, iterable2)
# Combine elements into tuples.

# list(enumerate(...))
# Convert enumerate object into a list.

# list(zip(...))
# Convert zip object into a list.

# =========================================================
# REMEMBER:
# enumerate() -> Gives you both index and value.
# enumerate(..., start) -> Custom starting index.
# zip() -> Iterates over multiple iterables together.
# Both functions return iterators.
# =========================================================