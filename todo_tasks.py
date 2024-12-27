task = []

# Add task function
def add_task():
    data = input("Enter the task you want to add: ")
    task.append(data)
    print(f"'{data}' has been added successfully.")

# Review tasks function
def review_task():
    if task:
        print("Your tasks:")
        for i, t in enumerate(task, 1):
            print(f"{i}. {t}")
    else:
        print("No tasks to review.")

# Remove task function
def remove_task():
    if task:
        task_index = int(input("Enter the task number you want to remove: "))
        if 1 <= task_index <= len(task):
            removed_task = task.pop(task_index - 1)
            print(f"'{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")

# Main menu function
def main_menu():
    while True:
        print("\n1. Add Task\n2. Review Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            review_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

# Run the program
if __name__ == '__main__':
    main_menu()
