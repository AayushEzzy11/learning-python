def find_number_index(numbers, target):
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return -1

# Test the function
numbers = [4, 2, 7, 1, 9, 5, 3]
target = 9
result = find_number_index(numbers, target)
print(f"Numbers: {numbers}")
print(f"Target: {target}")
print(f"Index: {result}")