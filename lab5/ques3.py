class EmptyListError(Exception):
    pass
try:
    numbers=input("Enter the number separed by space: ").split()
    if not numbers:
        raise EmptyListError("Error: List is empty.")
    numbers=[float(num) for num in numbers]
    average=sum(numbers)/len(numbers)
    print("Average:",average)
except ValueError:
    print("Error: Please enter only numberic values.")
except EmptyListError as e:
    print(e)