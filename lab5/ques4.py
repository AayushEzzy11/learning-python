attempts=3

while attempts>0:
    try:
        num=int(input("Enter the a number between 1 and 10: "))
        if 1 <= num <= 10:
            print("Valid number entered:",num)
            break
        else:
            raise ValueError("Numbers out of range.")
    except ValueError:
        attempts-=1
        print(f"Invalid input.{attempts} attempts lefts.")
if attempts==0:
    print("Error : Too many invalid attempts.")