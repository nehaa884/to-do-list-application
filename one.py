import os

FILE_NAME = "todo.txt"


def load_tasks():
    tasks = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    line = line.strip()

                    if "|" in line:
                        title, status = line.split("|", 1)
                        tasks.append({
                            "title": title,
                            "status": status
                        })
        except (OSError, ValueError):
            print("Error reading the task file.")

    return tasks


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(
                    task["title"] + "|" +
                    task["status"] + "\n"
                )
    except OSError:
        print("Error saving tasks.")


def add_task(tasks):
    title = input("Enter task name: ").strip()

    if title == "":
        print("Task title cannot be empty.")
        return

    tasks.append({
        "title": title,
        "status": "Pending"
    })

    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found. Your to-do list is empty.")
        return

    print("\n----- TO-DO LIST -----")

    for i, task in enumerate(tasks, start=1):
        print(
            i, "|", task["title"],
            "|", task["status"]
        )


def complete_task(tasks):
    try:
        number = int(input("Enter task number: "))

        if number < 1 or number > len(tasks):
            print("Task number not found.")
            return

        tasks[number - 1]["status"] = "Done"
        save_tasks(tasks)
        print("Task marked as completed.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Task number not found.")
            return

        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print("Task deleted:", removed["title"])

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    

     