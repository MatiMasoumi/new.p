from manager import Manager
def main():
     manager = Manager() 
     while True: 
        print("1. add task")
        print("2.mark task done") 
        print("3.display tasks") 
        print("4.task sammary")
        print("5. exit") 
        choice = input("choose an option") 
        if choice == '1':
             title = input("enter task title ") 
             description = input("enter task description ")
             task_id = input("enter unique task id ") 
             try:
                 manager.add_task(title, description, task_id)
                 print('task added')
            except ValueError as e:
                 print(e)
        elif choice == '2':
            task_id = input("enter task id ") 
            manager.mark_task_done(task_id)
        elif choice == '3':
            manager.display_tasks()
        elif choice == '4':
            new_func(manager) 
        elif choice == '5':
            print("exit..")
            break
        else:
            print("please try again") 

    if __name__ == "__main__":
       main()