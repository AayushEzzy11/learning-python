# Create a dictionary with three key-value pairs
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Display the original dictionary
print("Original dictionary:", my_dict)

# Add a new key-value pair
my_dict['profession'] = 'Engineer'  # Adding a new key-value pair

# Update an existing key-value pair
my_dict['age'] = 31  # Updating the age value

# Display the updated dictionary
print("Updated dictionary:", my_dict)

# Loop through the dictionary and display keys and values
print("Items in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")