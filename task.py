import datetime
class Task:
    def __init__(self,title,description,task_id):
        self.title=title
        self.description=description
        self.task_id=str(task_id)
        if not self.task_id.isdigit():
            raise ValueError('should digit')
        self.start_time=datetime.datetime.now()
        self.end_time=None
        self.status=False

    def mark_as_done(self):
        self.status=True
        self.end_time=datetime.datetime.now()
    def __str__(self):
        return f'ID:{self.task_id},Title:{self.title},
        Description:{self.description},'\
        f'start Time:{self.start_time},end Time:{self.end_time},
        status:{self.status}'
              
        

