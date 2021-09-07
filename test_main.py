import json
import requests
import pytest

PORT = 5000
SUCCESS_STATUS_CODE = 200
NO_OF_PROCESS = 1
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
MAIN_JSON = [
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


@pytest.fixture
def local_url():
    return f"http://localhost:{PORT}"


def test_get_all_data_request_pass(local_url):
    url = "{0}/api/tasks".format(local_url)

    response = requests.get(url, headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_json_data = json.loads(response.text)
    expected_json_data = MAIN_JSON
    assert actual_json_data == expected_json_data


def test_post_request_create_new(local_url):
    url = "{0}/api/task".format(local_url)
    post_data = {"task": {"id": 3, "name": "task3", "description": "This is task 3"}}

    response = requests.post(url, data=json.dumps(post_data), headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_json_data = json.loads(response.text)

    expected_json_data = {'message': 'Task Created Successfully'}

    assert actual_json_data == expected_json_data


def test_post_request_create_duplicate(local_url):
    url = "{0}/api/task".format(local_url)
    post_data = {"task": {"id": 3, "name": "task3", "description": "This is task 3"}}

    response = requests.post(url, data=json.dumps(post_data), headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_json_data = json.loads(response.text)

    expected_json_data = {'message': 'Duplicate creation found, try put method to update'}

    assert actual_json_data == expected_json_data


def test_put_request_update_exist_data(local_url):
    url = "{0}/api/task".format(local_url)
    put_data = {"task": {"id": 3, "name": "task4", "description": "task3 renamed to task4"}}

    response = requests.put(url, data=json.dumps(put_data), headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_json_data = json.loads(response.text)

    expected_json_data = {'message': 'Task Updated Successfully'}

    assert actual_json_data == expected_json_data


def test_put_request_update_non_exist_data(local_url):
    url = "{0}/api/task".format(local_url)
    put_data = {"task": {"id": 4, "name": "task4", "description": "This is task 4"}}

    response = requests.put(url, data=json.dumps(put_data), headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_json_data = json.loads(response.text)

    expected_json_data = {'message': 'Task id not found'}

    assert actual_json_data == expected_json_data
