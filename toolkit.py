def to_do_list():
    """Display the to-do menu and manage the user's tasks."""
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Return to main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append({"name": task, "complete": False})
                print("Task added.")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    status = "Complete" if task["complete"] else "Not complete"
                    print(f"{index}. {task['name']} — {status}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to mark complete.")
                continue
            try:
                task_number = int(input("Enter the task number: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["complete"] = True
                    print("Task marked as complete.")
                else:
                    print("That task number is not on the list.")
            except ValueError:
                print("Please enter a valid whole number.")
        elif choice == "4":
            break
        else:
            print("Sorry, that option isn't on the to-do menu. Please choose 1-4.")


def simple_calculator():
    """Calculate the result of a basic arithmetic operation."""
    try:
        first_number = float(input("\nEnter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                print("You cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            print("Sorry, that operation isn't supported.")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers.")


def countdown_timer():
    """Count down from a number of seconds entered by the user."""
    try:
        seconds = int(input("\nEnter the number of seconds: "))
        if seconds < 0:
            print("Please enter zero or a positive number.")
            return

        while seconds > 0:
            print(f"{seconds}...")
            time.sleep(1)
            seconds -= 1
        print("Time's up!")
    except ValueError:
        print("Please enter a whole number of seconds.")


def main():
    """Display the toolkit menu until the user chooses to quit."""
    while True:
        print("\n=================================")
        print("           MY TOOLKIT")
        print("=================================")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Countdown Timer")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            to_do_list()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            countdown_timer()
        elif choice == "5":
            print("Thanks for using My Toolkit. Goodbye!")
            break
        else:
            print("Sorry, that choice isn't on the menu. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()