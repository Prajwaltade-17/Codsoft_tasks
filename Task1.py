class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f'Added task: "{task}"')

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            print(f'Marked task "{self.tasks[task_index]["task"]}" as done.')
        else:
            print("Invalid task index. Please try again.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        print("Your To-Do List:")
        for index, task in enumerate(self.tasks):
            status = "✔️" if task["done"] else "❌"
            print(f"{index}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()  
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task index to mark as done: "))
                todo_list.mark_done(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
