# Get a list of integers from the user
input_list = input("Enter a list of integers separated by spaces: ")
# Convert the input string to a list of integers
numbers = [int(x) for x in input_list.split()]

# Use list comprehension to double the even numbers and filter out odd numbers
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]

# Print the resulting list
print("Doubled even numbers:", doubled_evens)