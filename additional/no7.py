# Loop until a valid number between 1 and 10 is entered
while True:
    # Ask the user for input
    user_input = input("Please enter a number between 1 and 10: ")
    
        # Try to convert the input to an integer
    number = int(user_input)
        
        # Check if the number is within the desired range
    if 1 <= number <= 10:
            print(f"Thank you! You entered the valid number: {number}")
            break  # Exit the loop
    else:
            print("The number is not between 1 and 10. Please try again.")

        # Handle the case where the input is not a number
    print("That's not a valid number. Please enter a number between 1 and 10.")