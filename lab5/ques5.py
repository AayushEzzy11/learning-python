class InvalidEgeError(Exception):
    pass
try:
    age=int(input("Enter your age:"))
    if age<0 or age>120:
        raise InvalidEgeError("Error : Age must be between 0 and 120.")
    print("Valid age entered:",age)
except ValueError:
    print("Error : Please enter a numberic value.")
except InvalidEgeError as e:
    print(e)