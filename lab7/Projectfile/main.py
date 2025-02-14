# from calculator.basic_operations import add, subtract, multiply, divide
# from calculator.advanced_operations import power, sqrt

# def main():
#     # Test all calculator functions
#     try:
#         # Basic operations
#         print("Basic Operations:")
#         print(f"Addition (5 + 3) = {add(5, 3)}")
#         print(f"Subtraction (10 - 4) = {subtract(10, 4)}")
#         print(f"Multiplication (6 * 7) = {multiply(6, 7)}")
#         print(f"Division (15 / 3) = {divide(15, 3)}")
        
#         # Advanced operations
#         print("\nAdvanced Operations:")
#         print(f"Power (2 ^ 3) = {power(2, 3)}")
#         print(f"Square root of 16 = {sqrt(16)}")
        
#     except ValueError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Unexpected error: {e}")

# if __name__ == "__main__":
#     main()
# main.py
from calculator.basic_operations import add, subtract, multiply, divide
from calculator.advanced_operations import power, sqrt

def get_numbers():
    """Get two numbers from user"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        raise ValueError("Please enter valid numbers")

def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")

        try:
            choice = input("\nEnter your choice (1-7): ")

            if choice == '7':
                print("Thank you for using the calculator!")
                break

            if choice == '6':
                num = float(input("Enter a number: "))
                result = sqrt(num)
                print(f"Square root of {num} = {result}")
                continue

            if choice in ['1', '2', '3', '4', '5']:
                num1, num2 = get_numbers()
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}")
            else:
                print("Invalid choice! Please select 1-7")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()