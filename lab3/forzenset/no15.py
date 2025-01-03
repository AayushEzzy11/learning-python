# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a frozenset from the list of numbers
my_frozenset = frozenset(numbers)

# Display the frozenset
print("Original frozenset:", my_frozenset)

# Attempt to add an element to the frozenset
try:
    my_frozenset.add(6)  # Trying to add an element
except AttributeError as e:
    print("Error:", e)  # Catch AttributeError for trying to add to frozenset

# Attempt to remove an element from the frozenset
try:
    my_frozenset.remove(4)  # Trying to remove an element
except AttributeError as e:
    print("Error:", e)  # Catch AttributeError for trying to remove from frozenset

# Display the frozenset after attempts to modify it
print("Frozenset after modification attempts:", my_frozenset)