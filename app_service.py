import json


class AppService:
    tasks = [
        {
            'id': 1,
            'name': "task1",
            "description": "This is task 1"
        },
        {
            "id": 2,
            "name": "task2",
            "description": "This is task 2"
        },
        {
            "id": 3,
            "name": "task3",
            "description": "This is task 3"
        }
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON

    def create_task(self, task):
        tasks_data = json.loads(self.tasksJSON)
        tasks_data.append(task)
        self.tasksJSON = json.dumps(tasks_data)
        return self.tasksJSON

    def update_task(self, request_task):
        tasks_data = json.loads(self.tasksJSON)
        for task in tasks_data:
            if task["id"] == request_task['id']:
                task.update(request_task)
                return json.dumps(tasks_data);
        return json.dumps({'message': 'task id not found'})
