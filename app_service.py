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
        }
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON

    def create_task(self, task):
        tasks_data = json.loads(self.tasksJSON)
        dup_count = 0
        for exist_task in tasks_data:
            if exist_task["id"] == task['id']:
                dup_count += 0
                return json.dumps({'message': 'Duplicate creation found, try put method to update'})
        if dup_count == 0:
            tasks_data.append(task)
        self.tasksJSON = json.dumps(tasks_data)
        return json.dumps({'message': 'Task Created Successfully'})

    def update_task(self, request_task):
        tasks_data = json.loads(self.tasksJSON)
        for task in tasks_data:
            if task["id"] == request_task['id']:
                task.update(request_task)
                self.tasksJSON = json.dumps(tasks_data)
                return json.dumps({'message': 'Task Updated Successfully'})
        return json.dumps({'message': 'Task id not found'})
