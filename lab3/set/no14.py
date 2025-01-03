# Initialize an empty set
my_set = set()

# Function to display the current set
def display_set():
    print("Current Set:", my_set)

# Add items to the set
my_set.add('apple')
my_set.add('banana')
my_set.add('cherry')

# Display the set after adding items
print("After adding items:")
display_set()

# Remove an item from the set
my_set.remove('banana')
print("\nAfter removing 'banana':")
display_set()

# Attempt to remove an item that is not in the set
item_to_remove = 'grape'
print(f"\nAttempting to remove '{item_to_remove}':")
try:
    my_set.remove(item_to_remove)  # This will raise a KeyError if the item is not present
except KeyError:
    print(f"Error: '{item_to_remove}' is not in the set!")

# Display the final set
print("\nFinal Set:")
display_set()