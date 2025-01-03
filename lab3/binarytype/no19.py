# Given string
input_string = "Hello, World!"

# Convert the string to binary representation using bytes()
binary_data = bytes(input_string, 'utf-8')

# Display the binary representation
print("Binary representation:", binary_data)

# Performing basic operations on the binary data
# Concatenation: Adding another binary string
additional_data = bytes(" How are you?", 'utf-8')
concatenated_data = binary_data + additional_data

# Display the concatenated binary data
print("Concatenated binary data:", concatenated_data)

# Slicing: Taking a slice of the first 5 bytes
sliced_data = concatenated_data[:5]

# Display the sliced binary data
print("Sliced binary data:", sliced_data)