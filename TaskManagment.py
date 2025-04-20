pending_tasks = []

def add_task(description):
    pending_tasks.append({"description": description, "completed": False})
    print("Task added successfully!")

def list_tasks():
    if not pending_tasks:
        print("No pending tasks.")
        return
    print("\nTask List:")
    for i, task in enumerate(pending_tasks):
        status = "✅" if task["completed"] else "❌"
        print(f"{i + 1}. {task['description']} - {status}")
    print()

def mark_task_completed(index):
    if 0 <= index - 1 < len(pending_tasks):
        pending_tasks[index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid index.")

def remove_task(index):
    if 0 <= index - 1 < len(pending_tasks):
        pending_tasks.pop(index - 1)
        print("Task removed successfully.")
    else:
        print("Invalid index.")

while True:
    print("\n===== Menu =====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")

    option = input("Choose an option (1-5): ")

    if option == "1":
        task = input("Enter the task description: ")
        add_task(task)

    elif option == "2":
        list_tasks()

    elif option == "3":
        list_tasks()
        if pending_tasks:
            try:
                index = int(input("Enter the task number to mark as completed: "))
                mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif option == "4":
        list_tasks()
        if pending_tasks:
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Invalid input.")

    elif option == "5":
        print("Exiting the program...")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")
