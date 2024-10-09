from task import*
class Manager:
    def __init__(self):
        self.tasks={}
    def add_task(self,title,description,task_id):
        if task_id in self.tasks:
             raise ValueError("Task ID must be unique")
        new_task = Task(title, description, task_id)
        self.tasks[task_id] = new_task
        new_task.start_task()
        print(f"Task '{title}' add ok")
    def mark_task_done(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_as_done()
            print(f"Task '{self.tasks[task_id].title}'
                     ' is mark")
        else:
            print("not found") 
    def display_tasks(self):
         if not self.tasks:
             print("is not task") 
             for task_id, task in self.tasks.items():
                 print(task)
    def task_summary(self):
         done_tasks = sum(task.status for task in self.tasks.values())
         not_done_tasks = len(self.tasks) - done_tasks
         print(f"task done :{done_tasks}, not done: {not_done_tasks}")