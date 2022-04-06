from unittest.mock import patch

from app.todo import Todo


@patch("app.todo.requests.get")
def test_request_response_ok(mock_get):
    todos = [{"userId": 1, "id": 1, "title": "Make the bed", "completed": False}]

    mock_get.return_value.ok = True
    mock_get.return_value.text = todos

    response = Todo().get_todos()

    assert response.ok
    assert len(response.text) == 1

@patch("app.todo.requests.get")
def test_request_response_not_ok(mock_get):
    mock_get.return_value.ok = False

    response = Todo().get_todos()

    assert response == None
