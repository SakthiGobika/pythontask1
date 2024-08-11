def display_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(1,len(tasks)+1):
            print(f"{i}. {tasks[i-1]}")

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_number < len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_number] = new_task
                print("Task after updation is ",new_task)
        else:
                print("Invalid task number.")
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num =int(input("Enter the task number to delete: ")) -1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print("The removed task is:",removed_task)
        else:
            print("Invalid task")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
