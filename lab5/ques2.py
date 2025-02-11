class NegativeNumberError(Exception):
    pass
try:
    num=int(input("Enter a positive number : "))
    if num<0:
        raise NegativeNumberError("Error : Negative number error.")
    print("you entered:",num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Error : Please enter an integer.")