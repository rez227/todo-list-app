print("Welcome to your To-Do List!")
import os

TASKS_FILE = "tasks.txt"
tasks = []

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    print("Saving tasks...")  # Add this line
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_menu():
    print("\n📋 To-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print(f"Task added: {task}")
    else:
        print("Cannot add an empty task.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():
    load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
