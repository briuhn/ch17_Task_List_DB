class Task:
    def __init__(self, description, completed, task_id):
        self.description = description
        self.completed = completed
        self.id = task_id

    def __str__(self):
        status = "(DONE)" if self.completed else ""
        return f"{self.id}. {self.description} {status}"
