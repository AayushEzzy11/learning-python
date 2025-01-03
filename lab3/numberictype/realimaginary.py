# Get input from user
print("Enter a complex number (Example: 3+4j or 2-3j)")
num = complex(input("Enter the number: "))

# Check if the number is complex
if isinstance(num, complex):
    print("\nResults:")
    print(f"This is a complex number: {num}")
    print(f"Real part: {num.real}")
    print(f"Imaginary part: {num.imag}")

