lucky_numbers = [8, 4, 23, 15, 16,  42]
friends = ["Alice", "Bob", "Carol", "Diana", "Eve", "Frank"]

# Merge the lists
#friends.extend(lucky_numbers)

# Add George at the end
friends.append("George")

# Add Henry at index 1
friends.insert(1, "Henry")

# Remove Eve from the list
friends.remove("Eve")

# Delete the last item
friends.pop()

# Sort alphabetically
friends.sort()
lucky_numbers.sort()

# Copy a list
friends2 = friends.copy()

print(friends)
print(friends2)
print(lucky_numbers)

# Get the index of a person in the list
print(f"Carol is at index {friends.index("Carol")}")

# Count how many times an item appears
print(f"Frank appears {friends.count("Frank")} times")

# Numbers sorted in reverse order
lucky_numbers.reverse()
print(lucky_numbers)

