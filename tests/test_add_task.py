import pytest
from pages.task_page import TaskPage

@pytest.mark.parametrize("task_text", [
    "Test task 1",
    "Test task 2",
    "Test task 3"
])
def test_add_task(page, task_text):
    task_page = TaskPage(page)
    task_page.add_task(task_text)
    assert task_page.is_task_present(task_text), f"Task '{task_text}' not found on the page"