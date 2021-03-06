from app_service import AppService
from flask import Flask, request
from multiprocessing.pool import ThreadPool


app = Flask(__name__)
appService = AppService();


@app.route('/')
def home():
    return 'Home Page'


@app.route('/api/tasks')
def tasks():
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(appService.get_tasks)
    return async_result.get()


@app.route('/api/task', methods=['POST'])
def create_task():
    request_data = request.get_json()
    task = request_data['task']
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(appService.create_task, (task,))
    return async_result.get()


@app.route('/api/task', methods=['PUT'])
def update_task():
    request_data = request.get_json()
    task = request_data['task']
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(appService.update_task, (task,))
    return async_result.get()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

