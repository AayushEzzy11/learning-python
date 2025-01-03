# Create a list with at least 5 elements
my_list = [10, 20, 30, 40, 50]

# Display the original list
print("Original list:", my_list)

# Add a new element to the list
new_element = int(input("Enter a new element to add to the list: "))
my_list.append(new_element)
print("List after adding an element:", my_list)

# Remove an element by its value
remove_element = int(input("Enter the value of the element to remove from the list: "))

# Check if the element is in the list before attempting to remove it
if remove_element in my_list:
    my_list.remove(remove_element)
    print("List after removing the element:", my_list)
else:
    print(f"{remove_element} is not in the list. No element removed.")