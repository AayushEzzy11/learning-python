import copy

# Original list containing other lists
original_list = [1, 2, [3, 4], 5]

# Shallow Copy
shallow_copied_list = copy.copy(original_list)

# Deep Copy
deep_copied_list = copy.deepcopy(original_list)

# Modify the original list
original_list[2][0] = 'Changed!'

# Display the results
print("Original List: ", original_list)          # [1, 2, ['Changed!', 4], 5]
print("Shallow Copied List: ", shallow_copied_list)  # [1, 2, ['Changed!', 4], 5]
print("Deep Copied List: ", deep_copied_list)    # [1, 2, [3, 4], 5]