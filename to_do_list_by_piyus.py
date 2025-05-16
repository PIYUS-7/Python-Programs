lst = []
i =1

def add_task(title,no):
    name_task = title.strip()
    task = {'No': no , 'Task' : name_task.title() , 'Done' : False}
    lst.append(task)
    
def view_task():
    print('\n*************** TO-DO LIST ***************')
    if not lst:
        print("No tasks available.")
    else:
        for task in lst:
            print('No : ',task['No'])
            print('Task : ',task['Task'])
            print('Done : ',task['Done'])
            print('------------------------------------------')
    print('******************************************\n')

def mark_task_done(option):
    for task in lst:
        if option == task['No']:
            task['Done'] = True
            break
    else:
        print("No task found with that number.")

def delete_task(option):
    for task in lst:
        if option == task['No']:
            lst.remove(task)
            view_task()
            break
    else:
        print("No task found with that number.")


print("-------> Welcome to To-Do List <-------")
print("              -> By Piyus                   ")


while True:
    choice = input('''
Choose option [1/2/3/4/5]
1. Add a task
2. View tasks
3. Mark a task as done
4. Delete a task
5. Exit the program
                       
----------------------> ''')
    if choice == '1':
        task_name = input('Enter your task : ')
        add_task(task_name,i)
        i+=1

    elif choice == '2':
        view_task()

    elif choice == '3':
        view_task()
        try:
            opt = int(input('Enter your task no to mark as done :'))
            mark_task_done(opt)
        except ValueError:
            print('Please enter a valid number')
    
    elif choice == '4':
        view_task()
        try:
            remove = int(input('Enter your task no to delete :'))
            delete_task(remove)
        except ValueError:
            print('Please enter a valid number')

    elif choice == '5':
        print('Exiting.........')
        break
    else:
        print('Invalid choice ! ! !')
