try:
    num1=float(input("Enter the first number :"))
    num2=float(input("Enter the second number :"))
    result=num1/num2
    print("Result :",result)
except ValueError:
    print("Error: Please enter numeric values only")
except ZeroDivisionError:
    print("Error: Division by zero is not alowed")