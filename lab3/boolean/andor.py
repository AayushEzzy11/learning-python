# Get user input
age = int(input("Enter your age: "))
has_permission = input("Do you have permission? (yes/no): ").strip().lower()
is_smart = input("Are you smart? (yes/no): ").strip().lower()

# Convert 'yes'/'no' to boolean values
has_permission = has_permission == 'yes'
is_smart = is_smart == 'yes'

# Evaluate conditions using logical operators
if age >= 18 and has_permission:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")

if is_smart or has_permission:
    print("You are either smart or have permission.")
else:
    print("You are neither smart nor have permission.")

if not is_smart:
    print("You might want to study more.")