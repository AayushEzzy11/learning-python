# Create a tuple with 5 elements
fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')

# Unpack the tuple into separate variables
fruit1, fruit2, fruit3, fruit4, fruit5 = fruits

# Print the unpacked variables
print("Fruit 1: ", fruit1)
print("Fruit 2: ", fruit2)
print("Fruit 3: ", fruit3)
print("Fruit 4: ", fruit4)
print("Fruit 5: ", fruit5)

# Convert the tuple to a list
fruit_list = list(fruits)

# Update the list
fruit_list[0] = 'apricot'

# Convert the list back to a tuple
updated_fruits = tuple(fruit_list)

# Print the updated tuple
print("Updated Fruits: ", updated_fruits)