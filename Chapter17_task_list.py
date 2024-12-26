import database
from business import Task

def display_tasks(tasks):
    for task in tasks:
        print(task)

def view_tasks():
    tasks = database.get_tasks()  
    task_list = []

     
    for task in tasks:
        task_id, description = task  
        task_list.append(Task(description, False, task_id))  

    
    display_tasks(task_list)

    return task_list

def view_history():
    tasks = database.get_tasks(completed=True)
    task_list = []  
    for task in tasks:
        task_id, description = task  
        task_list.append(Task(description, True, task_id))

    display_tasks(task_list)

    return task_list


def add_task():
    description = input("Description: ")
    database.add_task(description)
    print("Task added!")

def complete_task(task_list):
    try:
        task_id = int(input("Number: "))
        database.complete_task(task_list[task_id - 1].id)
        print("Task complete!")
    except ValueError:
        print("Invalid input!")

def delete_task(task_list):
    try:
        task_id = int(input("Number: "))
        database.delete_task(task_list[task_id - 1].id)
        print("Task deleted!")
    except (ValueError):
        print("Invalid selection!")

def main():
    task_list = []
    while True:
        print("\nCOMMAND MENU")
        print("view - View pending tasks")
        print("history - View completed tasks")
        print("add - Add a task")
        print("complete - Complete a task")
        print("delete - Delete a task")
        print("exit - Exit program")

        command = input("Command: ")

        if command == "view":
            task_list = view_tasks()
        elif command == "history":
            view_history()
        elif command == "add":
            add_task()
        elif command == "complete":
            complete_task(task_list)
        elif command == "delete":
            delete_task(task_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
